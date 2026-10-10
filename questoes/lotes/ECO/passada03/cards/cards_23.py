"""Cards do lote de redação 23 — ECO, passada 03 (notas 83: conjuntura brasileira; 84: conjuntura internacional)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "br": "🌋 Conjuntura brasileira",
    "int": "🌐 Conjuntura internacional",
}

CMD_TJPA_91 = ("No que se refere às desigualdades de renda no Brasil e ao sistema de previdência social, julgue os "
               "próximos itens.")

CMD_TJPA_98 = ("Julgue os itens que se seguem, referentes aos principais planos de estabilização econômica do século "
               "XX no Brasil e às relações comerciais e financeiras do Brasil com o mundo.")

CMD_BRICS = ("Acerca da arquitetura financeira internacional e dos novos bancos de desenvolvimento, julgue o item a "
             "seguir.")

CMD_G20 = "Acerca da atuação do G20 diante da crise financeira global de 2008, julgue o item a seguir."

CMD_SMI = "Acerca do sistema monetário internacional e do papel do dólar, julgue o item a seguir."

CMD_MSUE = "A respeito do tema, julgue (C ou E) os itens a seguir."

EXCERTO_MSUE = (
    "<p><i>Em dezembro de 2024, durante a 65ª Reunião de Cúpula do Mercosul em Montevidéu, foram anunciadas as "
    "últimas informações a respeito das negociações do Acordo de Parceria entre o Mercosul e a União Europeia. As "
    "decisões encerram um processo de negociações que se estendeu por mais de 25 anos. Esse acordo busca integrar "
    "dois dos maiores blocos econômicos do mundo, abrangendo aproximadamente 718 milhões de pessoas e um PIB "
    "combinado de cerca de US$ 22 trilhões.</i></p>"
)

CRONO_MSUE = (
    "⏳ (out/2026) Depois da conclusão de " + vd("dezembro de 2024") + ", a Comissão Europeia dividiu o texto em "
    "um Acordo de Parceria (EMPA, que exige ratificação também pelos Estados-membros) e um " + azb("Acordo "
    "Provisório de Comércio") + " (de competência exclusiva da UE). A assinatura ocorreu em " + vd("17/1/2026")
    + ", em Assunção; em " + vd("21/1/2026") + " o Parlamento Europeu enviou o texto ao Tribunal de Justiça da UE "
    "para parecer (334 × 324 votos), o que adia sua votação final; mesmo assim, o acordo comercial passou a ser "
    "aplicado provisoriamente entre a UE e o " + rx("Brasil") + " em " + vd("1º/5/2026") + ", após o Decreto "
    "Legislativo nº 14/2026 e o Decreto nº 12.953/2026."
)

CARDS = [
    # ------------------------------------------------------------------ E3-L00047
    {
        "id": "ECO-E3-L00047-1", "fonte_ref": "E3-L00047", "destino": "83", "subtema": H2["br"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA_91,
        "rotulo_item": "Item",
        "assertiva": ("Apesar de o sistema previdenciário ainda ser deficitário no Brasil, observou-se, em 2024, "
                      "redução do déficit do regime geral de previdência social."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Apesar de o sistema previdenciário <u>ainda ser deficitário</u> no Brasil, observou-se, em "
                      "2024, <u>redução do déficit</u> do regime geral de previdência social."),
        "poucas": ("O " + azb("RGPS") + " segue deficitário, mas o rombo encolheu em 2024: a arrecadação "
                   "previdenciária cresceu bem mais que a despesa com benefícios. Ser deficitário (sinal) e reduzir o "
                   "déficit (variação) não se contradizem."),
        "destrinchando": [
            "O " + azb("Regime Geral de Previdência Social") + " (RGPS), operado pelo INSS, cobre os "
            "trabalhadores do setor privado e funciona em " + azb("repartição simples") + ": as contribuições "
            "de hoje pagam os benefícios de hoje. Não se confunde com os " + azb("RPPS") + " (servidores "
            "públicos) nem com o sistema dos militares, que têm contas próprias.",
            "O déficit do RGPS é estrutural: o segmento " + azb("rural") + " é deficitário por desenho "
            "(benefício quase sem contrapartida contributiva, de caráter assistencial), e o urbano, que chegou "
            "a ser superavitário, passou ao vermelho em meados da década de 2010, com a recessão e o "
            "envelhecimento da população.",
            "⏳ (out/2026) Segundo o Tesouro Nacional, o déficit do RGPS acumulado em 12 meses caiu cerca de "
            + vd("R$ 21,7 bilhões") + " entre dez/2023 e dez/2024 (valores corrigidos pelo IPCA): a "
            "arrecadação subiu cerca de " + vd("R$ 23 bilhões") + ", e os benefícios, pouco mais de "
            + vd("R$ 1 bilhão") + ". Por trás disso, a recuperação do emprego formal e da massa salarial.",
            "Fatores estruturais que contêm a despesa: a " + azb("reforma da Previdência") + " (" + vd("EC "
            "103/2019") + ") instituiu idade mínima (65 anos para homens, 62 para mulheres, com transição) e "
            "mudou o cálculo dos benefícios. Do lado oposto, pressionam a despesa a política de valorização do "
            "salário mínimo (piso dos benefícios) e o envelhecimento demográfico.",
            vm("Regra-âncora: “deficitário” descreve o sinal do resultado; “redução do déficit” descreve sua "
               "variação — os dois podem ser verdadeiros ao mesmo tempo."),
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " O “Apesar de” arma a armadilha: o candidato lê "
                       "“deficitário” e conclui que o déficit não pode ter caído. O item exige separar nível e "
                       "variação e conhecer um dado de conjuntura do ano anterior à prova. 🔥 O CEBRASPE tem "
                       "cobrado conjuntura fiscal recente em provas de economia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em 2024, o regime geral de previdência social passou a registrar superávit, graças à reforma "
            "de 2019.”</i> → ERRADO (extrapolação: houve redução do déficit, não superávit)",
            "<i>“A reforma da Previdência de 2019 extinguiu o déficit do segmento rural do RGPS.”</i> → ERRADO "
            "(extrapolação: o rural segue estruturalmente deficitário)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["ainda", "apesar de"], "dificuldade": 2,
        "comentario_fonte": ("Seis respostas empilhadas, todas CERTO: o RGPS segue deficitário, mas em 2024 houve "
                             "redução do déficit, atribuída à recuperação do emprego formal, ao crescimento da "
                             "massa salarial e da arrecadação e aos efeitos da reforma de 2019 (EC 103)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: dado de 2024 conferido na apresentação do Resultado do Tesouro Nacional de "
                    "dez/2024 (valores em 12 meses, corrigidos pelo IPCA)"],
    },
    # ------------------------------------------------------------------ E3-L00054
    {
        "id": "ECO-E3-L00054-1", "fonte_ref": "E3-L00054", "destino": "83", "subtema": H2["br"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_98,
        "rotulo_item": "Item",
        "assertiva": ("Nas últimas décadas, a balança comercial brasileira tem-se caracterizado por um superávit "
                      "constante, impulsionado principalmente pela exportação de produtos de alta tecnologia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nas últimas décadas, a balança comercial brasileira tem-se caracterizado por um superávit ")
                    + vm("constante") + az(", impulsionado principalmente pela exportação de ")
                    + vm("produtos de alta tecnologia") + az(".")),
        "poucas": ("Dois erros: o saldo comercial brasileiro " + vm("não foi constante") + " (houve déficits na "
                   "segunda metade dos anos 1990 e em 2014), e os superávits vêm de " + azb("commodities")
                   + " (soja, petróleo bruto, minério de ferro), não de alta tecnologia."),
        "destrinchando": [
            "Trajetória: déficits comerciais em " + vd("1995–2000") + " (real valorizado da âncora cambial do "
            "Plano Real); superávits a partir de " + vd("2001") + ", ampliados pelo " + azb("superciclo das "
            "commodities") + " e pela demanda chinesa; novo déficit em " + vd("2014") + "; superávits "
            "ininterruptos desde " + vd("2015") + ".",
            "⏳ (out/2026) Saldo recorde de " + vd("US$ 98,9 bilhões em 2023") + "; " + vd("US$ 74,6 bilhões") + " em "
            "2024 e " + vd("US$ 68,3 bilhões") + " em 2025 (Secex/MDIC). A " + rx("China") + " é o principal "
            "destino das exportações brasileiras desde 2009.",
            "Composição: a pauta é puxada por " + azb("produtos básicos") + " — soja, petróleo bruto, minério "
            "de ferro, carnes, café, celulose, açúcar. Em bens de " + azb("alta e média-alta intensidade "
            "tecnológica") + " (química fina, eletrônicos, fármacos, máquinas) o Brasil é deficitário; a "
            "exceção notória é a aeronáutica (Embraer).",
            "Debate associado: " + azb("reprimarização") + " da pauta e " + azb("desindustrialização "
            "precoce") + " — a participação da indústria no PIB caiu antes de a renda per capita atingir níveis "
            "de país desenvolvido. Há também quem veja na produtividade do agronegócio uma vantagem comparativa "
            "a explorar, e não um sintoma.",
            vm("Regra-âncora: superávit comercial brasileiro = commodities + China; alta tecnologia é ponto de "
               "déficit."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Parte verdadeira: há superávits relevantes "
                       "nas últimas décadas. Enxertos: o adjetivo absoluto “constante” e a troca do motor do "
                       "saldo (commodities → alta tecnologia). Pista: “alta tecnologia” contradiz o perfil "
                       "conhecido da pauta brasileira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Desde 2015, a balança comercial brasileira registra superávits anuais, sustentados sobretudo "
            "por exportações de produtos básicos.”</i> → CERTO",
            "<i>“O superávit comercial recorde de 2023 decorreu principalmente da queda das exportações de "
            "commodities.”</i> → ERRADO (nexo indevido: decorreu do volume recorde de exportações agrícolas e de "
            "petróleo)",
        ]), ("🃏 Carta na manga", [
            "A combinação “superávit comercial + déficit em manufaturados de alta tecnologia” é o retrato da "
            "inserção externa brasileira e base empírica do debate sobre reprimarização e política industrial "
            "(Nova Indústria Brasil, 2024) ⏳ (out/2026).",
        ])],
        "reescrita": ("Nas últimas décadas, a balança comercial brasileira tem-se caracterizado por um superávit "
                      + hl("frequente") + ", impulsionado principalmente pela exportação de "
                      + hl("commodities agrícolas e minerais") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["constante", "principalmente"],
        "dificuldade": 1,
        "comentario_fonte": ("Seis respostas, todas ERRADO: superávits puxados por agronegócio e commodities, não "
                             "por alta tecnologia; o saldo não foi constante (déficits nos anos 1990 e início dos "
                             "2000); reprimarização e desindustrialização."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: duas respostas da fonte situam déficits no “início dos anos 2000”; a "
                    "balança voltou ao superávit em 2001 — o último déficit antes de 2014 foi o de 2000"],
    },
    # ------------------------------------------------------------------ E1-0698
    {
        "id": "ECO-E1-0698-1", "fonte_ref": "E1-0698", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Acerca da conjuntura do comércio internacional e das tarifas impostas pelos Estados Unidos, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Países atingidos pelas tarifas americanas responderam com medidas protecionistas próprias, o "
                      "que pode contribuir para menos comércio, incerteza para investidores e volatilidade nos "
                      "mercados financeiros globais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Países atingidos pelas tarifas americanas responderam com medidas protecionistas próprias, o "
                      "que <u>pode contribuir</u> para menos comércio, incerteza para investidores e volatilidade "
                      "nos mercados financeiros globais."),
        "poucas": ("A retaliação existiu (China e Canadá à frente) e a escalada tarifária reduz o comércio, eleva "
                   "a " + azb("incerteza") + " e alimenta a volatilidade. O “pode contribuir” torna o item "
                   "seguro."),
        "destrinchando": [
            "⏳ (out/2026) Em 2025, os EUA elevaram tarifas em série — sobre aço, alumínio e automóveis (Seção "
            "232) e as tarifas “recíprocas” anunciadas em " + vd("2/4/2025") + ". A " + azb("China") + " "
            "retaliou com sobretaxas que chegaram a " + vd("125%") + " em abril, até a trégua negociada em "
            "Genebra, em maio; o " + azb("Canadá") + " impôs contratarifas; a " + azb("União Europeia") + " "
            "preparou contramedidas, mas fechou acordo com tarifa-base de 15%; o México preferiu negociar.",
            "⏳ (out/2026) " + rx("Brasil") + ": sobretaxa adicional de 40% (50% no total) a partir de "
            "agosto de 2025, com longa lista de exceções; o país aprovou a " + azb("Lei da Reciprocidade "
            "Econômica") + " (" + vd("Lei 15.122/2025") + "), abriu consultas na OMC e privilegiou a "
            "negociação. Em " + vd("20/2/2026") + ", a Suprema Corte dos EUA decidiu que a IEEPA não autoriza o "
            "presidente a impor tarifas; o governo recorreu a outra base legal (Seção 122, tarifa temporária "
            "de 10%).",
            "Mecanismo: a retaliação transforma o protecionismo num " + azb("dilema do prisioneiro") + " — "
            "cada país “ganha” ao tarifar, mas todos perdem quando todos tarifam. O precedente clássico é a "
            "Smoot-Hawley (" + vd("1930") + "), seguida de retaliações que contraíram o comércio mundial na "
            "Depressão.",
            "Canais: (1) menos comércio — preços maiores, desvio e quebra de cadeias de valor; (2) "
            + azb("incerteza") + " — com investimento irreversível, a empresa adia decisões até a regra ficar "
            "clara (valor da espera); (3) volatilidade — ações, câmbio e commodities reagem a cada anúncio.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Item descritivo de conjuntura: o fato "
                       "(houve retaliação) é verdadeiro, e as consequências vêm suavizadas por “pode "
                       "contribuir”. Para errar, a banca precisaria de absolutos (“todos os países retaliaram”) "
                       "ou de efeitos invertidos (“mais comércio”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todos os países atingidos pelas tarifas americanas retaliaram com tarifas equivalentes.”</i> → "
            "ERRADO (modulador absoluto: México e UE preferiram negociar)",
            "<i>“A retaliação tarifária tende a ampliar o volume de comércio global, ao forçar a reabertura "
            "negociada dos mercados.”</i> → ERRADO (inversão: o efeito imediato é contração)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Retaliação de China, Canadá, México e UE é fato central da guerra comercial de "
                             "2025–2026; tarifas espelho reduzem o comércio e criam incerteza; o Brasil acionou "
                             "mecanismos de reciprocidade (notas do MDIC e do Itamaraty de fevereiro de 2026)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte inclui o México entre os retaliadores (o México optou por "
                    "negociar) e cita notas do MDIC/Itamaraty de fev/2026 não verificadas — ambas omitidas"],
    },
    # ------------------------------------------------------------------ E1-0958
    {
        "id": "ECO-E1-0958-1", "fonte_ref": "E1-0958", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_BRICS,
        "rotulo_item": "Item",
        "assertiva": ("O Arranjo Contingente de Reservas (CRA) e o Novo Banco de Desenvolvimento constituem passos "
                      "importantes na criação de uma arquitetura financeira conjunta do BRICS. Com função similar "
                      "à do Fundo Monetário Internacional, o CRA pretende complementar a rede global de proteção "
                      "financeira, ajudando a prevenir pressões de curto prazo, reais ou potenciais, sobre o "
                      "balanço de pagamentos dos países do grupo. Para isso, cada país contribuirá, inicialmente, "
                      "com um quinto do total de recursos (US$ 100 bilhões) comprometidos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Arranjo Contingente de Reservas (CRA) e o Novo Banco de Desenvolvimento constituem "
                       "passos importantes na criação de uma arquitetura financeira conjunta do BRICS. Com função "
                       "similar à do Fundo Monetário Internacional, o CRA pretende complementar a rede global de "
                       "proteção financeira, ajudando a prevenir pressões de curto prazo, reais ou potenciais, "
                       "sobre o balanço de pagamentos dos países do grupo. Para isso, cada país contribuirá, "
                       "inicialmente, com ") + vm("um quinto") + az(" do total de recursos (US$ 100 bilhões) "
                                                                      "comprometidos.")),
        "poucas": ("Os " + vd("US$ 100 bilhões") + " do " + azb("CRA") + " não são divididos em partes "
                   "iguais: " + vd("China 41") + ", " + vd("Brasil, Rússia e Índia 18 cada") + ", "
                   + vd("África do Sul 5") + ". A divisão igualitária é a do capital do Novo Banco de "
                   "Desenvolvimento."),
        "destrinchando": [
            "O " + azb("Arranjo Contingente de Reservas") + " foi criado pelo tratado assinado na Cúpula de "
            + vd("Fortaleza (julho de 2014)") + ", junto com o acordo do NDB. Não é um fundo com caixa "
            "próprio: cada país mantém suas reservas e se compromete a cedê-las, por " + azb("swaps de "
            "moeda") + ", ao sócio que enfrentar pressão sobre o balanço de pagamentos.",
            "Compromissos (total de " + vd("US$ 100 bilhões") + "): " + vd("China, US$ 41 bi") + "; "
            + rx("Brasil") + ", Rússia e Índia, " + vd("US$ 18 bi cada") + "; África do Sul, " + vd("US$ 5 bi")
            + ". O acesso é proporcional ao aporte, por multiplicadores: a China pode sacar metade do que "
            "comprometeu; a África do Sul, o dobro.",
            "Vínculo com o FMI: só " + vd("30%") + " do limite de cada país pode ser sacado livremente; os "
            + vd("70%") + " restantes exigem programa vigente com o " + azb("FMI") + ". Por isso o CRA "
            "<b>complementa</b> a rede global de proteção financeira em vez de substituí-la, como diz o item.",
            "Contraste com o " + azb("Novo Banco de Desenvolvimento") + " (NDB): capital autorizado de "
            + vd("US$ 100 bilhões") + " e capital subscrito inicial de " + vd("US$ 50 bilhões") + ", dividido "
            "<b>igualmente</b> entre os cinco fundadores, com voto igual. A igualdade é do banco; no CRA, a "
            "assimetria reflete o peso das reservas chinesas.",
            vm("Regra-âncora: NDB = cotas iguais (20% cada); CRA = 41 / 18 / 18 / 18 / 5."),
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " Todo o texto é correto até a última "
                       "frase, que transplanta para o CRA a divisão igualitária do NDB. O “um quinto” parece "
                       "natural num grupo de cinco — é justamente essa intuição que a banca explora."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O acesso integral aos recursos do CRA independe de acordo com o FMI.”</i> → ERRADO (restrição "
            "omitida: 70% exigem programa com o FMI)",
            "<i>“O capital subscrito inicial do NDB, de US$ 50 bilhões, foi dividido igualmente entre os "
            "membros fundadores.”</i> → CERTO",
        ])],
        "reescrita": ("O Arranjo Contingente de Reservas (CRA) e o Novo Banco de Desenvolvimento constituem passos importantes "
                      "na criação de uma arquitetura financeira conjunta do BRICS. Com função similar à do Fundo Monetário "
                      "Internacional, o CRA pretende complementar a rede global de proteção financeira, ajudando a prevenir "
                      "pressões de curto prazo, reais ou potenciais, sobre o balanço de pagamentos dos países do grupo. "
                      "Para isso, cada país contribuirá, inicialmente, com " + hl("uma parcela diferenciada")
                      + " do total de recursos (US$ 100 bilhões) comprometidos" + hl(": China, US$ 41 bilhões; "
                      "Brasil, Rússia e Índia, US$ 18 bilhões cada; África do Sul, US$ 5 bilhões") + "."),
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": ["cada"], "dificuldade": 2,
        "comentario_fonte": ("Errado: o erro estaria no capital do banco de desenvolvimento — capital subscrito "
                             "inicial de US$ 50 bilhões e autorizado de US$ 100 bilhões, divididos igualmente "
                             "entre os fundadores, e não para cada membro."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário da fonte explica o erro pelo capital do NDB; o item trata do "
                    "CRA, cujos US$ 100 bilhões têm aportes desiguais (41/18/18/18/5) — comentário corrigido, "
                    "gabarito mantido"],
    },
    # ------------------------------------------------------------------ E1-0959
    {
        "id": "ECO-E1-0959-1", "fonte_ref": "E1-0959", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_BRICS,
        "rotulo_item": "Item",
        "assertiva": ("A criação do Novo Banco de Desenvolvimento (NDB) e do Banco Asiático de Investimento em "
                      "Infraestrutura (AIIB) liderado pela China circunscreve-se a contexto no qual o papel dos "
                      "bancos de desenvolvimento voltou ao debate, seja por sua atuação anticíclica em momentos de "
                      "crise, seja pela função que exercem como canalizadores de recursos (públicos e privados) "
                      "para financiamento de projetos de longo prazo. Nessa direção, os mandatos do NDB e do AIIB "
                      "vão ao encontro dos compromissos assumidos pelo G20 em 2016 com a Agenda 2030 do "
                      "Desenvolvimento Sustentável."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A criação do Novo Banco de Desenvolvimento (NDB) e do Banco Asiático de Investimento em "
                      "Infraestrutura (AIIB) liderado pela China circunscreve-se a contexto no qual o papel dos "
                      "bancos de desenvolvimento voltou ao debate, seja por sua <u>atuação anticíclica</u> em "
                      "momentos de crise, seja pela função que exercem como <u>canalizadores de recursos (públicos "
                      "e privados)</u> para financiamento de projetos de longo prazo. Nessa direção, os mandatos do "
                      "NDB e do AIIB vão ao encontro dos compromissos assumidos pelo G20 em <u>2016</u> com a "
                      "Agenda 2030 do Desenvolvimento Sustentável."),
        "poucas": ("Depois de 2008, os " + azb("bancos de desenvolvimento") + " voltaram ao centro do debate "
                   "pelo papel anticíclico e pelo financiamento de longo prazo; NDB e AIIB, focados em "
                   "infraestrutura e sustentabilidade, alinham-se ao plano do " + azb("G20 de Hangzhou (2016)")
                   + " para a Agenda 2030."),
        "destrinchando": [
            "Papel " + azb("anticíclico") + ": na crise de 2008–2009, enquanto os bancos privados retraíam o "
            "crédito, bancos públicos de desenvolvimento ampliaram empréstimos — o " + rx("BNDES") + " no "
            "Brasil, o KfW na Alemanha, o Banco Mundial e o BID no plano multilateral. A experiência "
            "enfraqueceu a visão dos anos 1990, que os via como fonte de distorção a ser reduzida.",
            "Papel " + azb("estrutural") + ": projetos de infraestrutura têm prazo longo de maturação, grande "
            "escala e retornos sociais acima dos privados; o mercado privado oferece pouco crédito longo nessas "
            "condições. Bancos de desenvolvimento alongam prazos e " + azb("alavancam") + " capital privado "
            "(cofinanciamento, garantias).",
            "Os novos bancos: o " + azb("NDB") + " (BRICS, tratado de Fortaleza em 2014, sede em Xangai) tem "
            "mandato de infraestrutura e desenvolvimento sustentável em emergentes; o " + azb("AIIB") + " "
            "(proposto pela China em 2013, em operação desde " + vd("janeiro de 2016") + ", sede em Pequim) "
            "financia infraestrutura e conectividade na Ásia.",
            "G20: a Cúpula de " + vd("Hangzhou (2016)") + ", sob presidência chinesa, adotou o " + azb("Plano "
            "de Ação do G20 para a Agenda 2030") + ", aprovada na ONU em 2015 com os 17 ODS. O financiamento de "
            "infraestrutura por bancos multilaterais aparece também na Agenda de Ação de Adis Abeba (2015), "
            "sobre financiamento do desenvolvimento.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Item longo e descritivo, sem moduladores absolutos: "
                       "a dificuldade é só confirmar o detalhe do G20 em 2016 (Hangzhou). Itens da mesma família "
                       "costumam errar trocando o ano, o mandato (“exclusivamente asiático” para o NDB) ou "
                       "negando a função anticíclica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os bancos de desenvolvimento perderam relevância após a crise de 2008, por sua atuação "
            "pró-cíclica…”</i> → ERRADO (inversão: atuaram de forma anticíclica)",
            "<i>“…os mandatos do NDB e do AIIB restringem-se ao financiamento de projetos nos países-membros "
            "fundadores.”</i> → ERRADO (restrição indevida: ambos admitem novos membros e projetos neles)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Correto. A alternativa é exaustiva no que há de relevante ao tema escolhido.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0960
    {
        "id": "ECO-E1-0960-1", "fonte_ref": "E1-0960", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_G20,
        "rotulo_item": "Item",
        "assertiva": ("Em meio às turbulências da crise financeira global eclodida em 2008, a Cúpula do G20 emitiu "
                      "declaração em 2009, na qual seus líderes se comprometeram com reformas na governança do "
                      "Fundo Monetário Internacional (FMI) e do Banco Mundial. No primeiro, por meio de mudança na "
                      "quota de participação no FMI de, no mínimo, 5% em favor dos mercados emergentes e países em "
                      "desenvolvimento; no segundo, pela adoção de uma fórmula que refletisse o peso econômico dos "
                      "países em desenvolvimento e que acarretasse o aumento de seu poder de voto em pelo menos "
                      "3%, neles incluídos os países em transição."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em meio às turbulências da crise financeira global eclodida em 2008, a Cúpula do G20 emitiu "
                      "declaração em <u>2009</u>, na qual seus líderes se comprometeram com reformas na governança "
                      "do Fundo Monetário Internacional (FMI) e do Banco Mundial. No primeiro, por meio de mudança "
                      "na quota de participação no FMI de, <u>no mínimo, 5%</u> em favor dos mercados emergentes e "
                      "países em desenvolvimento; no segundo, pela adoção de uma fórmula que refletisse o peso "
                      "econômico dos países em desenvolvimento e que acarretasse o aumento de seu poder de voto em "
                      "<u>pelo menos 3%</u>, neles incluídos os países em transição."),
        "poucas": ("É a Declaração de " + vd("Pittsburgh (setembro de 2009)") + ": transferência de ao menos "
                   + vd("5%") + " das quotas do FMI para emergentes e em desenvolvimento e de ao menos "
                   + vd("3%") + " do poder de voto no Banco Mundial para países em desenvolvimento e em "
                   "transição."),
        "destrinchando": [
            "Contexto: a crise de 2008 projetou o " + azb("G20") + " (criado em 1999 no nível de ministros de "
            "Finanças) ao nível de chefes de Estado — Washington (nov/2008), Londres (abr/2009), " + vd("Pittsburgh "
            "(set/2009)") + " —, e Pittsburgh o declarou o principal foro de cooperação econômica internacional. "
            "A legitimidade das instituições de " + azb("Bretton Woods") + " dependia de dar mais voz aos "
            "emergentes.",
            "No " + azb("FMI") + ", as quotas definem contribuição, acesso a recursos e poder de voto. A promessa "
            "de Pittsburgh resultou na " + azb("reforma de 2010") + " (14ª Revisão Geral): duplicação das quotas "
            "e transferência de mais de " + vd("6%") + " delas para países dinâmicos sub-representados, com a "
            "China em 3º lugar e " + rx("Brasil") + ", Índia e Rússia entre os dez maiores cotistas. Só entrou "
            "em vigor em " + vd("janeiro de 2016") + ", depois da aprovação tardia pelo Congresso dos EUA, cujo "
            "voto era indispensável.",
            "No " + azb("Banco Mundial") + ", a reforma de “voz e participação” de 2010 transferiu "
            + vd("3,13%") + " do poder de voto no BIRD para países em desenvolvimento e em transição "
            "(" + vd("4,59%") + " somadas as etapas desde 2008), levando-os a cerca de " + vd("47%") + ".",
            "⏳ (out/2026) Os EUA mantêm cerca de 16,5% dos votos no FMI e, com isso, poder de veto nas "
            "decisões que exigem 85%. A 16ª Revisão (2023) aprovou aumento de 50% das quotas sem realinhamento — "
            "a redistribuição segue pendente, uma das razões apontadas para iniciativas como NDB e CRA.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item reproduz a declaração com seus números e "
                       "moduladores (“no mínimo”, “pelo menos”). A armadilha é a precisão: inverter 5% e 3%, "
                       "trocar 2009 por 2010 (ano da reforma do FMI) ou dizer que a reforma vigorou logo em "
                       "seguida."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a reforma de quotas do FMI acordada em 2010 entrou em vigor no mesmo ano, com o apoio imediato "
            "do Congresso dos EUA.”</i> → ERRADO (dado alterado: vigorou só em 2016)",
            "<i>“…mudança na quota de participação no FMI de, no mínimo, 3%…; no Banco Mundial, aumento de poder "
            "de voto de pelo menos 5%…”</i> → ERRADO (dados invertidos: 5% no FMI, 3% no Banco Mundial)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["no mínimo", "pelo menos"], "dificuldade": 2,
        "comentario_fonte": "Correto. A alternativa é exaustiva no que há de relevante ao tema escolhido.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0961
    {
        "id": "ECO-E1-0961-1", "fonte_ref": "E1-0961", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_G20,
        "rotulo_item": "Item",
        "assertiva": ("Em várias reuniões do G20 foram apontadas falhas graves de regulamentação e supervisão, além "
                      "dos riscos irresponsavelmente assumidos por parte de bancos e outras instituições "
                      "financeiras, que acabaram criando fragilidades que contribuíram para o agravamento da crise "
                      "econômica de 2008. Um ponto ausente nessas pautas foi a necessidade de reforma das agências "
                      "de classificação de risco, pois elas têm subestimado os impactos que uma classificação "
                      "equivocada de riscos pode provocar no mercado e nas economias sob suas análises."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em várias reuniões do G20 foram apontadas falhas graves de regulamentação e supervisão, "
                       "além dos riscos irresponsavelmente assumidos por parte de bancos e outras instituições "
                       "financeiras, que acabaram criando fragilidades que contribuíram para o agravamento da "
                       "crise econômica de 2008. Um ponto ") + vm("ausente") + az(" nessas pautas foi a "
                       "necessidade de reforma das agências de classificação de risco, pois elas têm subestimado "
                       "os impactos que uma classificação equivocada de riscos pode provocar no mercado e nas "
                       "economias sob suas análises.")),
        "poucas": ("As " + azb("agências de rating") + " estiveram na pauta do G20 desde a primeira cúpula "
                   "(" + vd("Washington, nov/2008") + "): registro, supervisão e redução da dependência regulatória "
                   "de suas notas."),
        "destrinchando": [
            "Por que as agências viraram alvo: deram nota máxima (AAA) a títulos lastreados em hipotecas "
            + azb("subprime") + " e a CDOs que se desvalorizaram em massa em 2007–2008. Problemas apontados: "
            + azb("conflito de interesses") + " (o emissor paga pela nota — modelo “issuer pays”), modelos que "
            "subestimavam a correlação dos calotes e uso mecânico das notas pela regulação.",
            "Respostas do G20: o Plano de Ação de " + vd("Washington (2008)") + " já previa que as agências "
            "evitassem conflitos de interesse e dessem mais transparência; em " + vd("Londres (abr/2009)")
            + ", os líderes acordaram submetê-las a " + azb("registro e supervisão") + " obrigatórios, em linha "
            "com o código da IOSCO, e transformaram o Fórum de Estabilidade Financeira no " + azb("Conselho de "
            "Estabilidade Financeira (FSB)") + ", ampliado a todos os membros do G20.",
            "Desdobramentos: regulamento da UE sobre agências de rating (2009), lei Dodd-Frank nos EUA (2010) e "
            "princípios do FSB (2010) para reduzir a dependência de notas externas em normas e contratos. No "
            "plano bancário, a agenda resultou em " + azb("Basileia III") + " (2010).",
            "O resto do item é verdadeiro: regulação e supervisão falhas e risco excessivo (alavancagem, "
            "securitização, sistema bancário paralelo) são o diagnóstico padrão das declarações do G20.",
            vm("Regra-âncora: as agências de rating estiveram na pauta do G20 desde 2008."),
        ],
        "dissecando": (cz("[contradição · meia-verdade]") + " Primeira frase verdadeira e longa; o erro é uma "
                       "só palavra (“ausente”), escondida no começo da segunda. A justificativa que vem depois "
                       "(“pois elas têm subestimado…”) é verdadeira e reforça a impressão de correção — mas "
                       "justifica exatamente por que o tema <b>esteve</b> na pauta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na Cúpula de Londres (2009), o G20 criou o Conselho de Estabilidade Financeira, sucessor do "
            "Fórum de Estabilidade Financeira.”</i> → CERTO",
            "<i>“O G20 decidiu proibir o modelo em que o emissor remunera a agência de rating.”</i> → ERRADO "
            "(extrapolação: houve registro e supervisão, não proibição do modelo)",
        ])],
        "reescrita": ("Em várias reuniões do G20 foram apontadas falhas graves de regulamentação e supervisão, além dos "
                      "riscos irresponsavelmente assumidos por parte de bancos e outras instituições financeiras, que "
                      "acabaram criando fragilidades que contribuíram para o agravamento da crise econômica de 2008. "
                      "Um ponto " + hl("presente") + " nessas pautas foi a necessidade de reforma das agências "
                      "de classificação de risco, pois elas têm subestimado os impactos que uma classificação "
                      "equivocada de riscos pode provocar no mercado e nas economias sob suas análises."),
        "tipo_erro": ["CONTRADICAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Errado: as agências de rating foram tratadas pelo G20 já em 2008; a expansão do "
                             "Financial Stability Board aos países do G20 incluiu, entre suas funções, a atribuição "
                             "e o desempenho das agências."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0975
    {
        "id": "ECO-E1-0975-1", "fonte_ref": "E1-0975", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": "Acerca dos processos de integração econômica na América Latina, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A integração econômica da América do Sul envolve a UNASUL e o MERCOSUL, mas não considera a "
                      "Comunidade dos Estados Latino-Americanos e Caribenhos (CELAC) nem a Cúpula da América Latina "
                      "e o Caribe (CALC), as quais tratam da integração da América do Sul e do Caribe."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A integração econômica da América do Sul envolve a UNASUL e o MERCOSUL, ")
                    + vm("mas não considera") + az(" a Comunidade dos Estados Latino-Americanos e Caribenhos "
                                                   "(CELAC) ") + vm("nem") + az(" a Cúpula da América Latina e o "
                                                                                "Caribe (CALC), as quais tratam "
                                                                                "da integração da ")
                    + vm("América do Sul") + az(" e do Caribe.")),
        "poucas": ("CALC e CELAC abrangem toda a " + azb("América Latina e o Caribe") + " — logo, também a "
                   "América do Sul. Ampliar o escopo não exclui a integração sul-americana; os foros se "
                   "sobrepõem."),
        "destrinchando": [
            "Os círculos concêntricos da integração regional: " + azb("MERCOSUL") + " (" + vd("1991") + ", "
            "Tratado de Assunção; integração econômica, união aduaneira imperfeita); " + azb("UNASUL") + " "
            "(tratado de Brasília, " + vd("2008") + "; 12 países sul-americanos; agenda política, de defesa e "
            "de infraestrutura); " + azb("CALC") + " e " + azb("CELAC") + ", no nível latino-americano e "
            "caribenho.",
            "A " + azb("CALC") + " — Cúpula da América Latina e do Caribe sobre Integração e Desenvolvimento — "
            "reuniu-se pela primeira vez em " + vd("dezembro de 2008") + ", na Costa do Sauípe (BA), por "
            "iniciativa do " + rx("Brasil") + ": foi a primeira cúpula dos países da região sem a presença de "
            "potências extrarregionais.",
            "A " + azb("CELAC") + " nasceu da fusão da CALC com o Grupo do Rio (decisão na Cúpula da Unidade, "
            + vd("2010") + "; fundação formal em Caracas, " + vd("2011") + "). Reúne os 33 Estados da América "
            "Latina e do Caribe, sem EUA e Canadá, e funciona como foro de concertação, sem secretariado nem "
            "tratado constitutivo; é a interlocutora regional em diálogos como CELAC–UE e CELAC–China.",
            "⏳ (out/2026) " + rx("Brasil") + ": deixou a UNASUL em 2019 e suspendeu sua participação na "
            "CELAC em 2020; retornou a ambas em 2023.",
        ],
        "dissecando": (cz("[restrição indevida · contradição]") + " O item cria uma exclusão (“mas não "
                       "considera… nem…”) e a justifica com um escopo errado: diz que CELAC e CALC tratam da "
                       "“América do Sul e do Caribe”, como se não incluíssem toda a América Latina. Pista: um "
                       "foro que abrange a América Latina abrange, por definição, a América do Sul."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A CELAC resultou da convergência entre o Grupo do Rio e a CALC e não inclui os Estados Unidos "
            "nem o Canadá.”</i> → CERTO",
            "<i>“A CELAC é uma organização internacional com tratado constitutivo e secretariado permanente, "
            "nos moldes da OEA.”</i> → ERRADO (troca de conceito: é foro de concertação, sem secretariado)",
        ])],
        "reescrita": ("A integração econômica da América do Sul envolve a UNASUL e o MERCOSUL, "
                      + hl("e também considera") + " a Comunidade dos Estados Latino-Americanos e Caribenhos "
                      "(CELAC) " + hl("e") + " a Cúpula da América Latina e o Caribe (CALC), as quais tratam da "
                      "integração da " + hl("América Latina") + " e do Caribe."),
        "tipo_erro": ["RESTRICAO", "CONTRADICAO"], "moduladores": ["não", "nem"], "dificuldade": 2,
        "comentario_fonte": ("Errado: após o Mercosul (1991), vieram a Unasul (2008) e a CELAC (2010); a CELAC "
                             "difere da OEA por excluir EUA e Canadá e é foro de declarações conjuntas; incorporar "
                             "América Central e Caribe não exclui o propósito integrador sul-americano, apenas "
                             "expande seu escopo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: tema de integração regional na fronteira com PI; mantido na nota 84 por falta "
                    "de nota de integração regional no plano de ECO"],
    },
    # ------------------------------------------------------------------ E1-0978
    {
        "id": "ECO-E1-0978-1", "fonte_ref": "E1-0978", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": CMD_BRICS,
        "rotulo_item": "Item",
        "assertiva": ("A criação de novos bancos de desenvolvimento em todos os níveis — nacional, regional e "
                      "internacional —, embora seja importante para atender as demandas de investimento em "
                      "infraestrutura e desenvolvimento sustentável, não tem sido vista como uma iniciativa "
                      "promissora devido à oferta inadequada de crédito de curto prazo para investimentos na "
                      "economia real."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A criação de novos bancos de desenvolvimento em todos os níveis — nacional, regional e "
                       "internacional —, ") + vm("embora seja") + az(" importante para atender as demandas de "
                                                                      "investimento em infraestrutura e "
                                                                      "desenvolvimento sustentável, ")
                    + vm("não") + az(" tem sido vista como uma iniciativa promissora devido à oferta inadequada "
                                                         "de crédito de ") + vm("curto") + az(" prazo para "
                                                                                              "investimentos na "
                                                                                              "economia real.")),
        "poucas": ("É o contrário: os novos bancos de desenvolvimento são vistos como " + azb("promissores")
                   + " justamente porque falta crédito de " + vm("longo") + " prazo para infraestrutura — o "
                   "crédito curto não financia projetos de longa maturação."),
        "destrinchando": [
            "Infraestrutura exige " + azb("funding de longo prazo") + ": investimentos volumosos, com décadas "
            "de vida útil e retorno lento. Financiá-los com crédito curto cria " + azb("descasamento de "
            "prazos") + " — o tomador precisa rolar a dívida em condições incertas.",
            "Os bancos privados preferem prazos curtos (capital de giro, desconto de recebíveis): têm passivo "
            "curto, metas de rentabilidade trimestral e aversão a riscos de projeto; o crédito curto também "
            "oscila com o ciclo e some na crise. Daí a " + azb("lacuna de financiamento") + " em "
            "infraestrutura, que os bancos de desenvolvimento preenchem.",
            "Por isso a década de 2010 viu a criação ou o fortalecimento desses bancos em todos os níveis: "
            "nacionais (BNDES, KfW, CDB chinês), regionais (CAF, BID) e internacionais (" + azb("NDB") + ", "
            + azb("AIIB") + "), com mandatos ligados à infraestrutura e à Agenda 2030.",
            "Críticas legítimas existem (subsídio implícito, risco fiscal, escolha de “campeões nacionais” no "
            "caso do " + rx("BNDES") + " entre 2008 e 2014), mas não por excesso de crédito de longo prazo no "
            "mercado.",
            vm("Regra-âncora: banco de desenvolvimento = resposta à escassez de crédito LONGO."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " Dois giros: inverte a avaliação (“não tem sido "
                       "vista como promissora”) e troca o prazo do crédito em falta (longo → curto). Pista: o "
                       "próprio item reconhece a importância para infraestrutura, que é investimento de longo "
                       "prazo por natureza."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A insuficiência de crédito de longo prazo para infraestrutura é um dos argumentos a favor da "
            "criação de novos bancos de desenvolvimento.”</i> → CERTO",
            "<i>“A volatilidade do crédito de curto prazo torna desnecessários os bancos de desenvolvimento, pois "
            "as empresas podem rolar dívidas curtas.”</i> → ERRADO (nexo indevido: a volatilidade reforça a "
            "necessidade deles)",
        ])],
        "reescrita": ("A criação de novos bancos de desenvolvimento em todos os níveis — nacional, regional e "
                      "internacional —, " + hl("por ser") + " importante para atender as demandas de investimento "
                      "em infraestrutura e desenvolvimento sustentável, <s>não</s> tem sido vista como uma "
                      "iniciativa promissora devido à oferta inadequada de crédito de " + hl("longo") + " prazo "
                      "para investimentos na economia real."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Errado: é exatamente porque o crédito de curto prazo oscila excessivamente que os "
                             "bancos de desenvolvimento se tornam importantes; infraestrutura exige financiamento "
                             "de longa maturidade, que só esses bancos logram oferecer."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0979-1 (mesma justificativa dos bancos de desenvolvimento, em versão "
                    "CERTO)"],
    },
    # ------------------------------------------------------------------ E1-0979
    {
        "id": "ECO-E1-0979-1", "fonte_ref": "E1-0979", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": CMD_BRICS,
        "rotulo_item": "Item",
        "assertiva": ("Existe uma grande lacuna a ser preenchida pelos novos bancos multilaterais de desenvolvimento "
                      "no atendimento das carências de crédito adequado para infraestrutura e desenvolvimento "
                      "sustentável. Além disso, devido a divergências entre retornos privados e retornos sociais, "
                      "escala de capital, altos riscos e tempo de maturação dos projetos, cabe a esses bancos atuar "
                      "onde o setor privado tem dificuldade de oferecer recursos no nível ótimo para investimento "
                      "em infraestrutura."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Existe uma grande lacuna a ser preenchida pelos novos bancos multilaterais de "
                      "desenvolvimento no atendimento das carências de crédito adequado para infraestrutura e "
                      "desenvolvimento sustentável. Além disso, devido a <u>divergências entre retornos privados e "
                      "retornos sociais, escala de capital, altos riscos e tempo de maturação</u> dos projetos, cabe "
                      "a esses bancos atuar onde o setor privado tem dificuldade de oferecer recursos no nível ótimo "
                      "para investimento em infraestrutura."),
        "poucas": ("É a justificativa clássica dos bancos de desenvolvimento por " + azb("falhas de mercado")
                   + ": quando o retorno social supera o privado e os projetos são grandes, arriscados e longos, o "
                   "mercado financia menos do que o ótimo."),
        "destrinchando": [
            azb("Retorno social × privado") + ": infraestrutura gera " + azb("externalidades positivas") + " "
            "(uma estrada valoriza terras, reduz custos de terceiros, integra mercados) que o investidor não "
            "consegue cobrar. Se ele só considera o retorno privado, investe abaixo do " + azb("nível ótimo")
            + " social.",
            "Escala e indivisibilidade: uma hidrelétrica ou um porto não se constroem pela metade; o volume de "
            "capital excede o apetite de um banco isolado. " + azb("Risco") + " e maturação: riscos de "
            "construção, regulatórios e cambiais, com retorno que só aparece após anos — o mercado exige prêmio "
            "alto ou não empresta.",
            "Informação imperfeita: " + oc("Stiglitz e Weiss") + " (1981) mostraram que, com assimetria de "
            "informação, os bancos racionam crédito em vez de subir juros, deixando projetos viáveis sem "
            "financiamento. Historicamente, " + oc("Gerschenkron") + " associou a industrialização tardia "
            "(Alemanha, Rússia) a bancos de investimento e ao Estado, que mobilizaram o capital que o mercado "
            "não reunia.",
            "Por que multilaterais: além do capital próprio, captam no mercado com boa classificação de risco, "
            "emprestam a prazos e custos inalcançáveis para muitos países e atraem capital privado por "
            "cofinanciamento e garantias. NDB e AIIB nasceram com esse discurso, sob a “lacuna de "
            "infraestrutura” dos emergentes.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " O item lista as falhas de mercado da "
                       "literatura sem enxerto falso. A versão ERRADO da mesma família costuma inverter o "
                       "diagnóstico (“o setor privado já oferece recursos no nível ótimo”) ou trocar o prazo do "
                       "crédito em falta (longo → curto)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…cabe a esses bancos substituir integralmente o setor privado no financiamento de "
            "infraestrutura.”</i> → ERRADO (modulador absoluto: o papel é complementar e de alavancagem)",
            "<i>“…porque os retornos privados dos projetos de infraestrutura superam sistematicamente os "
            "retornos sociais.”</i> → ERRADO (inversão: o social supera o privado)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Correto: a afirmativa define exatamente as motivações e critérios que justificam a "
                             "existência dos bancos de desenvolvimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0978-1 (versão ERRADO, crédito de curto × longo prazo)"],
    },
    # ------------------------------------------------------------------ E1-0980
    {
        "id": "ECO-E1-0980-1", "fonte_ref": "E1-0980", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": CMD_BRICS,
        "rotulo_item": "Item",
        "assertiva": ("O Novo Banco de Desenvolvimento (NDB), estabelecido pelo BRICS, passou a existir como "
                      "entidade legal em julho de 2015, com um capital autorizado de US$ 100 bilhões e a "
                      "possibilidade de mobilizar recursos para projetos de infraestrutura e desenvolvimento "
                      "sustentável nas economias emergentes e nos países em desenvolvimento. O NDB apresentou, "
                      "ainda, duas inovações institucionais: igual poder de voto entre seus sócios fundadores e a "
                      "possibilidade de ofertar empréstimos em moeda local para reduzir riscos aos tomadores, bem "
                      "como promover os mercados de capitais locais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Novo Banco de Desenvolvimento (NDB), estabelecido pelo BRICS, passou a existir como "
                      "entidade legal em <u>julho de 2015</u>, com um capital autorizado de <u>US$ 100 bilhões</u> e "
                      "a possibilidade de mobilizar recursos para projetos de infraestrutura e desenvolvimento "
                      "sustentável nas economias emergentes e nos países em desenvolvimento. O NDB apresentou, "
                      "ainda, duas inovações institucionais: <u>igual poder de voto entre seus sócios fundadores</u> "
                      "e a possibilidade de ofertar <u>empréstimos em moeda local</u> para reduzir riscos aos "
                      "tomadores, bem como promover os mercados de capitais locais."),
        "poucas": ("Dados corretos do " + azb("NDB") + ": acordo em vigor em " + vd("julho de 2015") + ", "
                   "capital autorizado de " + vd("US$ 100 bilhões") + ", voto igual entre os cinco fundadores e "
                   "crédito em " + azb("moeda local") + " para reduzir o descasamento cambial do tomador."),
        "destrinchando": [
            "Origem: proposto em 2012 (Nova Délhi), criado pelo acordo assinado na Cúpula de " + vd("Fortaleza "
            "(2014)") + ", em vigor desde " + vd("julho de 2015") + "; sede em Xangai, escritórios regionais "
            "(entre eles o das Américas, no " + rx("Brasil") + "). Capital autorizado de " + vd("US$ 100 bi")
            + "; subscrito inicial de " + vd("US$ 50 bi") + ", em partes iguais.",
            azb("Voto igual") + ": cada fundador detém 20% do capital e dos votos e nenhum tem veto — "
            "contraste deliberado com o FMI e o Banco Mundial, onde o voto acompanha as quotas e os EUA têm "
            "poder de veto nas decisões de supermaioria. É uma resposta à demora na reforma de quotas de 2010.",
            azb("Moeda local") + ": emprestar em dólar a quem fatura em real ou em rande transfere ao tomador o "
            "risco cambial (o “pecado original” da literatura). O NDB capta em moedas locais — emitiu títulos "
            "verdes em renminbi no mercado chinês já em 2016 — e repassa nessas moedas, ajudando a aprofundar os "
            "mercados de capitais domésticos.",
            "⏳ (out/2026) O banco admitiu novos membros (Bangladesh, Emirados Árabes Unidos, Egito, Argélia) "
            "e é presidido pela ex-presidente " + rx("Dilma Rousseff") + ", no cargo desde 2023 e reconduzida "
            "em 2025.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item informativo com três dados checáveis (data, "
                       "capital, inovações). As versões ERRADO usuais trocam “autorizado” por “subscrito” (US$ "
                       "50 bi), atribuem voto proporcional ao PIB ou dizem que o banco só empresta em dólar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No NDB, o poder de voto de cada sócio fundador é proporcional ao seu PIB, o que dá à China "
            "poder de veto.”</i> → ERRADO (troca de conceito: voto igual, sem veto)",
            "<i>“O capital inicial subscrito do NDB, de US$ 50 bilhões, foi dividido igualmente entre os cinco "
            "fundadores.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Correto: adequada caracterização do NDB e de suas inovações e particularidades frente "
                             "a outras iniciativas de bancos de desenvolvimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0981
    {
        "id": "ECO-E1-0981-1", "fonte_ref": "E1-0981", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": CMD_BRICS,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Asiático de Infraestrutura (AIIB), liderado pela China, entrou em operação em janeiro "
                      "de 2016 com um capital autorizado de US$ 100 bilhões, e já conta com oitenta e sete "
                      "países-membros. A despeito de ter como missão promover o investimento em infraestrutura e em "
                      "outros setores produtivos na Ásia, o compromisso com seus objetivos impede que o AIIB atue "
                      "de forma complementar em cooperação com outras instituições de desenvolvimento multilaterais "
                      "e bilaterais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Asiático de Infraestrutura (AIIB), liderado pela China, entrou em operação em "
                       "janeiro de 2016 com um capital autorizado de US$ 100 bilhões, e já conta com oitenta e sete "
                       "países-membros. ") + vm("A despeito de") + az(" ter como missão promover o investimento em "
                                                                      "infraestrutura e em outros setores "
                                                                      "produtivos na Ásia, o compromisso com seus "
                                                                      "objetivos ") + vm("impede") + az(" que o "
                       "AIIB atue de forma complementar em cooperação com outras instituições de desenvolvimento "
                       "multilaterais e bilaterais.")),
        "poucas": ("O " + azb("AIIB") + " foi desenhado para " + azb("cooperar") + ": seu acordo constitutivo "
                   "prevê atuação com outros bancos de desenvolvimento, e boa parte dos primeiros projetos foi "
                   "cofinanciada com o Banco Mundial e o BAD."),
        "destrinchando": [
            "Os dados da primeira frase estão corretos: proposto pela China em 2013, acordo assinado em 2015, "
            "operação desde " + vd("janeiro de 2016") + ", sede em Pequim, capital autorizado de "
            + vd("US$ 100 bilhões") + "; em 2018 tinha " + vd("87") + " membros aprovados. ⏳ (out/2026) Hoje "
            "passa de cem membros.",
            "O próprio acordo constitutivo determina que o banco promova a cooperação regional e trabalhe em "
            "parceria com outras instituições multilaterais e bilaterais de desenvolvimento. Na prática, entre "
            "os primeiros projetos aprovados em 2016, a maioria foi " + azb("cofinanciada") + " com o Banco "
            "Mundial, o Banco Asiático de Desenvolvimento (BAD) e o BERD; há acordos de cooperação também com o "
            "NDB.",
            "Leitura geopolítica: o AIIB foi visto como resposta chinesa à sub-representação nas instituições de "
            "Bretton Woods e ao domínio de EUA e Japão no BAD; os EUA tentaram dissuadir aliados, mas Reino "
            "Unido, Alemanha, França e Itália aderiram como fundadores. A China tem pouco mais de 26% dos votos ⏳ (out/2026), "
            "o que lhe dá veto nas decisões de supermaioria (75%).",
            "Diferença de desenho em relação ao " + azb("NDB") + ": no AIIB o voto acompanha o capital (com "
            "peso para membros regionais), enquanto no NDB os fundadores têm voto igual.",
            vm("Regra-âncora: novos bancos (AIIB, NDB) complementam e cofinanciam com os tradicionais; não os "
               "substituem."),
        ],
        "dissecando": (cz("[contradição · nexo indevido]") + " Os dados factuais da primeira frase dão "
                       "credibilidade; o erro está no nexo da segunda: “compromisso com seus objetivos impede” "
                       "cooperação — como se missão própria e parceria fossem incompatíveis. Pista: nenhum banco "
                       "multilateral proíbe cofinanciamento, que é a regra no setor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No AIIB, a China detém participação que lhe assegura poder de veto nas decisões que exigem "
            "supermaioria.”</i> → CERTO",
            "<i>“O AIIB adota voto igual entre os membros fundadores, como o NDB.”</i> → ERRADO (troca de "
            "conceito: o voto acompanha o capital)",
        ])],
        "reescrita": ("O Banco Asiático de Infraestrutura (AIIB), liderado pela China, entrou em operação em janeiro "
                      "de 2016 com um capital autorizado de US$ 100 bilhões, e já conta com oitenta e sete "
                      "países-membros. " + hl("Além de") + " ter como missão promover o investimento em "
                      "infraestrutura e em outros setores produtivos na Ásia, o compromisso com seus objetivos "
                      + hl("prevê") + " que o AIIB atue de forma complementar em cooperação com outras instituições "
                      "de desenvolvimento multilaterais e bilaterais."),
        "tipo_erro": ["CONTRADICAO", "NEXO_INDEVIDO"], "moduladores": ["impede"], "dificuldade": 1,
        "comentario_fonte": ("Errado: o AIIB foi visto como manobra de Pequim para rivalizar com as instituições "
                             "tradicionais, mas não há impedimento a parcerias; o Banco Mundial, o Banco Asiático "
                             "de Desenvolvimento e o NDB estão entre seus parceiros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00365
    {
        "id": "ECO-E2-L00365-1", "fonte_ref": "E2-L00365", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("A transição para um sistema monetário internacional multipolar é dificultada pela “inércia "
                      "institucional” e pelos fortes efeitos de rede (network externalities), que mantêm o dólar "
                      "como moeda predominante em funções de meio de troca, unidade de conta e reserva de valor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A transição para um sistema monetário internacional multipolar é <u>dificultada</u> pela "
                      "“inércia institucional” e pelos fortes <u>efeitos de rede</u> (network externalities), que "
                      "mantêm o dólar como moeda predominante em funções de meio de troca, unidade de conta e "
                      "reserva de valor."),
        "poucas": ("Moeda internacional é bem com " + azb("externalidade de rede") + ": quanto mais gente usa o "
                   "dólar, mais líquido e barato ele fica, o que reforça seu uso. Somada à inércia, essa "
                   "dinâmica retarda a multipolaridade."),
        "destrinchando": [
            azb("Efeitos de rede") + ": o valor de usar uma moeda cresce com o número de usuários — mercados "
            "mais profundos, spreads menores, mais contrapartes. O dólar é a " + azb("moeda veículo") + ": "
            "troca-se real por dólar e dólar por peso, em vez de real por peso diretamente (" + oc("Krugman")
            + " modelou essa lógica nos anos 1980).",
            azb("Inércia institucional") + ": contratos, faturamento de commodities, dívidas, sistemas de "
            "pagamento e reservas já estão em dólar; mudar exige coordenação e tem custo. Historicamente, a "
            "libra manteve papel relevante por décadas depois de o Reino Unido perder a primazia econômica.",
            "As três funções no plano internacional: " + azb("meio de troca") + " (comércio e câmbio), "
            + azb("unidade de conta") + " (faturamento, preços de commodities) e " + azb("reserva de valor")
            + " (reservas dos bancos centrais). ⏳ (out/2026) O dólar está em cerca de " + vd("88%") + " das "
            "operações de câmbio (BIS, pesquisa trienal de 2022) e responde por pouco menos de "
            + vd("60%") + " das reservas cambiais declaradas ao FMI (COFER), à frente do euro (cerca de 20%).",
            "Também sustentam o dólar a liquidez e a segurança dos Treasuries, o Estado de direito e a ausência "
            "de controles de capital nos EUA — atributos que o renminbi ainda não reúne. Do outro lado, sanções "
            "financeiras e o uso do dólar como arma geopolítica estimulam a busca de alternativas.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item reproduz a explicação-padrão da persistência do "
                       "dólar. O verbo “dificultada” é preciso — não diz “impede”. A versão ERRADO trocaria por "
                       "absoluto (“torna impossível a multipolaridade”) ou atribuiria a predominância só à "
                       "função de reserva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os efeitos de rede tornam impossível a coexistência de mais de uma moeda internacional "
            "relevante.”</i> → ERRADO (modulador absoluto: dificultam, não impedem)",
            "<i>“A predominância do dólar restringe-se à função de reserva de valor, tendo o euro superado o "
            "dólar como unidade de conta no comércio mundial.”</i> → ERRADO (restrição indevida: o dólar domina "
            "as três funções)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["dificultada"], "dificuldade": 1,
        "comentario_fonte": ("Externalidades de rede: quanto mais pessoas usam o dólar, mais barato e fácil é "
                             "usá-lo, o que cria barreira de entrada para concorrentes como o yuan ou o euro."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00369-1 (Eichengreen e a coexistência de moedas de reserva)"],
    },
    # ------------------------------------------------------------------ E2-L00368
    {
        "id": "ECO-E2-L00368-1", "fonte_ref": "E2-L00368", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("Iniciativas recentes, como o sistema mBridge (plataforma de moedas digitais de bancos "
                      "centrais) e o aumento do uso de moedas locais em trocas comerciais bilaterais (ex: "
                      "Brasil-China), representam desafios técnicos e políticos à hegemonia do sistema SWIFT e ao "
                      "domínio do dólar."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Iniciativas recentes, como o sistema mBridge (plataforma de moedas digitais de bancos "
                      "centrais) e o aumento do uso de moedas locais em trocas comerciais bilaterais (ex: "
                      "Brasil-China), <u>representam desafios</u> técnicos e políticos à hegemonia do sistema SWIFT "
                      "e ao domínio do dólar."),
        "poucas": ("O " + azb("mBridge") + " liquida pagamentos internacionais entre moedas digitais de bancos "
                   "centrais sem passar pela rede SWIFT nem pelo dólar; o comércio em moedas locais reduz a "
                   "necessidade da moeda veículo. São <b>desafios</b> — ainda não ameaças efetivas — à hegemonia."),
        "destrinchando": [
            "O " + azb("SWIFT") + " é a rede de mensagens que conecta bancos para ordens de pagamento "
            "internacionais (cooperativa sediada na Bélgica). Não movimenta dinheiro, mas é o “sistema nervoso” "
            "dos pagamentos — e a exclusão dele virou arma: bancos iranianos (2012) e russos (2022) foram "
            "desconectados, e cerca de US$ 300 bilhões em reservas russas foram congelados em 2022.",
            "O " + azb("mBridge") + " nasceu no Centro de Inovação do BIS com os bancos centrais de Hong Kong, "
            "Tailândia, China e Emirados Árabes Unidos; a Arábia Saudita aderiu em 2024, e o BIS deixou o "
            "projeto no mesmo ano, transferindo-o aos participantes. ⏳ (out/2026) Opera em escala ainda "
            "pequena. Ao lado dele, o CIPS (sistema chinês de pagamentos em renminbi) e o SPFS russo oferecem "
            "trilhos alternativos.",
            rx("Brasil–China") + ": em 2023 os dois países firmaram arranjos para liquidar operações diretamente "
            "em real e renminbi, com banco de compensação (clearing) de renminbi no Brasil e adesão de banco "
            "brasileiro ao CIPS. Vantagens: menor custo de conversão e menor exposição ao dólar.",
            "Limites: o dólar mantém liquidez, profundidade e conversibilidade que as alternativas não têm; o "
            "renminbi tem controles de capital. Por isso a literatura fala em " + azb("desdolarização "
            "gradual") + " e marginal, não em substituição.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " “Representam desafios” é afirmação "
                       "moderada e verdadeira. O item erraria com “já superaram” ou “eliminaram a dependência”. "
                       "Atenção ao detalhe técnico: mBridge é plataforma de CBDCs no atacado, não de "
                       "criptomoedas privadas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O mBridge, plataforma de criptomoedas privadas criada pelo BRICS, já substituiu o SWIFT nas "
            "transações entre seus membros.”</i> → ERRADO (troca de conceito e extrapolação: CBDCs de bancos "
            "centrais, uso ainda limitado)",
            "<i>“A exclusão de bancos russos do SWIFT em 2022 incentivou a busca por sistemas de pagamento "
            "alternativos.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["representam desafios"],
        "dificuldade": 1,
        "comentario_fonte": ("Sistemas alternativos de pagamento buscam reduzir a exposição a sanções financeiras "
                             "(como o congelamento de reservas) e os custos de conversão; são pilar da tendência "
                             "de desdolarização."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00369
    {
        "id": "ECO-E2-L00369-1", "fonte_ref": "E2-L00369", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o historiador Barry Eichengreen, a hegemonia de uma moeda de reserva é um "
                      "“monopólio natural”, o que torna impossível, do ponto de vista histórico e econômico, a "
                      "existência de mais de uma moeda de reserva internacional dominante simultaneamente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o historiador Barry Eichengreen, a hegemonia de uma moeda de reserva ")
                    + vm("é") + az(" um “monopólio natural”, o que torna ") + vm("impossível")
                    + az(", do ponto de vista histórico e econômico, a existência de mais de uma moeda de reserva "
                         "internacional dominante simultaneamente.")),
        "poucas": (oc("Eichengreen") + " contesta justamente a tese do “monopólio natural”: a história mostra "
                   + azb("várias moedas de reserva coexistindo") + " (libra e dólar no entreguerras), e ele "
                   "projeta um sistema multipolar."),
        "destrinchando": [
            "A " + azb("“visão antiga”") + " (associada a " + oc("Kindleberger") + " e à literatura de moeda "
            "veículo): os efeitos de rede são tão fortes que só cabe uma moeda internacional dominante por vez "
            "— o sistema funcionaria como um monopólio natural, com troca abrupta de hegemon.",
            "A " + azb("“visão nova”") + " de " + oc("Barry Eichengreen") + " (economista e historiador "
            "econômico, Berkeley): em " + oc("<i>Exorbitant Privilege</i>") + " (2011) e em "
            + oc("<i>How Global Currencies Work</i>") + " (2017, com Mehl e Chiţu), mostra que nos anos 1920 e "
            "1930 o dólar já rivalizava com a libra nas reservas, com as duas em posição de destaque ao mesmo "
            "tempo. As tecnologias financeiras modernas reduzem o custo de operar com várias moedas.",
            "Daí sua previsão: um sistema " + azb("multipolar") + ", com o dólar ainda à frente, mas "
            "dividindo espaço com euro, renminbi e outras moedas. ⏳ (out/2026) Os dados do FMI mostram queda "
            "lenta da fatia do dólar nas reservas, absorvida sobretudo por moedas “não tradicionais” (dólar "
            "australiano e canadense, won, renminbi), e não por um único rival.",
            "Rótulo correto: “privilégio exorbitante” é expressão de " + oc("Valéry Giscard d’Estaing") + " "
            "(anos 1960) para as vantagens dos EUA como emissor da moeda-reserva — Eichengreen a usou como título "
            "do livro.",
            vm("Regra-âncora: Eichengreen = coexistência de moedas de reserva e futuro multipolar."),
        ],
        "dissecando": (cz("[inversão · modulador absoluto]") + " O item atribui ao autor a tese que ele "
                       "refuta (troca a “visão nova” pela “antiga”) e reforça com um absoluto (“impossível”). "
                       "Pista: a expressão “do ponto de vista histórico” contraria a obra de um historiador que "
                       "documenta casos de coexistência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Eichengreen, no entreguerras a libra esterlina e o dólar desempenharam simultaneamente "
            "papel relevante como moedas de reserva.”</i> → CERTO",
            "<i>“Eichengreen sustenta que o renminbi substituirá o dólar como única moeda de reserva dominante "
            "ainda nesta década.”</i> → ERRADO (extrapolação: ele prevê multipolaridade, não troca de hegemon)",
        ])],
        "reescrita": ("De acordo com o historiador Barry Eichengreen, a hegemonia de uma moeda de reserva "
                      + hl("não constitui") + " um “monopólio natural”, o que torna " + hl("possível") + ", do "
                      "ponto de vista histórico e econômico, a existência de mais de uma moeda de reserva "
                      "internacional dominante simultaneamente."),
        "tipo_erro": ["INVERSAO", "GENERALIZACAO"], "moduladores": ["impossível"], "dificuldade": 2,
        "comentario_fonte": ("Eichengreen, em obras recentes (como Exorbitant Privilege), defende que a história "
                             "mostra a coexistência de várias moedas de reserva (libra e dólar no início do século "
                             "XX) e que o futuro tende a ser multipolar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00365-1 (efeitos de rede e persistência do dólar)"],
    },
    # ------------------------------------------------------------------ E3-L00360
    {
        "id": "ECO-E3-L00360-1", "fonte_ref": "E3-L00360", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_MSUE,
        "excerto": EXCERTO_MSUE,
        "rotulo_item": "Item",
        "assertiva": ("Após quase duas décadas de impasses, o acordo ganhou renovada prioridade em 2019 e, nos "
                      "últimos dois anos, os dois blocos realizaram sete rodadas de negociações, entre outras "
                      "reuniões, com foco em modernizar e equilibrar as relações comerciais entre as partes e "
                      "ajustar o acordo aos desafios atuais enfrentados nos níveis nacionais, regionais e global."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Após quase duas décadas de impasses, o acordo ganhou renovada prioridade em <u>2019</u> e, "
                      "nos últimos dois anos, os dois blocos realizaram <u>sete rodadas</u> de negociações, entre "
                      "outras reuniões, com foco em modernizar e equilibrar as relações comerciais entre as partes "
                      "e ajustar o acordo aos desafios atuais enfrentados nos níveis nacionais, regionais e "
                      "global."),
        "poucas": ("Reproduz a nota oficial do governo brasileiro de dezembro de 2024: negociações abertas em "
                   + vd("1999") + ", " + azb("acordo político em 2019") + " e, em 2023–2024, rodadas para "
                   "reequilibrar e atualizar o texto."),
        "destrinchando": [
            "Linha do tempo: lançamento das negociações em " + vd("1999") + "; suspensão em 2004 (divergências "
            "sobre agricultura, de um lado, e indústria, serviços e compras governamentais, de outro); "
            "relançamento em 2010; " + azb("acordo em princípio") + " em " + vd("junho de 2019") + ", que não "
            "foi assinado por resistências europeias ligadas sobretudo ao desmatamento e à concorrência "
            "agrícola.",
            "Reabertura em 2023–2024: a UE apresentou um instrumento adicional com exigências ambientais "
            "(2023), e o Mercosul respondeu pedindo reequilíbrio — o " + rx("Brasil") + " defendeu "
            "preservar margem em " + azb("compras governamentais") + " (para usá-las como política "
            "industrial, inclusive na saúde) e salvaguardas para a indústria. Pesaram a guerra na Ucrânia e a "
            "busca europeia por diversificação de fornecedores e de minerais críticos.",
            "Conclusão anunciada na Cúpula de Montevidéu, em " + vd("dezembro de 2024") + ", com textos "
            "fechados nos temas reabertos e nas pendências de 2019.",
            CRONO_MSUE,
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item copiado da nota oficial (“ctrl c ctrl v”, como "
                       "registra a fonte): a dificuldade são os pormenores (2019, sete rodadas, dois anos). Em "
                       "simulados de conjuntura, frases de comunicado oficial costumam vir CERTO, e o erro, "
                       "quando há, é um dado trocado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Após quase duas décadas de impasses, o acordo foi assinado e entrou em vigor em 2019.”</i> → "
            "ERRADO (dado alterado: 2019 foi só o acordo político, e a assinatura veio em 2026)",
            "<i>“As negociações entre Mercosul e União Europeia foram lançadas em 1999.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Questão copiada do site do governo (links do MDIC). Negociações iniciadas em 1999; "
                             "acordo político (em princípio) em junho de 2019; em 2023–2024, sob impulso renovado "
                             "(guerra na Ucrânia, diversificação de cadeias), múltiplas rodadas para modernizar o "
                             "texto; o side letter ambiental acomodou exigências europeias."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 513", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (links das notas oficiais; conteúdo no 📖)"}],
        "alertas": ["nota_redacao: cronologia de 2025–2026 (assinatura, envio ao TJUE, aplicação provisória com o "
                    "Brasil em 1º/5/2026) conferida em notícias de jan–abr/2026"],
    },
    # ------------------------------------------------------------------ E3-L00362
    {
        "id": "ECO-E3-L00362-1", "fonte_ref": "E3-L00362", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_MSUE,
        "excerto": EXCERTO_MSUE,
        "rotulo_item": "Item",
        "assertiva": ("Apesar dos avanços propostos, o capítulo do Acordo que trata das Medidas Sanitárias e "
                      "Fitossanitárias reforça o conceito de deterioração dos termos de troca proposto pela Crítica "
                      "Cepalina, uma vez que impõe novos padrões, como o “pre-listing” e a regionalização, que "
                      "dificultam o acesso de produtos agrícolas do Mercosul ao mercado europeu."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Apesar dos") + az(" avanços propostos, o capítulo do Acordo que trata das Medidas "
                                          "Sanitárias e Fitossanitárias ") + vm("reforça") + az(" o conceito de "
                    "deterioração dos termos de troca proposto pela Crítica Cepalina, ")
                    + vm("uma vez que impõe novos padrões") + az(", como o “pre-listing” e a regionalização, que ")
                    + vm("dificultam") + az(" o acesso de produtos agrícolas do Mercosul ao mercado europeu.")),
        "poucas": ("“Pre-listing” e regionalização são instrumentos de " + azb("facilitação") + " do comércio "
                   "agropecuário, não barreiras; e normas sanitárias nada têm a ver com a "
                   + azb("deterioração dos termos de troca") + ", que trata de preços relativos."),
        "destrinchando": [
            azb("Pre-listing") + ": a autoridade sanitária do país exportador lista os estabelecimentos "
            "habilitados, e o importador os aceita sem inspecionar um a um — o processo fica mais rápido e "
            "previsível. " + azb("Regionalização") + ": um surto (de febre aftosa, gripe aviária) numa região "
            "não fecha as exportações do país inteiro; zonas livres continuam exportando.",
            "Segundo a síntese oficial do governo brasileiro, o capítulo de " + azb("Medidas Sanitárias e "
            "Fitossanitárias") + " (SPS) " + azb("facilita") + " o comércio agropecuário com transparência e "
            "previsibilidade, preservando os padrões de produção dos dois blocos. A base é o Acordo SPS da OMC "
            "(1994): medidas sanitárias são legítimas se fundadas em ciência e não discriminatórias.",
            azb("Deterioração dos termos de troca") + " (" + oc("Prebisch") + " e " + oc("Singer") + ", 1949–"
            "1950; CEPAL): tendência de queda dos preços dos produtos primários exportados pela periferia em "
            "relação aos manufaturados importados do centro, por diferenças de elasticidade-renda e de poder de "
            "mercado. É um fenômeno de " + azb("preços relativos") + ", não de regulação sanitária.",
            "O que é legítimo debater: críticos no Mercosul apontam o risco de o acordo reforçar a "
            + azb("especialização primário-exportadora") + " (agro contra indústria europeia) — aí sim há "
            "ligação com a tese cepalina. Mas o capítulo SPS, em si, reduz barreiras.",
            vm("Regra-âncora: pre-listing e regionalização = facilitação; termos de troca = preços relativos."),
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " Junta dois temas sem relação (SPS e CEPAL) e "
                       "inverte o efeito dos mecanismos (facilitam → dificultam). O vocabulário técnico "
                       "(“pre-listing”, “regionalização”) intimida quem não o conhece; a saída é saber que ambos "
                       "existem para <b>agilizar</b> exportações."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O mecanismo de regionalização permite que áreas livres de determinada doença continuem a "
            "exportar mesmo diante de surto em outra região do país.”</i> → CERTO",
            "<i>“A deterioração dos termos de troca, segundo a CEPAL, decorre das barreiras sanitárias impostas "
            "pelos países centrais.”</i> → ERRADO (nexo indevido: decorre de elasticidades e estruturas de "
            "mercado)",
        ])],
        "reescrita": (hl("Entre os") + " avanços propostos, o capítulo do Acordo que trata das Medidas Sanitárias "
                      "e Fitossanitárias " + hl("não guarda relação com") + " o conceito de deterioração dos "
                      "termos de troca proposto pela Crítica Cepalina, " + hl("e prevê mecanismos") + ", como o "
                      "“pre-listing” e a regionalização, que " + hl("facilitam") + " o acesso de produtos agrícolas "
                      "do Mercosul ao mercado europeu."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Pre-listing e regionalização combatem a deterioração dos termos de troca (nota "
                             "oficial transcrita: o capítulo SPS facilita o comércio agropecuário com "
                             "transparência e previsibilidade). Termos de troca (Prebisch-Singer) referem-se a "
                             "preços relativos e não têm relação com SPS; pre-listing é facilitação, não barreira."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 516", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (repetia o enunciado)"},
                          {"ref": "IMAGEM 517", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (síntese oficial do capítulo SPS absorvida no 📖)"}],
        "alertas": ["qualidade_fonte: a abertura do verso diz que pre-listing e regionalização “combatem a "
                    "deterioração dos termos de troca”; eles facilitam o comércio, mas não têm relação com os "
                    "termos de troca — corrigido"],
    },
    # ------------------------------------------------------------------ E3-L00363
    {
        "id": "ECO-E3-L00363-1", "fonte_ref": "E3-L00363", "destino": "84", "subtema": H2["int"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_MSUE,
        "excerto": EXCERTO_MSUE,
        "rotulo_item": "Item",
        "assertiva": ("As negociações do Acordo de Parceria entre o MERCOSUL e a União Europeia encontram-se "
                      "totalmente concluídas. As partes pacificaram o entendimento em todos os textos, seja nos "
                      "temas objeto de reabertura, seja naquelas pendências que persistiam desde 2019. A conclusão "
                      "das negociações, contudo, não produz efeitos jurídicos imediatos, que ocorrem apenas com a "
                      "assinatura e entrada em vigor do Acordo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As negociações do Acordo de Parceria entre o MERCOSUL e a União Europeia encontram-se "
                      "<u>totalmente concluídas</u>. As partes pacificaram o entendimento em todos os textos, seja "
                      "nos temas objeto de reabertura, seja naquelas pendências que persistiam desde 2019. A "
                      "conclusão das negociações, contudo, <u>não produz efeitos jurídicos imediatos</u>, que "
                      "ocorrem apenas com a assinatura e entrada em vigor do Acordo."),
        "poucas": ("Texto literal da nota oficial de dezembro de 2024: negociação concluída ≠ tratado em vigor. "
                   "Faltavam " + azb("revisão jurídica, tradução, assinatura, internalização, ratificação e "
                   "entrada em vigor") + "."),
        "destrinchando": [
            "Etapas de um tratado: " + azb("negociação") + " → rubrica/conclusão → " + azb("revisão "
            "jurídica") + " (“legal scrubbing”) e tradução → " + azb("assinatura") + " → aprovação interna → "
            + azb("ratificação") + " → " + azb("entrada em vigor") + ". Só a partir desta o acordo obriga as "
            "partes; antes, no máximo, há o dever de não frustrar seu objeto depois de assinado (Convenção de "
            "Viena de 1969, art. 18).",
            "No " + rx("Brasil") + ", tratado que acarreta compromissos gravosos exige aprovação do Congresso "
            "por decreto legislativo (CF, art. 49, I), seguida de ratificação e promulgação por decreto "
            "presidencial. Na UE, o rito depende da competência: acordos só comerciais (competência exclusiva) "
            "passam pelo Conselho e pelo Parlamento Europeu; acordos mistos exigem também os parlamentos "
            "nacionais.",
            CRONO_MSUE,
            "Por isso o item é CERTO na data da prova e continua conceitualmente correto: a conclusão de 2024 não "
            "produziu efeitos; estes vieram, para a parte comercial e de forma provisória, só em 2026.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Cópia da nota conjunta. O risco estava no "
                       "“totalmente concluídas” (que parece exagero, mas é literal) e na distinção entre "
                       "concluir e pôr em vigor. Versões ERRADO típicas: “a conclusão produz efeitos imediatos” "
                       "ou “dispensa ratificação”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com a conclusão das negociações em dezembro de 2024, as reduções tarifárias passaram a vigorar "
            "imediatamente.”</i> → ERRADO (anacronismo jurídico: efeitos só após assinatura e entrada em vigor)",
            "<i>“A parte comercial do acordo pode ser aplicada provisoriamente antes da conclusão de todas as "
            "ratificações.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["totalmente", "apenas"], "dificuldade": 1,
        "comentario_fonte": ("Nota oficial transcrita (próximos passos: revisão legal, tradução, assinatura, "
                             "internalização, ratificação, entrada em vigor). Conclusão anunciada na 65ª Cúpula, em "
                             "Montevidéu; os efeitos vinculantes só vêm após ratificação (Parlamento Europeu e "
                             "Conselho; congressos nacionais no Mercosul)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 518", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (etapas seguintes absorvidas no 📖)"},
                          {"ref": "IMAGEM 513", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (links das notas oficiais)"}],
        "alertas": ["nota_redacao: cronologia de 2025–2026 conferida em notícias de jan–abr/2026"],
    },
]
