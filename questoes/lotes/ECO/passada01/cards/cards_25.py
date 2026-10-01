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
    # ------------------------------------------------------------------ E2-L00679
    {
        "id": "ECO-E2-L00679-1", "fonte_ref": "E2-L00679", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26B,
        "rotulo_item": "Item",
        "assertiva": ("A presença de externalidades negativas na produção faz com que o custo marginal social "
                      "seja superior ao custo marginal privado, resultando em uma quantidade de equilíbrio de "
                      "mercado superior à socialmente ótima."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A presença de externalidades negativas na produção faz com que o custo marginal social "
                      "seja <u>superior</u> ao custo marginal privado, resultando em uma quantidade de equilíbrio "
                      "de mercado <u>superior</u> à socialmente ótima."),
        "poucas": (vd("CMgS = CMgP + custo externo marginal") + ". O produtor decide pelo CMgP, mais baixo, e "
                   "produz até onde CMgP = demanda: " + azb("sobreprodução") + " em relação ao ótimo, onde "
                   "CMgS = demanda."),
        "destrinchando": [
            "Externalidade negativa na produção (poluição de uma siderúrgica, por exemplo): parte do custo de "
            "produzir recai sobre terceiros. O " + azb("custo marginal social") + " soma ao custo privado o "
            + azb("custo externo marginal") + ": CMgS = CMgP + CExtMg, e por isso a curva social fica "
            "<b>acima</b> da privada.",
            "Equilíbrio de mercado: oferta (CMgP) = demanda → Qₘ, com preço baixo demais (não embute o dano). "
            "Ótimo social: CMgS = demanda → " + vd("Q* < Qₘ") + ", com preço maior.",
            "As unidades entre Q* e Qₘ custam à sociedade mais do que valem para os consumidores: o triângulo "
            "entre CMgS e a demanda nesse trecho é o " + azb("peso morto") + " da externalidade.",
            "Correção: " + azb("imposto pigouviano") + " igual ao CExtMg em Q*, que desloca a oferta privada "
            "até cruzar a demanda no ótimo; ou cotas, padrões de emissão, licenças negociáveis.",
            "Espelho: externalidade positiva → benefício social acima do privado → " + vd("Qₘ < Q*") + " "
            "(subprodução).",
        ],
        "grafico_verso": "ECO-E2-L00679-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " Os dois “superior” estão no lugar certo. A banca fabrica o "
                       "ERRADO invertendo um deles: CMgS “inferior” ao privado (ECO-E2-L00971-1) ou curva "
                       "social “abaixo” (ECO-E2-L00871-1), ou ainda quantidade de mercado “inferior”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com externalidade negativa na produção, o preço de mercado fica acima do socialmente "
            "ótimo.”</i> → ERRADO (inversão: fica abaixo)",
            "<i>“Na presença de externalidade negativa, o equilíbrio competitivo deixa de ser eficiente no "
            "sentido de Pareto.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CMgS = CMgP + custo externo marginal; mercado decide pelo CMgP: preço menor e "
                             "quantidade maior que o ótimo social (superprodução)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00680
    {
        "id": "ECO-E2-L00680-1", "fonte_ref": "E2-L00680", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26B,
        "rotulo_item": "Item",
        "assertiva": ("O Teorema de Coase afirma que, na ausência de custos de transação e com direitos de "
                      "propriedade bem definidos, a negociação privada levará a uma alocação eficiente de "
                      "recursos, independentemente de a quem os direitos de propriedade sejam atribuídos "
                      "inicialmente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Teorema de Coase afirma que, na ausência de custos de transação e com direitos de "
                      "propriedade bem definidos, a negociação privada levará a uma alocação eficiente de "
                      "recursos, <u>independentemente de a quem</u> os direitos de propriedade sejam atribuídos "
                      "inicialmente."),
        "poucas": ("É o " + azb("teorema de Coase") + " em sua forma canônica: com direitos definidos e "
                   "negociação sem custo, as partes chegam ao " + azb("ótimo de Pareto") + ", seja quem for o "
                   "titular inicial do direito."),
        "destrinchando": [
            "Por que a atribuição não altera a alocação: o direito é um ativo negociável. Quem o valoriza mais "
            "acaba com ele — comprando-o ou deixando de vendê-lo. Exemplo numérico: uma fábrica ganha "
            + vd("50") + " poluindo um rio; pescadores perdem " + vd("80") + ".",
            "Se os pescadores têm o direito ao rio limpo, a fábrica precisaria pagar mais de 80 para poluir, "
            "mas só ganha 50: não polui. Se a fábrica tem o direito de poluir, os pescadores lhe pagam algo "
            "entre 50 e 80 para que pare: não polui. " + vd("Mesma alocação") + " (rio limpo), "
            "<b>distribuição diferente</b> (quem paga a quem).",
            "Agora inverta os números (fábrica ganha 80, dano de 50): em qualquer atribuição, a fábrica polui "
            "— e polui porque isso é eficiente. Coase não diz que a externalidade desaparece, e sim que se "
            "chega ao nível <b>eficiente</b> dela.",
            "Os limites estão nas premissas: custos de transação (muitas vítimas, litígio, fiscalização), "
            "informação assimétrica e comportamento estratégico. Quando eles pesam, voltam à mesa as soluções "
            "de " + oc("Pigou") + " (imposto) e a regulação.",
        ],
        "dissecando": (cz("[literalidade]") + " Mesmo enunciado de ECO-E2-L00517-1, com “levará” em vez de "
                       "“podem negociar”. O futuro categórico é seguro aqui porque as condições do teorema "
                       "foram dadas. As versões erradas mexem na atribuição do direito ou retiram uma das "
                       "condições."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema de Coase, a negociação privada sempre elimina por completo a "
            "externalidade.”</i> → ERRADO (leva ao nível eficiente, que pode ser positivo)",
            "<i>“Pelo teorema de Coase, a atribuição inicial dos direitos afeta a distribuição de renda entre "
            "as partes, mas não a eficiência.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["levará"], "dificuldade": 1,
        "comentario_fonte": ("Direitos bem definidos e custos de transação nulos → negociação de compensações "
                             "internaliza a externalidade; alocação eficiente (ótimo de Pareto) qualquer que seja "
                             "o detentor inicial do direito."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00517-1 (mesmo curso, outra lista) e ECO-E2-L00333-1 cobram o "
                    "mesmo enunciado com outra redação"],
    },
    # ------------------------------------------------------------------ E2-L00681
    {
        "id": "ECO-E2-L00681-1", "fonte_ref": "E2-L00681", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26B,
        "rotulo_item": "Item",
        "assertiva": ("Bens públicos puros são caracterizados por serem não rivais e não excludentes, o que leva "
                      "ao problema do “carona” (free-rider) e à suboferta pelo mercado privado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Bens públicos puros são caracterizados por serem não rivais e não excludentes, o que leva "
                      "ao problema do “carona” (free-rider) e à <u>suboferta</u> pelo mercado privado."),
        "poucas": ("Não exclusão → cada um pode usufruir sem pagar → ninguém revela quanto valoriza o bem → "
                   "a firma privada não consegue cobrar → " + azb("suboferta") + " (ou oferta nula)."),
        "destrinchando": [
            azb("Carona (free-rider)") + ": quem se beneficia de um bem sem contribuir para custeá-lo. Decorre "
            "da " + azb("não exclusão") + ": se não posso ser barrado, é racional esperar que os outros paguem. "
            "Se todos pensam assim, o bem não é produzido, embora valha mais, para o conjunto, do que custa.",
            "A " + azb("não rivalidade") + " acrescenta outra razão: o custo de servir mais um usuário é zero, "
            "e cobrar dele seria ineficiente mesmo que possível.",
            "Condição de " + oc("Samuelson") + " (" + vd("1954") + "): o bem público deve ser ofertado até que "
            + vd("a soma dos benefícios marginais de todos os usuários = custo marginal") + " (soma "
            "<b>vertical</b> das demandas, ao contrário da soma horizontal dos bens privados). O mercado, que "
            "só capta a disposição a pagar revelada, fica aquém.",
            "Respostas: provisão pública financiada por " + azb("tributos") + " (defesa, iluminação pública, "
            "pesquisa básica), contratação de produtores privados pelo Estado e, em pequenos grupos, "
            "cooperação voluntária (" + oc("Olson") + ", <i>A lógica da ação coletiva</i>, 1965: quanto maior o "
            "grupo, maior o incentivo à carona).",
        ],
        "dissecando": (cz("[literalidade]") + " Cadeia causal correta (características → carona → suboferta). "
                       "Cuidado com a variante que atribui a carona à não <b>rivalidade</b>: a causa direta é a "
                       "não exclusão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O problema do carona decorre da rivalidade no consumo dos bens públicos.”</i> → ERRADO (troca "
            "de conceito: decorre da não exclusão)",
            "<i>“A provisão eficiente de um bem público exige que a soma dos benefícios marginais dos "
            "consumidores iguale o custo marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Não rivalidade e não exclusão; a não exclusão gera o carona; firmas não conseguem "
                             "cobrar, logo suboferta ou inexistência do bem no mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00682
    {
        "id": "ECO-E2-L00682-1", "fonte_ref": "E2-L00682", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26B,
        "rotulo_item": "Item",
        "assertiva": ("O “Tragédia dos Comuns” refere-se ao uso excessivo de recursos comuns (bens rivais, mas "
                      "não excludentes), pois os indivíduos não consideram a externalidade negativa que seu "
                      "consumo impõe aos outros usuários."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O “Tragédia dos Comuns” refere-se ao uso excessivo de recursos comuns (bens <u>rivais, "
                      "mas não excludentes</u>), pois os indivíduos não consideram a <u>externalidade "
                      "negativa</u> que seu consumo impõe aos outros usuários."),
        "poucas": ("A " + azb("tragédia dos comuns") + " é uma externalidade negativa: cada usuário compara seu "
                   "benefício com seu custo privado e ignora o custo que impõe aos outros ao reduzir o estoque "
                   "comum."),
        "destrinchando": [
            "Mecanismo: o usuário explora até que seu benefício marginal iguale seu " + azb("custo marginal "
            "privado") + ". Mas cada unidade extraída também reduz a produtividade ou a disponibilidade do "
            "recurso para os demais — custo que ele não paga. Como CMg social > CMg privado, o uso agregado "
            "fica acima do eficiente.",
            "Por que a dupla rival + não excludente: sem rivalidade, o uso de um não prejudicaria os outros "
            "(não haveria tragédia); com exclusão, um dono cobraria pelo uso e racionaria o recurso.",
            "Exemplos: sobrepesca, desmatamento de áreas sem dono definido, esgotamento de aquíferos, "
            "congestionamento urbano, emissões de gases de efeito estufa (o clima como comum global).",
            "Remédios: definir direitos (privatização, concessão), cotas e licenças, tributar o uso, gestão "
            "comunitária (" + oc("Ostrom") + "). O texto clássico é de " + oc("Garrett Hardin") + " ("
            + vd("1968") + "), retomando a parábola das pastagens comuns.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição completa e com a causa certa (externalidade "
                       "ignorada). Mesmo tema de ECO-E2-L00518-1. A banca erra o item trocando “rivais” por "
                       "“não rivais” ou atribuindo a tragédia aos bens públicos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A tragédia dos comuns afeta os bens públicos puros, cujo uso por um indivíduo reduz a "
            "disponibilidade para os demais.”</i> → ERRADO (troca de conceito: bem público é não rival)",
            "<i>“Na tragédia dos comuns, o custo marginal privado do uso do recurso é inferior ao custo marginal "
            "social.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Recursos comuns rivais e não excludentes; cada um consome até benefício marginal = "
                             "custo privado e ignora o custo imposto aos outros; resultado: sobreuso."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00518-1 (mesmo curso, outra lista), ECO-E2-L01011-1 e "
                    "ECO-E2-L01175-1 cobram a tragédia dos comuns com outra redação"],
    },
    # ------------------------------------------------------------------ E2-L00744
    {
        "id": "ECO-E2-L00744-1", "fonte_ref": "E2-L00744", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_EST,
        "rotulo_item": "Item",
        "assertiva": ("A instalação de estações de pedágio logo após cada via de entrada em uma rodovia "
                      "administrada por concessionária privada resolve o problema do carona, a despeito dos "
                      "custos da transação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A instalação de estações de pedágio <u>logo após cada via de entrada</u> em uma rodovia "
                      "administrada por concessionária privada resolve o problema do carona, <u>a despeito dos "
                      "custos da transação</u>."),
        "poucas": ("O pedágio em <b>todas</b> as entradas torna a rodovia " + azb("excludente") + ": quem não "
                   "paga não usa. Sem a não exclusão, desaparece o carona — ainda que a cobrança tenha custos "
                   "(cabines, cobrança, filas)."),
        "destrinchando": [
            "O carona nasce da " + azb("não exclusão") + ". Qualquer tecnologia que permita barrar quem não "
            "paga — catraca, ingresso, senha, pedágio — o elimina e transforma o bem em algo que o mercado "
            "consegue vender.",
            "Classificação da rodovia segundo exclusão e rivalidade (" + oc("Mankiw") + "): "
            + azb("livre e sem pedágio") + " → bem público; " + azb("congestionada e sem pedágio")
            + " → recurso comum; " + azb("livre e com pedágio") + " → bem de clube (monopólio natural); "
            + azb("congestionada e com pedágio") + " → bem privado.",
            "O “a despeito dos custos da transação” lembra que excluir custa: a praça de pedágio, os "
            "funcionários e o tempo dos motoristas são " + azb("custos de transação") + ". Eles não fazem o "
            "carona voltar; só tornam a exclusão mais ou menos vantajosa. Hoje o pedágio eletrônico e o "
            + rx("sistema free flow, em implantação nas rodovias brasileiras") + " ⏳ (out/2026), reduzem "
            "esse custo.",
            "A exclusão resolve o carona, mas, numa rodovia não congestionada, cobrar afasta usuários cujo "
            "custo marginal é zero: há um peso morto típico dos bens de clube — por isso o debate entre "
            "pedágio e financiamento por tributos.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " O “logo após cada via de entrada” garante a "
                       "exclusão completa (ninguém entra sem passar pelo pedágio) e o “a despeito dos custos” "
                       "tenta assustar quem associa custos de transação ao fracasso da solução. A pergunta é "
                       "só: dá para excluir? Sim."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma rodovia livre de congestionamento e com pedágio é um bem público puro.”</i> → ERRADO "
            "(com exclusão vira bem de clube)",
            "<i>“A cobrança de pedágio em uma rodovia congestionada a transforma em bem privado.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Tabela de tipos de bens (exclusão × rivalidade) com exemplos de estradas; o pedágio "
                             "torna a rodovia excludente e resolve o carona."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 108", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (quadro exclusão × rivalidade no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00745
    {
        "id": "ECO-E2-L00745-1", "fonte_ref": "E2-L00745", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_EST,
        "rotulo_item": "Item",
        "assertiva": "Uma rodovia sem pedágio, sob a administração federal, é sempre um bem público.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma rodovia sem pedágio, sob a administração federal, é ") + vm("sempre") + az(" um bem "
                                                                                                    "público."),
        "poucas": ("Sem pedágio, a rodovia é " + azb("não excludente") + ", mas só é bem público se também for "
                   + azb("não rival") + ". Congestionada, o uso de um atrapalha o dos outros: vira "
                   + azb("recurso comum") + "."),
        "destrinchando": [
            "Bem público exige as <b>duas</b> propriedades: não exclusão <i>e</i> não rivalidade. A ausência de "
            "pedágio garante só a primeira.",
            "A rivalidade de uma rodovia depende do tráfego: vazia, mais um carro não atrapalha ninguém (não "
            "rival → bem público); congestionada, cada carro a mais reduz a velocidade de todos (rival → "
            + azb("recurso comum") + ", sujeito à tragédia dos comuns e ao sobreuso).",
            "“Sob a administração federal” é irrelevante: na economia, bem público é definido pelas "
            "características de consumo, não pela " + azb("titularidade") + ". Um bem estatal pode ser privado "
            "no sentido econômico (energia de estatal, cobrada por consumo), e um bem particular pode ter "
            "traços de bem público (um farol privado).",
            "O congestionamento é uma " + azb("externalidade negativa") + ": quem entra na via ignora o atraso "
            "que impõe aos demais. Solução clássica: pedágio urbano de congestionamento (Londres, Estocolmo, "
            "Singapura), que cobra mais no horário de pico.",
            vm("Regra-âncora: público no sentido econômico = não rival + não excludente, seja quem for o "
               "dono."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O “sempre” derruba o item: ignora a "
                       "rodovia congestionada. A menção à administração federal é a isca para confundir bem "
                       "público econômico com bem de propriedade pública."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma rodovia sem pedágio e não congestionada é exemplo de bem público.”</i> → CERTO",
            "<i>“Toda rodovia de propriedade do Estado é bem público em sentido econômico.”</i> → ERRADO "
            "(confunde titularidade com características de consumo)",
        ])],
        "reescrita": ("Uma rodovia sem pedágio, sob a administração federal, " + hl("só") + " é um bem público "
                      + hl("se não for congestionada; congestionada, é um recurso comum") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("Rodovia congestionada é rival, não bem público puro (fundido com o comentário da "
                             "linha duplicada E2-L00853: sem pedágio é não excluível; só é bem público se não "
                             "congestionada; congestionada é recurso comum)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00852
    {
        "id": "ECO-E2-L00852-1", "fonte_ref": "E2-L00852", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o teorema de Coase, desde que atribuído o direito de propriedade em favor do "
                      "agente que sofre os efeitos de uma externalidade negativa, a negociação privada entre quem "
                      "produz e quem sofre os efeitos da externalidade resultará em uma alocação socialmente "
                      "eficiente na ausência de custos de transação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o teorema de Coase, ")
                    + vm("desde que atribuído o direito de propriedade em favor do agente que sofre os efeitos de "
                         "uma externalidade negativa")
                    + az(", a negociação privada entre quem produz e quem sofre os efeitos da externalidade "
                         "resultará em uma alocação socialmente eficiente na ausência de custos de transação.")),
        "poucas": ("Coase exige que o direito esteja " + azb("bem definido") + ", não que pertença à vítima. "
                   "Atribuído ao poluidor ou ao prejudicado, a negociação chega à " + vd("mesma alocação "
                   "eficiente") + "."),
        "destrinchando": [
            "O núcleo do " + azb("teorema de Coase") + " (" + oc("Ronald Coase") + ", " + vd("1960")
            + ") é a <b>neutralidade</b> da atribuição: com custos de transação nulos, a eficiência vem de os "
            "direitos estarem definidos e serem negociáveis, qualquer que seja o titular.",
            "Teste com números: uma fazenda ganha 30 por usar um agrotóxico que causa dano de 20 ao apiário "
            "vizinho. Direito do apicultor: a fazenda paga entre 20 e 30 pela permissão e usa o produto. "
            "Direito da fazenda: o apicultor não consegue pagar mais de 20 para impedi-la; ela usa. Em ambos, "
            "o agrotóxico é usado (eficiente, pois 30 > 20).",
            "Dar o direito à vítima é intuição de <b>justiça</b> (“o poluidor-pagador”), não condição de "
            "eficiência. A atribuição afeta a " + azb("distribuição") + " — quem paga a quem —, não a "
            "alocação.",
            "O direito ambiental brasileiro adota o " + rx("princípio do poluidor-pagador") + " (Lei "
            + vd("6.938/1981") + ", art. 4º, VII), escolha normativa compatível com Coase, mas não exigida "
            "por ele.",
        ],
        "dissecando": (cz("[restrição indevida]") + " A conclusão do item é verdadeira para a hipótese "
                       "descrita, mas o “desde que” transforma um caso possível em condição necessária. Pista: "
                       "qualquer enunciado de Coase que privilegie um dos lados está errado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema de Coase, a alocação eficiente é alcançada tanto se o direito for atribuído ao "
            "poluidor quanto se for atribuído ao prejudicado.”</i> → CERTO",
            "<i>“Pelo teorema de Coase, só a atribuição do direito ao poluidor garante que ele internalize o "
            "dano.”</i> → ERRADO (restrição indevida; a atribuição é neutra)",
        ])],
        "reescrita": ("De acordo com o teorema de Coase, " + hl("desde que bem definido o direito de "
                      "propriedade, seja em favor do agente que gera, seja em favor do que sofre os efeitos de "
                      "uma externalidade negativa") + ", a negociação privada entre quem produz e quem sofre os "
                      "efeitos da externalidade resultará em uma alocação socialmente eficiente na ausência de "
                      "custos de transação."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["desde que"], "dificuldade": 2,
        "comentario_fonte": ("Direitos bem definidos, independentemente de quem os detenha, e custos de "
                             "transação nulos permitem resolver a externalidade pela negociação, sem coerção "
                             "governamental (Coase, 1960)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00854
    {
        "id": "ECO-E2-L00854-1", "fonte_ref": "E2-L00854", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("Por serem não excludentes e não rivais, os bens comuns em geral devem ser explorados e "
                      "ofertados livremente pelo setor privado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Por serem não excludentes e ") + vm("não rivais") + az(", os bens comuns em geral ")
                    + vm("devem ser explorados e ofertados livremente pelo setor privado") + az(".")),
        "poucas": ("Bens comuns são não excludentes, mas " + azb("rivais") + ". Explorados livremente, tendem "
                   "ao esgotamento (" + azb("tragédia dos comuns") + "): exigem regulação, não liberdade de "
                   "exploração."),
        "destrinchando": [
            "Dois erros empilhados. (1) Classificação: “não excludente e não rival” é o " + azb("bem público")
            + "; o " + azb("recurso comum") + " é não excludente e <b>rival</b> (ar e água limpos, fauna, "
            "flora, cardumes, florestas).",
            "(2) Prescrição: justamente por serem rivais e de acesso livre, cada usuário explora o recurso "
            "sem considerar o custo que impõe aos outros — " + azb("externalidade negativa") + " que leva à "
            "exaustão. A política adequada é limitar o uso (cotas, licenças, defeso, concessões, unidades de "
            "conservação), não liberá-lo.",
            "Também não faz sentido falar em “oferta” privada de bens não excludentes: sem poder cobrar, a "
            "firma não tem como se remunerar. Quando o setor privado entra, é porque se criou exclusão "
            "(concessão florestal, outorga de uso da água).",
            rx("No Brasil") + ": a " + vd("Lei 9.433/1997") + " (Política Nacional de Recursos Hídricos) cobra "
            "pelo uso da água e exige outorga; a " + vd("Lei 11.284/2006") + " criou as concessões de "
            "florestas públicas — exemplos de transformação de comuns em bens com exclusão regulada.",
        ],
        "dissecando": (cz("[troca de conceito · juízo indevido]") + " O item cola a definição de bem público no "
                       "bem comum e extrai dela uma recomendação de política sem base (“devem ser explorados "
                       "livremente”). Basta um dos erros para o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por serem não excludentes e rivais, os recursos comuns tendem a ser explorados além do nível "
            "socialmente ótimo.”</i> → CERTO",
            "<i>“Os bens comuns, por serem rivais, são excludentes.”</i> → ERRADO (rivalidade e exclusão são "
            "critérios independentes)",
        ])],
        "reescrita": ("Por serem não excludentes e " + hl("rivais") + ", os bens comuns em geral "
                      + hl("tendem a ser explorados em excesso e demandam regulação do seu uso") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "JUIZO_INDEVIDO"], "moduladores": ["em geral", "devem"],
        "dificuldade": 1,
        "comentario_fonte": ("Bens comuns são não excluíveis e rivais; não são ofertados nem controlados pelo "
                             "setor privado; uso excessivo leva à tragédia dos comuns; não rivais e não "
                             "excluíveis são bens públicos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00855
    {
        "id": "ECO-E2-L00855-1", "fonte_ref": "E2-L00855", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("A função alocativa do governo faz com que este forneça bens e serviços à sociedade devido a "
                      "característica de não-exclusão desses determinados. Bens meritórios não satisfazem o "
                      "princípio da exclusão."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A função alocativa do governo faz com que este forneça bens e serviços à sociedade "
                       "devido a característica de não-exclusão desses determinados. Bens meritórios ")
                    + vm("não satisfazem") + az(" o princípio da exclusão.")),
        "poucas": (azb("Bens meritórios") + " (saúde, educação) <b>são excludentes</b>: o mercado poderia "
                   "vendê-los e barrar quem não paga. O Estado os provê por mérito social e externalidades, não "
                   "por impossibilidade de exclusão."),
        "destrinchando": [
            "As três funções do governo de " + oc("Richard Musgrave") + " (<i>The Theory of Public Finance</i>, "
            + vd("1959") + "): " + azb("alocativa") + " (prover bens que o mercado não provê ou provê mal), "
            + azb("distributiva") + " (corrigir a distribuição de renda) e " + azb("estabilizadora")
            + " (emprego, preços, crescimento).",
            "Na função alocativa entram dois grupos distintos: " + azb("bens públicos") + ", providos porque a "
            "não exclusão impede a cobrança; e " + azb("bens meritórios") + ", que <b>satisfazem</b> o princípio "
            "da exclusão (escola e hospital podem cobrar), mas que a sociedade julga que todos devem consumir, "
            "independentemente da renda ou da preferência individual.",
            "Razões para prover meritórios: externalidades positivas (educação, vacinação), informação "
            "imperfeita do consumidor sobre o próprio benefício e equidade. Por isso coexistem oferta pública "
            "gratuita e oferta privada paga do mesmo bem.",
            rx("No Brasil") + ", saúde e educação são direitos sociais (CF/88, art. " + vd("6º") + "), com "
            "acesso universal ao SUS (art. " + vd("196") + ") e ensino público gratuito (art. " + vd("206, IV")
            + ") — o caso típico de bens meritórios.",
            vm("Regra-âncora: bem público → Estado provê porque não dá para excluir; bem meritório → dá para "
               "excluir, mas não se quer excluir."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira frase (truncada na fonte) descreve a provisão de "
                       "bens públicos; a segunda estende a não exclusão aos meritórios por contágio. O erro é "
                       "uma negação enxertada: “não satisfazem”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens meritórios podem ser ofertados pelo setor privado, pois satisfazem o princípio da "
            "exclusão.”</i> → CERTO",
            "<i>“A provisão de bens meritórios pelo governo justifica-se pela impossibilidade técnica de cobrar "
            "por eles.”</i> → ERRADO (isso é o bem público)",
        ])],
        "reescrita": ("A função alocativa do governo faz com que este forneça bens e serviços à sociedade devido "
                      "a característica de não-exclusão desses determinados. Bens meritórios "
                      + hl("satisfazem") + " o princípio da exclusão" + hl(", mas são providos pelo governo por "
                      "sua importância social") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Bens meritórios satisfazem o princípio da exclusão, mas o governo os produz por "
                             "externalidades positivas e para não excluir a população de baixa renda; exemplos: "
                             "saúde e educação, garantidas pela Constituição."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: a 1ª frase da assertiva vem truncada na fonte (“desses determinados”, "
                    "provavelmente “desses determinados bens”); mantida fiel"],
    },
    # ------------------------------------------------------------------ E2-L00869
    {
        "id": "ECO-E2-L00869-1", "fonte_ref": "E2-L00869", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_TIPOS,
        "rotulo_item": "Item",
        "assertiva": ("Os bens públicos e os recursos comuns não são excluíveis e estão à disposição de todos que "
                      "queiram utilizá-los, mas os recursos comuns, por serem rivais, demandam dos formuladores de "
                      "política econômica a regulação sobre as quantidades deles que podem ser utilizadas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os bens públicos e os recursos comuns <u>não são excluíveis</u> e estão à disposição de "
                      "todos que queiram utilizá-los, mas os recursos comuns, <u>por serem rivais</u>, demandam "
                      "dos formuladores de política econômica a regulação sobre as quantidades deles que podem "
                      "ser utilizadas."),
        "poucas": ("O que une bens públicos e recursos comuns é a " + azb("não exclusão") + "; o que os separa "
                   "é a " + azb("rivalidade") + ". Por serem rivais, os comuns se esgotam com o uso e pedem "
                   "limites de quantidade."),
        "destrinchando": [
            "Bem público (não rival): o problema é de <b>provisão</b> — ninguém paga, então ninguém produz; o "
            "Estado financia por tributos. Recurso comum (rival): o problema é de <b>uso</b> — o recurso já "
            "existe, mas é consumido em excesso; o Estado limita a quantidade usada.",
            "Exemplo: a madeira de uma floresta aberta. Quem corta reduz o estoque disponível para os outros "
            "(rivalidade) e ninguém pode ser impedido de cortar (não exclusão). Sabendo que o estoque diminui, "
            "cada um corre para cortar antes: " + azb("tragédia dos comuns") + ".",
            "Instrumentos de regulação quantitativa: cotas de captura e de corte, licenças, defeso, outorgas de "
            "uso da água, áreas protegidas; e instrumentos de preço (tributar o uso) ou de direitos "
            "(concessões, cotas individuais transferíveis).",
            "Recursos comuns típicos: minerais, peixes, florestas, ar e água limpos, espectro de rádio sem "
            "gestão, estradas congestionadas sem pedágio.",
        ],
        "dissecando": (cz("[literalidade]") + " O item acerta o ponto comum (não exclusão), a diferença "
                       "(rivalidade) e a consequência de política. A banca costuma inverter a atribuição: "
                       "“bens públicos, por serem rivais, exigem regulação”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bens públicos, por serem rivais, exigem regulação das quantidades utilizadas.”</i> → "
            "ERRADO (troca de ator: bem público é não rival)",
            "<i>“A diferença entre bens públicos e recursos comuns está na rivalidade, não na "
            "excludabilidade.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bens comuns são rivais e não exclusivos; competição pelo uso leva à exploração "
                             "excessiva e à tragédia dos comuns; exemplo da madeira; necessidade de "
                             "regulamentação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00871
    {
        "id": "ECO-E2-L00871-1", "fonte_ref": "E2-L00871", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_TIPOS,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado de equilíbrio competitivo com externalidade negativa, o custo social é maior "
                      "que o custo privado; nessa circunstância, portanto, em uma representação gráfica da relação "
                      "entre preço (eixo das ordenadas) e quantidade (eixo das abcissas), a curva de custo "
                      "marginal social fica abaixo da curva de custo marginal privado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um mercado de equilíbrio competitivo com externalidade negativa, o custo social é "
                       "maior que o custo privado; nessa circunstância, portanto, em uma representação gráfica da "
                       "relação entre preço (eixo das ordenadas) e quantidade (eixo das abcissas), a curva de "
                       "custo marginal social fica ") + vm("abaixo") + az(" da curva de custo marginal privado.")),
        "poucas": ("Se o custo social é <b>maior</b>, a curva de CMgS fica <b>acima</b> da de CMgP: a distância "
                   "vertical entre elas é o " + azb("custo externo marginal") + ". O item tira a conclusão "
                   "oposta da própria premissa."),
        "destrinchando": [
            vd("CMgS = CMgP + CExtMg") + ". Com o preço no eixo vertical, “custar mais” para a mesma quantidade "
            "significa estar <b>mais alto</b> no gráfico: em cada Q, a curva social está acima da privada, à "
            "distância do custo externo daquela unidade.",
            "Se o dano por unidade cresce com a produção (poluição que se acumula), as curvas se afastam à "
            "direita; se é constante, são paralelas.",
            "Consequência: a oferta de mercado (CMgP) cruza a demanda à direita do ponto em que o CMgS a "
            "cruza — " + azb("sobreprodução") + " e preço baixo demais.",
            "Caso espelho em que a curva social fica abaixo: " + azb("externalidade positiva na produção")
            + " (o pomar que beneficia o apicultor vizinho, ou a firma que treina mão de obra depois "
            "contratada por concorrentes): CMgS = CMgP − benefício externo marginal.",
        ],
        "grafico_verso": "ECO-E2-L00871-1-V1",
        "dissecando": (cz("[inversão · contradição]") + " O item enuncia a premissa certa (custo social > "
                       "privado) e inverte a tradução gráfica. Itens de “representação gráfica” costumam "
                       "apostar na confusão entre “acima” e “à direita”. Ver também ECO-E2-L00971-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com externalidade negativa na produção, a curva de custo marginal social situa-se à esquerda "
            "da curva de custo marginal privado.”</i> → CERTO (acima e à esquerda descrevem o mesmo "
            "deslocamento)",
            "<i>“A distância vertical entre as curvas de custo marginal social e privado corresponde ao "
            "benefício marginal do consumidor.”</i> → ERRADO (é o custo externo marginal)",
        ])],
        "reescrita": ("Em um mercado de equilíbrio competitivo com externalidade negativa, o custo social é "
                      "maior que o custo privado; nessa circunstância, portanto, em uma representação gráfica da "
                      "relação entre preço (eixo das ordenadas) e quantidade (eixo das abcissas), a curva de "
                      "custo marginal social fica " + hl("acima") + " da curva de custo marginal privado."),
        "tipo_erro": ["INVERSAO", "CONTRADICAO"], "moduladores": ["portanto"], "dificuldade": 1,
        "comentario_fonte": ("CMg social = CMg privado + custo externo; a curva social fica acima da privada."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00971-1 cobra a mesma relação CMgS × CMgP com outra redação "
                    "(mesmo curso, outra lista)"],
    },
    # ------------------------------------------------------------------ E2-L00872
    {
        "id": "ECO-E2-L00872-1", "fonte_ref": "E2-L00872", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_TIPOS,
        "rotulo_item": "Item",
        "assertiva": ("Se, ao produzir, uma firma gera externalidade negativa na forma de poluição, para cobrar "
                      "dessa firma um imposto de Pigou (que a faça considerar o custo social de produção, e não "
                      "apenas o custo privado), deve-se conhecer a externalidade marginal no nível de produto "
                      "socialmente eficiente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se, ao produzir, uma firma gera externalidade negativa na forma de poluição, para cobrar "
                      "dessa firma um imposto de Pigou (que a faça considerar o custo social de produção, e não "
                      "apenas o custo privado), deve-se conhecer a externalidade marginal <u>no nível de produto "
                      "socialmente eficiente</u>."),
        "poucas": ("O " + azb("imposto pigouviano ótimo") + " por unidade é igual ao " + vd("custo externo "
                   "marginal em Q*") + ": assim a curva de custo privado + imposto cruza a demanda exatamente "
                   "no ótimo. Calibrá-lo exige conhecer esse dano marginal."),
        "destrinchando": [
            "Mecânica: o imposto t por unidade desloca o custo privado para cima (CMgP + t). Para que a firma, "
            "maximizando lucro, escolha Q*, a curva CMgP + t deve passar pelo ponto em que CMgS cruza a "
            "demanda. Logo " + vd("t = CMgS(Q*) − CMgP(Q*) = CExtMg(Q*)") + ".",
            "Por que no ótimo e não na produção de mercado: se o dano marginal cresce com a quantidade, o "
            "CExtMg em Qₘ é <b>maior</b> que em Q*. Um imposto calibrado em Qₘ seria excessivo e levaria a "
            "produção abaixo do ótimo.",
            "Essa é a fraqueza prática da solução de " + oc("Pigou") + ": o regulador precisa conhecer as "
            "curvas de dano e de custo — informação difícil e politicamente disputada. Daí as alternativas: "
            + azb("licenças negociáveis") + " (fixa-se a quantidade e o mercado descobre o preço), "
            "a negociação de " + oc("Coase") + " e padrões de emissão.",
            "Imposto × licenças sob incerteza (" + oc("Weitzman") + ", 1974): o imposto fixa o preço da "
            "poluição e deixa a quantidade incerta; a licença fixa a quantidade e deixa o preço incerto.",
        ],
        "grafico_verso": "ECO-E2-L00872-1-V1",
        "dissecando": (cz("[detalhe]") + " O ponto fino é “no nível de produto socialmente eficiente”: a banca "
                       "troca isso por “no nível de produção de mercado” ou por “o custo externo total” para "
                       "fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O imposto de Pigou ótimo corresponde ao custo externo marginal avaliado na quantidade de "
            "equilíbrio do mercado sem intervenção.”</i> → ERRADO (dado trocado: avalia-se em Q*)",
            "<i>“O imposto de Pigou ótimo iguala o custo externo total dividido pela quantidade "
            "produzida.”</i> → ERRADO (troca marginal por médio)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["deve-se"], "dificuldade": 2,
        "comentario_fonte": ("Equilíbrio competitivo acima do ótimo; o imposto de Pigou desloca o CMg até o CMg "
                             "social; o cobrador deve conhecer a externalidade marginal. Gráfico com CMgS = CMgP "
                             "+ CMg da externalidade, pontos A (mercado) e B (ótimo)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 136", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00872-1-V1, com a cunha do imposto em Q*)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00971
    {
        "id": "ECO-E2-L00971-1", "fonte_ref": "E2-L00971", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("A externalidade negativa implica que o custo marginal social da produção é menor que o "
                      "custo marginal privado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A externalidade negativa implica que o custo marginal social da produção é ")
                    + vm("menor") + az(" que o custo marginal privado.")),
        "poucas": ("Externalidade negativa = custo que recai sobre terceiros, somado ao do produtor: "
                   + vd("CMgS = CMgP + CE") + ", portanto CMgS é <b>maior</b> que CMgP."),
        "destrinchando": [
            "O " + azb("custo marginal social") + " é tudo o que a sociedade perde para produzir mais uma "
            "unidade: o custo pago pela firma (insumos, salários — o " + azb("CMg privado") + ") mais o "
            "custo imposto a terceiros sem compensação (o " + azb("custo externo marginal") + ", CE): poluição, "
            "ruído, doenças respiratórias.",
            "Como CE > 0, " + vd("CMgS > CMgP") + "; graficamente, a curva social fica acima da privada. O "
            "mercado, que só enxerga CMgP, produz mais e cobra menos do que seria eficiente.",
            "Quando o CMgS seria menor que o CMgP? Na " + azb("externalidade positiva na produção") + ": o "
            "pomar cujas flores alimentam as abelhas do vizinho (exemplo de " + oc("James Meade") + ", 1952), "
            "a firma que treina trabalhadores depois contratados por outras, a P&amp;D que transborda. Aí o "
            "mercado produz de menos.",
            "Quadro de sinais: negativa → CMgS > CMgP (ou BMgS < BMgP, no consumo) → sobreprodução → imposto. "
            "Positiva → CMgS < CMgP (ou BMgS > BMgP) → subprodução → subsídio.",
        ],
        "dissecando": (cz("[inversão]") + " Inversão de sinal pura, sem enxerto. Mesma relação de "
                       "ECO-E2-L00871-1 e ECO-E2-L00679-1. Pista: “negativa” para a sociedade significa custo "
                       "<b>a mais</b>, nunca a menos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A externalidade positiva na produção implica que o custo marginal social é menor que o custo "
            "marginal privado.”</i> → CERTO",
            "<i>“Na externalidade negativa, o benefício marginal social do consumo supera o benefício marginal "
            "privado.”</i> → ERRADO (é a positiva no consumo)",
        ])],
        "reescrita": ("A externalidade negativa implica que o custo marginal social da produção é "
                      + hl("maior") + " que o custo marginal privado."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Custo externo torna o CMg social maior que o privado: CMgS = CMgP + CE.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00871-1 cobra a mesma relação CMgS × CMgP com outra redação "
                    "(mesmo curso, outra lista)"],
    },
    # ------------------------------------------------------------------ E2-L01009
    {
        "id": "ECO-E2-L01009-1", "fonte_ref": "E2-L01009", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONS,
        "rotulo_item": "Item",
        "assertiva": ("A partir de 2019, passou a ser cobrada uma taxa de entrada dos turistas que visitam certo "
                      "parque nacional, visando-se à remuneração dos investimentos em infraestrutura feitos pela "
                      "concessionária que administra o parque. Nesse caso, com o início da cobrança da taxa de "
                      "acesso, o parque nacional deixou de ser um bem público - no sentido econômico e se tornou "
                      "um bem quase público, em decorrência da possibilidade de exclusão de usuários que não "
                      "possam pagar a taxa de acesso, apesar de ainda se caracterizar pela não rivalidade no "
                      "consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A partir de 2019, passou a ser cobrada uma taxa de entrada dos turistas que visitam certo "
                      "parque nacional, […]. Nesse caso, com o início da cobrança da taxa de acesso, o parque "
                      "nacional deixou de ser um bem público - no sentido econômico e se tornou um <u>bem quase "
                      "público</u>, em decorrência da <u>possibilidade de exclusão</u> de usuários que não possam "
                      "pagar a taxa de acesso, apesar de ainda se caracterizar pela <u>não rivalidade</u> no "
                      "consumo."),
        "poucas": ("A taxa cria " + azb("exclusão") + "; a " + azb("não rivalidade") + " permanece (enquanto "
                   "o parque não lota). Excludente + não rival = " + azb("bem de clube") + ", também chamado "
                   "de bem quase público."),
        "destrinchando": [
            "Antes da cobrança: acesso livre (não excludente) e, sem lotação, um visitante a mais não reduz a "
            "experiência dos outros (não rival) → bem público no sentido econômico.",
            "Depois: quem não paga é barrado → passa a ser " + azb("excludente") + ". Como a rivalidade não "
            "mudou, o parque vira " + azb("bem de clube") + " (" + oc("Buchanan") + ", “An Economic Theory of "
            "Clubs”, 1965) — mesma família da TV a cabo, do cinema vazio, da rodovia livre com pedágio.",
            "Ressalva da rivalidade: com lotação (feriados, trilhas estreitas), cada visitante a mais degrada "
            "a visita dos outros e o bem passa a ser rival — aí o ingresso funciona também como "
            "racionamento. Por isso alguns parques limitam o número diário de visitantes.",
            "Bem quase público não significa privatizado: o parque continua público no sentido jurídico; o "
            "que muda é a característica econômica do consumo. " + rx("No Brasil") + ", parques nacionais "
            "com serviços concedidos à iniciativa privada (Iguaçu, Fernando de Noronha) cobram ingresso nesses "
            "moldes.",
        ],
        "dissecando": (cz("[detalhe · paráfrase fiel]") + " O enunciado longo esconde uma pergunta simples: o "
                       "que a taxa mudou? Só a exclusão. O “apesar de ainda se caracterizar pela não "
                       "rivalidade” é o detalhe que confirma o bem de clube. Termo “quase público” é usado em "
                       "manuais brasileiros como sinônimo de bem impuro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com a cobrança da taxa, o parque passou a ser rival no consumo, tornando-se bem "
            "privado.”</i> → ERRADO (a taxa cria exclusão, não rivalidade)",
            "<i>“Em feriados de lotação máxima, o parque com cobrança de ingresso se aproxima de um bem "
            "privado.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Bem público = não rival e não excludente; manteve-se só a não rivalidade (salvo "
                             "lotação); a cobrança tornou o parque excludente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01011
    {
        "id": "ECO-E2-L01011-1", "fonte_ref": "E2-L01011", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONS,
        "rotulo_item": "Item",
        "assertiva": ("No problema da tragédia dos comuns, o custo da super exploração do bem comum que pode levar "
                      "à sua extinção é um exemplo de externalidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No problema da tragédia dos comuns, o custo da super exploração do bem comum que pode "
                      "levar à sua extinção é um exemplo de <u>externalidade</u>."),
        "poucas": ("Cada usuário do recurso comum impõe aos demais um custo (menos estoque, menor "
                   "produtividade) que não paga: é uma " + azb("externalidade negativa") + ", e é ela que "
                   "produz a superexploração."),
        "destrinchando": [
            "A parábola: numa cidade medieval, as famílias criam ovelhas no pasto comum. A população e o "
            "rebanho crescem; a terra é fixa; a grama desaparece. Cada família ganha integralmente com a "
            "ovelha a mais, mas o desgaste do pasto é dividido entre todos (" + oc("Hardin") + ", "
            + vd("1968") + ").",
            "Tradução econômica: o " + azb("custo marginal privado") + " do uso é menor que o "
            + azb("custo marginal social") + ", porque não inclui a redução do recurso para os outros. Cada "
            "um usa até onde benefício = custo privado; o uso total fica acima do eficiente.",
            "Por isso a tragédia dos comuns é tratada como caso particular de externalidade negativa, com os "
            "mesmos remédios: tributar o uso (estilo " + oc("Pigou") + "), fixar quantidades (cotas, "
            "licenças), definir direitos de propriedade (estilo " + oc("Coase") + ") ou gestão comunitária "
            "(" + oc("Ostrom") + ").",
            "Conexão com temas atuais: a mudança climática é a tragédia dos comuns em escala global — a "
            "atmosfera é rival como depósito de carbono e ninguém pode ser excluído de emitir.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item liga dois capítulos do manual (recursos comuns e "
                       "externalidades). Quem os estuda separados hesita; a ligação é exatamente a que "
                       + oc("Mankiw") + " faz. Mesmo tema de ECO-E2-L01175-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na tragédia dos comuns, o custo marginal privado de explorar o recurso supera o custo marginal "
            "social.”</i> → ERRADO (inversão: o privado é menor)",
            "<i>“A tragédia dos comuns decorre da não exclusão combinada com a rivalidade no uso do "
            "recurso.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Recursos comuns usados em excesso quando não se cobra pelo uso; CMg privado menor "
                             "que o social; resultado ineficiente: externalidade negativa; parábola das ovelhas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01175-1 cobra a tragédia dos comuns como externalidade com outra "
                    "redação (mesmo curso, outra lista)"],
    },
    # ------------------------------------------------------------------ E2-L01175
    {
        "id": "ECO-E2-L01175-1", "fonte_ref": "E2-L01175", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_EXT,
        "rotulo_item": "Item",
        "assertiva": ("O fenômeno econômico conhecido como Tragédia dos Comuns é um caso de externalidade "
                      "associado à utilização excessiva de um recurso de produção, o qual pertence a toda a "
                      "sociedade, e não a uma pessoa em particular."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O fenômeno econômico conhecido como Tragédia dos Comuns é um caso de externalidade "
                      "associado à utilização excessiva de um recurso de produção, o qual <u>pertence a toda a "
                      "sociedade, e não a uma pessoa em particular</u>."),
        "poucas": ("A tragédia ocorre porque o recurso é de " + azb("acesso comum") + " (de todos e de "
                   "ninguém): sem dono que cobre pelo uso, cada um ignora o custo que impõe aos outros — uma "
                   + azb("externalidade negativa") + "."),
        "destrinchando": [
            "Recursos comuns compartilham com os bens públicos o " + azb("livre acesso") + " (não exclusão) e "
            "por isso oferecem pouco incentivo a que empresas os produzam ou conservem. O problema adicional "
            "é a " + azb("rivalidade") + ": o uso de cada um reduz o que sobra para os outros.",
            "“Pertence a toda a sociedade, e não a uma pessoa” descreve a ausência de " + azb("direito de "
            "propriedade individual") + ". Um proprietário único internalizaria o custo do esgotamento (o "
            "pasto exaurido reduziria o valor do <b>seu</b> ativo) e racionaria o uso.",
            "O papel do governo é garantir que o recurso não seja usado em excesso: limites de uso, tributação, "
            "concessões ou atribuição de direitos.",
            "Atenção ao vocabulário: “propriedade comum” aqui é o regime de acesso livre. " + oc("Ostrom")
            + " distinguiu o acesso aberto (onde a tragédia ocorre) da propriedade comunal gerida por regras "
            "locais, que muitas vezes evita a tragédia.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " A definição é ampla (“recurso de produção”), mas correta. "
                       "Igual a ECO-E2-L01011-1 em conteúdo. A variante errada típica diria que o recurso "
                       "“pertence a um particular” ou que a tragédia é falha de governo, e não de mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A atribuição de direitos de propriedade sobre o recurso comum tende a reduzir sua "
            "superexploração.”</i> → CERTO",
            "<i>“A tragédia dos comuns ocorre porque o recurso, sendo não rival, pode ser usado "
            "indefinidamente.”</i> → ERRADO (troca de conceito: o recurso comum é rival)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Recursos comuns não excludentes e rivais; uso excessivo; papel do governo é evitar o "
                             "sobreuso; parábola das ovelhas: a tragédia decorre de uma externalidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01011-1 cobra a tragédia dos comuns como externalidade com outra "
                    "redação (mesmo curso, outra lista)"],
    },
    # ------------------------------------------------------------------ E2-L01176
    {
        "id": "ECO-E2-L01176-1", "fonte_ref": "E2-L01176", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_EXT,
        "rotulo_item": "Item",
        "assertiva": ("Do ponto de vista econômico, governos cobram impostos para minimizarem as perdas com os "
                      "“caronas” — que usufruem sem pagar — nas ofertas de bens públicos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Do ponto de vista econômico, governos cobram impostos para minimizarem as perdas com os "
                      "“caronas” — que usufruem sem pagar — nas ofertas de bens públicos."),
        "poucas": ("O " + azb("tributo") + " é contribuição <b>compulsória</b>: obriga todos a financiar o bem "
                   "público, de que se beneficiariam de qualquer modo. É a resposta clássica ao "
                   + azb("carona") + "."),
        "destrinchando": [
            "Sem exclusão, a contribuição voluntária fracassa: cada um prefere que os outros paguem. O bem não "
            "é produzido, embora o conjunto dos usuários o valorize mais do que custa (" + oc("Mankiw")
            + ": o exemplo da queima de fogos da cidade).",
            "O Estado contorna o problema pela " + azb("coerção fiscal") + ": define a quantidade a ofertar e "
            "a financia com impostos que ninguém pode recusar. Converte o comportamento voluntário em "
            "obrigatório.",
            "Limite: o governo também não observa as preferências individuais (ninguém declara quanto valoriza "
            "a defesa nacional), então decide a quantidade por " + azb("análise custo-benefício") + " e "
            "processo político — fontes de falhas de governo.",
            "Nota técnica: os impostos são o meio de financiar a oferta; a provisão pode ser pública ou "
            "contratada de empresas privadas. O que o mercado não resolve é o <b>financiamento</b>, não "
            "necessariamente a produção.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " “Do ponto de vista econômico” delimita o item à "
                       "justificativa alocativa do tributo (há outras: redistribuição, estabilização). A "
                       "versão errada costuma dizer que os impostos “eliminam” os caronas ou que o carona "
                       "decorre da rivalidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O problema do carona é resolvido pelo mercado, desde que os bens públicos sejam ofertados por "
            "empresas privadas.”</i> → ERRADO (sem exclusão, a firma não consegue cobrar)",
            "<i>“A tributação compulsória permite financiar bens públicos cuja provisão voluntária seria "
            "insuficiente.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["minimizarem"], "dificuldade": 1,
        "comentario_fonte": ("Carona recebe o benefício sem pagar; sem exclusão, o bem não é produzido mesmo que "
                             "valorizado coletivamente; o governo financia a provisão com impostos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01177
    {
        "id": "ECO-E2-L01177-1", "fonte_ref": "E2-L01177", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_EXT,
        "rotulo_item": "Item",
        "assertiva": ("Pode-se dizer que existe externalidade quando há conluio entre os produtores que operam em "
                      "um mercado oligopolista."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Pode-se dizer que existe ") + vm("externalidade") + az(" quando há conluio entre os "
                                                                              "produtores que operam em um "
                                                                              "mercado oligopolista.")),
        "poucas": ("Conluio é " + azb("poder de mercado") + " (outra falha de mercado): os produtores combinam "
                   "preços via mercado. " + azb("Externalidade") + " é efeito sobre terceiros que <b>não "
                   "passa</b> pelo preço."),
        "destrinchando": [
            "Falhas de mercado clássicas, cada uma com mecanismo próprio: " + azb("poder de mercado")
            + " (monopólio, cartel), " + azb("externalidades") + ", " + azb("bens públicos") + ", "
            + azb("informação assimétrica") + ". Todas afastam o mercado da eficiência de Pareto, mas não se "
            "confundem.",
            "No " + azb("conluio") + " (cartel), as firmas agem como monopolista: restringem a quantidade e "
            "elevam o preço acima do custo marginal. O consumidor perde, mas a perda vem <b>pelo preço</b> que "
            "ele paga na transação — não é efeito externo.",
            "Externalidade exige que alguém fora da transação (ou um aspecto não precificado dela) seja "
            "afetado: a fumaça da fábrica sobre o vizinho, e não o preço alto do produto sobre o comprador.",
            "Remédio próprio do conluio: " + azb("defesa da concorrência") + ". " + rx("No Brasil") + ", o "
            "cartel é infração da ordem econômica (Lei " + vd("12.529/2011") + ", art. 36) julgada pelo "
            + rx("Cade") + ", e também crime (Lei " + vd("8.137/1990") + ").",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca uma falha de mercado por outra. O “pode-se dizer” "
                       "tenta amaciar a afirmação, mas o conceito está errado em qualquer grau. Pista: "
                       "pergunte se há terceiro afetado fora do preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O conluio entre oligopolistas é falha de mercado associada ao exercício de poder de "
            "mercado.”</i> → CERTO",
            "<i>“Toda falha de mercado é uma externalidade.”</i> → ERRADO (modulador absoluto: há poder de "
            "mercado, bens públicos, assimetria)",
        ])],
        "reescrita": ("Pode-se dizer que existe " + hl("poder de mercado (falha distinta da externalidade)")
                      + " quando há conluio entre os produtores que operam em um mercado oligopolista."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode-se dizer"], "dificuldade": 1,
        "comentario_fonte": ("Externalidade: efeito de produção ou consumo que impõe custos ou benefícios a "
                             "terceiros não refletidos nos preços."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01178
    {
        "id": "ECO-E2-L01178-1", "fonte_ref": "E2-L01178", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_EXT,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento no preço das passagens aéreas, ao provocar a redução da demanda por serviços "
                      "aeroportuários, é um sinal da existência de externalidade negativa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento no preço das passagens aéreas, ao provocar a redução da demanda por serviços "
                       "aeroportuários, ") + vm("é um sinal da existência de externalidade negativa") + az(".")),
        "poucas": ("Passagem aérea e serviços aeroportuários são " + azb("bens complementares") + ": o efeito "
                   "corre pelo sistema de preços. É o funcionamento normal do mercado (efeito pecuniário), não "
                   "externalidade."),
        "destrinchando": [
            "A cadeia do item é a da " + azb("elasticidade-preço cruzada") + " negativa: passagem mais cara → "
            "menos voos → menos demanda por serviços de aeroporto (estacionamento, lojas, táxis). Isso "
            "desloca a demanda de um mercado vizinho; não há custo imposto fora do mercado.",
            "Essas transmissões via preço são chamadas de " + azb("externalidades pecuniárias") + ": "
            "redistribuem renda entre agentes, mas não geram ineficiência, porque os preços estão fazendo "
            "exatamente o seu papel de sinalizar escassez.",
            "Externalidade “de verdade” (tecnológica) no mesmo setor: o ruído das aeronaves sobre os "
            "moradores do entorno, as emissões de carbono, o congestionamento das pistas — efeitos que ninguém "
            "paga na passagem.",
            vm("Regra-âncora: se o efeito passa pelo preço de mercado, não é externalidade; se fica fora dele, "
               "é."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " A banca descreve uma relação "
                       "correta entre mercados complementares e lhe cola o rótulo errado. A pista é o verbo "
                       "“provocar” ligado a preço: o canal é o mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O ruído provocado pelos pousos e decolagens sobre os moradores próximos ao aeroporto é exemplo "
            "de externalidade negativa.”</i> → CERTO",
            "<i>“A queda da demanda por serviços aeroportuários após a alta das passagens indica que os dois "
            "serviços são substitutos.”</i> → ERRADO (são complementares)",
        ])],
        "reescrita": ("Um aumento no preço das passagens aéreas, ao provocar a redução da demanda por serviços "
                      "aeroportuários, " + hl("não é sinal de externalidade, mas de complementaridade entre os "
                      "dois serviços, transmitida pelos preços") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Externalidade: efeito sobre terceiros não refletido nos preços dos bens e "
                             "serviços."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01179
    {
        "id": "ECO-E2-L01179-1", "fonte_ref": "E2-L01179", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_COASE,
        "rotulo_item": "Item",
        "assertiva": ("O chamado teorema de Coase assevera que os atores privados podem resolver, de forma "
                      "eficiente, o problema das externalidades entre si, dependendo apenas da distribuição "
                      "inicial de direitos entre esses atores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O chamado teorema de Coase assevera que os atores privados podem resolver, de forma "
                       "eficiente, o problema das externalidades entre si, ")
                    + vm("dependendo apenas da distribuição inicial de direitos") + az(" entre esses atores.")),
        "poucas": ("No " + azb("teorema de Coase") + " a eficiência é <b>independente</b> da distribuição "
                   "inicial dos direitos e depende de duas condições: " + vd("direitos bem definidos") + " e "
                   + vd("custos de transação nulos") + "."),
        "destrinchando": [
            "O item comete dois erros numa só expressão: troca “independentemente” por “dependendo” e reduz as "
            "condições do teorema a uma só (“apenas”), apagando os custos de transação.",
            "Formulação correta (" + oc("Ronald Coase") + ", " + vd("1960") + "): se os agentes podem negociar "
            "sem custo sobre a alocação dos recursos, e os direitos estão definidos, resolvem a externalidade "
            "por conta própria, e chegam ao mesmo resultado eficiente seja quem for o titular.",
            "O que depende da distribuição inicial é a <b>repartição dos ganhos</b> (quem paga a quem), não a "
            "eficiência. E o que realmente decide se a solução privada funciona são os " + azb("custos de "
            "transação") + ": com muitos afetados, negociar é caro ou impossível.",
            "Por isso Coase é lido como argumento a favor de " + azb("instituições") + " que reduzam custos "
            "de transação (direito claro, tribunais eficientes, registros), e não como receita de "
            "laissez-faire.",
        ],
        "dissecando": (cz("[inversão · restrição indevida]") + " Inverte a relação central do teorema "
                       "(independência → dependência) e acrescenta um “apenas” que apaga a outra condição. "
                       "Mesma família de ECO-E2-L00852-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema de Coase, na ausência de custos de transação, a solução privada é eficiente "
            "qualquer que seja a distribuição inicial dos direitos de propriedade.”</i> → CERTO",
            "<i>“Pelo teorema de Coase, a distribuição inicial dos direitos não afeta a riqueza final das "
            "partes.”</i> → ERRADO (afeta a distribuição, não a eficiência)",
        ])],
        "reescrita": ("O chamado teorema de Coase assevera que os atores privados podem resolver, de forma "
                      "eficiente, o problema das externalidades entre si, " + hl("independentemente da "
                      "distribuição inicial de direitos, desde que bem definidos e sem custos de transação")
                      + " entre esses atores."),
        "tipo_erro": ["INVERSAO", "RESTRICAO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Direitos bem definidos, independentemente de quem os detenha, e ausência de custos "
                             "de transação: os privados resolvem a externalidade; resultado eficiente "
                             "independe da distribuição inicial (Coase, 1960)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
