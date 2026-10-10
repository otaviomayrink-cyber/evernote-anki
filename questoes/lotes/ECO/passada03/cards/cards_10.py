"""Cards do lote de redação 10 — ECO, passada 03 (notas 69: câmbio-juros-inflação; 70: IS-LM-BP)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "par": "🔗 Paridades e repasse cambial",
    "bp": "📍 Curva BP e mobilidade de capital",
    "fixo": "🔒 Câmbio fixo",
    "flut": "🌊 Câmbio flutuante",
}

CMD_RT_JUROS = ("Recentemente o Banco Central iniciou um ciclo de alta dos juros, tendo em vista as pressões "
                "inflacionárias na economia brasileira. Sobre este tema, avalie as proposições abaixo.")

CMD_RT_ABERTA = "A respeito dos conceitos e teorias da macroeconomia aberta, julgue o item (C ou E)."

CMD_RT_CAMBIO = ("A respeito dos conceitos de taxa de câmbio e das relações entre câmbio, juros e inflação, julgue "
                 "o item (C ou E).")

CMD_NIDI_PRECOS = ("A compreensão da macroeconomia e dos seus agregados depende de algumas variáveis-chave, em "
                   "especial, depende daquilo que alguns autores chamam de preços fundamentais, dentre os quais "
                   "encontramos: i) a taxa de câmbio, o preço da moeda nacional em termos de moedas estrangeiras, "
                   "ii) a taxa de juros, o preço intertemporal da moeda nacional em termos da própria moeda "
                   "nacional, iii) a taxa de lucro e outros. A respeito da taxa de câmbio e taxa de juros, julgue "
                   "os itens a seguir (C ou E).")

CARDS = [
    # ------------------------------------------------------------------ E2-L01581
    {
        "id": "ECO-E2-L01581-1", "fonte_ref": "E2-L01581", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_JUROS,
        "rotulo_item": "Item",
        "assertiva": ("A elevação dos juros, <i>ceteris paribus</i>, tem como efeito a apreciação cambial, que acaba "
                      "tendo efeito contrário ao desejado pela autoridade monetária por pressionar para cima a taxa "
                      "de inflação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elevação dos juros, <i>ceteris paribus</i>, tem como efeito a apreciação cambial, que "
                       "acaba tendo efeito ") + vm("contrário ao") + az(" desejado pela autoridade monetária por ")
                    + vm("pressionar para cima") + az(" a taxa de inflação.")),
        "poucas": ("A primeira metade está certa (juros ↑ → entrada de capital → " + azb("apreciação") + "), mas a "
                   "apreciação barateia importados e " + vm("reduz") + " a inflação: ela reforça, e não contraria, "
                   "o aperto monetário."),
        "destrinchando": [
            "Juros domésticos mais altos, com o resto constante, elevam o retorno dos ativos em reais em relação "
            "aos externos. Pela " + azb("paridade de juros") + " (i = i* + desvalorização esperada + prêmio de "
            "risco), o diferencial atrai capital, aumenta a oferta de dólares e " + vd("aprecia") + " a moeda "
            "nacional.",
            "Com o real apreciado: (1) bens finais importados ficam mais baratos em reais; (2) insumos importados "
            "e " + azb("commodities") + " cotadas em dólar (combustíveis, trigo, fertilizantes) pesam menos nos "
            "custos; (3) a concorrência externa limita reajustes dos bens comercializáveis. Resultado: efeito "
            + vd("desinflacionário") + ".",
            "Por isso o " + azb("canal do câmbio") + " é um dos canais de transmissão da política monetária, ao "
            "lado do canal do crédito, da demanda agregada e das expectativas. Em economias abertas e com alto "
            "repasse cambial, como a " + rx("brasileira") + ", ele costuma ser o canal mais rápido de chegada "
            "dos juros aos preços.",
            "Efeito colateral real existe, mas é outro: a apreciação reduz a competitividade das exportações e "
            "piora o saldo comercial — o que também esfria a demanda e, de novo, ajuda a conter a inflação.",
            vm("Regra-âncora: juros ↑ → câmbio aprecia → inflação ↓ (o câmbio trabalha a favor do BC)."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " O item começa com o elo verdadeiro (juros → "
                       "apreciação) e enxerta no fim o sinal invertido do efeito da apreciação sobre os preços. A "
                       "pista é o “efeito contrário ao desejado”: se o câmbio apreciado barateia importados, ele só "
                       "pode ajudar quem quer derrubar a inflação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação dos juros tende a apreciar o câmbio, o que reforça o efeito desinflacionário da "
            "política monetária.”</i> → CERTO",
            "<i>“A redução dos juros tende a apreciar o câmbio, reforçando o combate à inflação.”</i> → ERRADO "
            "(inversão: corte de juros deprecia o câmbio)",
        ])],
        "reescrita": ("A elevação dos juros, <i>ceteris paribus</i>, tem como efeito a apreciação cambial, que acaba "
                      "tendo efeito " + hl("alinhado ao") + " desejado pela autoridade monetária por "
                      + hl("pressionar para baixo") + " a taxa de inflação."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["ceteris paribus"], "dificuldade": 1,
        "comentario_fonte": "Juros altos atraem capital e apreciam o câmbio; a apreciação barateia importados e reduz "
                            "a inflação, reforçando o objetivo da autoridade monetária (várias respostas de IA "
                            "concordantes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01625
    {
        "id": "ECO-E2-L01625-1", "fonte_ref": "E2-L01625", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Se for válida a paridade coberta de juros, ao sofrer um súbito aumento do seu risco, um país "
                      "precisará aumentar sua taxa de juros ou vender reservas internacionais, se quiser manter a "
                      "taxa de câmbio estável."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se for válida a paridade coberta de juros, ao sofrer um súbito aumento do seu risco, um país "
                      "precisará <u>aumentar sua taxa de juros ou vender reservas internacionais</u>, se quiser "
                      "manter a taxa de câmbio estável."),
        "poucas": ("Na paridade com prêmio de risco, " + vd("i = i* + Δeᵉ + PR") + ": se PR sobe, ou o juro "
                   "doméstico sobe, ou o câmbio cede. Para segurar o câmbio, restam " + azb("juros maiores")
                   + " ou " + azb("venda de reservas") + "."),
        "destrinchando": [
            "Nos manuais brasileiros de macroeconomia aberta, a condição de curto prazo é apresentada em duas "
            "versões: " + azb("paridade descoberta") + " i = i* + Δeᵉ (juro doméstico = juro externo + "
            "desvalorização esperada) e a versão que soma o " + azb("prêmio de risco") + " (PR), chamada no curso "
            "de “coberta”: " + vd("i = i* + Δeᵉ + PR") + ".",
            "Leitura do equilíbrio: se i &gt; i* + Δeᵉ + PR, entra capital e o câmbio aprecia; se i &lt; i* + "
            "Δeᵉ + PR, sai capital e o câmbio deprecia. Um choque que eleva PR (crise política, risco fiscal, "
            "rebaixamento de rating) joga o país no segundo caso.",
            "Três saídas possíveis: (1) deixar o câmbio " + vd("depreciar") + " até a desvalorização esperada se "
            "ajustar; (2) " + vd("subir i") + " para recompor a igualdade; (3) atender a demanda por dólares "
            + vd("vendendo reservas") + " (ou swaps cambiais, no caso " + rx("brasileiro") + "). Quem quer o "
            "câmbio estável descarta a primeira e fica com as outras duas — exatamente o que diz o item.",
            "Nota técnica: na literatura internacional, “paridade coberta” é a que usa o câmbio a termo (forward), "
            "sem risco cambial; o prêmio de risco-país aparece como desvio dela. O raciocínio do item, porém, vale "
            "nas duas nomenclaturas.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item reproduz a lógica da paridade e se "
                       "protege com dois condicionais (“se for válida”, “se quiser manter”) e com a disjunção "
                       "“ou”: não exige as duas medidas juntas. A armadilha seria trocar “ou” por “e” ou dizer "
                       "que o câmbio se aprecia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…precisará reduzir sua taxa de juros ou comprar reservas internacionais…”</i> → ERRADO "
            "(inversão: isso aprofundaria a depreciação)",
            "<i>“…precisará, necessariamente, aumentar a taxa de juros e vender reservas…”</i> → ERRADO "
            "(modulador absoluto: basta uma das medidas)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["se", "ou"], "dificuldade": 2,
        "comentario_fonte": "Aumento de risco pressiona saída de capitais e depreciação; para manter o câmbio, o BC "
                            "eleva juros ou vende reservas. Imagem do verso com a regra i ⋛ i* + Δeᵉ + PR.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 466", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["nota_redacao: a fonte chama de “coberta” a paridade com prêmio de risco (convenção de manual "
                    "brasileiro); o card registra a diferença em relação à CIP com câmbio a termo"],
    },
    # ------------------------------------------------------------------ E2-L01768
    {
        "id": "ECO-E2-L01768-1", "fonte_ref": "E2-L01768", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CAMBIO,
        "rotulo_item": "Item",
        "assertiva": ("Um país que inicialmente está na paridade coberta de juros, ao sofrer um súbito aumento do "
                      "risco, tende a apresentar fuga de capital e depreciação de sua moeda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um país que inicialmente está na paridade coberta de juros, ao sofrer um súbito aumento do "
                      "risco, <u>tende a</u> apresentar fuga de capital e depreciação de sua moeda."),
        "poucas": ("Com " + vd("i = i* + Δeᵉ + PR") + " de partida, um PR maior torna i insuficiente: o capital "
                   "sai e a moeda " + azb("deprecia") + " até que a igualdade se recomponha."),
        "destrinchando": [
            "Partindo do equilíbrio i = i* + Δeᵉ + PR, o aumento súbito do " + azb("prêmio de risco") + " deixa "
            "o lado direito maior que o esquerdo: o retorno doméstico, ajustado ao risco, ficou baixo demais.",
            "Investidores vendem ativos e moeda do país e compram moeda estrangeira (" + azb("fuga de capital")
            + "). A procura por dólares eleva o câmbio nominal: " + vd("depreciação") + " da moeda doméstica.",
            "Como a igualdade volta? Ou pelo próprio câmbio (a depreciação de hoje, sem mudança do câmbio "
            "esperado de longo prazo, reduz a desvalorização esperada daí em diante), ou pela reação do BC: "
            "juros mais altos ou venda de reservas.",
            "Exemplos " + rx("brasileiros") + ": 2002 (incerteza eleitoral, risco-país acima de 2.000 pontos, "
            "dólar perto de R$ 4) e 2015 (perda do grau de investimento): saída de capital e forte depreciação.",
            vm("Regra-âncora: risco ↑ sem reação do BC → saída de capital → moeda deprecia."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Mecanismo direto da paridade, salvo pelo "
                       "“tende a”. A dúvida que o item explora é de nomenclatura: quem associa “paridade coberta” "
                       "a hedge cambial acha que o risco não mexeria no câmbio — mas o prêmio de risco-país não é "
                       "coberto pelo contrato a termo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tende a apresentar entrada de capital e apreciação de sua moeda.”</i> → ERRADO (inversão do "
            "sentido do fluxo)",
            "<i>“…a fuga de capital ocorre ainda que o banco central eleve os juros na mesma proporção do aumento "
            "do risco.”</i> → ERRADO (a alta de i compensaria o PR)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Aumento do risco-país rompe a paridade, investidores exigem prêmio maior: fuga de "
                            "capitais e depreciação até nova paridade. Imagens do verso com as duas paridades.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 532", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 533", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01625-1 (mesma prova; aqui o efeito do choque, lá a resposta do BC)"],
    },
    # ------------------------------------------------------------------ E2-L01769
    {
        "id": "ECO-E2-L01769-1", "fonte_ref": "E2-L01769", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CAMBIO,
        "rotulo_item": "Item",
        "assertiva": ("A apreciação cambial pode ser utilizada como um mecanismo de controle inflacionário, uma vez "
                      "que torna mais baratos os itens importados e eleva a concorrência no mercado interno."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A apreciação cambial <u>pode</u> ser utilizada como um mecanismo de controle inflacionário, "
                      "uma vez que torna mais baratos os itens importados e eleva a concorrência no mercado "
                      "interno."),
        "poucas": ("Moeda apreciada = importados mais baratos em moeda local + " + azb("disciplina competitiva")
                   + " sobre os produtores domésticos de comercializáveis: menos inflação."),
        "destrinchando": [
            "Dois canais, os dois citados no item: (1) " + azb("canal direto") + " — o preço em reais de um bem "
            "importado é P* × e; se e cai (apreciação), o preço cai; (2) " + azb("canal da concorrência") + " — "
            "o produtor nacional de bens comercializáveis não consegue reajustar acima do similar importado.",
            "Há ainda o canal dos custos: insumos importados mais baratos reduzem o custo de produção de bens "
            "nacionais, inclusive de não comercializáveis.",
            "Uso histórico: a " + azb("âncora cambial") + " foi peça central do " + rx("Plano Real") + " "
            "(1994–1999), com o real valorizado e a abertura comercial segurando os preços dos comercializáveis. "
            "Planos de estabilização na Argentina (Conversibilidade, 1991) e no México seguiram lógica parecida.",
            "O custo: apreciação persistente piora a conta corrente, prejudica a indústria exportadora e pode "
            "levar a crises de balanço de pagamentos se o déficit externo ficar insustentável — foi o que forçou "
            "a flutuação do real em " + vd("janeiro de 1999") + ".",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item conceitual protegido pelo “pode”: não "
                       "diz que a apreciação é sempre desejável nem que é o único instrumento. Erraria quem "
                       "lembrasse só dos custos da apreciação (perda de competitividade) e generalizasse."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A depreciação cambial pode ser usada como mecanismo de controle inflacionário, pois barateia os "
            "importados.”</i> → ERRADO (inversão: depreciação encarece importados)",
            "<i>“A apreciação cambial controla a inflação sem custos para o balanço de pagamentos.”</i> → ERRADO "
            "(piora a conta corrente)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "A apreciação reduz o preço dos importados em moeda doméstica e aumenta a concorrência "
                            "interna, pressionando os preços para baixo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01581-1 (mesmo canal: apreciação cambial reduz a inflação)"],
    },
    # ------------------------------------------------------------------ E3-L00316
    {
        "id": "ECO-E3-L00316-1", "fonte_ref": "E3-L00316", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NIDI_PRECOS,
        "rotulo_item": "Item",
        "assertiva": "Variações na taxa de câmbio nominal não impacta a inflação dos países relevantes.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Variações na taxa de câmbio nominal ") + vm("não impacta")
                    + az(" a inflação dos países relevantes.")),
        "poucas": ("Variações do câmbio nominal chegam aos preços pelo " + azb("repasse cambial") + " "
                   "(<i>pass-through</i>): depreciação encarece importados e insumos; apreciação os barateia."),
        "destrinchando": [
            azb("Câmbio nominal") + " (e) = preço da moeda estrangeira em moeda nacional; " + azb("câmbio real")
            + " = e·P*/P. Uma depreciação nominal eleva, de imediato, o preço em moeda local de tudo o que tem "
            "preço formado lá fora.",
            "Canais do repasse: (1) " + azb("direto") + " — bens finais importados (eletrônicos, veículos); "
            "(2) " + azb("custos") + " — insumos e commodities cotadas em dólar (trigo, combustíveis, "
            "fertilizantes); (3) " + azb("expectativas") + " — em economias com memória inflacionária ou "
            "indexação, a depreciação contamina reajustes de contratos, salários e preços administrados.",
            "O repasse é parcial e varia: maior em economias abertas, dependentes de importados essenciais, com "
            "indexação e com política monetária pouco crível; menor quando a economia está em recessão (as "
            "empresas absorvem parte do custo) e quando as expectativas estão ancoradas.",
            "Ordem de grandeza " + rx("no Brasil") + ": estimativas do " + rx("Banco Central") + " situam o "
            "repasse para o IPCA em " + vd("cerca de 5% a 15% em 12 meses") + " ⏳ (out/2026). Em 2015, com "
            "forte depreciação do real, o IPCA fechou em " + vd("10,67%") + ".",
            vm("Regra-âncora: depreciação → inflação ↑; apreciação → inflação ↓ (com repasse parcial)."),
        ],
        "dissecando": (cz("[contradição · modulador absoluto]") + " Negação categórica de um mecanismo "
                       "consagrado: “não impacta”, sem qualquer qualificação. 🔥 Itens com negação total sobre "
                       "relações macroeconômicas básicas quase sempre são ERRADO; a versão defensável trataria do "
                       "<b>grau</b> do repasse, não da sua existência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O repasse das variações do câmbio nominal para a inflação tende a ser maior em economias mais "
            "abertas e com maior grau de indexação.”</i> → CERTO",
            "<i>“O repasse cambial é integral e imediato: uma depreciação de 10% eleva a inflação em 10 pontos "
            "percentuais.”</i> → ERRADO (o repasse é parcial e defasado)",
        ])],
        "reescrita": "Variações na taxa de câmbio nominal " + hl("impactam") + " a inflação dos países relevantes.",
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": "Três respostas de IA (Gemini, Claude, Grok) concordantes: pass-through cambial pelos "
                            "canais de importados, custos e expectativas; grau de repasse varia com abertura, "
                            "indexação e credibilidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0309
    {
        "id": "ECO-E1-0309-1", "fonte_ref": "E1-0309", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False, "errei": False,
        "comando": "Acerca da relação entre as políticas monetária e cambial, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Dada a relação existente entre as políticas monetária e cambial, os efeitos da política "
                      "monetária executada pelo banco central de um país dependem fundamentalmente do tipo de regime "
                      "cambial adotado. Assim, em um sistema de taxas de câmbio flexíveis com mobilidade "
                      "internacional de capital, a fixação da taxa de juros básica como instrumento para o objetivo "
                      "de estabilizar preços é inalcançável."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Dada a relação existente entre as políticas monetária e cambial, os efeitos da política "
                       "monetária executada pelo banco central de um país dependem fundamentalmente do tipo de "
                       "regime cambial adotado. Assim, em um sistema de taxas de câmbio flexíveis com mobilidade "
                       "internacional de capital, a fixação da taxa de juros básica como instrumento para o "
                       "objetivo de estabilizar preços ") + vm("é inalcançável") + az(".")),
        "poucas": ("É o contrário: com " + azb("câmbio flexível") + ", o BC recupera a autonomia monetária e pode "
                   "usar a taxa básica de juros para mirar a inflação — é a configuração do " + rx("regime de "
                   "metas brasileiro") + ". Inviável seria com câmbio fixo e capital livre."),
        "destrinchando": [
            "A 1ª frase está certa: o alcance da política monetária depende do regime cambial. É a lição do "
            + azb("trilema") + " (ou trindade impossível): entre câmbio fixo, livre mobilidade de capitais e "
            "política monetária autônoma, só se escolhem dois.",
            "Câmbio fixo + mobilidade de capital → o juro doméstico fica preso ao externo (i = i*) e a oferta de "
            "moeda vira " + azb("endógena") + ": aí, sim, usar o juro para estabilizar preços seria inalcançável.",
            "Câmbio flexível + mobilidade de capital → o BC abre mão de controlar o câmbio e, em troca, fixa "
            "livremente a taxa básica. É o arranjo do " + rx("tripé macroeconômico") + " brasileiro desde "
            + vd("1999") + ": câmbio flutuante, metas de inflação com a Selic como instrumento e meta fiscal.",
            "Mecanismo: juros ↑ → demanda agregada ↓ (crédito, consumo, investimento) e, ao mesmo tempo, entrada "
            "de capital → " + azb("apreciação cambial") + " → importados mais baratos. Os dois canais empurram "
            "a inflação para baixo — o câmbio flexível <b>reforça</b> a política monetária.",
            vm("Regra-âncora: câmbio flutuante = política monetária ativa; câmbio fixo com capital livre = "
               "política monetária amarrada."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " A premissa (dependência do regime cambial) é "
                       "verdadeira e dá credibilidade ao “Assim”; a conclusão atribui ao câmbio flexível a "
                       "limitação típica do câmbio fixo. 🔥 Item de trilema: identifique o regime e pergunte qual "
                       "dos três vértices foi sacrificado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…em um sistema de taxas de câmbio fixas com perfeita mobilidade internacional de capital, a "
            "fixação autônoma da taxa de juros básica para estabilizar preços é inalcançável.”</i> → CERTO",
            "<i>“…com câmbio flexível, a alta de juros deprecia a moeda e enfraquece o combate à inflação.”</i> "
            "→ ERRADO (inversão: a alta de juros aprecia a moeda)",
        ])],
        "reescrita": ("Dada a relação existente entre as políticas monetária e cambial, os efeitos da política "
                      "monetária executada pelo banco central de um país dependem fundamentalmente do tipo de regime "
                      "cambial adotado. Assim, em um sistema de taxas de câmbio flexíveis com mobilidade "
                      "internacional de capital, a fixação da taxa de juros básica como instrumento para o objetivo "
                      "de estabilizar preços " + hl("é viável") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["fundamentalmente"], "dificuldade": 1,
        "comentario_fonte": "Com câmbio flutuante a política monetária é ativa e determina a inflação; a alta de "
                            "juros reduz a demanda e atrai capitais, barateando importados.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: frente marcada com ⌚ e ano 2017; possível prova do CACD, sem confirmação na "
                    "fonte"],
    },
    # ------------------------------------------------------------------ E1-0448
    {
        "id": "ECO-E1-0448-1", "fonte_ref": "E1-0448", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("O modelo IS-LM-BP representa o comportamento de uma economia aberta, incorporando o mercado de "
                    "bens, monetário e o setor externo. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Em regime de câmbio fixo com mobilidade perfeita de capitais, a política fiscal é ineficaz, "
                      "pois qualquer expansão é anulada por movimentos automáticos na taxa de câmbio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em regime de câmbio fixo com mobilidade perfeita de capitais, a política fiscal é ")
                    + vm("ineficaz") + az(", pois qualquer expansão é ") + vm("anulada por movimentos automáticos "
                                                                            "na taxa de câmbio") + az(".")),
        "poucas": ("No câmbio fixo com capital perfeitamente móvel, a fiscal tem " + azb("eficácia máxima")
                   + ": a entrada de capitais obriga o BC a emitir moeda para segurar o câmbio, e a LM acompanha a "
                   "IS. O câmbio, por definição, não se move."),
        "destrinchando": [
            "Mobilidade perfeita → " + azb("BP horizontal") + " em i = i*: qualquer juro acima de i* atrai "
            "capital sem limite; abaixo, expulsa.",
            "Sequência da expansão fiscal: G ↑ → IS para a direita → i tende a subir acima de i* → entrada "
            "maciça de capital → pressão de " + vd("apreciação") + " → para manter a paridade, o BC " + vd("compra "
            "divisas") + " e emite moeda → " + vd("M ↑") + " → LM para a direita até i voltar a i*.",
            "Resultado: Y sobe pelo " + azb("multiplicador keynesiano pleno") + " (sem crowding out, porque o "
            "juro não sobe), as reservas crescem e o câmbio fica onde estava. A política monetária torna-se "
            + azb("acomodatícia") + ": a oferta de moeda é endógena.",
            "A frase do item descreve outro caso: no " + azb("câmbio flutuante") + " com mobilidade perfeita, a "
            "expansão fiscal é anulada pela apreciação, que derruba as exportações líquidas (crowding out "
            "externo total). O item “importa” para o câmbio fixo um movimento cambial que ele proíbe.",
            vm("Regra-âncora (Mundell-Fleming, mobilidade perfeita): fixo → fiscal eficaz, monetária "
               "ineficaz; flutuante → monetária eficaz, fiscal ineficaz."),
        ],
        "grafico_verso": "ECO-E1-0448-1-V1",
        "dissecando": (cz("[troca de conceito · contradição]") + " Troca o regime: o mecanismo descrito (anulação "
                       "por câmbio) é o do flutuante. Pista interna: “movimentos automáticos na taxa de câmbio” "
                       "contradiz o próprio “câmbio fixo”. 🔥 A banca alterna as quatro casas da tabela de "
                       "Mundell-Fleming trocando regime ou política."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio flutuante com mobilidade perfeita de capitais, a política fiscal é ineficaz, "
            "pois a expansão é anulada pela apreciação cambial.”</i> → CERTO",
            "<i>“Em câmbio fixo com mobilidade perfeita, a expansão fiscal reduz as reservas internacionais.”</i> "
            "→ ERRADO (as reservas aumentam: o BC compra divisas)",
        ])],
        "reescrita": ("Em regime de câmbio fixo com mobilidade perfeita de capitais, a política fiscal é "
                      + hl("eficaz") + ", pois qualquer expansão é " + hl("acomodada pela expansão monetária que o "
                      "banco central faz para manter a taxa de câmbio") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": "Sob câmbio fixo e mobilidade perfeita, a fiscal é muito eficaz: a entrada de capital "
                            "força o BC a comprar divisas, expandindo a moeda e potencializando o efeito fiscal "
                            "(resposta de IA longa e correta, repetida na linha duplicada).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E1-0550 (mesma assertiva, mesmo simulado) fundida neste card"],
    },
    # ------------------------------------------------------------------ E1-0449
    {
        "id": "ECO-E1-0449-1", "fonte_ref": "E1-0449", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("O modelo IS-LM-BP representa o comportamento de uma economia aberta, incorporando o mercado de "
                    "bens, monetário e o setor externo. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Sob câmbio flutuante e mobilidade perfeita de capitais, a política monetária é mais eficaz do "
                      "que a fiscal, pois afeta simultaneamente o nível de atividade e o saldo da balança de "
                      "pagamentos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Sob câmbio flutuante e mobilidade perfeita de capitais, a política monetária é <u>mais "
                      "eficaz do que a fiscal</u>, pois afeta simultaneamente o nível de atividade e o saldo da "
                      "<u>balança de pagamentos</u>."),
        "poucas": ("A conclusão é a de " + oc("Mundell-Fleming") + ": no flutuante, a monetária é muito eficaz e "
                   "a fiscal, ineficaz. A justificativa, porém, é frouxa: o que muda é o " + azb("saldo comercial")
                   + " (via depreciação), não o saldo do balanço de pagamentos."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá CERTO, e a primeira oração é inatacável. Mas, com câmbio flutuante, o "
                          "câmbio se ajusta justamente para que o " + vm("saldo total do balanço de pagamentos "
                          "seja nulo") + " (sem variação de reservas). A política monetária afeta a "
                          + azb("balança comercial") + " e a conta corrente, não o saldo do BP. Uma banca "
                          "rigorosa poderia dar ERRADO pela justificativa.")],
        "destrinchando": [
            "Expansão monetária: M ↑ → LM para a direita → i tende a cair abaixo de i* → saída de capitais → "
            + vd("depreciação") + " → exportações líquidas ↑ → IS também vai para a direita. A economia volta a "
            "i = i* com " + vd("Y bem maior") + ": os dois canais (juros e câmbio) somam.",
            "Expansão fiscal: G ↑ → IS para a direita → i tende a subir → entrada de capitais → "
            + vd("apreciação") + " → exportações líquidas ↓ → IS volta ao ponto inicial. Y não muda: "
            + azb("crowding out externo") + " total (troca-se exportação líquida por gasto público).",
            "Por que a justificativa é frágil: no flutuante puro o BC não compra nem vende divisas, logo as "
            "reservas não variam e o " + azb("BP fecha em zero") + " sempre — é o câmbio que garante isso. O que "
            "a política monetária altera é a <b>composição</b> do BP: conta corrente melhora, conta financeira "
            "piora na mesma medida.",
            "Leitura benevolente: a fonte chama de “saldo da balança de pagamentos” o saldo em transações "
            "correntes (ou da balança comercial), que de fato melhora com a depreciação.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Conclusão de manual com justificativa imprecisa. Em "
                       "prova CEBRASPE, vale ler o “pois”: se a causa estiver errada, o item cai. Aqui o gabarito "
                       "da fonte considerou a justificativa no sentido amplo (efeito sobre as contas externas)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio flutuante e mobilidade perfeita de capitais, a política fiscal é mais eficaz do que a "
            "monetária.”</i> → ERRADO (inversão das políticas)",
            "<i>“…a política monetária é eficaz porque a depreciação cambial estimula as exportações "
            "líquidas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["mais eficaz", "pois"], "dificuldade": 2,
        "comentario_fonte": "Monetária muito eficaz (desvaloriza o câmbio e estimula exportações líquidas); fiscal "
                            "ineficaz (valorização anula o estímulo).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: com câmbio flutuante o saldo do BP é nulo; a política monetária altera a balança "
                    "comercial e a conta corrente, não o saldo do BP",
                    "duplicata: linha E1-0551 (mesma assertiva, mesmo simulado) fundida neste card"],
    },
    # ------------------------------------------------------------------ E1-0450
    {
        "id": "ECO-E1-0450-1", "fonte_ref": "E1-0450", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("O modelo IS-LM-BP representa o comportamento de uma economia aberta, incorporando o mercado de "
                    "bens, monetário e o setor externo. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A curva BP é horizontal em regime de perfeita mobilidade de capitais, indicando que qualquer "
                      "desvio entre a taxa doméstica e a taxa mundial gera fluxos imediatos de capitais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva BP é <u>horizontal</u> em regime de <u>perfeita</u> mobilidade de capitais, "
                      "indicando que qualquer desvio entre a taxa doméstica e a taxa mundial gera fluxos imediatos "
                      "de capitais."),
        "poucas": ("Com mobilidade perfeita, o BP só fecha em " + vd("i = i*") + ", qualquer que seja a renda: a "
                   "BP é uma " + azb("reta horizontal") + " na altura do juro internacional."),
        "destrinchando": [
            "A " + azb("curva BP") + " reúne os pares (Y, i) com saldo nulo no balanço de pagamentos: conta "
            "corrente + conta financeira = 0. Acima dela, há superávit (juros atraem capital); abaixo, déficit.",
            "A inclinação mede a mobilidade de capitais: " + vd("vertical") + " → mobilidade nula (só a conta "
            "corrente importa e o equilíbrio fixa um único Y); " + vd("positivamente inclinada") + " → "
            "mobilidade imperfeita (renda maior → mais importações → é preciso juro maior para atrair capital); "
            + vd("horizontal") + " → mobilidade perfeita.",
            "Na mobilidade perfeita, ativos domésticos e externos são " + azb("substitutos perfeitos") + " e não "
            "há custo de transação nem controle: um diferencial mínimo gera fluxos virtualmente ilimitados, que "
            "eliminam o desvio. É a hipótese da " + azb("pequena economia aberta") + " do modelo de "
            + oc("Mundell") + " e " + oc("Fleming") + " (anos 1960): o país toma i* como dado.",
            "Regra prática de leitura: quanto mais <b>plana</b> a BP, maior a mobilidade. Se a BP é mais plana "
            "que a LM, a expansão fiscal gera superávit externo; se é mais inclinada, gera déficit.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. Os pontos de risco são a forma da curva "
                       "(horizontal × vertical) e o grau de mobilidade (perfeita × nula): a banca costuma trocá-los. "
                       "“Imediatos” é coerente com a hipótese de mobilidade perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva BP é vertical em regime de perfeita mobilidade de capitais.”</i> → ERRADO (vertical = "
            "mobilidade nula)",
            "<i>“Quanto maior a mobilidade de capitais, mais inclinada é a curva BP.”</i> → ERRADO (inversão: "
            "mais mobilidade, BP mais plana)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": "Mobilidade perfeita implica i = i*; qualquer desvio gera fluxos infinitos; BP "
                            "horizontal. Respostas de IA longas explicam as três inclinações da BP.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E1-0552 (mesma assertiva, mesmo simulado) fundida neste card"],
    },
    # ------------------------------------------------------------------ E1-0640
    {
        "id": "ECO-E1-0640-1", "fonte_ref": "E1-0640", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Set/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Com base no modelo IS-LM-BP (Mundell-Fleming), julgue o item a seguir.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM-BP, com mobilidade perfeita de capitais e câmbio flexível, uma expansão "
                      "monetária provoca apreciação cambial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo IS-LM-BP, com mobilidade perfeita de capitais e câmbio flexível, uma expansão "
                       "monetária provoca ") + vm("apreciação") + az(" cambial.")),
        "poucas": ("Expansão monetária derruba o juro doméstico abaixo de i*, o capital sai e a moeda "
                   + azb("deprecia") + ". A depreciação eleva as exportações líquidas e a renda."),
        "destrinchando": [
            "Passo 1: M ↑ → LM para a direita → i cai abaixo de i* (ponto provisório abaixo da BP horizontal, "
            "com déficit no BP).",
            "Passo 2: com mobilidade perfeita, o diferencial negativo provoca " + azb("saída de capitais") + " — "
            "aumenta a procura por moeda estrangeira.",
            "Passo 3: com câmbio flexível, o BC não intervém; o preço da divisa sobe: " + vd("depreciação") + " "
            "da moeda nacional.",
            "Passo 4: a depreciação torna os bens domésticos mais baratos lá fora → exportações ↑, importações ↓ "
            "→ IS para a direita, até i voltar a i* com " + vd("Y bem maior") + ". Política monetária com "
            + azb("eficácia máxima") + ".",
            "Contraponto: a apreciação aparece na expansão <b>fiscal</b> no flutuante (juros ↑ → entrada de "
            "capital), o que anula o efeito sobre a renda.",
            vm("Regra-âncora: no flutuante, monetária expansionista deprecia; fiscal expansionista aprecia."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sentido do câmbio: atribui à expansão monetária o efeito "
                       "cambial da expansão fiscal. Para não errar, siga sempre o juro: i ↓ → capital sai → "
                       "moeda deprecia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma expansão fiscal provoca apreciação cambial e deixa a renda inalterada.”</i> → CERTO",
            "<i>“…uma expansão monetária provoca depreciação cambial, mas não altera a renda.”</i> → ERRADO (a "
            "renda sobe: a depreciação eleva as exportações líquidas)",
        ])],
        "reescrita": ("No modelo IS-LM-BP, com mobilidade perfeita de capitais e câmbio flexível, uma expansão "
                      "monetária provoca " + hl("depreciação") + " cambial."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O erro está em afirmar apreciação: a expansão monetária reduz o juro, provoca saída de "
                            "capitais e depreciação, que estimula exportações líquidas e renda (duas respostas de "
                            "IA concordantes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (185).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "irrecuperavel"},
                          {"ref": "image (181).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "irrecuperavel"},
                          {"ref": "image (184).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada"}],
        "alertas": ["texto_reconstruido: a frente era só duas imagens não preservadas; assertiva reconstruída pelo "
                    "comentário, que diz que “o erro da assertiva está em afirmar que ocorre uma apreciação "
                    "cambial” com mobilidade perfeita e câmbio flexível; redação original pode ser mais longa"],
    },
    # ------------------------------------------------------------------ E1-0703
    {
        "id": "ECO-E1-0703-1", "fonte_ref": "E1-0703", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": "Acerca do modelo IS-LM-BP e da economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta com mobilidade perfeita de capitais, uma política fiscal expansionista "
                      "aumenta a taxa de juros doméstica, atrai entrada de capital estrangeiro e provoca apreciação "
                      "da moeda, neutralizando parcialmente seu efeito sobre o produto agregado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia aberta com mobilidade perfeita de capitais, uma política fiscal "
                       "expansionista aumenta a taxa de juros doméstica, atrai entrada de capital estrangeiro e "
                       "provoca apreciação da moeda, neutralizando ") + vm("parcialmente")
                    + az(" seu efeito sobre o produto agregado.")),
        "poucas": ("Com mobilidade perfeita e câmbio flutuante (implícito na “apreciação”), a apreciação anula "
                   + vm("totalmente") + " o efeito da expansão fiscal sobre o produto: " + azb("crowding out "
                   "externo completo") + "."),
        "condicionais": [("🏛️ Justificativa da banca",
                          cz("Gabarito preliminar CERTO, alterado para ERRADO: “se a economia aberta tem perfeita "
                             "mobilidade de capitais, então a apreciação da moeda não reverte apenas parcialmente "
                             "o aumento do produto, mas o reverte totalmente”."))],
        "destrinchando": [
            "Sequência no " + azb("câmbio flutuante") + ": G ↑ → IS para a direita → i tende a subir acima de i* "
            "→ entrada de capital → " + vd("apreciação") + " → exportações líquidas ↓ → IS volta para a "
            "esquerda.",
            "Até onde ela volta? Até i = i*, porque a BP é horizontal. Como a LM não se moveu (o BC não "
            "intervém), o único ponto com i = i* sobre a LM é o <b>equilíbrio inicial</b>: " + vd("Y final = Y "
            "inicial") + ". O gasto público expulsou, real por real, exportações líquidas.",
            "Por isso a alta de juros é só <b>provisória</b>: no equilíbrio final i = i*. A neutralização "
            "“parcial” valeria com " + azb("mobilidade imperfeita") + " (BP inclinada), em que o juro final fica "
            "acima de i* e a renda sobe um pouco.",
            "E o regime não declarado? A assertiva fala em apreciação, o que só ocorre com câmbio flexível. No "
            + azb("câmbio fixo") + ", o BC compraria as divisas, a LM acompanharia a IS e a fiscal seria "
            "plenamente eficaz — mas aí não haveria apreciação.",
            vm("Regra-âncora: flutuante + mobilidade perfeita → fiscal com eficácia nula (crowding out externo "
               "total)."),
        ],
        "grafico_verso": "ECO-E1-0703-1-V1",
        "dissecando": (cz("[restrição indevida · dado alterado]") + " A cadeia causal está toda certa; o erro "
                       "está num único advérbio de grau: “parcialmente” no lugar de “totalmente”. 🔥 Em "
                       "Mundell-Fleming com mobilidade perfeita, os resultados são extremos (eficácia nula ou "
                       "máxima); “parcial” é sinal de mobilidade imperfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…neutralizando totalmente seu efeito sobre o produto agregado.”</i> → CERTO",
            "<i>“Com mobilidade imperfeita de capitais e câmbio flutuante, a apreciação neutraliza parcialmente "
            "o efeito da expansão fiscal.”</i> → CERTO",
            "<i>“…sob câmbio fixo, a expansão fiscal provoca apreciação e neutraliza seu efeito.”</i> → ERRADO "
            "(no fixo, o BC impede a apreciação e a fiscal é eficaz)",
        ])],
        "reescrita": ("Em uma economia aberta com mobilidade perfeita de capitais, uma política fiscal "
                      "expansionista aumenta a taxa de juros doméstica, atrai entrada de capital estrangeiro e "
                      "provoca apreciação da moeda, neutralizando " + hl("totalmente") + " seu efeito sobre o "
                      "produto agregado."),
        "tipo_erro": ["RESTRICAO", "DADO_ALTERADO"], "moduladores": ["parcialmente"], "dificuldade": 3,
        "comentario_fonte": "Gabarito alterado de CERTO para ERRADO (neutralização total, não parcial). Anotação "
                            "pessoal de recurso e respostas de IA discutindo a omissão do regime cambial.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (208).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida"}],
        "alertas": ["nota_redacao: gabarito oficial final ERRADO (alterado de CERTO); as respostas de IA do verso "
                    "defendiam CERTO e foram corrigidas no comentário"],
    },
    # ------------------------------------------------------------------ E1-0705
    {
        "id": "ECO-E1-0705-1", "fonte_ref": "E1-0705", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca do modelo IS-LM-BP e da economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em regimes de câmbio fixo, uma política monetária expansionista doméstica tem efeito "
                      "irrestrito sobre o produto agregado, independentemente da reação do banco central para manter "
                      "a paridade cambial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em regimes de câmbio fixo, uma política monetária expansionista doméstica tem efeito ")
                    + vm("irrestrito") + az(" sobre o produto agregado, ") + vm("independentemente")
                    + az(" da reação do banco central para manter a paridade cambial.")),
        "poucas": ("No câmbio fixo, defender a paridade obriga o BC a " + azb("desfazer") + " a expansão "
                   "monetária (vende reservas e recolhe moeda): com mobilidade de capitais, o efeito sobre o "
                   "produto é " + vm("nulo") + ", e é justamente a reação do BC que o anula."),
        "destrinchando": [
            "Sequência (mobilidade perfeita): M ↑ → LM para a direita → i cai abaixo de i* → fuga de capitais → "
            "pressão de " + vd("depreciação") + " → para manter a paridade, o BC " + vd("vende reservas") + " e "
            "compra moeda doméstica → " + vd("M ↓") + " → LM volta à posição original.",
            "Resultado: Y, i e câmbio iguais aos iniciais; só muda a " + azb("composição da base monetária") + " "
            "(menos reservas, mais crédito doméstico do BC). A oferta de moeda é " + azb("endógena") + ": o BC "
            "não a controla.",
            "Com mobilidade imperfeita, a expansão pode ter efeito transitório enquanto as reservas se esgotam, "
            "mas não sustentável; com mobilidade nula, o déficit em conta corrente produz o mesmo desfecho, só "
            "que mais devagar.",
            "Ligação com o " + azb("trilema") + ": câmbio fixo + capital livre ⇒ sem política monetária "
            "autônoma. A única forma de a monetária “funcionar” seria abandonar a paridade (desvalorização) ou "
            "esterilizar até as reservas acabarem.",
            vm("Regra-âncora: câmbio fixo + mobilidade de capitais → monetária ineficaz; fiscal eficaz."),
        ],
        "grafico_verso": "ECO-E1-0705-1-V1",
        "dissecando": (cz("[modulador absoluto · contradição]") + " Dois absolutos empilhados (“irrestrito”, "
                       "“independentemente”) e uma contradição interna: o item reconhece que o BC precisa “manter "
                       "a paridade” e, ao mesmo tempo, diz que essa reação não importa. É ela que anula a política."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regimes de câmbio fixo com mobilidade perfeita de capitais, uma política monetária "
            "expansionista reduz as reservas internacionais sem alterar o produto.”</i> → CERTO",
            "<i>“Em regimes de câmbio flutuante, a política monetária expansionista é ineficaz sobre o "
            "produto.”</i> → ERRADO (inversão: no flutuante ela é muito eficaz)",
        ])],
        "reescrita": ("Em regimes de câmbio fixo, uma política monetária expansionista doméstica tem efeito "
                      + hl("nulo") + " sobre o produto agregado, " + hl("em razão") + " da reação do banco central "
                      "para manter a paridade cambial."),
        "tipo_erro": ["GENERALIZACAO", "CONTRADICAO"], "moduladores": ["irrestrito", "independentemente"],
        "dificuldade": 1,
        "comentario_fonte": "No câmbio fixo com mobilidade, a monetária é ineficaz: fuga de capitais, BC vende "
                            "reservas e contrai a base, LM volta à posição original.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0753
    {
        "id": "ECO-E1-0753-1", "fonte_ref": "E1-0753", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Acerca da política monetária em economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O aumento temporário da oferta de moeda, em regime de câmbio flutuante, resulta em queda da "
                      "taxa doméstica de juros e depreciação da moeda doméstica. Em curto prazo, haverá redução da "
                      "demanda agregada e do produto da economia, em razão da queda dos preços relativos dos bens "
                      "produzidos localmente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O aumento temporário da oferta de moeda, em regime de câmbio flutuante, resulta em queda "
                       "da taxa doméstica de juros e depreciação da moeda doméstica. Em curto prazo, haverá ")
                    + vm("redução") + az(" da demanda agregada e do produto da economia, em razão da queda dos "
                                         "preços relativos dos bens produzidos localmente.")),
        "poucas": ("A 1ª frase está certa; a 2ª inverte o efeito. Bens locais relativamente mais baratos (câmbio "
                   "real depreciado) " + azb("aumentam") + " as exportações líquidas: a demanda agregada e o "
                   "produto " + vm("sobem") + "."),
        "destrinchando": [
            "Expansão monetária no flutuante: M ↑ → i ↓ → saída de capitais → " + vd("depreciação") + " "
            "(e ↑). Com preços rígidos no curto prazo, o " + azb("câmbio real") + " (eP*/P) também sobe: os bens "
            "produzidos no país ficam relativamente mais baratos.",
            "Consequência: exportações ↑ e importações ↓ → " + vd("NX ↑") + " → IS para a direita → "
            + vd("Y ↑") + ". Soma-se o canal do juro (i ↓ → investimento ↑). Os dois empurram a demanda "
            "agregada para cima.",
            "O resultado vale com qualquer grau de mobilidade de capitais: com mobilidade perfeita, a monetária "
            "tem " + azb("eficácia máxima") + " (a renda sobe só pelo câmbio, com i voltando a i*); com "
            "mobilidade imperfeita ou nula, a renda também sobe.",
            "Como resume " + oc("Mankiw") + ": na pequena economia aberta, a política monetária afeta a renda "
            "alterando o câmbio, não o juro.",
            "Ressalva de médio prazo: com preços flexíveis, a inflação gerada pela depreciação corrói o ganho de "
            "câmbio real, e o efeito sobre o produto se dissipa — mas o item fala em curto prazo.",
        ],
        "grafico_verso": "ECO-E1-0753-1-V1",
        "dissecando": (cz("[meia-verdade · inversão]") + " Primeira frase perfeita, segunda com o sinal trocado. "
                       "A “queda dos preços relativos dos bens locais” é a causa da <b>expansão</b> (ganho de "
                       "competitividade), e o item a usa para justificar uma contração. Mnemônico de cursinho: "
                       "<b>FI</b>xo → <b>FI</b>scal; <b>MÓ</b>vel (flutuante) → <b>MO</b>netária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…Em curto prazo, haverá aumento da demanda agregada e do produto, em razão da queda dos preços "
            "relativos dos bens produzidos localmente.”</i> → CERTO",
            "<i>“O aumento da oferta de moeda, em regime de câmbio flutuante, resulta em apreciação da moeda "
            "doméstica.”</i> → ERRADO (inversão: deprecia)",
        ])],
        "reescrita": ("O aumento temporário da oferta de moeda, em regime de câmbio flutuante, resulta em queda da "
                      "taxa doméstica de juros e depreciação da moeda doméstica. Em curto prazo, haverá "
                      + hl("aumento") + " da demanda agregada e do produto da economia, em razão da queda dos "
                      "preços relativos dos bens produzidos localmente."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["temporário", "em curto prazo"],
        "dificuldade": 1,
        "comentario_fonte": "Vários comentários de professores (Jetro Coutinho, Michelle Miltons, Daniel Sousa) e "
                            "alunos: no flutuante, a expansão monetária eleva o produto via juros e exportações "
                            "líquidas, com qualquer grau de mobilidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "cbbcc60f-a8c9-40ad-9961-ee33545af969", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada"},
                          {"ref": "fb030e39-450d-4bfc-a87f-c93f7b3769f7", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada"}],
        "alertas": ["banca_provavel: marca ⌚ e ano 2019 sugerem CEBRASPE (CACD 2019); não confirmado na fonte"],
    },
    # ------------------------------------------------------------------ E1-0754
    {
        "id": "ECO-E1-0754-1", "fonte_ref": "E1-0754", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Acerca da política monetária em economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta com livre movimentação de capitais, sob uma taxa de câmbio fixa, os "
                      "instrumentos de política monetária do Banco Central não são eficazes para aumentar a oferta de "
                      "moeda ou o produto da economia, mas podem afetar o nível das respectivas reservas "
                      "internacionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia aberta com livre movimentação de capitais, sob uma taxa de câmbio fixa, os "
                      "instrumentos de política monetária do Banco Central <u>não são eficazes para aumentar a "
                      "oferta de moeda ou o produto</u> da economia, mas <u>podem afetar o nível das respectivas "
                      "reservas internacionais</u>."),
        "poucas": ("Câmbio fixo + capital livre: a tentativa de expandir M provoca fuga de capitais, o BC vende "
                   "divisas para segurar a paridade e a moeda volta ao nível inicial. Sobram " + azb("menos "
                   "reservas") + ", com M e Y inalterados."),
        "destrinchando": [
            "A âncora nominal é o câmbio: o BC precisa vender ou comprar divisas, ao preço fixado, em qualquer "
            "quantidade. Por isso a " + azb("oferta de moeda é endógena") + ": ela se ajusta à demanda de moeda "
            "compatível com i = i*.",
            "Operação expansionista (compra de títulos, corte de compulsório): i tende a cair → saída de capitais "
            "→ demanda por divisas → BC " + vd("vende reservas") + " e recolhe moeda doméstica → M retorna. "
            "Efeito líquido: troca de reservas por títulos domésticos no ativo do BC.",
            "Operação contracionista: o espelho — entrada de capitais, compra de divisas, " + vd("reservas ↑") + ".",
            "Esterilização (vender títulos para compensar a emissão causada pela compra de divisas, ou o "
            "inverso) adia o ajuste, mas com mobilidade perfeita não se sustenta.",
            "Corolário: no câmbio fixo, a inflação doméstica tende a acompanhar a inflação do país-âncora, e a "
            "política anti-inflacionária é a própria paridade.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item une as duas metades do resultado clássico: "
                       "ineficácia sobre M e Y e efeito sobre as reservas. O detalhe que derruba candidatos é o "
                       "“oferta de moeda”: muita gente aceita a ineficácia sobre o produto, mas acha que o BC ainda "
                       "controla M."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os instrumentos de política monetária não afetam o produto, mas elevam de forma permanente a "
            "oferta de moeda.”</i> → ERRADO (M volta ao nível inicial)",
            "<i>“Sob câmbio flutuante com livre movimentação de capitais, a política monetária altera as "
            "reservas internacionais, mas não o produto.”</i> → ERRADO (inversão de regime)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["podem"], "dificuldade": 2,
        "comentario_fonte": "Com câmbio fixo e plena mobilidade, o BC abre mão da autonomia monetária; expansão "
                            "gera fuga de capitais; o BC compra ou vende divisas para manter o câmbio. O comentário "
                            "diz, por engano, que “a taxa de câmbio deve subir para manter a paridade”.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ e ano 2019 sugerem CEBRASPE (CACD 2019); não confirmado na fonte",
                    "quase_duplicata: ECO-E1-0705-1 (mesmo mecanismo: monetária ineficaz no câmbio fixo)"],
    },
    # ------------------------------------------------------------------ E1-0759
    {
        "id": "ECO-E1-0759-1", "fonte_ref": "E1-0759", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos das políticas monetária e fiscal em economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de taxas de câmbio flutuantes, uma expansão monetária provoca a desvalorização "
                      "da moeda nacional, o que tende a favorecer as exportações líquidas e, consequentemente, a "
                      "renda nacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de taxas de câmbio flutuantes, uma expansão monetária provoca a "
                      "<u>desvalorização</u> da moeda nacional, o que <u>tende a favorecer</u> as exportações "
                      "líquidas e, consequentemente, a renda nacional."),
        "poucas": ("Mais moeda → juros menores → saída de capital → " + azb("desvalorização") + " → exportações "
                   "líquidas ↑ → " + vd("renda ↑") + ". É o canal cambial da política monetária."),
        "destrinchando": [
            "No flutuante, a expansão monetária reduz o juro doméstico; o capital sai, a procura por divisas "
            "sobe e a moeda nacional se " + vd("desvaloriza") + ".",
            "Com preços rígidos no curto prazo, a desvalorização nominal é também real: os produtos nacionais "
            "ficam mais baratos para estrangeiros e os importados mais caros para residentes. "
            + azb("Exportações líquidas") + " sobem e a IS se desloca para a direita.",
            "O “tende a” protege o item da " + azb("curva J") + ": logo após a desvalorização, o saldo comercial "
            "pode piorar (volumes demoram a reagir, mas o preço dos importados sobe na hora); a melhora vem "
            "quando vale a " + azb("condição de Marshall-Lerner") + " (soma das elasticidades-preço de "
            "exportações e importações, em módulo, maior que 1).",
            "Por isso a política monetária é eficaz no flutuante (máxima com mobilidade perfeita), ao passo que "
            "a fiscal perde força com a apreciação que provoca.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Mecanismo de manual, com o “tende a” "
                       "deixando espaço para curva J e Marshall-Lerner. As versões erradas costumam trocar "
                       "“desvalorização” por “valorização” ou “monetária” por “fiscal”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um regime de câmbio flutuante, uma expansão fiscal provoca a desvalorização da moeda "
            "nacional e eleva as exportações líquidas.”</i> → ERRADO (troca de política: a fiscal aprecia)",
            "<i>“…a desvalorização melhora imediatamente o saldo comercial, qualquer que seja a elasticidade das "
            "exportações e importações.”</i> → ERRADO (curva J; depende de Marshall-Lerner)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Política monetária eficaz em elevar a renda pela expansão das exportações líquidas, "
                            "graças à desvalorização da moeda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ e ano 2020 sugerem CEBRASPE (CACD 2020); não confirmado na fonte",
                    "quase_duplicata: ECO-E1-0753-1 (mesmo mecanismo, outra prova)"],
    },
    # ------------------------------------------------------------------ E1-0760
    {
        "id": "ECO-E1-0760-1", "fonte_ref": "E1-0760", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos das políticas monetária e fiscal em economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "O efeito final sobre a renda de uma expansão fiscal sob um regime de câmbio flutuante pode ser nulo.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O efeito final sobre a renda de uma expansão fiscal sob um regime de câmbio flutuante "
                      "<u>pode</u> ser nulo."),
        "poucas": ("Com câmbio flutuante e " + azb("mobilidade perfeita") + " de capitais, a apreciação provocada "
                   "pela expansão fiscal derruba as exportações líquidas na mesma medida: efeito final " + vd("nulo")
                   + ". O “pode” acomoda os outros graus de mobilidade."),
        "destrinchando": [
            "G ↑ → IS para a direita → i tende a subir → entrada de capital → " + vd("apreciação") + " → "
            "NX ↓ → IS volta. Com BP horizontal e LM parada, o equilíbrio só pode voltar ao ponto inicial: "
            + azb("crowding out externo total") + ".",
            "Com " + azb("mobilidade imperfeita") + " (BP inclinada), o resultado depende das inclinações: se a BP "
            "é mais plana que a LM, a fiscal gera superávit, a moeda aprecia e o efeito é parcialmente "
            "anulado; se a BP é mais inclinada, gera déficit, a moeda deprecia e a fiscal é reforçada.",
            "Com " + azb("mobilidade nula") + " (BP vertical), a expansão fiscal piora a conta corrente, deprecia "
            "a moeda e a renda sobe bastante — a fiscal fica eficaz.",
            "Daí a importância do modal: sem dizer o grau de mobilidade, “é nulo” seria generalização; “pode ser "
            "nulo” é verdadeiro porque existe o caso (mobilidade perfeita) em que isso ocorre.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O item é salvo pelo “pode”. Trocar por “é sempre nulo” "
                       "tornaria o item ERRADO, porque o resultado depende do grau de mobilidade de capitais. 🔥 "
                       "Em itens curtos de Mundell-Fleming, procure primeiro o modal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito final sobre a renda de uma expansão fiscal sob câmbio flutuante é sempre nulo, "
            "qualquer que seja a mobilidade de capitais.”</i> → ERRADO (modulador absoluto)",
            "<i>“O efeito final sobre a renda de uma expansão fiscal sob câmbio fixo e mobilidade perfeita pode "
            "ser nulo.”</i> → ERRADO (no fixo a fiscal tem eficácia máxima)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Expansão fiscal eleva juros; com livre mobilidade, a entrada de capitais aprecia a "
                            "moeda e reduz as exportações líquidas, podendo anular o efeito inicial.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ e ano 2020 sugerem CEBRASPE (CACD 2020); não confirmado na fonte",
                    "quase_duplicata: ECO-E1-0703-1 (neutralização total da fiscal no flutuante)"],
    },
    # ------------------------------------------------------------------ E1-0761
    {
        "id": "ECO-E1-0761-1", "fonte_ref": "E1-0761", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": True,
        "comando": "Acerca dos efeitos das políticas econômicas em economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A imposição de uma política comercial, como tarifas generalizadas sobre as importações sob o "
                      "regime de taxas de câmbio fixas, tende a reduzir a renda do país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de uma política comercial, como tarifas generalizadas sobre as importações sob "
                       "o regime de taxas de câmbio fixas, tende a ") + vm("reduzir") + az(" a renda do país.")),
        "poucas": ("No câmbio fixo, a tarifa age como uma " + azb("expansão da demanda") + ": importações ↓ → "
                   "exportações líquidas ↑ → IS para a direita; a entrada de capitais obriga o BC a emitir, a LM "
                   "acompanha e a renda " + vm("sobe") + "."),
        "destrinchando": [
            "Tarifa generalizada → importações mais caras → " + vd("M ↓") + " → exportações líquidas ↑ a cada "
            "nível de renda e câmbio → a " + azb("IS se desloca para a direita") + ", como numa expansão fiscal.",
            "Com câmbio fixo e mobilidade de capitais: juros tendem a subir → entrada de capital → pressão de "
            "apreciação → BC compra divisas e expande a moeda → LM para a direita → i volta a i* com "
            + vd("Y maior") + ". O mecanismo é o mesmo que torna a fiscal eficaz no câmbio fixo.",
            "Contraste com o " + azb("câmbio flutuante") + " (mobilidade perfeita): a pressão de apreciação se "
            "materializa, a moeda valoriza, as importações das outras categorias sobem e as exportações caem; a "
            "IS volta e a renda " + vd("não muda") + " — a proteção só altera a composição do comércio.",
            "Isso é a análise de curto prazo do " + oc("Mundell-Fleming") + ". Fora do modelo, tarifas "
            "generalizadas têm custos de eficiência (peso morto, retaliação, insumos mais caros), que podem "
            "reduzir a renda no longo prazo — mas não é isso que o item cobra.",
        ],
        "dissecando": (cz("[inversão]") + " Troca o sinal do efeito: a banca aposta no candidato que pensa em "
                       "“protecionismo é ruim” (argumento de eficiência) em vez de aplicar o modelo. 🔥 Política "
                       "comercial em Mundell-Fleming é tratada como choque na IS: eficaz no fixo, neutra no "
                       "flutuante com mobilidade perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio flutuante e mobilidade perfeita de capitais, uma tarifa generalizada sobre as "
            "importações não altera a renda, mas aprecia a moeda.”</i> → CERTO",
            "<i>“Sob câmbio fixo, uma tarifa sobre as importações eleva a renda e reduz as reservas "
            "internacionais.”</i> → ERRADO (as reservas aumentam: o BC compra divisas)",
        ])],
        "reescrita": ("A imposição de uma política comercial, como tarifas generalizadas sobre as importações sob o "
                      "regime de taxas de câmbio fixas, tende a " + hl("elevar") + " a renda do país."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": "A tarifa eleva as exportações líquidas, desloca a IS e eleva os juros; a entrada de "
                            "capitais expande a base monetária e desloca a LM; a renda sobe.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ e ano 2020 sugerem CEBRASPE (CACD 2020); não confirmado na fonte"],
    },
    # ------------------------------------------------------------------ E1-0762
    {
        "id": "ECO-E1-0762-1", "fonte_ref": "E1-0762", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": True,
        "comando": "Acerca dos efeitos das políticas econômicas em economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Sempre que uma política fiscal ou monetária provoca efeitos cambiais, há variação nas "
                      "exportações líquidas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Sempre") + az(" que uma política fiscal ou monetária provoca efeitos cambiais, há variação "
                                      "nas exportações líquidas.")),
        "poucas": ("Nem sempre: no " + azb("câmbio fixo") + ", a pressão cambial de uma expansão monetária é "
                   "absorvida pelo BC (venda de reservas), a moeda volta ao nível inicial e as exportações líquidas "
                   "não se alteram."),
        "destrinchando": [
            "Caso da fonte: câmbio fixo, expansão monetária → juros caem → demanda por dólares sobe (pressão de "
            "depreciação) → o BC vende divisas ao preço fixado → M volta a cair → juros retornam a i*. Houve "
            "efeito cambial (no mercado e nas " + vd("reservas") + "), mas o câmbio não mudou e as "
            + azb("exportações líquidas ficaram iguais") + ".",
            "Outras situações em que o efeito cambial não chega às exportações líquidas: (1) " + azb("câmbio "
            "real constante") + " — se a inflação doméstica acompanha a depreciação nominal (preços flexíveis, "
            "médio prazo), eP*/P não muda; (2) " + azb("curva J") + " ou falha da condição de "
            + oc("Marshall-Lerner") + " — o efeito-preço compensa o efeito-quantidade.",
            "Quando há variação: no flutuante, a monetária expansionista deprecia e eleva NX; a fiscal "
            "expansionista aprecia e reduz NX (até anular o estímulo, com mobilidade perfeita).",
            vm("Regra-âncora: o que move as exportações líquidas é o câmbio real efetivo, não a mera pressão "
               "cambial."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " O “sempre” transforma uma regularidade do câmbio flutuante "
                       "em lei geral. Basta um contraexemplo — e o câmbio fixo, em que o BC neutraliza a pressão, "
                       "é o mais cobrado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio flutuante e preços rígidos, a depreciação provocada por uma expansão monetária tende "
            "a elevar as exportações líquidas.”</i> → CERTO",
            "<i>“Sob câmbio fixo, uma expansão monetária deprecia a moeda e eleva as exportações líquidas.”</i> → "
            "ERRADO (o BC mantém a paridade; NX não muda)",
        ])],
        "reescrita": (hl("Nem sempre") + " que uma política fiscal ou monetária provoca efeitos cambiais, há "
                      "variação nas exportações líquidas."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": "No câmbio fixo, a expansão monetária pressiona o câmbio, o BC vende dólares, a moeda "
                            "doméstica se contrai e os juros voltam ao patamar inicial, sem afetar as exportações "
                            "líquidas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ e ano 2020 sugerem CEBRASPE (CACD 2020); não confirmado na fonte"],
    },
    # ------------------------------------------------------------------ E1-0768
    {
        "id": "ECO-E1-0768-1", "fonte_ref": "E1-0768", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": "Acerca do modelo IS-LM-BP, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio flutuante e com perfeita mobilidade de capitais, a política monetária "
                      "neste caso, é plenamente eficaz, pois aumenta o nível de renda geral da economia sem que haja "
                      "um aumento na taxa de juros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de câmbio flutuante e com perfeita mobilidade de capitais, a política monetária "
                      "neste caso, é <u>plenamente eficaz</u>, pois aumenta o nível de renda geral da economia "
                      "<u>sem que haja um aumento na taxa de juros</u>."),
        "poucas": ("No flutuante com mobilidade perfeita, a expansão monetária eleva a renda pelo canal do câmbio, "
                   "e o juro termina onde começou (" + vd("i = i*") + "): " + azb("eficácia máxima") + "."),
        "destrinchando": [
            "Mobilidade perfeita → BP horizontal em i*. Qualquer equilíbrio final tem de estar sobre ela: o juro "
            "doméstico " + vd("não se altera") + " entre o ponto inicial e o final.",
            "Trajetória: M ↑ → LM para a direita → i cai provisoriamente → saída de capital → "
            + vd("depreciação") + " → exportações líquidas ↑ → IS para a direita até cruzar a nova LM em i*. "
            "Resultado: " + vd("Y bem maior") + ".",
            "Atenção à redação: o juro não <b>sobe</b> (nem fica mais baixo no final). A queda é apenas "
            "transitória, o que torna a afirmação “sem aumento na taxa de juros” verdadeira.",
            "“Plenamente eficaz” é a linguagem dos manuais para o caso de eficácia máxima: todo o efeito da "
            "expansão monetária se converte em renda, sem dissipação em juros.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item de manual com dois pontos que assustam: o "
                       "absoluto “plenamente” (que aqui é correto) e a justificativa sobre os juros (que exige "
                       "lembrar que o equilíbrio final está na BP horizontal). Quem errou desconfiou do absoluto — "
                       "em Mundell-Fleming com mobilidade perfeita, os extremos costumam ser verdadeiros."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio fixo e com perfeita mobilidade de capitais, a política monetária é "
            "plenamente eficaz.”</i> → ERRADO (troca de regime: no fixo ela é ineficaz)",
            "<i>“…a política monetária é eficaz porque reduz permanentemente a taxa de juros doméstica.”</i> → "
            "ERRADO (o juro volta a i*; o canal é o câmbio)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["plenamente"], "dificuldade": 2,
        "comentario_fonte": "Com perfeita mobilidade, a taxa de juros inicial e final não se altera; juros interno "
                            "e externo se equilibram (duas imagens de gráfico no verso).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (263).png", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"},
                          {"ref": "image (265).png", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"}],
        "alertas": ["quase_duplicata: ECO-E1-0753-1, ECO-E1-0759-1 (monetária eficaz no flutuante)"],
    },
    # ------------------------------------------------------------------ E1-0769
    {
        "id": "ECO-E1-0769-1", "fonte_ref": "E1-0769", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca do modelo IS-LM-BP e dos regimes cambiais, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se há perfeita mobilidade de capitais e o Banco Central implementa uma política monetária "
                      "ativa, então o regime cambial não poderá ser do tipo câmbio fixo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se há perfeita mobilidade de capitais e o Banco Central implementa uma política monetária "
                      "ativa, então o regime cambial <u>não poderá</u> ser do tipo câmbio fixo."),
        "poucas": ("É o " + azb("trilema") + " (trindade impossível): câmbio fixo, mobilidade perfeita de capitais "
                   "e política monetária autônoma não convivem. Escolhidos os dois últimos, o câmbio tem de "
                   + vd("flutuar") + "."),
        "destrinchando": [
            "A " + azb("trindade impossível") + " (associada a " + oc("Mundell") + " e ao modelo "
            "Mundell-Fleming) diz que um país só consegue ter, ao mesmo tempo, dois de três objetivos: "
            "(1) câmbio fixo; (2) livre mobilidade de capitais; (3) política monetária independente.",
            "Por quê: com capital livre e câmbio fixo, a paridade de juros obriga i = i*. Se o BC tentar fixar "
            "outro juro, o diferencial gera fluxos de capital que o forçam a comprar ou vender reservas até "
            "desfazer a política.",
            "As três combinações possíveis: " + vd("fixo + capital livre") + " (sem política monetária — ex.: "
            "currency boards, União Monetária); " + vd("fixo + política monetária") + " (com controles de "
            "capital — ex.: Bretton Woods, China por longo tempo); " + vd("flutuante + capital livre + política "
            "monetária") + " (ex.: " + rx("Brasil desde 1999") + ", EUA, Reino Unido).",
            "Ressalva acadêmica: " + oc("Hélène Rey") + " argumentou que o ciclo financeiro global reduz a "
            "autonomia monetária mesmo com câmbio flutuante (“dilema”, não trilema) — debate útil em "
            "discursiva, mas fora do escopo do item.",
        ],
        "dissecando": (cz("[literalidade]") + " Formulação condicional direta do trilema: fixados dois vértices "
                       "(mobilidade perfeita + política monetária ativa), o terceiro cai. O “não poderá” é "
                       "absoluto, mas correto — o trilema é uma impossibilidade lógica no modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se há perfeita mobilidade de capitais e câmbio fixo, o Banco Central pode conduzir política "
            "monetária autônoma, desde que tenha reservas.”</i> → ERRADO (a esterilização não se sustenta com "
            "mobilidade perfeita)",
            "<i>“Com controles de capital, é possível combinar câmbio fixo e política monetária ativa.”</i> → "
            "CERTO",
        ]), ("🃏 Carta na manga", [
            "O tripé macroeconômico brasileiro (câmbio flutuante, metas de inflação, meta fiscal) é a escolha do "
            "vértice “flutuante” do trilema após a crise cambial de 1999."])],
        "tipo_erro": ["LITERAL"], "moduladores": ["não poderá"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito CERTO.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0309-1 (trilema aplicado ao câmbio flexível)"],
    },
    # ------------------------------------------------------------------ E1-0861
    {
        "id": "ECO-E1-0861-1", "fonte_ref": "E1-0861", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False,
        "errei": True,
        "comando": ("O diplomata responsável pelo setor econômico da embaixada brasileira em determinado país "
                    "elaborou e enviou à Secretaria de Estado um relatório sobre a situação econômica desse país. "
                    "Considerando o fato de que uma das funções do diplomata é manter o governo brasileiro "
                    "informado a respeito do contexto político, econômico e cultural do país onde ele esteja "
                    "temporariamente vivendo, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Considere que o referido país esteja em recessão e seja uma economia aberta, com câmbio "
                      "flutuante e mobilidade de capitais forte, porém não perfeita. Nesse caso, de acordo com o "
                      "modelo IS-LM-BP, a implementação de uma política fiscal expansionista, para tentar impulsionar "
                      "a atividade econômica, seria ineficaz."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considere que o referido país esteja em recessão e seja uma economia aberta, com câmbio "
                       "flutuante e mobilidade de capitais forte, porém não perfeita. Nesse caso, de acordo com o "
                       "modelo IS-LM-BP, a implementação de uma política fiscal expansionista, para tentar "
                       "impulsionar a atividade econômica, seria ") + vm("ineficaz") + az(".")),
        "poucas": ("Ineficácia total da fiscal no flutuante só ocorre com mobilidade " + azb("perfeita") + ". Com "
                   "mobilidade forte mas imperfeita (BP inclinada), a apreciação devolve " + vm("só parte") + " do "
                   "ganho: a renda final fica acima da inicial."),
        "destrinchando": [
            "Mobilidade imperfeita → " + azb("BP positivamente inclinada") + "; mobilidade forte → BP mais plana "
            "que a LM.",
            "Expansão fiscal: IS para a direita → Y e i sobem (ponto E′). Como a BP é mais plana que a LM, E′ "
            "fica <b>acima</b> da BP: a entrada de capitais supera o aumento das importações → superávit → "
            + vd("apreciação") + ".",
            "A apreciação reduz as exportações líquidas: a IS recua e a BP sobe (é preciso juro maior para "
            "equilibrar o BP com câmbio apreciado). O novo equilíbrio E₃ tem " + vd("Y₃ &gt; Y₁") + " e juro acima "
            "do inicial — o juro não precisa voltar a i*, porque a mobilidade não é perfeita.",
            "Com BP mais inclinada que a LM (mobilidade fraca), E′ ficaria abaixo da BP: déficit, depreciação e "
            "a fiscal seria até <b>reforçada</b>. Nos dois casos, eficaz.",
            vm("Regra-âncora: no flutuante, a fiscal só é ineficaz com mobilidade perfeita; quanto menor a "
               "mobilidade, mais eficaz."),
        ],
        "grafico_verso": "ECO-E1-0861-1-V1",
        "dissecando": (cz("[extrapolação · troca de conceito]") + " Estende o resultado do caso-limite "
                       "(mobilidade perfeita) para a mobilidade “forte, porém não perfeita”. O “porém não perfeita” "
                       "é a pista plantada: no IS-LM-BP, ineficácia total só aparece nos extremos. 🔥 A mesma prova "
                       "trouxe a versão com câmbio fixo e mobilidade fraca, também ERRADO pela mesma lógica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com câmbio flutuante e mobilidade perfeita de capitais […] a política fiscal expansionista "
            "seria ineficaz.”</i> → CERTO",
            "<i>“…com câmbio flutuante e mobilidade forte, porém não perfeita, a política fiscal expansionista "
            "seria eficaz, ainda que parcialmente neutralizada pela apreciação.”</i> → CERTO",
        ])],
        "reescrita": ("Considere que o referido país esteja em recessão e seja uma economia aberta, com câmbio "
                      "flutuante e mobilidade de capitais forte, porém não perfeita. Nesse caso, de acordo com o "
                      "modelo IS-LM-BP, a implementação de uma política fiscal expansionista, para tentar "
                      "impulsionar a atividade econômica, seria " + hl("eficaz, ainda que parcialmente "
                      "neutralizada pela apreciação cambial") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "TROCA_CONCEITO"], "moduladores": ["porém não perfeita"], "dificuldade": 3,
        "comentario_fonte": "Vários comentários: com mobilidade imperfeita e câmbio flutuante, a fiscal é eficaz "
                            "(a IS volta só em parte); tabela-resumo de eficácia por regime e mobilidade. O 1º "
                            "comentário descreve, por engano, o caso de câmbio fixo com mobilidade fraca.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (293).png", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "image (296).png", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "00035.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "redesenhada"},
                          {"ref": "image (292).png", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"},
                          {"ref": "image (300).png", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"},
                          {"ref": "image (299).png", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"}],
        "alertas": ["banca_provavel: contexto do diplomata e ano 2016 sugerem CEBRASPE (CACD 2016); não confirmado "
                    "na fonte",
                    "quase_duplicata: ECO-E1-0862-1 (mesma prova; câmbio fixo e mobilidade fraca)"],
    },
    # ------------------------------------------------------------------ E1-0862
    {
        "id": "ECO-E1-0862-1", "fonte_ref": "E1-0862", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False,
        "errei": False,
        "comando": ("O diplomata responsável pelo setor econômico da embaixada brasileira em determinado país "
                    "elaborou e enviou à Secretaria de Estado um relatório sobre a situação econômica desse país. "
                    "Considerando o fato de que uma das funções do diplomata é manter o governo brasileiro "
                    "informado a respeito do contexto político, econômico e cultural do país onde ele esteja "
                    "temporariamente vivendo, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Considere que o referido país esteja em recessão e seja uma economia aberta, com câmbio fixo "
                      "e fraca mobilidade de capitais. Nesse caso, de acordo com o modelo IS-LM-BP, a implementação "
                      "de uma política fiscal expansionista, para tentar impulsionar a atividade econômica, seria "
                      "ineficaz."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considere que o referido país esteja em recessão e seja uma economia aberta, com câmbio "
                       "fixo e fraca mobilidade de capitais. Nesse caso, de acordo com o modelo IS-LM-BP, a "
                       "implementação de uma política fiscal expansionista, para tentar impulsionar a atividade "
                       "econômica, seria ") + vm("ineficaz") + az(".")),
        "poucas": ("No câmbio fixo, a fiscal só é ineficaz com mobilidade " + azb("nula") + " (BP vertical). Com "
                   "mobilidade fraca, o BC enxuga moeda para defender a paridade e corta parte do ganho, mas a "
                   "renda final " + vm("sobe") + ": eficácia reduzida, não nula."),
        "destrinchando": [
            "Mobilidade fraca → " + azb("BP inclinada e mais íngreme que a LM") + ": é preciso muito juro para "
            "atrair pouco capital.",
            "Expansão fiscal: IS para a direita → Y e i sobem (E′). Como a BP é mais íngreme, E′ fica "
            "<b>abaixo</b> dela: o aumento das importações supera a entrada de capitais → " + vd("déficit no "
            "BP") + " → pressão de depreciação.",
            "Para manter o câmbio, o BC " + vd("vende reservas") + " e recolhe moeda doméstica → LM para a "
            "esquerda → juros sobem mais e o investimento cai (" + azb("crowding out") + "). O equilíbrio final "
            "E₂ fica sobre a BP, com " + vd("Y₂ &gt; Y₁") + ".",
            "Se a mobilidade fosse forte (BP mais plana que a LM), E′ ficaria acima da BP: superávit, compra de "
            "reservas, LM para a direita e fiscal <b>reforçada</b>. Com mobilidade perfeita, eficácia máxima.",
            "Quadro-síntese (eficácia da fiscal): câmbio fixo — ineficaz só sem mobilidade; câmbio flutuante — "
            "ineficaz só com mobilidade perfeita. A monetária é ineficaz no fixo (qualquer mobilidade) e eficaz "
            "no flutuante.",
        ],
        "grafico_verso": "ECO-E1-0862-1-V1",
        "dissecando": (cz("[extrapolação · troca de conceito]") + " Confunde eficácia <b>reduzida</b> com "
                       "<b>nula</b>: a mobilidade fraca diminui o efeito, mas não o elimina. Para cravar "
                       "“ineficaz”, o item precisaria do extremo (mobilidade nula). Mnemônico de cursinho: "
                       "<b>FI</b>xo-<b>FI</b>scal e <b>MO</b>vel-<b>MO</b>netária valem para mobilidade perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com câmbio fixo e ausência de mobilidade de capitais […] a política fiscal expansionista seria "
            "ineficaz.”</i> → CERTO",
            "<i>“…com câmbio fixo e fraca mobilidade de capitais, a expansão fiscal levaria o banco central a "
            "comprar reservas, reforçando seu efeito.”</i> → ERRADO (com mobilidade fraca há déficit e venda de "
            "reservas)",
        ])],
        "reescrita": ("Considere que o referido país esteja em recessão e seja uma economia aberta, com câmbio fixo "
                      "e fraca mobilidade de capitais. Nesse caso, de acordo com o modelo IS-LM-BP, a implementação "
                      "de uma política fiscal expansionista, para tentar impulsionar a atividade econômica, seria "
                      + hl("eficaz, ainda que com efeito reduzido") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "TROCA_CONCEITO"], "moduladores": ["fraca"], "dificuldade": 3,
        "comentario_fonte": "Vários comentários concordam com ERRADO: com mobilidade fraca, o BP fica deficitário, "
                            "o BC vende reservas, a LM recua e o efeito sobre a renda é pequeno, mas positivo. Um "
                            "dos comentários afirma, por engano, que haveria superávit e compra de reservas.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "00036.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "redesenhada"},
                          {"ref": "image (302).png", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "image (301).png", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "image (298).png", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["banca_provavel: contexto do diplomata e ano 2016 sugerem CEBRASPE (CACD 2016); não confirmado "
                    "na fonte",
                    "quase_duplicata: ECO-E1-0861-1 (mesma prova; câmbio flutuante e mobilidade forte imperfeita)"],
    },
    # ------------------------------------------------------------------ E1-0865
    {
        "id": "ECO-E1-0865-1", "fonte_ref": "E1-0865", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, acerca do modelo de Mundell-Fleming.",
        "rotulo_item": "Item",
        "assertiva": ("É possível afirmar, segundo o Modelo de Mundell-Fleming, que uma política monetária "
                      "expansionista do BACEN pode gerar dois efeitos macroeconômicos: apreciação da taxa de câmbio e "
                      "elevação do montante de investimentos domésticos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("É possível afirmar, segundo o Modelo de Mundell-Fleming, que uma política monetária "
                       "expansionista do BACEN pode gerar dois efeitos macroeconômicos: ") + vm("apreciação")
                    + az(" da taxa de câmbio e elevação do montante de investimentos domésticos.")),
        "poucas": ("Expansão monetária reduz o juro, provoca saída de capitais e " + azb("deprecia") + " o câmbio "
                   "(no flutuante); no fixo, o câmbio nem se move. Em nenhum caso há " + vm("apreciação") + "."),
        "destrinchando": [
            "Câmbio flutuante: M ↑ → i ↓ → saída de capitais → " + vd("depreciação") + " → exportações "
            "líquidas ↑ → Y ↑. A renda sobe pelo canal cambial.",
            "E o investimento? Com " + azb("mobilidade perfeita") + ", o juro final volta a i*: o investimento "
            "final não muda, e toda a expansão vem das exportações líquidas. Com " + azb("mobilidade "
            "imperfeita") + ", o juro final fica abaixo do inicial e o investimento sobe — daí o “pode” salvar "
            "esta parte do item.",
            "Câmbio fixo com mobilidade: o BC vende reservas para defender a paridade, a expansão é revertida e "
            "nem câmbio, nem juro, nem investimento mudam.",
            "A apreciação está associada à expansão <b>fiscal</b> no flutuante (juros ↑ atraem capital) ou a "
            "uma política monetária <b>contracionista</b>.",
            vm("Regra-âncora: monetária expansionista → juro ↓ → câmbio deprecia (nunca aprecia)."),
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " Dois efeitos listados: um impossível (apreciação) e um "
                       "possível (investimento, sob mobilidade imperfeita). Basta o primeiro para o ERRADO. O "
                       "“pode” e o “é possível afirmar” tentam suavizar, mas não salvam uma direção trocada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política monetária expansionista do BACEN pode gerar depreciação da taxa de câmbio e "
            "aumento das exportações líquidas.”</i> → CERTO",
            "<i>“…uma política monetária contracionista do BACEN pode gerar apreciação da taxa de câmbio.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("É possível afirmar, segundo o Modelo de Mundell-Fleming, que uma política monetária "
                      "expansionista do BACEN pode gerar dois efeitos macroeconômicos: " + hl("depreciação") + " da "
                      "taxa de câmbio e elevação do montante de investimentos domésticos."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["pode", "é possível"], "dificuldade": 1,
        "comentario_fonte": "No flexível com mobilidade perfeita, a expansão monetária deprecia o câmbio e eleva o "
                            "produto; no fixo, não tem efeito. O efeito cambial seria o oposto (depreciação).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0640-1 (expansão monetária no flutuante deprecia, não aprecia)"],
    },
]
