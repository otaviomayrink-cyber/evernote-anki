"""Cards do lote de redação 18 — ECO, passada 03 (notas 75, 76 e 77: novas teorias do comércio, cadeias
globais de valor, IED)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ntc": "🔬 Novas teorias do comércio",
    "cgv": "⭐ Cadeias globais de valor",
    "ied": "💼 IED e portfólio",
}

CMD_NAB_NTC = "Em relação à Nova Teoria do Comércio, julgue o item a seguir."

CMD_RT_INT = "Acerca dos temas de economia internacional, julgue o item a seguir."

CMD_RT_CONC = "Sobre os conceitos e teorias do comércio internacional, julgue o item a seguir."

CMD_RT_TEO = "Julgue o item a seguir, acerca das teorias do comércio internacional."

CMD_NIDI_CGV = "No que diz respeito à teoria do comércio internacional, julgue o item a seguir."

CMD_ARM = "Acerca das cadeias globais de valor, julgue o item a seguir."

ASSERT_BLOCOS_INI = (
    "Admita que a economia global seja dividida em dois blocos: países desenvolvidos, abundantes em capital; e "
    "países em desenvolvimento, abundantes em trabalho. Considere, adicionalmente, que ambos os blocos contêm dois "
    "setores produtivos: o setor agrícola, que produz bens homogêneos, é intensivo em trabalho e opera com retornos "
    "constantes de escala e condições de concorrência perfeita; e o setor industrial, que produz bens "
    "diferenciados, é intensivo em capital e opera com retornos crescentes de escala e condições de concorrência "
    "monopolística. De acordo com as novas teorias de comércio internacional (new trade theories), se os dois "
    "blocos se engajassem em práticas de livre-comércio puro, os fluxos de comércio entre ambos seriam "
    "predominantemente interindustriais, explicados por vantagens comparativas")

ANOT_BLOCOS_INI = (
    "Admita que a economia global seja dividida em dois blocos [...]. De acordo com as novas teorias de comércio "
    "internacional (new trade theories), se os dois blocos se engajassem em práticas de livre-comércio puro, os "
    "fluxos de comércio entre ambos seriam predominantemente interindustriais, explicados por vantagens "
    "comparativas")

ASSERT_CGV_OMC = ("Uma característica marcante das Cadeias Globais de Valor (CGVs) é a existência de uma estrutura de "
                  "governança distribuída entre várias unidades em diversos países. Essa característica é um dos "
                  "principais fatores que dificulta o enquadramento das CGVs nas normas vigentes da OMC.")

ASSERT_IED = ("Do ponto de vista dos impactos, pode-se considerar que o investimento direto é um tipo de capital de "
              "longo prazo, mais resiliente a crises, com efeitos potencialmente positivos sobre uma economia por se "
              "tratar de uma das formas de internacionalização da produção, permitindo que um país tenha acesso a "
              "tecnologia, bens ou serviços originários de outros países.")

CARDS = [
    # ------------------------------------------------------------------ E2-L00574
    {
        "id": "ECO-E2-L00574-1", "fonte_ref": "E2-L00574", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_NTC,
        "rotulo_item": "Item",
        "assertiva": ("A Nova Teoria do Comércio foi desenvolvida principalmente para explicar o comércio "
                      "interindústria entre países com dotações de fatores muito distintas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Nova Teoria do Comércio foi desenvolvida principalmente para explicar o comércio ")
                    + vm("interindústria") + az(" entre países com dotações de fatores ") + vm("muito distintas")
                    + az(".")),
        "poucas": ("A Nova Teoria do Comércio nasceu para explicar o " + azb("comércio intraindústria")
                   + " entre países " + vd("parecidos") + " em dotações e tecnologia; o comércio interindústria entre "
                   "países diferentes já era explicado pelas vantagens comparativas."),
        "destrinchando": [
            azb("Comércio interindústria") + " (ou intersetorial): o país exporta bens de um setor e importa de "
            "outro — o Brasil vende soja e compra máquinas. É o que " + oc("Ricardo") + " (diferenças de "
            "tecnologia) e " + oc("Heckscher-Ohlin") + " (diferenças de dotação de fatores) explicam: quanto "
            "<b>mais diferentes</b> os países, mais comércio desse tipo.",
            azb("Comércio intraindústria") + ": o país exporta e importa produtos do <b>mesmo</b> setor — a "
            "Alemanha vende carros à França e compra carros franceses. Nos anos 1960–70, dados de " + oc("Grubel e "
            "Lloyd") + " mostraram que boa parte do comércio entre países ricos era desse tipo, justamente entre "
            "economias com dotações semelhantes — um fato que H-O não previa.",
            "A resposta veio com " + oc("Paul Krugman") + " (1979, 1980), " + oc("Helpman") + " e " + oc("Lancaster")
            + ": com " + azb("economias de escala internas") + ", cada firma produz poucas variedades; com "
            + azb("concorrência monopolística") + " e consumidores que gostam de variedade, cada país se "
            "especializa em algumas marcas e troca com o outro. Krugman recebeu o Nobel de " + vd("2008") + ".",
            "Os modelos de síntese (Helpman-Krugman) juntam os dois mundos: diferenças de dotação geram o "
            "componente interindustrial; escala e diferenciação geram o intraindustrial, que cresce quanto mais "
            "parecidos forem os países.",
            vm("Regra-âncora: países diferentes → comércio interindústria (vantagem comparativa); países "
               "semelhantes → comércio intraindústria (escala + diferenciação)."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O item troca “intra” por “inter” e, coerentemente "
                       "com a troca, inverte a condição dos países (“muito distintas”). Tudo “fecha” internamente — "
                       "mas descreve o objeto da teoria clássica, não da nova. 🔥 Prefixo inter/intra é a pegadinha "
                       "número um deste tema."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Nova Teoria do Comércio foi desenvolvida para explicar o comércio intraindústria entre países "
            "com dotações de fatores semelhantes.”</i> → CERTO",
            "<i>“A Nova Teoria do Comércio substituiu o modelo de Heckscher-Ohlin, que deixou de ter poder "
            "explicativo.”</i> → ERRADO (as teorias se complementam)",
        ])],
        "reescrita": ("A Nova Teoria do Comércio foi desenvolvida principalmente para explicar o comércio "
                      + hl("intraindústria") + " entre países com dotações de fatores " + hl("semelhantes") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["principalmente"], "dificuldade": 1,
        "comentario_fonte": "Foi desenvolvida para explicar o comércio intraindústria entre países com dotações e "
                            "tecnologia semelhantes; o interindústria é explicado por vantagens comparativas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00575
    {
        "id": "ECO-E2-L00575-1", "fonte_ref": "E2-L00575", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_NTC,
        "rotulo_item": "Item",
        "assertiva": ("A Nova Teoria do Comércio assume concorrência perfeita nos mercados, similarmente aos "
                      "modelos clássicos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Nova Teoria do Comércio assume concorrência ") + vm("perfeita") + az(" nos mercados, ")
                    + vm("similarmente aos") + az(" modelos clássicos.")),
        "poucas": ("A ruptura da Nova Teoria do Comércio é justamente abandonar a concorrência perfeita: ela supõe "
                   + azb("concorrência imperfeita") + " (em geral, " + azb("monopolística") + "), ao contrário de "
                   "Ricardo e Heckscher-Ohlin."),
        "destrinchando": [
            "Os modelos tradicionais (" + oc("Ricardo") + ", " + oc("Heckscher-Ohlin") + ") trabalham com bens "
            "homogêneos, " + azb("retornos constantes de escala") + " e " + azb("concorrência perfeita") + ": "
            "preço = custo marginal, lucro econômico zero, nenhum poder de mercado.",
            "Com " + azb("economias de escala internas à firma") + ", a concorrência perfeita deixa de ser "
            "sustentável: se o custo médio cai com a produção, a firma maior sempre derruba a menor. Por isso a "
            "Nova Teoria precisa de uma estrutura de mercado imperfeita.",
            "A solução de " + oc("Krugman") + " (1979) foi a " + azb("concorrência monopolística") + " de "
            + oc("Chamberlin") + ", formalizada por " + oc("Dixit e Stiglitz") + " (1977): muitas firmas, cada "
            "uma com uma variedade diferenciada e algum poder de preço (markup). No curto prazo há lucro; no longo, "
            "a entrada livre leva o lucro a zero, com preço = custo médio.",
            "Outra vertente usa " + azb("oligopólio") + " — o modelo de dumping recíproco de " + oc("Brander e "
            "Krugman") + " e a " + azb("política comercial estratégica") + " de " + oc("Brander e Spencer")
            + " (disputa Boeing × Airbus).",
            vm("Regra-âncora: Nova Teoria = retornos crescentes + concorrência imperfeita + diferenciação de "
               "produtos."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O item atribui à Nova Teoria a hipótese que ela "
                       "veio derrubar e reforça o erro com “similarmente aos modelos clássicos”. Pista: escala "
                       "crescente e concorrência perfeita são incompatíveis — se o item fala em Nova Teoria, a "
                       "concorrência é imperfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Nova Teoria do Comércio admite que as firmas tenham poder de mercado e lucros positivos no "
            "curto prazo.”</i> → CERTO",
            "<i>“No modelo de Krugman, as economias de escala são externas à firma, o que preserva a concorrência "
            "perfeita.”</i> → ERRADO (no modelo de concorrência monopolística elas são internas)",
        ])],
        "reescrita": ("A Nova Teoria do Comércio assume concorrência " + hl("imperfeita") + " nos mercados, "
                      + hl("diferentemente dos") + " modelos clássicos."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A ruptura da Nova Teoria é supor concorrência imperfeita (monopolística), com lucros "
                            "positivos e diferenciação de produtos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00576
    {
        "id": "ECO-E2-L00576-1", "fonte_ref": "E2-L00576", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_NTC,
        "rotulo_item": "Item",
        "assertiva": ("As economias externas de escala são benefícios externos às empresas que surgem da "
                      "concentração geográfica de atividades econômicas, contribuindo para a redução dos custos "
                      "médios das firmas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As economias externas de escala são benefícios <u>externos às empresas</u> que surgem da "
                      "<u>concentração geográfica</u> de atividades econômicas, contribuindo para a redução dos "
                      "custos médios das firmas."),
        "poucas": ("É a definição de " + azb("economias externas de escala") + " (ou de aglomeração): o custo médio "
                   "de cada firma cai porque a <b>indústria</b> cresce no local, não porque a firma cresce."),
        "destrinchando": [
            "Distinção-chave: nas " + azb("economias internas") + " o custo médio cai com o tamanho da "
            "<b>própria firma</b> (favorecem grandes empresas e concorrência imperfeita); nas "
            + azb("economias externas") + " cai com o tamanho do <b>setor</b> na região (compatíveis com muitas "
            "firmas pequenas e concorrência perfeita).",
            "As três fontes clássicas, de " + oc("Alfred Marshall") + " (<i>Princípios de Economia</i>, 1890): "
            "(1) " + vd("fornecedores especializados") + " que só sobrevivem com uma clientela grande; (2) "
            + vd("mercado de trabalho comum") + " de mão de obra qualificada; (3) " + vd("transbordamento de "
            "conhecimento") + " (<i>knowledge spillovers</i>) — “os segredos da indústria estão no ar”.",
            "Exemplos: Vale do Silício (semicondutores, software), Hollywood (cinema), a City de Londres "
            "(finanças); no " + rx("Brasil") + ", o polo calçadista do Vale dos Sinos (RS) e o de Franca (SP).",
            "Consequência para o comércio: com economias externas, o padrão de especialização pode ser fruto de "
            "<b>acidente histórico</b> — quem começou primeiro ganha escala e trava a vantagem, mesmo que outro "
            "país pudesse produzir mais barato. É uma das justificativas para a proteção à indústria nascente.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem modulador perigoso. O risco está em achar "
                       "que “redução dos custos médios” só existe com firmas grandes — confusão com economias "
                       "internas, que a banca explora em outros itens."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As economias externas de escala exigem que cada firma aumente sua escala individual de "
            "produção.”</i> → ERRADO (troca com economias internas)",
            "<i>“A presença de economias externas de escala é compatível com mercados formados por muitas "
            "empresas pequenas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Definição correta: economias de aglomeração reduzem o custo médio de todas as firmas do "
                            "setor (mão de obra especializada, fornecedores, transbordamento de conhecimento), sem "
                            "que cada firma precise crescer.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00577
    {
        "id": "ECO-E2-L00577-1", "fonte_ref": "E2-L00577", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_NTC,
        "rotulo_item": "Item",
        "assertiva": ("A interação entre economias de escala, concorrência imperfeita e diferenciação de produtos é "
                      "crucial para a explicação do comércio interindústria na Nova Teoria do Comércio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A interação entre economias de escala, concorrência imperfeita e diferenciação de produtos "
                       "é crucial para a explicação do comércio ") + vm("interindústria")
                    + az(" na Nova Teoria do Comércio.")),
        "poucas": ("O trio escala + concorrência imperfeita + diferenciação explica o comércio "
                   + azb("intraindústria") + ". O interindústria vem das " + azb("vantagens comparativas") + "."),
        "destrinchando": [
            "Por que o trio gera comércio <b>dentro</b> do mesmo setor: (1) com " + azb("economias de escala")
            + ", nenhum país produz todas as variedades de forma eficiente; (2) com " + azb("diferenciação")
            + " e consumidores que gostam de variedade, há demanda pelas marcas estrangeiras; (3) a "
            + azb("concorrência monopolística") + " é a estrutura que acomoda as duas coisas. Resultado: cada "
            "país produz algumas variedades e importa as outras.",
            "O " + azb("comércio interindústria") + " não precisa de nada disso: basta haver diferença de custo "
            "de oportunidade, por tecnologia (" + oc("Ricardo") + ") ou por dotação de fatores ("
            + oc("Heckscher-Ohlin") + ").",
            "Medida usual: o " + azb("índice de Grubel-Lloyd") + ", " + vd("GL = 1 − |X − M| / (X + M)")
            + ", calculado por setor. GL = 1 → comércio puramente intraindústria (exporta e importa o mesmo "
            "valor); GL = 0 → puramente interindústria (só exporta ou só importa).",
            "Os ganhos do comércio intraindústria são diferentes: além da especialização, vêm da "
            + vd("maior variedade") + " e da " + vd("maior escala") + " (custo médio menor), com custos de ajuste "
            "menores, porque os trabalhadores não mudam de setor.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Todos os ingredientes estão certos; só o objeto foi trocado "
                       "(“inter” no lugar de “intra”). Leia o prefixo antes de julgar: é uma letra que inverte o "
                       "gabarito."),
        "modulos": [("🧠 Mnemônico", ["<b>Intra</b> = <b>i</b>guais trocando o mesmo bem; <b>inter</b> = "
                                     "diferentes trocando bens diferentes."])],
        "reescrita": ("A interação entre economias de escala, concorrência imperfeita e diferenciação de produtos é "
                      "crucial para a explicação do comércio " + hl("intraindústria") + " na Nova Teoria do "
                      "Comércio."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Esses elementos explicam o comércio intraindústria, não o interindústria.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00629
    {
        "id": "ECO-E2-L00629-1", "fonte_ref": "E2-L00629", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito das estruturas de mercado, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na presença de economias externas de escala, não é possível que a estrutura de mercado seja "
                      "composta por várias empresas pequenas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na presença de economias externas de escala, ") + vm("não é possível")
                    + az(" que a estrutura de mercado seja composta por várias empresas pequenas.")),
        "poucas": ("Economias " + azb("externas") + " dependem do tamanho do <b>setor</b>, não da firma: são "
                   "perfeitamente compatíveis com muitas empresas pequenas e até com " + vd("concorrência perfeita")
                   + "."),
        "destrinchando": [
            "Nas " + azb("economias internas de escala") + ", o custo médio cai à medida que a <b>própria "
            "firma</b> cresce. Quem cresce primeiro fica mais barato e expulsa os rivais: o mercado tende à "
            "concentração (oligopólio, concorrência monopolística, no limite monopólio natural).",
            "Nas " + azb("economias externas de escala") + ", o custo médio de cada firma cai quando a "
            "<b>indústria local</b> cresce — fornecedores especializados, mão de obra qualificada disponível, "
            "infraestrutura, transbordamento de conhecimento (" + oc("Marshall") + "). A firma individual pode "
            "operar com retornos constantes: não há vantagem em ser grande, só em estar no aglomerado.",
            "Por isso o caso típico de economias externas é um " + azb("distrito industrial") + " de muitas "
            "empresas pequenas: as confecções de Bangalore e do norte da Itália, ou, no " + rx("Brasil") + ", os "
            "polos de calçados de Franca (SP) e de confecções do Agreste pernambucano.",
            "No modelo de " + oc("Krugman e Obstfeld") + " (<i>Economia Internacional</i>), a curva de oferta da "
            "indústria com economias externas é <b>decrescente</b> (custo médio da indústria cai com a produção "
            "total), mas o mercado continua competitivo: cada firma toma preço.",
            vm("Regra-âncora: economias internas → concentração; economias externas → muitas firmas pequenas "
               "podem coexistir."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " O item aplica às economias externas a "
                       "consequência das internas (concentração) e a radicaliza com “não é possível”. Pista: a "
                       "palavra “externas” já diz que o ganho está fora da firma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença de economias internas de escala, a estrutura de mercado tende a ser concentrada.”</i> "
            "→ CERTO",
            "<i>“Economias externas de escala decorrem do aumento do tamanho de cada empresa.”</i> → ERRADO "
            "(troca com economias internas)",
        ])],
        "reescrita": ("Na presença de economias externas de escala, " + hl("é possível") + " que a estrutura de "
                      "mercado seja composta por várias empresas pequenas."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["não é possível"], "dificuldade": 1,
        "comentario_fonte": "Economias externas: custo médio cai com o crescimento do setor, não da firma; "
                            "compatíveis com muitas empresas pequenas em concorrência perfeita.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00644
    {
        "id": "ECO-E2-L00644-1", "fonte_ref": "E2-L00644", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação às teorias do comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": (ASSERT_BLOCOS_INI + " e sem a possibilidade de uma parcela desses fluxos ser intraindustrial, "
                      "explicada por economias de escala e diferenciação de produtos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az(ANOT_BLOCOS_INI + " ") + vm("e sem") + az(" a possibilidade de uma parcela desses fluxos ser "
                                                                  "intraindustrial, explicada por economias de "
                                                                  "escala e diferenciação de produtos.")),
        "poucas": ("No modelo de síntese (" + oc("Helpman-Krugman") + "), o comércio entre os blocos é "
                   "predominantemente interindustrial, mas " + vm("não exclui") + " uma parcela intraindustrial: "
                   "havendo variedades de manufaturas nos dois blocos, elas são trocadas."),
        "destrinchando": [
            "O enunciado monta o " + azb("modelo integrado") + " de " + oc("Helpman e Krugman") + " (<i>Market "
            "Structure and Foreign Trade</i>, 1985): um setor H-O clássico (agricultura homogênea, retornos "
            "constantes) e um setor Krugman (indústria diferenciada, retornos crescentes, concorrência "
            "monopolística).",
            "Componente " + azb("interindustrial") + ": como os blocos têm dotações diferentes, vale H-O no "
            "agregado — o bloco rico exporta, em termos líquidos, manufaturas (intensivas em capital) e o bloco em "
            "desenvolvimento exporta alimentos (intensivos em trabalho). Esse fluxo predomina.",
            "Componente " + azb("intraindustrial") + ": se o bloco em desenvolvimento produz algumas variedades de "
            "manufaturas, os consumidores do bloco rico também as compram (gosto pela variedade). Há troca de "
            "manufaturas por manufaturas, ainda que menor.",
            "Previsão central: a participação do comércio intraindustrial é " + vd("maior quanto mais "
            "semelhantes") + " forem as dotações. Entre países muito diferentes ela é pequena, mas não nula — por "
            "isso o item, ao dizer “sem a possibilidade”, contraria a teoria.",
            "A versão com “com a possibilidade de uma parcela desses fluxos ser intraindustrial” é a correta: a "
            "banca cobra as duas formulações.",
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " Até “vantagens comparativas”, o item está "
                       "certo (o fluxo predominante é interindustrial). O erro está na exclusão final, “sem a "
                       "possibilidade”: a teoria fala em intensidade relativa, nunca em impossibilidade. 🔥 "
                       "Enunciados longos costumam guardar o erro na última oração."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os fluxos de comércio entre ambos seriam predominantemente intraindustriais…”</i> → ERRADO "
            "(dotações diferentes → predomina o interindustrial)",
            "<i>“…a parcela intraindustrial seria tanto maior quanto mais semelhantes fossem as dotações relativas "
            "dos blocos.”</i> → CERTO",
        ])],
        "reescrita": (ANOT_BLOCOS_INI + hl(", com") + " a possibilidade de uma parcela desses fluxos ser "
                      "intraindustrial, explicada por economias de escala e diferenciação de produtos."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["predominantemente", "sem a possibilidade"],
        "dificuldade": 2,
        "comentario_fonte": "O item erra ao excluir o comércio intraindustrial: nos modelos de síntese "
                            "(Helpman-Krugman), o comércio soma fluxos inter e intraindustriais; o intraindustrial é "
                            "mais intenso quanto mais similares os países, mas não inexistente entre diferentes.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01162-1 (mesmo enunciado, versão “com a possibilidade”, gabarito "
                    "CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L01162
    {
        "id": "ECO-E2-L01162-1", "fonte_ref": "E2-L01162", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Com relação às teorias do comércio internacional e aos instrumentos de política comercial, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": (ASSERT_BLOCOS_INI + ", com a possibilidade de uma parcela desses fluxos ser intraindustrial, "
                      "explicada por economias de escala e diferenciação de produtos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az(ANOT_BLOCOS_INI.replace("predominantemente interindustriais",
                                              "<u>predominantemente</u> interindustriais")
                      + ", <u>com a possibilidade</u> de uma parcela desses fluxos ser intraindustrial, explicada "
                        "por economias de escala e diferenciação de produtos."),
        "poucas": ("Com dotações diferentes, predomina o comércio " + azb("interindustrial") + " (H-O); com escala e "
                   "diferenciação no setor industrial, sobra espaço para uma parcela " + azb("intraindustrial")
                   + ". É o modelo de síntese de " + oc("Helpman-Krugman") + "."),
        "destrinchando": [
            azb("Comércio intersetorial") + " (interindustrial): um país exporta e importa bens de setores "
            "diferentes. Os modelos ricardiano e de " + oc("Heckscher-Ohlin") + " o explicam: países com "
            "estruturas produtivas diferentes concentram-se nos bens em que têm vantagem comparativa. No "
            "enunciado, o bloco abundante em capital exporta manufaturas e o abundante em trabalho exporta "
            "alimentos.",
            azb("Comércio intrassetorial") + " (intraindustrial): o mesmo país exporta e importa o mesmo tipo de "
            "bem. Exige " + azb("retornos crescentes") + " (nenhum país produz todas as variedades) e "
            + azb("diferenciação") + " (há quem queira a variedade estrangeira) — exatamente as hipóteses do "
            "setor industrial no enunciado.",
            "O " + azb("modelo integrado") + " de " + oc("Helpman e Krugman") + " (1985) soma os dois fluxos: "
            "diferença de dotação → componente interindustrial (predominante aqui); escala e diferenciação → "
            "componente intraindustrial, maior quanto mais parecidos os países.",
            "Exemplo real: o " + rx("Brasil") + " exporta soja e minério e importa eletrônicos (inter), mas "
            "também troca automóveis e autopeças com a Argentina e o México (intra).",
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " O item se protege com “predominantemente” e “com a "
                       "possibilidade”: não diz que todo o comércio é de um tipo. A banca cobra também a versão "
                       "“sem a possibilidade de uma parcela intraindustrial”, que é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…seriam exclusivamente interindustriais, explicados por vantagens comparativas…”</i> → ERRADO "
            "(modulador absoluto: há parcela intraindustrial)",
            "<i>“…seriam predominantemente intraindustriais, explicados por economias de escala…”</i> → ERRADO "
            "(dotações diferentes → predomina o interindustrial)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["predominantemente", "com a possibilidade"],
        "dificuldade": 2,
        "comentario_fonte": "Definições de comércio intersetorial (Ricardo e H-O, vantagens comparativas) e "
                            "intrassetorial (economias de escala); imagem com país abundante em capital exportando "
                            "manufaturas e país abundante em trabalho exportando alimentos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 193", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00644-1 (mesmo enunciado, versão “sem a possibilidade”, gabarito "
                    "ERRADO)",
                    "nota_redacao: a classificação fundiu este item como duplicata de E2-L00644, mas a assertiva "
                    "é outra (“com a possibilidade”) e o gabarito também (CERTO); convertido em card próprio"],
    },
    # ------------------------------------------------------------------ E2-L00844
    {
        "id": "ECO-E2-L00844-1", "fonte_ref": "E2-L00844", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Com relação às teorias do desenvolvimento e do comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O comércio interindústrias é relativamente mais importante do que o comércio intraindústrias "
                      "nas relações comerciais entre países similares em termos de desenvolvimento tecnológico e "
                      "dotação de fatores de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O comércio interindústrias é relativamente ") + vm("mais") + az(" importante do que o "
                    "comércio intraindústrias nas relações comerciais entre países similares em termos de "
                    "desenvolvimento tecnológico e dotação de fatores de produção.")),
        "poucas": ("Entre países " + azb("semelhantes") + " quase não há diferença de custo de oportunidade: o "
                   "comércio interindústrias é pequeno e predomina o " + azb("intraindústrias") + "."),
        "destrinchando": [
            "O " + azb("comércio interindústrias") + " nasce de " + azb("vantagens comparativas") + ": custos "
            "relativos diferentes, por tecnologia (" + oc("Ricardo") + ") ou dotação de fatores ("
            + oc("Heckscher-Ohlin") + "). Se dois países têm a mesma tecnologia e a mesma razão capital/trabalho, "
            "os preços relativos de autarquia coincidem e esse comércio tende a zero.",
            "O " + azb("comércio intraindústrias") + " não depende de vantagem comparativa: com "
            + azb("economias de escala") + ", cada país produz só algumas variedades; com "
            + azb("concorrência monopolística") + " e gosto pela variedade, troca-se o excedente. Ele existiria "
            "até entre países idênticos (" + oc("Krugman") + ", 1979).",
            "Evidência: o comércio entre União Europeia, Estados Unidos e Japão é majoritariamente intraindústria "
            "(automóveis, máquinas, químicos); o comércio Norte–Sul tem peso maior do interindústria "
            "(commodities × manufaturas).",
            vm("Regra-âncora: quanto mais parecidos os países, maior o peso relativo do comércio intraindústria."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o comparativo (“mais” no lugar de “menos”). A pista é a "
                       "condição dada — países similares em tecnologia <b>e</b> dotação —, que elimina as duas "
                       "fontes de vantagem comparativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O comércio interindústrias é relativamente mais importante nas relações entre países com "
            "dotações de fatores muito diferentes.”</i> → CERTO",
            "<i>“Entre países idênticos em tecnologia e dotações, não há incentivo algum ao comércio.”</i> → "
            "ERRADO (escala e diferenciação geram comércio intraindústria)",
        ])],
        "reescrita": ("O comércio interindústrias é relativamente " + hl("menos") + " importante do que o comércio "
                      "intraindústrias nas relações comerciais entre países similares em termos de desenvolvimento "
                      "tecnológico e dotação de fatores de produção."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["relativamente"], "dificuldade": 1,
        "comentario_fonte": "Interindústria decorre de vantagens comparativas; entre países semelhantes há pouco "
                            "desse comércio; o intraindústria decorre de escala e concorrência monopolística e "
                            "existe mesmo sem diferenças de dotação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01158
    {
        "id": "ECO-E2-L01158-1", "fonte_ref": "E2-L01158", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Com relação às teorias do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Pela teoria do Ciclo-Produto, a produção de um novo modelo de veículo, com tecnologia "
                      "inovadora, tende a migrar para país com baixo custo de mão de obra logo que essa se torne "
                      "padronizada e pouco intensiva em pesquisa e trabalho qualificado, mesmo que esse país não "
                      "possua demanda interna pelo veículo que justifique o investimento em novas plantas "
                      "produtivas em seu território."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Pela teoria do Ciclo-Produto, a produção de um novo modelo de veículo, com tecnologia "
                       "inovadora, tende a migrar para país com baixo custo de mão de obra logo que essa se torne "
                       "padronizada e pouco intensiva em pesquisa e trabalho qualificado, ")
                    + vm("mesmo que esse país não possua") + az(" demanda interna pelo veículo que justifique o "
                                                                "investimento em novas plantas produtivas em seu "
                                                                "território.")),
        "poucas": ("Para a fonte, o erro está no final: no modelo de " + oc("Vernon") + ", a produção se "
                   "desloca para onde já existe " + azb("mercado") + " — os países que antes importavam o produto "
                   "e cuja demanda passa a justificar plantas locais."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O gabarito ERRADO se apoia na sequência clássica do ciclo: a produção sai primeiro para "
                          "outros países ricos cuja demanda, atendida antes por importações, passa a justificar a "
                          "fábrica local. Mas o próprio " + oc("Vernon") + " (1966) admite que, na fase de "
                          + azb("produto padronizado") + ", países em desenvolvimento podem receber a produção "
                          "como " + vm("plataforma de exportação") + ", atraídos só pelo custo da mão de obra, "
                          "sem mercado interno relevante. Por essa leitura, o item seria CERTO. Fica o gabarito "
                          "da fonte, com a ressalva.")],
        "destrinchando": [
            oc("Raymond Vernon") + " (“International Investment and International Trade in the Product Cycle”, "
            + vd("1966") + ") liga comércio e investimento externo ao " + azb("ciclo de vida do produto") + ". "
            "A vantagem comparativa deixa de ser estática: muda à medida que o produto amadurece.",
            vd("Fase 1 — produto novo") + ": a produção fica no país inovador (os EUA, no artigo), perto do "
            "mercado de alta renda e dos centros de P&amp;D; a tecnologia muda depressa, o preço importa pouco e o "
            "país exporta para outros ricos.",
            vd("Fase 2 — produto em amadurecimento") + ": a demanda cresce nos outros países ricos e a "
            "tecnologia se difunde; quando o mercado externo é grande o bastante e as tarifas e os fretes pesam, "
            "a empresa instala filiais lá (IED) para atender localmente. É aqui que a <b>demanda interna do "
            "destino</b> é condição para o investimento.",
            vd("Fase 3 — produto padronizado") + ": a concorrência passa a ser por custo; a produção migra para "
            "países de mão de obra barata, e o país de origem pode virar importador.",
            "Limites da teoria, apontados pelo próprio Vernon nos anos 1970: com multinacionais que lançam "
            "produtos ao mesmo tempo em vários mercados e fragmentam a produção em cadeias globais, o ciclo "
            "“EUA → outros ricos → periferia” ficou menos nítido.",
        ],
        "dissecando": (cz("[extrapolação]") + " Até “trabalho qualificado”, o item descreve a fase de padronização. "
                       "A banca enxertou a concessiva “mesmo que esse país não possua demanda interna”, que a fonte "
                       "trata como contrária ao pressuposto do modelo. Desconfie de concessivas que dispensam uma "
                       "condição da teoria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela teoria do ciclo do produto, a produção de um bem inovador tende a começar no país com maior "
            "dotação de tecnologia e mão de obra qualificada.”</i> → CERTO",
            "<i>“Na fase de produto novo, a produção é deslocada para países de baixo custo, pois a demanda é "
            "muito sensível ao preço.”</i> → ERRADO (inversão: no início a demanda é pouco sensível ao preço)",
        ])],
        "reescrita": ("Pela teoria do Ciclo-Produto, a produção de um novo modelo de veículo, com tecnologia "
                      "inovadora, tende a migrar para país com baixo custo de mão de obra logo que essa se torne "
                      "padronizada e pouco intensiva em pesquisa e trabalho qualificado, " + hl("desde que esse "
                      "país possua") + " demanda interna pelo veículo que justifique o investimento em novas plantas "
                      "produtivas em seu território."),
        "tipo_erro": ["EXTRAPOLACAO"], "moduladores": ["tende a", "logo que", "mesmo que"], "dificuldade": 3,
        "comentario_fonte": "Teoria de Vernon (1966); o erro está no final: os países que internalizavam a produção "
                            "eram os que antes importavam, de modo que a demanda interna era pressuposto. Fases de "
                            "introdução, crescimento e maturidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 192", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (curvas de produção e consumo por fase, descritas no 📖)"}],
        "alertas": ["contestavel: na fase de produto padronizado, Vernon admite produção em países de baixo custo "
                    "para exportação, sem mercado interno relevante; a leitura CERTO é defensável",
                    "quase_duplicata: ECO-E2-L01430-1 (ciclo do produto, versão CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L01428
    {
        "id": "ECO-E2-L01428-1", "fonte_ref": "E2-L01428", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_INT,
        "rotulo_item": "Item",
        "assertiva": ("A teoria da demanda de Linder busca explicar o comércio entre países com perfil de demanda "
                      "semelhante, sendo útil para explicar o comércio intrafirma."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A teoria da demanda de Linder busca explicar o comércio entre países com perfil de demanda "
                       "semelhante, sendo útil para explicar o comércio ") + vm("intrafirma") + az(".")),
        "poucas": ("A hipótese de " + oc("Linder") + " explica o comércio de manufaturas entre países de "
                   + azb("renda e demanda parecidas") + " — comércio " + azb("intraindustrial") + ". O comércio "
                   + vm("intrafirma") + " é assunto da teoria das multinacionais."),
        "destrinchando": [
            oc("Staffan Burenstam Linder") + " (<i>An Essay on Trade and Transformation</i>, " + vd("1961")
            + "): um país só exporta, com sucesso, manufaturas para as quais já tem " + azb("demanda interna "
            "representativa") + " — é o mercado doméstico que induz a inovação e a escala. Logo, exporta para "
            "países com padrão de demanda parecido, isto é, renda per capita parecida.",
            "Previsão: o comércio de manufaturas é mais intenso entre países de " + vd("renda per capita "
            "semelhante") + " — uma explicação pelo lado da <b>demanda</b>, oposta à de Heckscher-Ohlin (lado da "
            "oferta). Ajuda a entender o comércio Norte–Norte de produtos diferenciados (carros alemães × "
            "franceses), ou seja, o intraindustrial.",
            azb("Comércio intrafirma") + ": transações entre unidades da <b>mesma empresa</b> em países "
            "diferentes (matriz ↔ filial). É explicado pela teoria da " + azb("internalização") + " e pelos "
            "custos de transação (" + oc("Coase") + ", " + oc("Williamson") + "), pelo paradigma eclético OLI de "
            + oc("Dunning") + " e pela fragmentação vertical das cadeias. Estima-se que algo como um terço do "
            "comércio mundial seja intrafirma ⏳ (out/2026).",
            "Atenção aos três “intra”: " + vd("intraindustrial") + " (mesmo setor, empresas diferentes), "
            + vd("intrafirma") + " (mesma empresa, países diferentes) e " + vd("intrarregional") + " (dentro do "
            "mesmo bloco).",
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira oração é a definição correta de Linder; o erro está "
                       "na troca de “intraindustrial” por “intrafirma”, palavras parecidas com objetos diferentes. "
                       "🔥 Bancas de curso adoram empilhar inter/intra/intrafirma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A hipótese de Linder explica o comércio de manufaturas pelo lado da demanda, prevendo maior "
            "intercâmbio entre países de renda per capita semelhante.”</i> → CERTO",
            "<i>“A teoria de Linder explica o comércio de produtos primários entre países com dotações "
            "diferentes.”</i> → ERRADO (troca de conceito: isso é H-O)",
        ])],
        "reescrita": ("A teoria da demanda de Linder busca explicar o comércio entre países com perfil de demanda "
                      "semelhante, sendo útil para explicar o comércio " + hl("intraindustrial") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Linder (1961) explica o comércio entre países com demanda semelhante (renda per "
                            "capita); o comércio intrafirma é explicado por internalização, custos de transação e "
                            "estratégia das multinacionais. Trecho errado: “útil para explicar o comércio "
                            "intrafirma”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 337", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01429
    {
        "id": "ECO-E2-L01429-1", "fonte_ref": "E2-L01429", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_INT,
        "rotulo_item": "Item",
        "assertiva": ("A existência de retornos de escala crescentes na produção de vacinas pode, em determinadas "
                      "situações, tornar uma proteção comercial mais vantajosa que o livre comércio, por meio do "
                      "ganho de vantagens comparativas com o crescimento da escala de produção no país que "
                      "implementa a proteção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A existência de retornos de escala crescentes na produção de vacinas <u>pode, em "
                      "determinadas situações</u>, tornar uma proteção comercial mais vantajosa que o livre "
                      "comércio, por meio do ganho de vantagens comparativas com o crescimento da escala de "
                      "produção no país que implementa a proteção."),
        "poucas": ("Com " + azb("retornos crescentes") + ", a vantagem é construída pela escala: uma proteção "
                   "temporária pode deixar a indústria local “descer a curva de custo médio” e tornar-se "
                   "competitiva. Com “pode, em determinadas situações”, o item está certo."),
        "destrinchando": [
            "Nos modelos tradicionais, a vantagem comparativa é dada (tecnologia, dotações) e o livre-comércio é "
            "ótimo. Com " + azb("retornos crescentes") + ", ela passa a ser " + azb("criada") + ": quem produz "
            "mais fica mais barato, e o padrão de especialização pode refletir apenas quem começou primeiro.",
            "Exemplo de " + oc("Krugman e Obstfeld") + " (relógios): a Suíça domina o mercado por ter começado "
            "antes; a Tailândia teria custo menor em grande escala, mas, partindo do zero, seu custo inicial "
            + vd("C₀") + " supera o preço mundial " + vd("P₁") + ". Sem proteção, nunca entra; protegendo o "
            "mercado interno, ganha escala, pode chegar a " + vd("P₂ < P₁") + " e o mundo fica melhor.",
            "É a lógica da " + azb("indústria nascente") + " (" + oc("Hamilton") + ", " + oc("List") + ") e, em "
            "oligopólios, da " + azb("política comercial estratégica") + " (" + oc("Brander e Spencer") + "). "
            "Vacinas encaixam bem: P&amp;D e plantas com " + vd("custo fixo altíssimo") + " e forte aprendizado.",
            "Ressalvas que a banca pode cobrar: o argumento vale “em determinadas situações” — exige proteção "
            "temporária, escolha certa do setor (o governo não sabe quem será competitivo), risco de captura e "
            "de retaliação, e só se justifica se o ganho futuro compensar o custo presente para os consumidores.",
            "No " + rx("Brasil") + ", o argumento aparece no debate sobre o " + rx("Complexo Econômico-Industrial "
            "da Saúde") + " e a produção local de vacinas (Butantan, Bio-Manguinhos/Fiocruz), reforçado pela "
            "pandemia.",
        ],
        "grafico_verso": "ECO-E2-L01429-1-V1",
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " O item contraria o senso comum “livre "
                       "comércio é sempre melhor”, mas se protege com “pode, em determinadas situações”. Sem esse "
                       "modulador (“sempre torna a proteção mais vantajosa”), seria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de retornos crescentes torna a proteção comercial sempre superior ao "
            "livre-comércio.”</i> → ERRADO (modulador absoluto)",
            "<i>“Com economias externas de escala, o padrão de especialização pode ser determinado por acidentes "
            "históricos.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["pode", "em determinadas situações"],
        "dificuldade": 2,
        "comentario_fonte": "Argumento da indústria nascente / economias de escala dinâmicas: proteção temporária "
                            "permite descer a curva de custo médio e criar vantagem comparativa dinâmica; vacinas "
                            "têm altos custos fixos. Exemplo gráfico: Tailândia × Suíça (relógios).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 338", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01429-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01430
    {
        "id": "ECO-E2-L01430-1", "fonte_ref": "E2-L01430", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_INT,
        "rotulo_item": "Item",
        "assertiva": ("A teoria do ciclo de vida do produto, de Vernon, explica por que a produção de um bem "
                      "inovador pode iniciar-se num país com maior dotação de tecnologia e mão de obra qualificada, "
                      "e posteriormente, com a massificação, ser transferida para países com menores custos em "
                      "fatores de produção tradicional, como mão de obra barata."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria do ciclo de vida do produto, de Vernon, explica por que a produção de um bem "
                      "inovador pode iniciar-se num país com maior dotação de tecnologia e mão de obra qualificada, "
                      "e posteriormente, com a <u>massificação</u>, ser transferida para países com menores custos "
                      "em fatores de produção tradicional, como mão de obra barata."),
        "poucas": ("É o resumo do " + azb("ciclo do produto") + " de " + oc("Vernon") + ": o bem nasce no país "
                   "inovador e, ao se padronizar, sua produção migra para onde os fatores tradicionais são mais "
                   "baratos."),
        "destrinchando": [
            oc("Raymond Vernon") + " (" + vd("1966") + ") propôs uma " + azb("vantagem comparativa dinâmica")
            + ": a localização ótima da produção muda conforme o produto envelhece.",
            vd("Introdução") + ": produto novo, tecnologia instável, demanda pouco sensível ao preço. Produz-se "
            "no país inovador (rico, com P&amp;D e mão de obra qualificada), perto do consumidor de alta renda, e "
            "exporta-se para outros ricos.",
            vd("Massificação / maturidade") + ": a tecnologia se difunde, a demanda cresce no exterior e a "
            "empresa instala filiais nos outros países ricos que antes importavam (IED defensivo, para não perder "
            "o mercado para imitadores).",
            vd("Padronização") + ": o produto vira commodity tecnológica, a concorrência é por preço e a "
            "produção vai para países de mão de obra barata; o país de origem passa a importar.",
            "Lições para a prova: (1) a teoria liga " + azb("comércio e investimento direto") + " numa só "
            "explicação; (2) trabalha com " + azb("concorrência imperfeita") + " e inovação, ao contrário de H-O; "
            "(3) explica por que o mesmo bem muda de exportador ao longo do tempo (rádios, TVs, têxteis).",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Reproduz as fases sem exagero (“pode "
                       "iniciar-se”). Versões erradas costumam inverter a ordem (começar no país de mão de obra "
                       "barata) ou acrescentar condições estranhas ao modelo, como dispensar a demanda interna do "
                       "país que recebe a produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela teoria do ciclo do produto, a produção de um bem inovador começa em países de baixo custo de "
            "mão de obra e migra, com a maturidade, para países desenvolvidos.”</i> → ERRADO (inversão da "
            "sequência)",
            "<i>“A teoria do ciclo do produto articula comércio internacional e investimento direto "
            "estrangeiro.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Vernon: produção começa no país inovador (P&D, feedback) e, com a padronização e a "
                            "massificação, transfere-se para países com mão de obra mais barata.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 339", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01158-1 (ciclo do produto, versão ERRADO com a concessiva sobre a "
                    "demanda interna)"],
    },
    # ------------------------------------------------------------------ E2-L01575
    {
        "id": "ECO-E2-L01575-1", "fonte_ref": "E2-L01575", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("A diferenciação de produto, bem como os retornos crescentes de escala, permitiram a "
                      "explicação de padrões de comércio entre países com dotações de fatores semelhantes, que "
                      "escapava ao modelo de Heckscher-Ohlin."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A diferenciação de produto, bem como os retornos crescentes de escala, permitiram a "
                      "explicação de padrões de comércio entre países com dotações de fatores <u>semelhantes</u>, "
                      "que <u>escapava</u> ao modelo de Heckscher-Ohlin."),
        "poucas": ("H-O prevê comércio entre países " + azb("diferentes") + "; o intenso comércio entre países "
                   "ricos e parecidos só foi explicado quando a Nova Teoria introduziu " + azb("diferenciação")
                   + " e " + azb("retornos crescentes") + "."),
        "destrinchando": [
            "No modelo de " + oc("Heckscher-Ohlin") + ", cada país exporta o bem intensivo no fator que tem em "
            "abundância. Se as dotações são iguais, os preços relativos de autarquia coincidem e "
            + vm("não há motivo para comerciar") + ". O modelo supõe bens homogêneos, retornos constantes e "
            "concorrência perfeita.",
            "Os dados contrariavam isso: a maior parte do comércio mundial ocorre entre os países "
            + vd("desenvolvidos") + ", de dotações parecidas, e muito dele é de produtos do mesmo setor. Somou-se "
            "o " + azb("paradoxo de Leontief") + " (1953): os EUA, abundantes em capital, exportavam bens "
            "relativamente intensivos em trabalho.",
            "A partir dos anos 1960, surgiram explicações que não se baseiam em vantagens comparativas: "
            "tecnologia (hiato tecnológico de " + oc("Posner") + ", ciclo do produto de " + oc("Vernon")
            + "), demanda (" + oc("Linder") + ") e, sobretudo nos anos 1970–80, a " + azb("Nova Teoria do "
            "Comércio") + " de " + oc("Krugman") + ", " + oc("Helpman") + " e " + oc("Lancaster") + ".",
            "O mecanismo: retornos crescentes limitam o número de variedades que cada país produz; consumidores "
            "valorizam a variedade; daí a troca de variedades do mesmo bem entre países iguais "
            "(" + azb("comércio intraindústria") + "), com ganhos de escala e de variedade.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de manual, bem calibrado. O risco é o candidato achar que "
                       "a Nova Teoria “reforça” ou “é um caso de” H-O; versões erradas costumam trocar "
                       "“semelhantes” por “diferentes” ou “escapava” por “confirmava”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferenciação de produto e os retornos crescentes reforçam as conclusões do modelo de "
            "Heckscher-Ohlin.”</i> → ERRADO (explicam o que H-O não explicava)",
            "<i>“…permitiram explicar o comércio entre países com dotações muito diferentes, que escapava ao "
            "modelo de Heckscher-Ohlin.”</i> → ERRADO (H-O explica justamente esse caso)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "H-O explica o comércio por diferenças de dotação e não explicava o intenso comércio "
                            "entre países desenvolvidos semelhantes; a Nova Teoria (Krugman) incorporou "
                            "diferenciação e escala. Slides sobre os limites da abordagem tradicional.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 433", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 434", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01692-1 (mesmo começo, versão “reforçam as conclusões”, ERRADO)"],
    },
    # ------------------------------------------------------------------ E2-L01669
    {
        "id": "ECO-E2-L01669-1", "fonte_ref": "E2-L01669", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a nova teoria do comércio internacional, a dotação relativa de fatores de produção "
                      "exerce influência significativa sobre o padrão de comércio entre os países, explicando a "
                      "maior parte do volume de comércio entre os países industrializados."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a nova teoria do comércio internacional, a dotação relativa de fatores de "
                       "produção exerce influência significativa sobre o padrão de comércio entre os países, "
                       "explicando ") + vm("a maior parte do volume de comércio entre os países industrializados")
                    + az(".")),
        "poucas": ("O grosso do comércio entre países industrializados é " + azb("intraindustrial") + " e, para a "
                   "Nova Teoria, decorre de " + azb("escala e diferenciação") + "; a dotação de fatores explica "
                   "o componente interindustrial entre países diferentes."),
        "destrinchando": [
            "A dotação relativa de fatores é o motor do modelo de " + oc("Heckscher-Ohlin") + ": cada país "
            "exporta o bem intensivo no fator abundante. Ela explica bem o " + azb("comércio interindustrial")
            + " entre países <b>diferentes</b> (Norte–Sul: manufaturas × alimentos e matérias-primas).",
            "A Nova Teoria (" + oc("Krugman") + ", anos 1980) surgiu justamente porque a dotação de fatores "
            + vm("não explicava") + " o comércio entre países industrializados: dotações parecidas, enorme "
            "volume de trocas, muitas delas de produtos do mesmo setor.",
            "Nos modelos de síntese (" + oc("Helpman-Krugman") + ") a dotação continua relevante: determina o "
            "componente interindustrial e o saldo líquido setorial de cada país. Por isso a primeira parte do "
            "item (influência significativa sobre o padrão) se sustenta; o erro está em lhe atribuir a maior "
            "parte do comércio entre industrializados.",
            "Medida: o " + azb("índice de Grubel-Lloyd") + " é alto (próximo de 1) no comércio entre países "
            "europeus, EUA e Japão, e baixo no comércio entre países de dotações muito distintas.",
            vm("Regra-âncora: dotação de fatores → comércio interindustrial entre diferentes; escala e "
               "diferenciação → comércio intraindustrial entre semelhantes."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Começa com algo defensável (a dotação influi "
                       "no padrão de comércio) e enxerta a conclusão de H-O que a Nova Teoria veio corrigir. Pista: "
                       "“países industrializados” é o terreno onde a Nova Teoria nasceu."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a nova teoria do comércio internacional, economias de escala e diferenciação de "
            "produtos explicam boa parte do comércio entre países industrializados.”</i> → CERTO",
            "<i>“Segundo o modelo de Heckscher-Ohlin, países com dotações idênticas comerciam intensamente "
            "bens do mesmo setor.”</i> → ERRADO (com dotações idênticas, H-O não prevê comércio)",
        ])],
        "reescrita": ("Segundo a nova teoria do comércio internacional, a dotação relativa de fatores de produção "
                      "exerce influência significativa sobre o padrão de comércio entre os países, explicando "
                      + hl("o comércio interindustrial entre países com dotações distintas") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["a maior parte"], "dificuldade": 2,
        "comentario_fonte": "A explicação pela dotação de fatores é a essência de H-O; a Nova Teoria surgiu porque "
                            "ela não explicava o comércio intraindustrial entre países industrializados, enfatizando "
                            "escala, diferenciação e concorrência imperfeita.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 486", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: “comercio” → “comércio” (acento ausente na fonte)"],
    },
    # ------------------------------------------------------------------ E2-L01670
    {
        "id": "ECO-E2-L01670-1", "fonte_ref": "E2-L01670", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("Ganhos de escala e concorrência imperfeita são alguns dos temas tratados pela nova teoria do "
                      "comércio internacional, que busca explicar o padrão de comércio entre países com dotações de "
                      "fatores semelhantes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ganhos de escala e concorrência imperfeita são <u>alguns dos temas</u> tratados pela nova "
                      "teoria do comércio internacional, que busca explicar o padrão de comércio entre países com "
                      "dotações de fatores <u>semelhantes</u>."),
        "poucas": (azb("Escala") + " e " + azb("concorrência imperfeita") + " (com diferenciação) são os pilares "
                   "da Nova Teoria, criada para explicar o comércio entre países parecidos."),
        "destrinchando": [
            "Os três pilares da Nova Teoria do Comércio: " + vd("retornos crescentes de escala") + " (internos "
            "ou externos à firma), " + vd("concorrência imperfeita") + " (monopolística ou oligopólio) e "
            + vd("diferenciação de produtos") + " com gosto dos consumidores pela variedade.",
            "Resultado central de " + oc("Krugman") + " (1979): mesmo entre países " + azb("idênticos")
            + " em tecnologia e dotações, há comércio — cada um se especializa em variedades diferentes para "
            "aproveitar a escala, e ambos ganham com mais variedade e custos médios menores.",
            "Contribuições vizinhas: " + oc("Helpman") + " (síntese com H-O), " + oc("Brander e Spencer")
            + " (política comercial estratégica em oligopólio), " + oc("Krugman") + " (1991, “nova geografia "
            "econômica”, aglomeração centro–periferia). Krugman recebeu o Nobel em " + vd("2008") + " “pela "
            "análise dos padrões de comércio e da localização da atividade econômica”.",
            "Mais tarde veio a “nova nova teoria do comércio” de " + oc("Melitz") + " (" + vd("2003") + "), com "
            "firmas heterogêneas: só as mais produtivas exportam, e a abertura realoca produção para elas.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " “Alguns dos temas” evita a armadilha da "
                       "lista exaustiva. A versão errada mais comum troca “semelhantes” por “diferentes”, ou "
                       "atribui à Nova Teoria a concorrência perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…que busca explicar o padrão de comércio entre países com dotações de fatores muito "
            "diferentes.”</i> → ERRADO (isso é H-O)",
            "<i>“Ganhos de escala e concorrência perfeita são os fundamentos da nova teoria do comércio.”</i> → "
            "ERRADO (a concorrência é imperfeita)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["alguns dos"], "dificuldade": 1,
        "comentario_fonte": "A NTT foca em ganhos de escala e concorrência imperfeita (com diferenciação) para "
                            "explicar o comércio entre países semelhantes, inclusive intraindustrial (Krugman, Nobel "
                            "2008).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01692
    {
        "id": "ECO-E2-L01692-1", "fonte_ref": "E2-L01692", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("A diferenciação de produto, bem como os retornos crescentes de escala, reforçam as conclusões "
                      "da teoria que explica a origem das vantagens comparativas nas diferenças entre as dotações "
                      "relativas de fatores de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A diferenciação de produto, bem como os retornos crescentes de escala, ")
                    + vm("reforçam as conclusões da") + az(" teoria que explica a origem das vantagens comparativas "
                                                           "nas diferenças entre as dotações relativas de fatores "
                                                           "de produção.")),
        "poucas": ("A teoria das dotações é a de " + oc("Heckscher-Ohlin") + ", que supõe bens homogêneos e "
                   "retornos constantes. Diferenciação e retornos crescentes " + vm("não a reforçam") + ": explicam "
                   "o comércio que ela não previa."),
        "destrinchando": [
            "A “teoria que explica a origem das vantagens comparativas nas diferenças entre as dotações relativas "
            "de fatores” é o modelo " + azb("Heckscher-Ohlin") + " (" + oc("Heckscher") + ", 1919; "
            + oc("Ohlin") + ", 1933; formalizado por " + oc("Samuelson") + "). Hipóteses: dois fatores, "
            "tecnologias iguais, " + vd("bens homogêneos") + ", " + vd("retornos constantes") + ", concorrência "
            "perfeita.",
            "Diferenciação e retornos crescentes são justamente as hipóteses que H-O exclui. Ao incluí-las, a "
            + azb("Nova Teoria do Comércio") + " (" + oc("Krugman") + ") mostra que há comércio "
            + azb("mesmo sem diferença de dotações") + " — o comércio intraindústria entre países semelhantes.",
            "As duas abordagens são " + vd("complementares") + ", não uma reforço da outra: nos modelos de síntese, "
            "a diferença de dotações gera o comércio interindústria e a escala com diferenciação gera o "
            "intraindústria. Quanto mais parecidos os países, menos H-O explica.",
            "Nuance: com retornos crescentes, a especialização pode ser fruto de acaso histórico, e o padrão de "
            "comércio deixa de ser determinado pelas dotações — o que, em alguns casos, leva a resultados "
            "diferentes dos de H-O.",
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " O item cria uma relação de reforço entre teorias que "
                       "competem: os elementos citados ampliam (ou contestam) a explicação por dotações, não a "
                       "confirmam. Pista: a teoria descrita por perífrase é H-O, cujas hipóteses excluem "
                       "diferenciação e escala crescente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferenciação de produto e os retornos crescentes de escala permitiram explicar o comércio "
            "entre países com dotações semelhantes, que escapava ao modelo de Heckscher-Ohlin.”</i> → CERTO",
            "<i>“O modelo de Heckscher-Ohlin pressupõe retornos crescentes de escala.”</i> → ERRADO (supõe "
            "retornos constantes)",
        ])],
        "reescrita": ("A diferenciação de produto, bem como os retornos crescentes de escala, " + hl("explicam "
                      "padrões de comércio não previstos pela") + " teoria que explica a origem das vantagens "
                      "comparativas nas diferenças entre as dotações relativas de fatores de produção."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Diferenciação e retornos crescentes são conceitos da Nova Teoria, que critica e "
                            "complementa H-O, sem reforçá-lo; H-O supõe retornos constantes e bens homogêneos. "
                            "Trecho errado: “reforçam as conclusões”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01575-1 (mesmo começo, versão CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L01765
    {
        "id": "ECO-E2-L01765-1", "fonte_ref": "E2-L01765", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito da teoria do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("As novas teorias do comércio internacional, como as teorias baseadas em ganhos de escala e na "
                      "diferenciação de produto, explicam o comércio entre países com dotações de fatores "
                      "diferentes, ao passo que o modelo Heckscher-Ohlin explica o comércio entre países que têm "
                      "dotações de fatores semelhantes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As novas teorias do comércio internacional, como as teorias baseadas em ganhos de escala e "
                       "na diferenciação de produto, explicam o comércio entre países com dotações de fatores ")
                    + vm("diferentes") + az(", ao passo que o modelo Heckscher-Ohlin explica o comércio entre "
                                            "países que têm dotações de fatores ") + vm("semelhantes") + az(".")),
        "poucas": ("Está invertido: " + oc("Heckscher-Ohlin") + " explica o comércio entre dotações "
                   + vd("diferentes") + "; as novas teorias, o comércio entre dotações " + vd("semelhantes") + "."),
        "destrinchando": [
            azb("Heckscher-Ohlin") + ": o comércio nasce da " + azb("diferença") + " de dotações relativas. O país "
            "abundante em capital exporta bens intensivos em capital; o abundante em trabalho, bens intensivos em "
            "trabalho. Sem diferença de dotações (e com tecnologia igual), não há comércio no modelo.",
            azb("Novas teorias") + " (" + oc("Krugman") + ", " + oc("Helpman") + ", " + oc("Lancaster") + "): "
            "economias de escala e diferenciação geram comércio " + azb("mesmo entre países iguais") + ", "
            "principalmente intraindústria — o que explica o grande volume de trocas entre economias "
            "desenvolvidas.",
            "Tabela mental: " + vd("Ricardo") + " → diferença de tecnologia; " + vd("H-O") + " → diferença de "
            "dotações; " + vd("Linder") + " → semelhança de demanda; " + vd("Krugman") + " → escala e variedade, "
            "países semelhantes; " + vd("Vernon") + " → ciclo do produto, vantagem dinâmica.",
            vm("Regra-âncora: H-O precisa de diferença; a Nova Teoria funciona com semelhança."),
        ],
        "dissecando": (cz("[inversão]") + " Os dois polos foram trocados entre si; cada metade, isolada, soa "
                       "familiar. Teste rápido: pergunte “sem diferença de dotação, H-O prevê comércio?” — não; "
                       "logo, H-O não pode ser a teoria das dotações semelhantes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As novas teorias explicam o comércio entre países com dotações semelhantes, ao passo que H-O "
            "explica o comércio entre países com dotações diferentes.”</i> → CERTO",
            "<i>“As novas teorias negam qualquer papel das dotações de fatores no padrão de comércio.”</i> → "
            "ERRADO (modulador absoluto: nos modelos de síntese elas explicam o componente interindústria)",
        ])],
        "reescrita": ("As novas teorias do comércio internacional, como as teorias baseadas em ganhos de escala e na "
                      "diferenciação de produto, explicam o comércio entre países com dotações de fatores "
                      + hl("semelhantes") + ", ao passo que o modelo Heckscher-Ohlin explica o comércio entre "
                      "países que têm dotações de fatores " + hl("diferentes") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A assertiva inverte os modelos: H-O explica o comércio entre dotações diferentes; as "
                            "novas teorias, o comércio intraindústria entre dotações semelhantes.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00084
    {
        "id": "ECO-E3-L00084-1", "fonte_ref": "E3-L00084", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": ("O modelo de vantagens comparativas de David Ricardo é um dos principais modelos de teoria "
                    "econômica e é amplamente utilizado para explicar relações de trocas em diferentes contextos. "
                    "No que se refere a esse modelo, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Na existência de economias de escala na produção de um bem, a fronteira de possibilidades "
                      "de produção de um país é linear."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na existência de economias de escala na produção de um bem, a fronteira de possibilidades "
                       "de produção de um país ") + vm("é linear") + az(".")),
        "poucas": ("FPP linear = " + azb("custo de oportunidade constante") + " (Ricardo, retornos constantes). Com "
                   "economias de escala, o custo de oportunidade " + vd("cai") + " com a especialização e a FPP "
                   "tende a ficar " + azb("convexa em relação à origem") + " (curvada para dentro)."),
        "destrinchando": [
            "A inclinação da FPP é a " + azb("taxa marginal de transformação") + " — quanto de Y se sacrifica "
            "por uma unidade a mais de X. A forma da curva diz como esse custo varia.",
            vd("Reta") + ": custo de oportunidade constante. É o caso de " + oc("Ricardo") + ": um só fator "
            "(trabalho), produtividade constante, retornos constantes de escala.",
            vd("Côncava em relação à origem") + " (abaulada para fora): custo de oportunidade " + azb("crescente")
            + ", porque os recursos não são igualmente bons para os dois bens ou há rendimentos decrescentes. É a "
            "FPP “padrão” dos manuais e a do modelo de fatores específicos e de H-O.",
            vd("Convexa em relação à origem") + " (curvada para dentro): custo de oportunidade "
            + azb("decrescente") + ". Ocorre com " + azb("economias de escala") + ": quanto mais o país produz "
            "de X, mais produtivo fica nele, e cada unidade extra custa menos Y.",
            "Consequência para o comércio: com FPP convexa, a especialização tende a ser " + vd("completa")
            + " (soluções de canto), e o padrão de especialização pode depender de quem começou primeiro — base da "
            "Nova Teoria do Comércio (" + oc("Krugman") + ").",
            "Cuidado com a terminologia: parte do material de estudo chama a curva das economias de escala de "
            "“côncava” — é erro. Côncava (para fora) é a dos custos crescentes; a das economias de escala é a "
            "convexa (para dentro).",
        ],
        "grafico_verso": "ECO-E3-L00084-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item associa economias de escala à forma que corresponde ao "
                       "custo de oportunidade constante. O comando, centrado em Ricardo, induz a pensar em FPP reta; "
                       "mas a hipótese do item (escala crescente) tira o modelo do mundo ricardiano."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, com um único fator e produtividade constante, a FPP é linear.”</i> → CERTO",
            "<i>“Com economias de escala, a FPP é côncava em relação à origem, refletindo custos de oportunidade "
            "crescentes.”</i> → ERRADO (troca de conceito: custo decrescente, FPP convexa)",
        ])],
        "reescrita": ("Na existência de economias de escala na produção de um bem, a fronteira de possibilidades de "
                      "produção de um país " + hl("deixa de ser linear e tende a ser convexa em relação à origem")
                      + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Vários comentários empilhados; concordam que a FPP linear supõe custos constantes, mas "
                            "divergem sobre a forma com economias de escala (alguns dizem “côncava”, outros "
                            "“convexa em relação à origem”, com custos decrescentes).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 41", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (ilegível na transcrição)"},
                          {"ref": "IMAGEM 42", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (ilegível na transcrição)"}],
        "alertas": ["qualidade_fonte: parte dos comentários afirma que economias de escala geram FPP “côncava” "
                    "(curvada para fora); o correto é convexa em relação à origem (custos de oportunidade "
                    "decrescentes) — corrigido"],
    },
    # ------------------------------------------------------------------ E3-L00221
    {
        "id": "ECO-E3-L00221-1", "fonte_ref": "E3-L00221", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": "Acerca da teoria do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de concorrência monopolística centrado na produção de manufaturas, um país tanto "
                      "produzirá e exportará bens manufaturados como também os importará, alimentando assim o "
                      "comércio intraindústrias e gerando ganhos extras no comércio internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de concorrência monopolística centrado na produção de manufaturas, um país "
                      "<u>tanto</u> produzirá e exportará bens manufaturados <u>como também os importará</u>, "
                      "alimentando assim o comércio intraindústrias e gerando <u>ganhos extras</u> no comércio "
                      "internacional."),
        "poucas": ("Com variedades diferenciadas e escala, cada país exporta algumas manufaturas e importa outras: "
                   "é o " + azb("comércio intraindústrias") + ", que soma ganhos de " + vd("variedade") + " e de "
                   + vd("escala") + " aos ganhos da vantagem comparativa."),
        "destrinchando": [
            "No modelo de " + azb("concorrência monopolística") + " (" + oc("Krugman") + ", com base em "
            + oc("Dixit-Stiglitz") + "), cada firma produz uma variedade própria com " + azb("economias de "
            "escala internas") + ". O número de variedades que um mercado comporta é limitado pelo seu tamanho.",
            "A abertura junta os mercados: o mercado integrado comporta mais firmas, cada uma maior. Os "
            "consumidores ganham em " + vd("variedade") + " e em " + vd("custo médio menor") + " (mais escala "
            "por firma); as firmas menos eficientes saem.",
            "Como as variedades são diferentes, o país exporta as suas e importa as do outro — carros alemães "
            "para o Japão e carros japoneses para a Alemanha. Nos modelos de síntese, o país abundante em "
            "capital é exportador " + azb("líquido") + " de manufaturas, mas também as importa.",
            "Os “ganhos extras” são esses ganhos de variedade e escala, que se somam aos da especialização por "
            "vantagem comparativa (" + oc("Krugman e Obstfeld") + "). Além disso, o comércio intraindústria "
            "gera menos conflito distributivo: os trabalhadores não precisam mudar de setor.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Descreve corretamente o resultado do modelo. A dúvida possível é "
                       "“ganhos extras” — extras em relação aos da vantagem comparativa, e é isso mesmo que o "
                       "modelo mostra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de concorrência monopolística, cada país se especializa completamente em um setor, "
            "eliminando o comércio intraindústrias.”</i> → ERRADO (inversão: o modelo gera comércio "
            "intraindústrias)",
            "<i>“A integração de mercados em concorrência monopolística aumenta o número de variedades "
            "disponíveis ao consumidor.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Produtos diferenciados e amor à variedade: a Alemanha exporta BMWs ao Japão e importa "
                            "Toyotas; comércio intraindústria e ganhos de bem-estar pela variedade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00430
    {
        "id": "ECO-E3-L00430-1", "fonte_ref": "E3-L00430", "destino": "75", "subtema": H2["ntc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": ("A partir da interpretação das teorias clássicas de comércio, a abertura ao comércio "
                    "internacional leva a um aumento do bem-estar social [...]. Considerando as diferentes "
                    "estruturas de mercado e as interpretações das teorias de comércio mais modernas, julgue o "
                    "item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Segundo o modelo desenvolvido por Krugman em 1979, a abertura ao comércio internacional, em "
                      "um modelo de concorrência monopolista, pode levar ao aumento da variedade de bens disponíveis "
                      "para os consumidores, mas não necessariamente à redução dos preços no mercado interno."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o modelo desenvolvido por Krugman em 1979, a abertura ao comércio internacional, em "
                      "um modelo de concorrência monopolista, <u>pode</u> levar ao aumento da variedade de bens "
                      "disponíveis para os consumidores, mas <u>não necessariamente</u> à redução dos preços no "
                      "mercado interno."),
        "poucas": ("O ganho típico do comércio em " + oc("Krugman") + " é a " + azb("variedade") + ": mais marcas "
                   "disponíveis. A queda de preços pode ocorrer, mas depende do markup e da escala — por isso o "
                   "“não necessariamente” torna o item certo."),
        "destrinchando": [
            oc("Paul Krugman") + ", “Increasing Returns, Monopolistic Competition, and International Trade” "
            "(<i>Journal of International Economics</i>, " + vd("1979") + "): dois países idênticos, um fator, "
            "firmas com custo fixo (escala interna) e consumidores com gosto pela variedade. Mesmo sem nenhuma "
            "vantagem comparativa, há comércio e ganho mútuo.",
            "Canal da " + azb("variedade") + ": com o mercado integrado, o consumidor tem acesso às variedades "
            "dos dois países. É o ganho que o modelo destaca e que as teorias clássicas não captam.",
            "Canal do " + azb("preço") + ": na versão de 1979, a ampliação do mercado aumenta a escala das firmas "
            "e pode reduzir o preço relativo ao salário (efeito pró-competitivo). Na formulação com elasticidade "
            "constante (" + oc("Krugman") + ", " + vd("1980") + "), o markup é fixo e o preço não muda: o ganho "
            "vem só da variedade. Daí o “não necessariamente”.",
            "Exemplo: após a abertura dos anos 1990, o consumidor " + rx("brasileiro") + " passou a ter acesso a "
            "dezenas de marcas de automóveis; mesmo sem queda proporcional de preço, o bem-estar subiu pela "
            "diversidade.",
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " “Pode levar” e “não necessariamente” protegem o "
                       "item: ele não nega que os preços possam cair, só que caiam obrigatoriamente. A banca "
                       "testaria o contrário com “necessariamente reduz os preços” ou “não altera a variedade”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Krugman (1979), o ganho do comércio decorre exclusivamente da especialização "
            "segundo as vantagens comparativas.”</i> → ERRADO (troca de conceito: o ganho vem de escala e "
            "variedade, mesmo entre países idênticos)",
            "<i>“No modelo de Krugman (1979), há comércio mesmo entre países idênticos em tecnologia e "
            "dotações.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["pode", "não necessariamente"],
        "dificuldade": 2,
        "comentario_fonte": "Krugman (1979): economias de escala e amor à variedade; o ganho vem principalmente da "
                            "variedade; o preço depende do markup e da elasticidade e pode não cair. Exemplo dos "
                            "carros no Brasil.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 596", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_parcial: o texto motivador vem truncado na fonte (“…”); mantido com [...]"],
    },
    # ------------------------------------------------------------------ E1-0443
    {
        "id": "ECO-E1-0443-1", "fonte_ref": "E1-0443", "destino": "76", "subtema": H2["cgv"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Conflitos comerciais entre países, conhecidos como guerras comerciais, têm se tornado eventos "
                    "recorrentes na economia global contemporânea. Geralmente caracterizadas pela imposição "
                    "recíproca de tarifas, essas disputas afetam tanto o fluxo de bens quanto as expectativas dos "
                    "agentes econômicos. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Guerras comerciais, ao comprometerem a previsibilidade do ambiente econômico internacional, "
                      "tendem a reduzir os investimentos produtivos, em especial aqueles voltados a cadeias de "
                      "suprimento transnacionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Guerras comerciais, ao comprometerem a previsibilidade do ambiente econômico internacional, "
                      "<u>tendem a</u> reduzir os investimentos produtivos, em especial aqueles voltados a cadeias "
                      "de suprimento transnacionais."),
        "poucas": ("Tarifas recíprocas elevam a " + azb("incerteza") + " sobre o acesso futuro a mercados; como o "
                   "investimento produtivo é irreversível, as empresas adiam projetos — sobretudo os que dependem "
                   "de " + azb("cadeias transnacionais") + ", que cruzam várias fronteiras."),
        "destrinchando": [
            "Investimento produtivo tem custo afundado: uma fábrica não se desmonta se a tarifa mudar. Pela teoria "
            "da " + azb("opção de esperar") + " (" + oc("Dixit e Pindyck") + ", <i>Investment under "
            "Uncertainty</i>, 1994), quanto maior a incerteza, maior o valor de adiar a decisão.",
            "As " + azb("cadeias globais de valor") + " são as mais expostas: um insumo pode cruzar fronteiras "
            "várias vezes antes do produto final, e cada travessia sofre a tarifa — o efeito se acumula "
            "(“efeito cascata”). Uma mudança de regra pode inviabilizar a localização escolhida.",
            "Evidência: a guerra comercial EUA–China (" + vd("2018–2019") + ") elevou os índices de incerteza de "
            "política comercial e foi associada a queda do investimento; o FMI e a UNCTAD apontaram "
            "desaceleração do comércio e do IED. As empresas reagiram com " + azb("diversificação") + " ("
            "“China + 1”), " + azb("nearshoring") + " e " + azb("friendshoring") + ".",
            "Efeito colateral: o desvio de comércio pode favorecer terceiros países (Vietnã, México) — e o "
            + rx("Brasil") + " ganhou mercado de soja na China em 2018. Mas o efeito agregado sobre o investimento "
            "global é negativo ⏳ (out/2026).",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Raciocínio econômico padrão, protegido por "
                       "“tendem a”. Versões erradas trocariam o sentido (“estimulam o investimento em cadeias "
                       "transnacionais”) ou absolutizariam (“eliminam”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Guerras comerciais, ao elevarem tarifas, estimulam o investimento em cadeias de suprimento "
            "transnacionais.”</i> → ERRADO (inversão)",
            "<i>“Guerras comerciais podem beneficiar terceiros países por meio do desvio de comércio.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": "A incerteza das guerras comerciais aumenta o risco percebido dos investimentos de "
                            "longo prazo; as empresas hesitam, sobretudo em cadeias globais de valor.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
