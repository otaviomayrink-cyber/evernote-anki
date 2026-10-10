"""Cards do lote de redação 20 — ECO, passada 03 (nota 79: políticas comerciais — tarifas, cotas, subsídios)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "tar": "🧾 Tarifas",
    "cot": "🚫 Cotas e barreiras não tarifárias",
    "sub": "💰 Subsídios e defesa comercial",
    "omc": "🏛️ Política comercial e OMC",
}

CMD_OMC = "Acerca do sistema multilateral de comércio e das regras do GATT/OMC, julgue o item a seguir."

CMD_POL = "Acerca dos instrumentos de política comercial e de seus efeitos econômicos, julgue o item a seguir."

CMD_MACRO = ("Acerca dos efeitos macroeconômicos da política comercial em economia aberta, julgue o item a "
             "seguir.")

CMD_DOHA = ("Considerando que a Rodada Doha, no Catar, lançada em novembro de 2001, propôs um compromisso em prol da "
            "liberalização comercial e do crescimento econômico, com especial atenção aos países em "
            "desenvolvimento, julgue o item a seguir.")

CMD_BOZAN_1 = "Com relação aos instrumentos de política comercial, julgue o item a seguir."

CMD_BOZAN_5 = "Sobre os instrumentos de proteção ao comércio, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0903
    {
        "id": "ECO-E1-0903-1", "fonte_ref": "E1-0903", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_OMC,
        "rotulo_item": "Item",
        "assertiva": "Não existem regras multilaterais aplicáveis a investimentos.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("Não existem") + az(" regras multilaterais aplicáveis a investimentos."),
        "poucas": ("Não há um acordo <b>abrangente</b> de investimentos na OMC, mas há regras multilaterais "
                   "parciais: o " + azb("Acordo TRIMs") + " (medidas de investimento relacionadas ao comércio) "
                   "e o " + azb("GATS") + ", que cobre o investimento em serviços (modo 3)."),
        "destrinchando": [
            "O " + azb("Acordo sobre Medidas de Investimento Relacionadas ao Comércio (TRIMs)") + ", resultado "
            "da Rodada Uruguai e em vigor desde " + vd("1995") + ", proíbe medidas de investimento "
            "incompatíveis com o " + vd("art. III") + " do GATT (tratamento nacional) e com o " + vd("art. XI")
            + " (eliminação de restrições quantitativas). Sua lista ilustrativa inclui exigências de "
            + azb("conteúdo local") + " (comprar insumo nacional para obter incentivo) e de "
            + azb("equilíbrio comercial") + " (importar só na proporção do que se exporta).",
            "Essas exigências são " + azb("requisitos de desempenho") + ": a empresa precisa fazer algo "
            "(usar insumo local, exportar certa parcela) para receber um benefício, em geral fiscal. O TRIMs "
            "disciplina as que distorcem o comércio de <b>bens</b>; não regula a entrada, a proteção nem a "
            "expropriação do investimento.",
            "Outras peças multilaterais tocam o tema: o " + azb("GATS") + " trata a " + azb("presença "
            "comercial") + " (modo 3) como forma de prestar serviços — investimento estrangeiro em bancos, "
            "telecomunicações etc. —, e o " + azb("TRIPS") + " protege ativos intangíveis do investidor.",
            "O que fracassou foi o acordo amplo: o investimento foi um dos " + azb("temas de Cingapura")
            + " (" + vd("1996") + ", quando se criou o grupo de trabalho sobre comércio e investimento, o "
            "WGTI) e saiu da agenda de Doha em " + vd("2004") + "; na OCDE, o Acordo Multilateral de "
            "Investimentos (MAI) foi abandonado em " + vd("1998") + ". A proteção do investimento segue "
            "majoritariamente em acordos bilaterais (BITs).",
            vm("Regra-âncora: não há acordo abrangente de investimentos na OMC, mas há regras multilaterais "
               "parciais (TRIMs, GATS modo 3)."),
        ],
        "dissecando": (cz("[generalização · troca de conceito]") + " O item converte “não há acordo "
                       "abrangente” em “não existem regras”. A negação categórica (“não existem”) é o sinal: "
                       "basta um contraexemplo — o TRIMs — para derrubá-la."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " evitou os BITs clássicos (assinou vários nos anos 1990, mas não os "
                "ratificou) e criou, em " + vd("2015") + ", o modelo próprio de " + rx("Acordo de Cooperação e "
                "Facilitação de Investimentos (ACFI)") + ", focado em facilitação e prevenção de disputas, sem "
                "arbitragem investidor-Estado.",
                "No contencioso " + rx("Inovar-Auto") + ", painel da OMC (" + vd("2017") + ") condenou "
                "exigências de conteúdo local do programa automotivo brasileiro — exemplo concreto de que as "
                "regras do TRIMs e do art. III do GATT têm dentes.",
            ]),
            ("😈 Para dificultar", [
                "<i>“Não existe na OMC acordo abrangente sobre proteção de investimentos estrangeiros.”</i> → "
                "CERTO",
                "<i>“O Acordo TRIMs proíbe exigências de conteúdo local e regula a expropriação de investimentos "
                "estrangeiros.”</i> → ERRADO (extrapolação: o TRIMs não trata de expropriação)",
            ]),
        ],
        "reescrita": (hl("Existem") + " regras multilaterais aplicáveis a investimentos" + hl(", como o Acordo "
                      "TRIMs e o modo 3 do GATS, embora não haja acordo abrangente na OMC") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["não existem"], "dificuldade": 1,
        "comentario_fonte": ("TRIMs estabelecem requisitos de desempenho proibidos relativos aos arts. III e XI do "
                             "GATT (conteúdo nacional, limitação de importações); grupo de trabalho WGTI criado em "
                             "1996, sem acordo multilateral de investimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0904
    {
        "id": "ECO-E1-0904-1", "fonte_ref": "E1-0904", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_OMC,
        "rotulo_item": "Item",
        "assertiva": ("Acordos comerciais regionais são incompatíveis com as normas multilaterais, a menos que a "
                      "liberalização neles prevista abranja a totalidade do universo tarifário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Acordos comerciais regionais são incompatíveis com as normas multilaterais, a menos que a "
                       "liberalização neles prevista abranja ") + vm("a totalidade do universo tarifário")
                    + az(".")),
        "poucas": ("O " + azb("art. XXIV do GATT") + " exige que zonas de livre comércio e uniões aduaneiras "
                   "liberalizem " + vd("“substancialmente todo o comércio”") + " entre as partes — não 100% das "
                   "linhas tarifárias."),
        "destrinchando": [
            "Acordos regionais são uma " + azb("exceção à cláusula da nação mais favorecida") + " (art. I do "
            "GATT): concedem aos parceiros preferências negadas aos demais membros. A OMC os admite porque, "
            "bem desenhados, ampliam o comércio em vez de apenas desviá-lo.",
            "Condições do " + azb("art. XXIV") + " (detalhadas no Entendimento de " + vd("1994") + "): (i) "
            "eliminar tarifas e outras restrições sobre " + vd("substancialmente todo o comércio")
            + " (<i>substantially all the trade</i>) entre os membros; (ii) não elevar, no conjunto, as barreiras "
            "contra terceiros; (iii) acordos interinos devem completar-se em prazo razoável, em regra até "
            + vd("10 anos") + ".",
            "“Substancialmente todo” nunca foi quantificado oficialmente; a prática aceita a exclusão de setores "
            "sensíveis (com frequência, agrícolas), desde que não se excluam setores inteiros de forma ampla. "
            "Exigir a totalidade do universo tarifário endurece um critério que é deliberadamente flexível.",
            "Há ainda duas outras portas: o " + azb("art. V do GATS") + " (acordos de integração em serviços) e "
            "a " + azb("Cláusula de Habilitação") + " (" + vd("1979") + "), que permite preferências entre "
            "países em desenvolvimento com requisitos mais brandos — base usada pelo " + rx("Mercosul") + ".",
            vm("Regra-âncora: acordo regional compatível = substancialmente todo o comércio + sem novas barreiras "
               "contra terceiros."),
        ],
        "dissecando": (cz("[dado alterado · generalização]") + " A estrutura do item (incompatível, salvo se…) "
                       "está correta; o erro foi enxertado na condição, trocando “substancialmente todo o "
                       "comércio” por “totalidade do universo tarifário”. 🔥 A banca cobra esse requisito "
                       "trocando o grau (“totalidade”, “maior parte”, “metade”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Acordos comerciais regionais podem ser compatíveis com o GATT, desde que cubram substancialmente "
            "todo o comércio entre as partes e não elevem as barreiras contra terceiros.”</i> → CERTO",
            "<i>“Por constituírem exceção à nação mais favorecida, acordos regionais dependem de aprovação "
            "unânime dos membros da OMC.”</i> → ERRADO (requisito inventado: basta notificar e cumprir o "
            "art. XXIV)",
        ])],
        "reescrita": ("Acordos comerciais regionais são incompatíveis com as normas multilaterais, a menos que a "
                      "liberalização neles prevista abranja " + hl("substancialmente todo o comércio entre as "
                      "partes") + "."),
        "tipo_erro": ["DADO_ALTERADO", "GENERALIZACAO"], "moduladores": ["totalidade"], "dificuldade": 2,
        "comentario_fonte": ("Comentário original: acordos regionais só seriam incompatíveis se previssem "
                             "coordenação predatória contra terceiros. Duplicata (E3-L00467): art. XXIV do GATT exige "
                             "liberalização de “substancialmente todo o comércio”, não da totalidade; também não "
                             "pode elevar barreiras a terceiros."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 672 (duplicata E3-L00467)", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E3-L00467-1 (mesmo item em outra prova)", "duplicata: E3-L00467 fundida (mesmo item, comentários somados)",
                    "qualidade_fonte: o comentário do caderno E1 justifica o ERRADO com um critério inexistente "
                    "(coordenação predatória contra terceiros); o critério é o do art. XXIV"],
    },
    # ------------------------------------------------------------------ E1-0909
    {
        "id": "ECO-E1-0909-1", "fonte_ref": "E1-0909", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": CMD_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, a adoção de barreiras comerciais, como, por exemplo, tarifas e quotas à "
                      "importação, conduz ao aumento da taxa de câmbio real, o que favorece o aumento das "
                      "exportações líquidas da economia e a redução do deficit de conta-corrente na economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No longo prazo, a adoção de barreiras comerciais, como, por exemplo, tarifas e quotas à "
                       "importação, conduz ") + vm("ao aumento") + az(" da taxa de câmbio real, o que ")
                    + vm("favorece o aumento das exportações líquidas da economia e a redução do deficit de "
                         "conta-corrente") + az(" na economia.")),
        "poucas": ("A proteção eleva a demanda por exportações líquidas a cada câmbio, e o câmbio real se "
                   + azb("aprecia") + ". No longo prazo, " + vd("NX = S − I") + ": como a tarifa não muda "
                   "poupança nem investimento, o saldo externo " + vm("não melhora") + "."),
        "destrinchando": [
            "Modelo de economia aberta de longo prazo (" + oc("Mankiw") + ", <i>Macroeconomia</i>): a conta "
            "corrente é dada pela identidade " + vd("NX = S − I") + ", e o câmbio real é o preço que ajusta a "
            "demanda por exportações líquidas a esse montante.",
            "Uma tarifa ou cota reduz as importações a cada câmbio: a curva de NX se desloca para fora. Como "
            "S − I não mudou, o excesso de demanda pela moeda nacional faz o câmbio real se "
            + azb("apreciar") + " até que NX volte ao nível inicial. Resultado: importa-se menos do bem "
            "protegido, mas exporta-se menos (e importa-se mais) do resto — o " + azb("volume") + " de "
            "comércio cai, o " + azb("saldo") + " fica igual.",
            "Atenção à convenção: no Brasil, câmbio real = E × P*/P (reais por unidade de moeda estrangeira, "
            "corrigido por preços), e " + vd("“aumento” = depreciação") + ". Em " + oc("Mankiw")
            + ", ε = eP/P* e o aumento significa apreciação. Pela convenção brasileira, o item erra o sentido "
            "do câmbio; por qualquer convenção, erra o efeito sobre o saldo.",
            "Para melhorar a conta corrente de forma duradoura, a política precisa mexer em S − I: elevar a "
            "poupança pública (ajuste fiscal) ou privada.",
            vm("Regra-âncora: protecionismo muda a composição e o volume do comércio, não o saldo de longo prazo."),
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " O item encadeia uma intuição de curto prazo "
                       "(“menos importação → saldo melhor”) e a projeta para o longo prazo, quando o câmbio real "
                       "anula o efeito. A palavra-chave é “no longo prazo”: nesse horizonte, saldo externo é "
                       "poupança menos investimento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, tarifas e cotas à importação apreciam o câmbio real e deixam inalterado o saldo "
            "das exportações líquidas.”</i> → CERTO",
            "<i>“No longo prazo, a redução do deficit público melhora a conta corrente ao elevar a poupança "
            "nacional.”</i> → CERTO",
            "<i>“Tarifas reduzem o volume de importações e, por isso, aumentam o volume total de comércio.”</i> → "
            "ERRADO (inversão: o volume de comércio cai)",
        ])],
        "reescrita": ("No longo prazo, a adoção de barreiras comerciais, como, por exemplo, tarifas e quotas à "
                      "importação, conduz " + hl("à apreciação") + " da taxa de câmbio real, o que "
                      + hl("deixa inalterados o saldo das exportações líquidas e o deficit de conta-corrente")
                      + " na economia."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": ["no longo prazo"], "dificuldade": 2,
        "comentario_fonte": ("Barreiras elevam os preços internos e apreciam o câmbio real [E × P*/P], o que "
                             "aumenta as importações e deteriora a balança comercial."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem conclui que a balança se deteriora; no modelo de "
                    "longo prazo a apreciação apenas anula o ganho inicial, e o saldo fica inalterado (NX = S − I)",
                    "quase_duplicata: ECO-E1-0933-1, ECO-E2-L00186-1 (tarifa anulada pelo câmbio)"],
    },
    # ------------------------------------------------------------------ E1-0925
    {
        "id": "ECO-E1-0925-1", "fonte_ref": "E1-0925", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado 07/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": "Acerca das teorias do comércio internacional e da política comercial, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("As barreiras tarifárias do tipo ad valorem são um dos instrumentos advogados pelas teorias "
                      "modernas do comércio internacional como meio de promover a aceleração do desenvolvimento "
                      "das economias emergentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As barreiras tarifárias do tipo ad valorem são um dos instrumentos advogados ")
                    + vm("pelas teorias modernas do comércio internacional") + az(" como meio de promover a "
                    "aceleração do desenvolvimento das economias emergentes.")),
        "poucas": ("As teorias convencionais do comércio — clássica, neoclássica e a " + azb("nova teoria do "
                   "comércio") + " — recomendam, como regra, o livre-comércio. Quem defende a proteção tarifária "
                   "para acelerar o desenvolvimento é a " + azb("crítica cepalina") + " (estruturalismo)."),
        "destrinchando": [
            "Teorias convencionais: " + oc("Ricardo") + " (vantagens comparativas), o modelo "
            + oc("Heckscher-Ohlin") + " (dotação de fatores) e a " + azb("nova teoria do comércio") + " de "
            + oc("Krugman") + " (economias de escala e concorrência monopolística) mostram ganhos do comércio "
            "livre. Nelas, a tarifa — ad valorem ou específica — gera " + azb("peso morto") + " e só se "
            "justifica em casos excepcionais.",
            "Exceções que a teoria admite, sem convertê-las em receita de desenvolvimento: " + azb("tarifa ótima")
            + " (país grande que melhora seus termos de troca) e " + azb("política comercial estratégica")
            + " (" + oc("Brander e Spencer") + ", anos 1980, que usa sobretudo <b>subsídios</b> em oligopólios). "
            "O próprio " + oc("Krugman") + " alertou para os riscos de captura e retaliação.",
            "A defesa da proteção como instrumento de " + azb("industrialização") + " vem de outra linhagem: "
            + oc("Hamilton") + " e " + oc("List") + " (indústria nascente, século XIX) e, na América Latina, "
            + oc("Prebisch") + " e a " + rx("CEPAL") + " (anos 1950): com a deterioração dos termos de troca "
            "dos primários, tarifas e controles cambiais sustentariam a " + rx("industrialização por "
            "substituição de importações") + ".",
            "Tipos de tarifa, para não confundir: " + azb("ad valorem") + " = percentual sobre o valor (ex.: "
            + vd("10%") + "); " + azb("específica") + " = valor fixo por unidade (ex.: US$ 2/kg); " +
            azb("mista") + " = combinação. A crítica teórica vale para todas.",
        ],
        "dissecando": (cz("[troca de ator]") + " O item atribui às teorias “modernas” uma tese da crítica "
                       "estruturalista. A pista é a palavra “advogados”: a teoria convencional, no máximo, "
                       "<b>tolera</b> exceções; quem advoga a proteção como estratégia de desenvolvimento é a "
                       "CEPAL. O “ad valorem” é distrator: o tipo de tarifa não muda o julgamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A proteção tarifária é defendida pelo pensamento cepalino como instrumento da industrialização "
            "por substituição de importações.”</i> → CERTO",
            "<i>“A nova teoria do comércio internacional, ao incorporar economias de escala, conclui que a "
            "proteção tarifária é sempre superior ao livre-comércio.”</i> → ERRADO (modulador absoluto: admite "
            "exceções pontuais)",
        ])],
        "reescrita": ("As barreiras tarifárias do tipo ad valorem são um dos instrumentos advogados "
                      + hl("pela crítica cepalina às teorias convencionais do comércio internacional")
                      + " como meio de promover a aceleração do desenvolvimento das economias emergentes."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Teorias do comércio internacional são, em geral, antitarifárias (vale para qualquer "
                             "tarifa); quem defende tarifas para favorecer o crescimento é a crítica cepalina."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0933
    {
        "id": "ECO-E1-0933-1", "fonte_ref": "E1-0933", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": True,
        "comando": CMD_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("A introdução de uma tarifa alfandegária causará efeitos de longo prazo sobre a balança "
                      "comercial se houver livre mobilidade de capital e regime cambial flexível."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A introdução de uma tarifa alfandegária ") + vm("causará") + az(" efeitos de longo prazo "
                    "sobre a balança comercial se houver livre mobilidade de capital e regime cambial flexível.")),
        "poucas": ("Com câmbio flutuante e capital livre, a tarifa melhora a balança só de início: a "
                   + azb("apreciação cambial") + " que ela provoca reabre as importações e corta exportações, e "
                   "o saldo volta ao ponto de partida."),
        "destrinchando": [
            "Sequência (" + oc("Mundell-Fleming") + "): a tarifa reduz importações → demanda por bens domésticos "
            "↑ → a IS se desloca para a direita → os juros tendem a subir acima do internacional → entra "
            "capital → com câmbio flexível, a moeda nacional " + azb("se valoriza") + " → importações dos "
            "demais bens sobem e exportações caem → a IS volta ao lugar.",
            "Resultado com " + vd("câmbio flexível") + ": renda e saldo comercial inalterados; mudam o câmbio "
            "(mais apreciado) e a <b>composição</b> do comércio (menos importação do bem protegido, menos "
            "exportação dos outros). Fundamento contábil: " + vd("NX = S − I") + "; a tarifa não altera "
            "poupança nem investimento.",
            "Com " + vd("câmbio fixo") + ", o resultado muda: para impedir a apreciação, o Banco Central compra "
            "divisas, a oferta de moeda aumenta e a renda e o saldo comercial melhoram. A política comercial é "
            "eficaz em câmbio fixo e ineficaz em câmbio flutuante — o espelho da política fiscal.",
            vm("Regra-âncora: câmbio flutuante + capital livre → a tarifa é neutralizada pela apreciação "
               "cambial."),
        ],
        "dissecando": (cz("[inversão]") + " O item escolhe justamente as condições (capital livre e câmbio "
                       "flexível) em que a tarifa é <b>ineficaz</b> para o saldo e afirma o contrário. Itens "
                       "de Mundell-Fleming quase sempre giram na tabela de quatro casas: fiscal/comercial × "
                       "monetária, câmbio fixo × flutuante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio fixo e perfeita mobilidade de capital, a imposição de uma tarifa eleva a renda e "
            "melhora a balança comercial.”</i> → CERTO",
            "<i>“Sob câmbio flexível e perfeita mobilidade de capital, a tarifa deprecia a moeda nacional.”</i> → "
            "ERRADO (inversão: a moeda se aprecia)",
        ])],
        "reescrita": ("A introdução de uma tarifa alfandegária " + hl("não causará") + " efeitos de longo prazo "
                      "sobre a balança comercial se houver livre mobilidade de capital e regime cambial flexível."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A tarifa equivale a elevar o câmbio real; no curto prazo a balança melhora, mas a "
                             "entrada de divisas reduz o câmbio nominal e restaura o equilíbrio anterior. "
                             "Duplicata (E3-L00466): com câmbio flexível, a apreciação anula o ganho; saldo dado "
                             "por S − I."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 669, 671 (duplicata E3-L00466)", "tipo_fonte": "TEXTO",
                           "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 670 (duplicata E3-L00466)", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (sequência IS-LM-BP descrita no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00466-1 (mesmo item em outra prova)", "duplicata: E3-L00466 fundida (mesmo item, comentários somados)",
                    "quase_duplicata: ECO-E2-L00186-1, ECO-E1-0909-1 (tarifa neutralizada pelo câmbio)"],
    },
    # ------------------------------------------------------------------ E1-0937
    {
        "id": "ECO-E1-0937-1", "fonte_ref": "E1-0937", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("Em economias que privilegiam a produção, tarifas são preferíveis a quotas, porque, embora "
                      "reduzam o excedente do consumidor, deixam o do produtor inalterado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em economias que privilegiam a produção, tarifas ") + vm("são preferíveis a quotas")
                    + az(", porque, embora reduzam o excedente do consumidor, ") + vm("deixam") + az(" o do "
                    "produtor ") + vm("inalterado") + az(".")),
        "poucas": ("A tarifa eleva o preço interno e, por isso, " + azb("aumenta") + " o excedente do produtor "
                   "doméstico. Uma quota que gere o mesmo preço produz o mesmo ganho ao produtor: não há razão "
                   "para preferir a tarifa pelo lado da produção."),
        "destrinchando": [
            "País pequeno, preço mundial Pm. Com a tarifa t, o preço interno sobe a " + vd("Pm + t") + ": a "
            "produção doméstica cresce (q₁ˢ → q₂ˢ), o consumo cai (q₁ᵈ → q₂ᵈ) e as importações encolhem.",
            "Repartição do bem-estar: o consumidor perde a faixa entre os dois preços, à esquerda da demanda; "
            "o produtor " + vd("ganha") + " a faixa à esquerda da oferta; o governo arrecada t × importações; "
            "sobram dois triângulos de " + azb("peso morto") + " (produção ineficiente e consumo perdido).",
            "Uma " + azb("quota") + " que limite as importações ao mesmo volume eleva o preço ao mesmo nível: "
            "consumidor, produtor e peso morto ficam idênticos. A diferença está no retângulo: com a tarifa, é "
            + azb("receita do governo") + "; com a quota, " + azb("renda de quota") + " de quem detém as "
            "licenças (importadores ou exportadores estrangeiros), salvo se o governo as leiloar.",
            "Fora da equivalência estática, a quota protege mais: com a demanda em alta, a tarifa deixa entrar "
            "mais importação ao mesmo preço, enquanto a quota trava o volume e o preço interno sobe. Por isso a "
            "OMC prefere tarifas (transparentes) e promoveu a " + azb("tarificação") + " na Rodada Uruguai.",
            vm("Regra-âncora: tarifa e quota equivalente → mesmo ganho do produtor e mesma perda do consumidor; "
               "muda só quem fica com o retângulo."),
        ],
        "grafico_verso": "ECO-E1-0937-1-V1",
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira metade da justificativa (reduz o "
                       "excedente do consumidor) é verdadeira; o erro está em “deixam o do produtor inalterado”, "
                       "que contradiz o próprio objetivo da proteção. A conclusão (preferir tarifas) depende "
                       "dessa premissa falsa — caindo ela, cai tudo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Do ponto de vista da arrecadação, tarifas são preferíveis a quotas cujas licenças são "
            "distribuídas gratuitamente.”</i> → CERTO",
            "<i>“A quota de importação, ao contrário da tarifa, não eleva o preço doméstico do bem.”</i> → "
            "ERRADO (troca de conceito: ambas elevam o preço)",
        ])],
        "reescrita": ("Em economias que privilegiam a produção, tarifas " + hl("e quotas equivalentes produzem o "
                      "mesmo efeito") + ", porque, embora reduzam o excedente do consumidor, " + hl("elevam")
                      + " o do produtor " + hl("na mesma medida") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A tarifa reduz o excedente do consumidor e aumenta o ganho do produtor (área verde "
                             "do gráfico); verso com duas figuras de excedentes em economia aberta."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "00047.jpeg, 00048.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (fundidas em ECO-E1-0937-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0943
    {
        "id": "ECO-E1-0943-1", "fonte_ref": "E1-0943", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("A obtenção de economias crescentes de escala é um dos benefícios indiretos do "
                      "estabelecimento de restrições fitossanitárias, o qual, em razão de sua natureza concreta e "
                      "objetiva, propicia retaliações internacionais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A obtenção de economias crescentes de escala ") + vm("é um dos benefícios indiretos")
                    + az(" do estabelecimento de restrições fitossanitárias, o qual, em razão de sua natureza "
                         "concreta e objetiva, propicia retaliações internacionais.")),
        "poucas": ("Restrições fitossanitárias " + azb("fragmentam") + " o mercado mundial e criam reservas de "
                   "mercado: reduzem a escala acessível às empresas, em vez de ampliá-la."),
        "destrinchando": [
            "Economias de escala dependem de mercado grande: custo médio cai quando a produção cresce. É um "
            "argumento a favor da " + azb("abertura") + " (" + oc("Krugman") + ", nova teoria do comércio), "
            "não de barreiras que segmentam mercados por normas nacionais divergentes.",
            "As " + azb("medidas sanitárias e fitossanitárias (SPS)") + " protegem a vida e a saúde humana, "
            "animal e vegetal. O " + azb("Acordo SPS") + " da OMC (" + vd("1995") + ") as admite, desde que "
            "tenham " + vd("base científica") + " (avaliação de risco) e não discriminem arbitrariamente; "
            "estimula a harmonização com padrões do Codex Alimentarius, da OIE e da CIPV.",
            "Sem base científica, a medida vira " + azb("protecionismo disfarçado") + " e pode ser contestada no "
            "Órgão de Solução de Controvérsias, que chega a autorizar " + azb("retaliação") + " — caso "
            + vd("CE–Hormônios") + " (carne bovina com hormônios), em que EUA e Canadá foram autorizados a "
            "retaliar em " + vd("1999") + ". Por terem parâmetros técnicos verificáveis, essas medidas podem "
            "ser testadas e punidas.",
            "Efeito econômico típico: reserva de mercado para quem já cumpre a norma, custo de adaptação para o "
            "exportador e preços internos mais altos — ineficiência, e não ganho de escala.",
        ],
        "dissecando": (cz("[nexo indevido]") + " O item atribui a uma barreira um benefício que nasce justamente "
                       "da ausência de barreiras (mercado ampliado). O vocabulário técnico (“benefícios "
                       "indiretos”, “natureza concreta e objetiva”) dá aparência de rigor a um nexo causal "
                       "inexistente."),
        "modulos": [("🟣 Posição do Brasil", [
            rx("O Brasil") + ", grande exportador de carnes e grãos, é um dos membros mais ativos contra SPS sem "
            "base científica — barreiras sanitárias a carnes brasileiras estão entre os principais entraves às "
            "suas exportações agrícolas."])],
        "reescrita": ("A obtenção de economias crescentes de escala " + hl("não é benefício") + " do "
                      "estabelecimento de restrições fitossanitárias, o qual, em razão de sua natureza concreta e "
                      "objetiva, propicia retaliações internacionais."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Restrições fitossanitárias geram apenas reservas de mercado, ineficientes por "
                             "impedirem a livre concorrência e estratificarem o mercado mundial pela adequação às "
                             "normas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: a segunda oração (natureza concreta e objetiva → retaliações) é imprecisa, mas "
                    "defensável pelo Acordo SPS; o vermelho ficou só no nexo das economias de escala, que é o que "
                    "o gabarito e o comentário apontam"],
    },
    # ------------------------------------------------------------------ E1-0944
    {
        "id": "ECO-E1-0944-1", "fonte_ref": "E1-0944", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("Um dos argumentos em favor da imposição de barreiras alfandegárias é o de que, com esse "
                      "procedimento, se evita a exportação de empregos, que, igualmente, tende a ocorrer quando, "
                      "por efeito da valorização do câmbio, as exportações de um país se tornam menos "
                      "competitivas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um dos argumentos em favor da imposição de barreiras alfandegárias é o de que, com esse "
                      "procedimento, se evita a <u>exportação de empregos</u>, que, igualmente, tende a ocorrer "
                      "quando, por efeito da <u>valorização do câmbio</u>, as exportações de um país se tornam "
                      "menos competitivas."),
        "poucas": ("O item <b>descreve</b> um argumento protecionista clássico (proteger o emprego doméstico) e "
                   "um mecanismo verdadeiro: câmbio valorizado desloca demanda para o exterior e também "
                   + azb("“exporta” empregos") + "."),
        "destrinchando": [
            "Lógica do argumento: cada bem importado no lugar de um produzido no país transfere demanda — e, "
            "com ela, emprego — para o exterior. A barreira devolve essa demanda ao produtor doméstico.",
            "O câmbio valorizado produz o mesmo efeito por outro caminho: encarece as exportações e barateia as "
            "importações; a demanda agregada doméstica cai e a do parceiro sobe. Por isso o argumento do "
            "emprego costuma vir junto da defesa de " + azb("câmbio competitivo") + ".",
            "Crítica da teoria convencional: no longo prazo, o nível de emprego depende de fatores "
            "macroeconômicos (demanda agregada, mercado de trabalho), não da política comercial; a barreira "
            "apenas " + azb("realoca") + " empregos — salva os do setor protegido e destrói os de setores "
            "exportadores e usuários de insumos importados —, além de convidar à " + azb("retaliação") + ".",
            "Em recessão com desemprego keynesiano, a proteção pode elevar o emprego no curto prazo, mas é uma "
            "política de “empobrecer o vizinho” (<i>beggar-thy-neighbour</i>), como a escalada tarifária dos anos "
            "1930 (Smoot-Hawley, " + vd("1930") + ").",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O verbo decisivo é “um dos argumentos em "
                       "favor”: o item não diz que o argumento é correto, só que existe. Quem julga o mérito "
                       "(“protecionismo não cria empregos”) marca ERRADO por engano. 🔥 A banca usa muito "
                       "“argumento em favor de…” para testar se o candidato separa descrição de endosso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A imposição de barreiras alfandegárias eleva de forma permanente o nível de emprego da "
            "economia.”</i> → ERRADO (extrapolação: no longo prazo, só realoca empregos)",
            "<i>“A desvalorização cambial, ao baratear as exportações, tende a deslocar demanda e empregos para o "
            "país que desvaloriza.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Exportações menos competitivas reduzem a demanda agregada e destroem empregos; o país "
                             "concorrente recebe mais demanda. Nas barreiras, a importação de bens desloca demanda "
                             "para o exterior."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0947
    {
        "id": "ECO-E1-0947-1", "fonte_ref": "E1-0947", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifas, além de transferir recursos dos consumidores para o governo, conduz "
                      "ao aumento dos preços dos bens domésticos e eleva a ineficiência na economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de tarifas, <u>além de</u> transferir recursos dos consumidores para o governo, "
                      "conduz ao aumento dos preços dos bens domésticos e eleva a ineficiência na economia."),
        "poucas": ("A tarifa eleva o preço interno do bem (importado e nacional concorrente), transfere parte do "
                   "excedente do consumidor ao " + azb("governo") + " (receita) e ao produtor, e gera "
                   + azb("peso morto") + "."),
        "destrinchando": [
            "Com a tarifa, o preço doméstico sobe de Pm para " + vd("Pm + t") + " — tanto o do importado quanto "
            "o do similar nacional, que passa a vender ao preço protegido.",
            "Contabilidade de " + oc("Krugman e Obstfeld") + " (país pequeno): consumidor perde a + b + c + d; "
            "produtor ganha " + vd("a") + "; governo arrecada " + vd("c") + " (t × importações); "
            + azb("perda líquida") + " = " + vd("b + d") + ".",
            "Os dois triângulos são a ineficiência: " + vd("b") + " = " + azb("distorção na produção")
            + " (produzir internamente, a custo maior, o que se importava mais barato); " + vd("d") + " = "
            + azb("distorção no consumo") + " (consumo que deixou de existir).",
            "O item não diz que o governo é o <b>único</b> beneficiário (“além de transferir…”), por isso a "
            "omissão do ganho do produtor não o torna errado.",
            "Exceção teórica: para um país grande, o ganho nos termos de troca pode superar b + d (" + azb("tarifa "
            "ótima") + "), mas à custa dos parceiros e sob risco de retaliação.",
        ],
        "dissecando": (cz("[literalidade]") + " O item reproduz a lista de efeitos da tarifa no país pequeno. A "
                       "armadilha seria exigir a menção ao produtor: o item é incompleto, não errado. "
                       "🔥 Cebraspe considera certo o item incompleto, salvo se houver restrição (“apenas”, "
                       "“somente”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A imposição de tarifas transfere recursos dos consumidores apenas para o governo.”</i> → ERRADO "
            "(restrição indevida: também para os produtores)",
            "<i>“A receita tarifária corresponde integralmente à perda do consumidor.”</i> → ERRADO (a perda "
            "inclui o ganho do produtor e o peso morto)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["além de"], "dificuldade": 1,
        "comentario_fonte": ("Tarifas favorecem o produtor nacional às custas do consumidor; criam preço artificial "
                             "e tornam a economia menos eficiente, sem estímulo a melhorias produtivas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0937-1 (mesma contabilidade de bem-estar da tarifa)"],
    },
    # ------------------------------------------------------------------ E1-0950
    {
        "id": "ECO-E1-0950-1", "fonte_ref": "E1-0950", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("Para o bem-estar dos consumidores, os efeitos negativos da imposição de uma tarifa ad "
                      "valorem sobre as importações podem ser compensados por ganhos nos termos de troca, quando a "
                      "demanda do país que impõe a tarifa é capaz de influenciar os preços mundiais de um "
                      "produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Para o bem-estar dos consumidores, os efeitos negativos da imposição de uma tarifa ad "
                      "valorem sobre as importações <u>podem</u> ser compensados por ganhos nos termos de troca, "
                      "<u>quando a demanda do país que impõe a tarifa é capaz de influenciar os preços "
                      "mundiais</u> de um produto."),
        "poucas": ("Num " + azb("país grande") + ", a tarifa reduz a demanda mundial e " + vd("derruba o preço "
                   "mundial") + ": parte da tarifa é paga pelo exportador estrangeiro, e esse " + azb("ganho de "
                   "termos de troca") + " pode compensar as perdas de eficiência."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá CERTO, e a ideia central — a " + azb("tarifa ótima") + " do país grande — é "
                          "correta. Mas o ganho de termos de troca é do <b>país</b>: chega ao governo como receita "
                          "paga em parte pelo exportador estrangeiro. O consumidor continua pagando preço interno "
                          "maior (o preço sobe menos que t, mas sobe) e perde excedente. Rigorosamente, o item "
                          "seria indiscutível com “bem-estar nacional”; com “bem-estar dos consumidores”, ERRADO "
                          "seria defensável. Mantém-se o gabarito da fonte.")],
        "destrinchando": [
            "País pequeno: toma o preço mundial como dado; a tarifa eleva o preço interno em t inteiro e só gera "
            "perdas líquidas (os dois triângulos de " + azb("peso morto") + ").",
            "País grande: ao importar menos, reduz a demanda mundial e o " + vd("preço mundial cai") + ". O "
            "preço interno sobe menos que t; a diferença é suportada pelo estrangeiro. Na contabilidade de "
            + oc("Krugman e Obstfeld") + ", o retângulo de receita tem uma parte paga pelos consumidores "
            "domésticos e outra (" + azb("ganho de termos de troca") + ") paga pelo exportador estrangeiro.",
            "Se o ganho de termos de troca supera o peso morto, o " + azb("bem-estar nacional") + " aumenta. A "
            + azb("tarifa ótima") + " é a que maximiza essa diferença: positiva e tanto maior quanto menos "
            "elástica a oferta estrangeira.",
            "Limites: o ganho é obtido à custa do parceiro (política de “empobrecer o vizinho”), o mundo como um "
            "todo perde eficiência e o parceiro pode " + azb("retaliar") + " — uma guerra tarifária deixa "
            "ambos piores.",
            vm("Regra-âncora: tarifa de país grande → preço mundial cai → ganho de termos de troca pode superar o "
               "peso morto."),
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " O item se protege com “podem” e com a condição "
                       "exata (“capaz de influenciar os preços mundiais”), que é a definição de país grande. "
                       "Quem só conhece o caso do país pequeno marca ERRADO. O ponto frágil é o sujeito "
                       "(“consumidores” no lugar de “país”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para um país pequeno, os efeitos negativos de uma tarifa podem ser compensados por ganhos nos "
            "termos de troca.”</i> → ERRADO (troca de conceito: país pequeno não afeta o preço mundial)",
            "<i>“Ao impor uma tarifa, o país grande eleva o preço mundial do bem importado.”</i> → ERRADO "
            "(inversão: o preço mundial cai)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["podem", "quando"], "dificuldade": 3,
        "comentario_fonte": ("V: possibilidade teórica; a tarifa impõe preço interno P0 acima do internacional PW; "
                             "se a economia for grande, o deslocamento da demanda elevaria os preços internacionais "
                             "até P0 (situação incomum)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "00049.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo explicado no 📖)"}],
        "alertas": ["contestavel: o ganho de termos de troca beneficia o bem-estar nacional (via receita), não o "
                    "dos consumidores, que ainda pagam preço interno maior; gabarito CERTO da fonte mantido",
                    "qualidade_fonte: o comentário de origem diz que o país grande eleva os preços internacionais; "
                    "a tarifa de país grande reduz o preço mundial"],
    },
    # ------------------------------------------------------------------ E1-0951
    {
        "id": "ECO-E1-0951-1", "fonte_ref": "E1-0951", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("A concessão de um subsídio às exportações de um produto resulta em ganhos para os "
                      "exportadores e em perdas para o governo em razão dos custos do subsídio, sem efeitos "
                      "negativos para o bem-estar dos consumidores do país exportador."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A concessão de um subsídio às exportações de um produto resulta em ganhos para os "
                       "exportadores e em perdas para o governo em razão dos custos do subsídio, ")
                    + vm("sem efeitos negativos") + az(" para o bem-estar dos consumidores do país exportador.")),
        "poucas": ("O subsídio torna a venda externa mais vantajosa: os produtores desviam oferta para fora e o "
                   + vd("preço interno sobe") + " até Pm + s. O " + azb("consumidor doméstico perde") + "."),
        "destrinchando": [
            "País pequeno exportador, preço mundial Pm. Com subsídio s por unidade exportada, ninguém aceita "
            "vender internamente por menos que " + vd("Pm + s") + ": o preço doméstico sobe, a produção "
            "aumenta e o consumo interno cai — as exportações crescem pelos dois lados.",
            "Bem-estar (" + oc("Krugman e Obstfeld") + "): " + azb("consumidores perdem") + " a faixa entre os "
            "dois preços à esquerda da demanda; " + azb("produtores ganham") + " a faixa à esquerda da oferta; "
            "o " + azb("governo gasta") + " s × exportações. O custo fiscal supera a soma dos efeitos privados, "
            "e o resultado líquido é perda: dois triângulos de " + azb("peso morto") + ".",
            "País grande: ao inundar o mercado, ele " + vd("derruba o preço mundial") + " e ainda perde termos "
            "de troca — o subsídio fica mais caro e beneficia consumidores estrangeiros.",
            "Contraste útil: um subsídio à <b>produção</b> numa economia fechada beneficia consumidores e "
            "produtores (o preço ao consumidor cai). O subsídio à <b>exportação</b> faz o contrário com o "
            "consumidor doméstico, porque eleva o preço interno.",
            "Na OMC, subsídios à exportação de " + azb("bens industriais") + " são proibidos (Acordo SMC, "
            "subsídios “vermelhos”); os " + azb("agrícolas") + " foram eliminados por decisão da Conferência "
            "de " + vd("Nairóbi (2015)") + ".",
        ],
        "grafico_verso": "ECO-E1-0951-1-V1",
        "dissecando": (cz("[meia-verdade]") + " Ganho dos exportadores e custo fiscal estão certos; o erro foi "
                       "enxertado no fim (“sem efeitos negativos para os consumidores”). A pista é que o "
                       "subsídio é à <b>exportação</b>: tudo o que torna a venda externa mais atraente encarece "
                       "o mercado interno."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O subsídio à exportação de um país pequeno eleva o preço interno do bem e reduz o consumo "
            "doméstico.”</i> → CERTO",
            "<i>“O subsídio à exportação gera ganho líquido de bem-estar, porque o ganho dos produtores supera "
            "o custo fiscal.”</i> → ERRADO (inversão: o custo fiscal supera os ganhos privados)",
        ])],
        "reescrita": ("A concessão de um subsídio às exportações de um produto resulta em ganhos para os "
                      "exportadores e em perdas para o governo em razão dos custos do subsídio, "
                      + hl("com efeitos negativos") + " para o bem-estar dos consumidores do país exportador."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["sem"], "dificuldade": 1,
        "comentario_fonte": ("O subsídio é um imposto negativo; o benefício é repartido entre compradores e "
                             "vendedores conforme as elasticidades; consumidores e produtores se beneficiam e o "
                             "Estado arca com o custo fiscal (gráfico de subsídio)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "00050.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0951-1-V1, subsídio à exportação em vez de subsídio à "
                                   "produção)"}],
        "alertas": ["qualidade_fonte: o comentário de origem descreve um subsídio à produção em economia fechada "
                    "(consumidores ganham) e o aplica ao subsídio à exportação, que eleva o preço interno e "
                    "prejudica o consumidor doméstico",
                    "quase_duplicata: ECO-E2-L00185-1, ECO-E2-L00201-1 (subsídio à exportação reduz o excedente "
                    "do consumidor)"],
    },
    # ------------------------------------------------------------------ E1-0952
    {
        "id": "ECO-E1-0952-1", "fonte_ref": "E1-0952", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("Do ponto de vista do governo, os efeitos da imposição de uma tarifa ou de uma cota de "
                      "importação são equivalentes, uma vez que o resultado final de ambos os instrumentos de "
                      "política comercial é a elevação dos preços internos do bem importado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Do ponto de vista do governo, os efeitos da imposição de uma tarifa ou de uma cota de "
                       "importação ") + vm("são equivalentes") + az(", ") + vm("uma vez que") + az(" o resultado "
                       "final de ambos os instrumentos de política comercial ") + vm("é") + az(" a elevação dos "
                       "preços internos do bem importado.")),
        "poucas": ("Para consumidores e produtores, tarifa e cota equivalente se parecem (mesmo preço interno). "
                   "Para o <b>governo</b>, não: a tarifa gera " + azb("receita") + "; a cota, em regra, gera "
                   + azb("renda de cota") + " para quem tem as licenças."),
        "destrinchando": [
            "Uma cota que limite as importações ao mesmo volume que a tarifa deixaria entrar produz o mesmo "
            "preço interno, a mesma produção, o mesmo consumo e o mesmo " + azb("peso morto") + ". Daí a ideia "
            "de " + azb("equivalência tarifa–cota") + ".",
            "A diferença é o retângulo (preço interno − preço mundial) × importações: com a tarifa, é "
            + azb("receita tributária") + "; com a cota, vira " + azb("renda de cota") + " de quem obtém as "
            "licenças. Se forem dadas a importadores domésticos, a renda fica no país; se a cota for "
            "administrada pelo exportador (" + azb("restrição voluntária de exportação") + ", como a dos "
            "automóveis japoneses nos EUA nos anos 1980), a renda vai para o estrangeiro e a perda nacional "
            "aumenta.",
            "Exceção: se o governo " + azb("leiloar") + " as licenças, captura a renda e a equivalência volta a "
            "valer também para ele.",
            "A equivalência quebra com mudanças na demanda ou com poder de mercado: com demanda crescente, a "
            "cota trava o volume e eleva o preço; com produtor doméstico monopolista, a cota permite exercer "
            "poder de mercado que a tarifa não permite.",
            vm("Regra-âncora: tarifa → receita do governo; cota → renda de quem detém as licenças."),
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A justificativa (ambas elevam o preço interno) "
                       "é verdadeira, mas não sustenta a conclusão para o <b>governo</b>, cujo critério é a "
                       "arrecadação. A pista está no recorte inicial: “do ponto de vista do governo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Do ponto de vista dos consumidores, uma tarifa e uma cota de importação equivalentes produzem "
            "a mesma elevação do preço interno.”</i> → CERTO",
            "<i>“Na restrição voluntária de exportação, a renda de cota é apropriada pelo governo do país "
            "importador.”</i> → ERRADO (troca de ator: fica com os exportadores estrangeiros)",
        ])],
        "reescrita": ("Do ponto de vista do governo, os efeitos da imposição de uma tarifa ou de uma cota de "
                      "importação " + hl("diferem") + ", " + hl("pois, em regra, só a tarifa gera receita, "
                      "embora") + " o resultado final de ambos os instrumentos de política comercial " + hl("seja")
                      + " a elevação dos preços internos do bem importado."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A cota não gera receita fiscal; a receita da tarifa pode compensar consumidores via "
                             "subsídios. Para os excedentes do consumidor e do produtor, os efeitos são similares."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0953
    {
        "id": "ECO-E1-0953-1", "fonte_ref": "E1-0953", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_POL,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifas à exportação é adotada, em certos casos, como mecanismo de "
                      "estabilização dos preços internos e contenção de pressões inflacionárias, mas, em longo "
                      "prazo, pode resultar em desestímulo à produção e consequente redução da oferta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de tarifas à exportação é adotada, <u>em certos casos</u>, como mecanismo de "
                      "estabilização dos preços internos e contenção de pressões inflacionárias, mas, em longo "
                      "prazo, <u>pode</u> resultar em desestímulo à produção e consequente redução da oferta."),
        "poucas": ("O imposto de exportação reduz o que o produtor recebe lá fora e o faz " + azb("vender mais no "
                   "mercado interno") + ": o preço doméstico cai (efeito anti-inflacionário). Mas a remuneração "
                   "menor " + vd("desestimula investimento e produção") + " no longo prazo."),
        "destrinchando": [
            "País pequeno exportador: com imposto t por unidade exportada, o produtor só recebe Pm − t pela venda "
            "externa; para ele, vender internamente por mais que isso compensa. O " + vd("preço interno cai "
            "para Pm − t") + ": o consumo sobe, a produção cai e as exportações encolhem.",
            "Bem-estar: " + azb("consumidores ganham") + "; " + azb("produtores perdem") + " mais do que isso; "
            "o governo arrecada t × exportações; sobram dois triângulos de " + azb("peso morto") + " — é o "
            "espelho do subsídio à exportação.",
            "Uso típico: segurar o preço de alimentos e commodities em surtos inflacionários ou garantir "
            "abastecimento — as " + azb("retenciones") + " argentinas sobre a soja são o exemplo clássico; "
            "em 2008 e em 2022, vários países restringiram exportações de alimentos.",
            "Longo prazo: rentabilidade menor → menos investimento, menos área plantada, perda de mercados "
            "externos → a curva de oferta se desloca para a <b>esquerda</b> (redução da oferta), o que pode "
            "reverter o próprio efeito sobre os preços.",
            "No " + rx("Brasil") + ", o Imposto de Exportação (art. 153, II, da CF) tem função " + azb("extrafiscal")
            + " e uso raro; a regra é desonerar exportações (ICMS afastado pela " + rx("Lei Kandir") + ", "
            + vd("1996") + ").",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O item se protege duas vezes: “em certos "
                       "casos” (não diz que é a regra) e “pode resultar” (não diz que sempre resulta). Combina "
                       "o efeito de curto prazo (preço interno menor) com o de longo prazo (oferta menor) "
                       "sem contradição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tarifas à exportação elevam o preço interno do bem tributado.”</i> → ERRADO (inversão: o "
            "preço interno cai)",
            "<i>“Tarifas à exportação sempre resultam em aumento permanente da oferta doméstica.”</i> → ERRADO "
            "(modulador absoluto e inversão: no longo prazo a oferta tende a cair)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["em certos casos", "pode"],
        "dificuldade": 1,
        "comentario_fonte": ("Tarifas à exportação garantem suprimento interno e reduzem pressões inflacionárias, "
                             "mas reduzem o preço recebido pelo produtor; no longo prazo, a oferta se deslocaria "
                             "para a direita, reduzindo a quantidade produzida."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem fala em deslocamento da oferta para a direita com "
                    "redução da quantidade; a redução da oferta é deslocamento para a esquerda"],
    },
    # ------------------------------------------------------------------ E1-0955
    {
        "id": "ECO-E1-0955-1", "fonte_ref": "E1-0955", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado 07/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Acerca dos argumentos em favor do protecionismo, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A utilização de políticas protecionistas tende a priorizar mercados em que ocorram "
                      "externalidades negativas, como o baixo efeito de transbordamento. Este é o caso da campanha "
                      "“O petróleo é nosso!” de Getúlio Vargas em 1948, que, por meio da proteção ao mercado de "
                      "petróleo nacional, permitiu o aumento do efeito transbordamento do setor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A utilização de políticas protecionistas tende a priorizar mercados em que ocorram "
                       "externalidades ") + vm("negativas, como o baixo") + az(" efeito de transbordamento. Este "
                       "é o caso da campanha “O petróleo é nosso!” ") + vm("de Getúlio Vargas em 1948")
                    + az(", que, por meio da proteção ao mercado de petróleo nacional, permitiu o aumento do "
                         "efeito transbordamento do setor.")),
        "poucas": ("O argumento das externalidades justifica proteger setores com " + azb("externalidades "
                   "positivas") + " — alto " + azb("transbordamento") + " (tecnologia, qualificação, "
                   "encadeamentos). O item se contradiz: chama o baixo transbordamento de externalidade e depois "
                   "elogia seu aumento."),
        "destrinchando": [
            azb("Externalidade") + " é efeito de uma atividade sobre terceiros que o preço não capta. "
            + azb("Transbordamento") + " (<i>spillover</i>) é externalidade <b>positiva</b>: o conhecimento, a "
            "mão de obra treinada e os fornecedores criados por um setor beneficiam outros.",
            "Argumento protecionista das " + azb("falhas de mercado") + ": se o setor gera benefícios sociais "
            "maiores que os privados, o mercado o subdimensiona; a proteção (ou, melhor, o subsídio direto) "
            "corrige a falha. Por isso a proteção “prioriza” setores de alto transbordamento — indústria "
            "nascente, alta tecnologia.",
            "Na linguagem de " + oc("Hirschman") + " (<i>A estratégia do desenvolvimento econômico</i>, 1958), "
            "devem-se priorizar setores com fortes " + azb("encadeamentos") + " para trás (demanda por "
            "insumos) e para a frente (oferta para outros setores) — o petróleo é exemplo típico.",
            "História: a campanha " + rx("“O petróleo é nosso!”") + " foi um movimento da sociedade civil "
            "(estudantes, militares nacionalistas, o Centro de Estudos e Defesa do Petróleo, de "
            + vd("1948") + ") contra o Estatuto do Petróleo do governo " + rx("Dutra") + ". " + rx("Vargas")
            + " só voltou ao poder em " + vd("1951") + " e criou a " + rx("Petrobras") + " pela Lei "
            + vd("2.004/1953") + ", com monopólio estatal.",
            "Teoria convencional: diante de uma externalidade, o melhor instrumento é atacá-la na origem "
            "(subsídio à P&amp;D ou ao treinamento), não a tarifa, que cria distorções no consumo.",
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " A troca principal é “negativas” por "
                       "“positivas”, com o adjetivo “baixo” fabricando a contradição interna (baixo "
                       "transbordamento na 1ª frase, aumento celebrado na 2ª). A atribuição da campanha a Vargas "
                       "em 1948 é uma segunda imprecisão: ele não governava naquele ano."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Setores com externalidades positivas, como o transbordamento tecnológico, são candidatos "
            "frequentes à proteção pelo argumento das falhas de mercado.”</i> → CERTO",
            "<i>“A Petrobras foi criada em 1948, no auge da campanha “O petróleo é nosso!”.”</i> → ERRADO "
            "(dado alterado: Lei 2.004/1953)",
        ])],
        "reescrita": ("A utilização de políticas protecionistas tende a priorizar mercados em que ocorram "
                      "externalidades " + hl("positivas, como o elevado") + " efeito de transbordamento. Este é o "
                      "caso da campanha “O petróleo é nosso!” " + hl("(iniciada em 1947–1948 e encampada por "
                      "Getúlio Vargas na criação da Petrobras, em 1953)") + ", que, por meio da proteção ao "
                      "mercado de petróleo nacional, permitiu o aumento do efeito transbordamento do setor."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("Item contraditório: políticas protecionistas priorizam mercados com externalidades "
                             "positivas; Vargas buscava o transbordamento, estruturando a cadeia do petróleo "
                             "(qualificação, insumos, siderurgia)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: vermelho também em “de Getúlio Vargas em 1948” (campanha civil no governo Dutra; "
                    "Vargas criou a Petrobras em 1953); o comentário de origem não aponta essa imprecisão"],
    },
    # ------------------------------------------------------------------ E1-0962
    {
        "id": "ECO-E1-0962-1", "fonte_ref": "E1-0962", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_DOHA,
        "rotulo_item": "Item",
        "assertiva": "O Brasil tem defendido o acesso aos mercados mediante a imposição e majoração de tarifas.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Brasil tem defendido o acesso aos mercados mediante a ") + vm("imposição e majoração")
                    + az(" de tarifas.")),
        "poucas": ("" + azb("Acesso a mercados") + " se obtém " + vd("reduzindo") + " tarifas — o que o "
                   + rx("Brasil") + " pede, sobretudo para produtos agrícolas nos países desenvolvidos."),
        "destrinchando": [
            "Na OMC, “" + azb("acesso a mercados") + "” é um dos pilares das negociações (ao lado de apoio "
            "doméstico e subsídios à exportação, na agricultura) e significa reduzir tarifas e barreiras para que "
            "o produto estrangeiro entre. Majorar tarifas é o oposto.",
            "Agenda brasileira em Doha: cortes nas tarifas agrícolas (picos tarifários e escalada tarifária dos "
            "desenvolvidos), redução do apoio doméstico distorcivo e eliminação dos subsídios à exportação. Em "
            "troca, admitia reduzir tarifas em bens industriais (NAMA) e serviços, preservando flexibilidades "
            "para setores sensíveis (automóveis, têxteis, calçados).",
            "A rodada emperrou: em " + vd("julho de 2008") + ", a miniministerial de Genebra fracassou, entre "
            "outros pontos, na disputa EUA × Índia sobre o mecanismo de salvaguarda especial agrícola. Ganhos "
            "parciais vieram depois: Acordo de Facilitação de Comércio (" + vd("Bali, 2013") + ") e fim dos "
            "subsídios à exportação agrícola (" + vd("Nairóbi, 2015") + ").",
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o instrumento: “acesso a mercados” com “majoração de "
                       "tarifas” é contradição nos próprios termos. Basta saber o que a expressão significa no "
                       "jargão da OMC."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " liderou, na Conferência de " + vd("Cancún (2003)") + ", a criação do "
                + rx("G-20 comercial") + ", coalizão de países em desenvolvimento exportadores agrícolas (com "
                "Índia, China, África do Sul, Argentina) que bloqueou a proposta conjunta EUA–UE e recolocou a "
                "agricultura no centro de Doha."]),
            ("😈 Para dificultar", [
                "<i>“O Brasil tem defendido, na Rodada Doha, a redução de tarifas e de subsídios agrícolas nos "
                "países desenvolvidos.”</i> → CERTO",
                "<i>“O Brasil defendeu em Doha a eliminação imediata e total de suas tarifas industriais.”</i> → "
                "ERRADO (extrapolação: aceitava cortes com flexibilidades)",
            ]),
        ],
        "reescrita": ("O Brasil tem defendido o acesso aos mercados mediante a " + hl("redução") + " de "
                      "tarifas."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Acesso a mercados envolve redução de tarifas; o Brasil busca reduzir tarifas dos "
                             "desenvolvidos sobre produtos agrícolas, em troca de reduzir as suas em setores como "
                             "automóveis, têxteis, vestuário, calçados e brinquedos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0963
    {
        "id": "ECO-E1-0963-1", "fonte_ref": "E1-0963", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_DOHA,
        "rotulo_item": "Item",
        "assertiva": ("O Brasil e vários países em desenvolvimento deram ênfase às negociações relativas aos "
                      "produtos agrícolas, dada a concentração desses produtos em suas pautas de exportação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Brasil e vários países em desenvolvimento deram ênfase às negociações relativas aos "
                      "<u>produtos agrícolas</u>, dada a concentração desses produtos em suas pautas de "
                      "exportação."),
        "poucas": ("A agricultura foi o " + azb("eixo de Doha") + " para os exportadores agrícolas em "
                   "desenvolvimento: é onde estão suas vantagens comparativas e onde os desenvolvidos mantêm "
                   "as maiores distorções."),
        "destrinchando": [
            "Por décadas a agricultura ficou à margem do GATT (derrogações e políticas como a " + azb("Política "
            "Agrícola Comum") + " europeia, de " + vd("1962") + "). Só a Rodada Uruguai trouxe disciplinas, "
            "com o Acordo sobre Agricultura, e o próprio acordo previa nova negociação — que entrou em Doha.",
            "Três pilares negociados: " + azb("acesso a mercados") + " (tarifas e cotas), " + azb("apoio "
            "doméstico") + " (subsídios à produção, as “caixas” amarela, azul e verde) e " + azb("concorrência "
            "nas exportações") + " (subsídios à exportação).",
            "Interesse dos desenvolvidos: serviços, propriedade intelectual, compras governamentais e acesso a "
            "mercados industriais (NAMA). A troca “agricultura por NAMA e serviços” nunca fechou, o que explica "
            "em boa parte o impasse da rodada.",
            "⏳ (out/2026) A Rodada Doha segue sem conclusão; os resultados agrícolas mais relevantes foram o fim "
            "dos subsídios à exportação (Nairóbi, " + vd("2015") + ") e decisões sobre estoques públicos para "
            "segurança alimentar (Bali, " + vd("2013") + ").",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item que descreve corretamente a agenda e o motivo (pauta "
                       "exportadora concentrada em agrícolas). A troca que a banca costuma fazer é a do tema: "
                       "atribuir ao Brasil a ênfase em serviços ou propriedade intelectual."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " articulou o " + rx("G-20 comercial") + " (Cancún, " + vd("2003") + ") e "
                "integra o " + rx("Grupo de Cairns") + " (exportadores agrícolas, desde 1986). Venceu, no Órgão "
                "de Solução de Controvérsias, os casos do " + rx("algodão") + " contra os EUA e do "
                + rx("açúcar") + " contra a UE (" + vd("2004–2005") + "), ambos sobre subsídios agrícolas."]),
            ("😈 Para dificultar", [
                "<i>“O Brasil e os demais latino-americanos priorizaram, em Doha, as negociações sobre serviços e "
                "propriedade intelectual.”</i> → ERRADO (troca de tema: essa é a agenda dos desenvolvidos)",
            ]),
        ],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A dificuldade da rodada veio de prioridades inconciliáveis: países em desenvolvimento "
                             "defendiam a derrubada das proteções aos produtores agrícolas dos desenvolvidos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0970-1 (agenda latino-americana em Doha: agricultura, não serviços)"],
    },
    # ------------------------------------------------------------------ E1-0964
    {
        "id": "ECO-E1-0964-1", "fonte_ref": "E1-0964", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_DOHA,
        "rotulo_item": "Item",
        "assertiva": ("Nas Rodadas do antigo GATT, avanços mais significativos ocorreram em relação a produtos "
                      "manufaturados, em comparação com os modestos resultados na liberalização do setor agrícola, "
                      "para o qual não se logrou, de modo geral, a eliminação das barreiras às importações."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nas Rodadas do antigo GATT, avanços mais significativos ocorreram em relação a produtos "
                      "<u>manufaturados</u>, em comparação com os modestos resultados na liberalização do setor "
                      "agrícola, para o qual não se logrou, <u>de modo geral</u>, a eliminação das barreiras às "
                      "importações."),
        "poucas": ("As oito rodadas do GATT derrubaram as tarifas industriais dos países desenvolvidos a "
                   + vd("poucos pontos percentuais") + ", enquanto a " + azb("agricultura") + " permaneceu "
                   "protegida e quase fora das disciplinas até a Rodada Uruguai."),
        "destrinchando": [
            "Rodadas do GATT: Genebra (" + vd("1947") + "), Annecy, Torquay, Genebra, Dillon, " + azb("Kennedy")
            + " (" + vd("1964–67") + ", cortes lineares e antidumping), " + azb("Tóquio") + " (" + vd("1973–79")
            + ", códigos de barreiras não tarifárias, Cláusula de Habilitação) e " + azb("Uruguai") + " ("
            + vd("1986–94") + ", criação da OMC).",
            "Nos manufaturados, a tarifa média dos países industrializados caiu de níveis próximos de "
            + vd("40%") + " no pós-guerra para menos de " + vd("5%") + " ao fim da Rodada Uruguai — o grande "
            "sucesso do GATT.",
            "Na agricultura, o oposto: derrogação concedida aos EUA em " + vd("1955") + ", a Política Agrícola "
            "Comum europeia, cotas e subsídios generalizados. Só o " + azb("Acordo sobre Agricultura")
            + " (Uruguai) trouxe a " + azb("tarificação") + " (cotas convertidas em tarifas) e compromissos de "
            "redução de apoio doméstico e de subsídios à exportação — sem eliminar as barreiras.",
            "Têxteis também ficaram fora, regidos pelo " + azb("Acordo Multifibras") + " (cotas), até a "
            "integração gradual concluída em " + vd("2005") + ".",
            "Razão política: o GATT foi conduzido pelos países industrializados, que liberalizaram onde eram "
            "competitivos (manufaturas) e protegeram onde não eram (agricultura, têxteis).",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item é seguro pelo contraste "
                       "manufaturas × agricultura e pelo “de modo geral”, que admite exceções. A versão errada "
                       "típica inverte os setores ou afirma que o GATT eliminou as barreiras agrícolas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Rodada Uruguai eliminou as barreiras às importações agrícolas, convertendo-as em cotas.”</i> → "
            "ERRADO (inversão: cotas foram convertidas em tarifas, que permaneceram)",
            "<i>“Os têxteis foram integralmente liberalizados já nas primeiras rodadas do GATT.”</i> → ERRADO "
            "(anacronismo: regidos por cotas até 2005)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["de modo geral"],
        "dificuldade": 1,
        "comentario_fonte": ("O GATT foi liderado pelas nações industrializadas, e o foco das negociações atendeu "
                             "aos interesses delas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: tarifa média industrial de ~40% (pós-guerra) para menos de 5% (fim da Rodada "
                    "Uruguai), ordem de grandeza usual nos manuais"],
    },
    # ------------------------------------------------------------------ E1-0965
    {
        "id": "ECO-E1-0965-1", "fonte_ref": "E1-0965", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_DOHA,
        "rotulo_item": "Item",
        "assertiva": ("Entre as principais distorções que caracterizam o comércio agrícola, destacam-se os "
                      "subsídios às importações e o aumento da taxação da produção interna."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Entre as principais distorções que caracterizam o comércio agrícola, destacam-se os "
                       "subsídios ") + vm("às importações") + az(" e ") + vm("o aumento da taxação da produção "
                       "interna") + az(".")),
        "poucas": ("As distorções são o inverso: " + azb("subsídios à produção e à exportação") + " nos países "
                   "desenvolvidos e " + azb("tarifas elevadas sobre as importações") + "."),
        "destrinchando": [
            "Os três pilares do Acordo sobre Agricultura correspondem às três distorções: (1) " + azb("barreiras "
            "às importações") + " — tarifas altas, picos e escalada tarifária, cotas tarifárias; (2) " + azb("apoio "
            "doméstico") + " — subsídios à produção e preços garantidos; (3) " + azb("subsídios à exportação")
            + ".",
            "Efeito sobre o mercado mundial: o subsídio estimula a produção nos países ricos, gera excedentes "
            "despejados no exterior e " + vd("deprime os preços internacionais") + ", prejudicando os "
            "exportadores competitivos sem subsídio — como os do Mercosul.",
            "Subsidiar importações e tributar a própria produção prejudicaria o produtor doméstico — o contrário "
            "do que fazem as políticas agrícolas dos desenvolvidos. (Há casos históricos de taxação da "
            "agricultura em países em desenvolvimento, via câmbio ou impostos de exportação, mas não é a "
            "distorção que marca o comércio agrícola mundial.)",
            "Classificação do apoio doméstico na OMC: " + azb("caixa amarela") + " (distorcivo, sujeito a "
            "redução), " + azb("caixa azul") + " (atrelado a limites de produção) e " + azb("caixa verde")
            + " (minimamente distorcivo, isento: pesquisa, ambiental, renda desvinculada da produção).",
        ],
        "dissecando": (cz("[inversão]") + " Dupla inversão: troca o alvo do subsídio (produção/exportação → "
                       "importação) e o alvo da tributação (importação → produção interna). Quem lembra que a "
                       "política agrícola dos ricos <b>protege</b> o produtor doméstico desmonta as duas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Subsídios agrícolas nos países desenvolvidos tendem a deprimir os preços internacionais dos "
            "produtos subsidiados.”</i> → CERTO",
            "<i>“Os subsídios classificados na caixa verde estão sujeitos a compromissos de redução.”</i> → "
            "ERRADO (troca de conceito: isso vale para a caixa amarela)",
        ])],
        "reescrita": ("Entre as principais distorções que caracterizam o comércio agrícola, destacam-se os "
                      "subsídios " + hl("à produção e às exportações") + " e " + hl("a elevada taxação das "
                      "importações") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Os subsídios são dados aos produtores dos desenvolvidos, reduzindo custos para "
                             "concorrer com importados; a taxação recai sobre os importados, não sobre a produção "
                             "doméstica."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0970
    {
        "id": "ECO-E1-0970-1", "fonte_ref": "E1-0970", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_OMC,
        "rotulo_item": "Item",
        "assertiva": ("Um dos objetivos da Rodada de Desenvolvimento de Doha, primeira a tratar de negociações "
                      "multilaterais no âmbito da OMC, é assegurar tratamento especial e diferenciado aos países "
                      "emergentes (BRICS). O Brasil e os demais latino-americanos enfatizam as negociações de "
                      "comércio de serviços e as questões relacionadas à propriedade intelectual."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um dos objetivos da Rodada de Desenvolvimento de Doha, primeira a tratar de negociações "
                       "multilaterais no âmbito da OMC, é assegurar tratamento especial e diferenciado aos países ")
                    + vm("emergentes (BRICS)") + az(". O Brasil e os demais latino-americanos enfatizam as "
                    "negociações de ") + vm("comércio de serviços e as questões relacionadas à propriedade "
                    "intelectual") + az(".")),
        "poucas": ("Doha é de fato a 1ª rodada da OMC, mas o " + azb("tratamento especial e diferenciado")
                   + " vale para os <b>países em desenvolvimento</b> em geral, e a prioridade latino-americana é a "
                   + azb("agricultura") + ". Serviços e propriedade intelectual são a agenda dos desenvolvidos."),
        "destrinchando": [
            "Doha (" + vd("novembro de 2001") + ") foi a primeira rodada lançada pela OMC; as oito anteriores "
            "ocorreram no GATT, a última delas a Uruguai (" + vd("1986–94") + "), que criou a OMC (Marraqueche, "
            + vd("1994") + "; em funcionamento desde " + vd("1995") + ").",
            "O " + azb("tratamento especial e diferenciado (TED)") + " — prazos maiores, compromissos menores, "
            "assistência técnica — beneficia os <b>países em desenvolvimento</b> (que se autodeclaram como tais) "
            "e, com mais intensidade, os " + azb("países de menor desenvolvimento relativo") + ". Não há regime "
            "próprio para os BRICS, agrupamento político sem estatuto na OMC.",
            "Agendas: " + rx("Brasil") + " e latino-americanos (vários no Grupo de Cairns) priorizam acesso a "
            "mercados agrícolas e corte de subsídios; EUA, UE e Japão priorizam serviços, propriedade "
            "intelectual (TRIPS-plus) e bens industriais.",
            "O próprio nome — “Agenda de Desenvolvimento” — expressa o compromisso de colocar as necessidades dos "
            "países em desenvolvimento no centro, o que a rodada não conseguiu entregar.",
        ],
        "dissecando": (cz("[troca de ator · restrição indevida]") + " A abertura verdadeira (1ª rodada da OMC) "
                       "dá credibilidade ao resto. Depois, troca as agendas (serviços/PI dos desenvolvidos "
                       "atribuídos aos latino-americanos) e restringe o TED aos BRICS. 🔥 Agenda brasileira em "
                       "Doha = agricultura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Rodada Doha foi a primeira rodada de negociações comerciais multilaterais lançada no âmbito "
            "da OMC.”</i> → CERTO",
            "<i>“A Rodada Uruguai, última do GATT, foi concluída com a criação da OIC.”</i> → ERRADO (troca de "
            "conceito: criou a OMC; a OIC nunca existiu)",
        ])],
        "reescrita": ("Um dos objetivos da Rodada de Desenvolvimento de Doha, primeira a tratar de negociações "
                      "multilaterais no âmbito da OMC, é assegurar tratamento especial e diferenciado aos países "
                      + hl("em desenvolvimento") + ". O Brasil e os demais latino-americanos enfatizam as "
                      "negociações de " + hl("agricultura") + "."),
        "tipo_erro": ["TROCA_ATOR", "RESTRICAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Rodadas anteriores foram do GATT; Doha, iniciada em 2001, foi a primeira da OMC e não "
                             "chegou a acordo; serviços e propriedade intelectual são pleitos dos desenvolvidos."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: o comentário de origem só aponta o erro de serviços/propriedade intelectual; o "
                    "vermelho em “emergentes (BRICS)” corrige também a restrição do tratamento especial e "
                    "diferenciado"],
    },
    # ------------------------------------------------------------------ E1-0971
    {
        "id": "ECO-E1-0971-1", "fonte_ref": "E1-0971", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": True,
        "comando": "Acerca das instituições do sistema multilateral de comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Resultante das pressões de países com menor nível de desenvolvimento, a Conferência das "
                      "Nações Unidas sobre Comércio e Desenvolvimento (UNCTAD), estabelecida em 1964, é um órgão "
                      "das Nações Unidas que, entre outras funções, atua no sentido de disciplinar práticas "
                      "empresariais tidas como restritivas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Resultante das pressões de países com menor nível de desenvolvimento, a Conferência das "
                      "Nações Unidas sobre Comércio e Desenvolvimento (UNCTAD), estabelecida em <u>1964</u>, é um "
                      "órgão das Nações Unidas que, entre outras funções, atua no sentido de <u>disciplinar "
                      "práticas empresariais tidas como restritivas</u>."),
        "poucas": ("A " + azb("UNCTAD") + " nasceu em " + vd("1964") + " por pressão do Terceiro Mundo e, entre "
                   "suas funções, mantém o conjunto de princípios da ONU sobre " + azb("práticas comerciais "
                   "restritivas") + " (direito da concorrência), adotado em " + vd("1980") + "."),
        "destrinchando": [
            "Origem: insatisfeitos com um GATT que liberalizava sobretudo manufaturas dos países ricos, os países "
            "em desenvolvimento pressionaram por um foro próprio. A I UNCTAD reuniu-se em Genebra em "
            + vd("1964") + ", com " + oc("Raúl Prebisch") + " como primeiro secretário-geral; no mesmo ano "
            "formou-se o " + azb("G-77") + ".",
            "Natureza: órgão subsidiário permanente da " + azb("Assembleia Geral da ONU") + " (não é agência "
            "especializada nem cria regras vinculantes como a OMC). Trabalha com pesquisa, assistência técnica e "
            "construção de consensos; publica o " + azb("World Investment Report") + " e o "
            + azb("Trade and Development Report") + ".",
            "Práticas restritivas: o “Conjunto de Princípios e Regras Equitativos Multilateralmente Acordados "
            "para o Controle de Práticas Comerciais Restritivas” (" + vd("1980") + ", adotado pela Assembleia "
            "Geral) é administrado pela UNCTAD, que também elabora uma lei-modelo de concorrência e revisa as "
            "políticas de concorrência dos países.",
            "Legado: o " + azb("Sistema Geral de Preferências (SGP)") + " nasceu na II UNCTAD (Nova Délhi, "
            + vd("1968") + ") e foi acolhido no GATT pela Cláusula de Habilitação (" + vd("1979") + ").",
        ],
        "dissecando": (cz("[detalhe]") + " Item verdadeiro por um pormenor pouco estudado: a função de "
                       "concorrência da UNCTAD. Quem associa a UNCTAD só a comércio e desenvolvimento estranha "
                       "“práticas empresariais restritivas” e marca ERRADO. Data, origem e natureza estão "
                       "corretas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A UNCTAD, agência especializada da ONU, profere decisões vinculantes sobre práticas comerciais "
            "restritivas.”</i> → ERRADO (troca de conceito: é órgão subsidiário da AGNU, sem poder vinculante)",
            "<i>“O Sistema Geral de Preferências originou-se nas discussões da UNCTAD.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["entre outras funções"], "dificuldade": 2,
        "comentario_fonte": ("A UNCTAD informa sobre práticas empresariais e divulga indicadores de desempenho "
                             "voltados ao desenvolvimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0972
    {
        "id": "ECO-E1-0972-1", "fonte_ref": "E1-0972", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": "Acerca das instituições do sistema multilateral de comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O Acordo Geral sobre Tarifas e Comércio (GATT) passou a vigorar depois da Segunda Guerra "
                      "Mundial, diante do fracasso no estabelecimento da OIC, não se constituindo, entretanto, "
                      "como organismo formal até a criação da OMC."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Acordo Geral sobre Tarifas e Comércio (GATT) passou a vigorar depois da Segunda Guerra "
                      "Mundial, diante do fracasso no estabelecimento da OIC, <u>não se constituindo</u>, "
                      "entretanto, <u>como organismo formal</u> até a criação da OMC."),
        "poucas": ("O GATT era um " + azb("acordo provisório") + ", aplicado desde " + vd("1948") + " para "
                   "suprir a OIC que nunca nasceu; funcionou como organização <i>de facto</i>, sem personalidade "
                   "jurídica, até a " + azb("OMC") + " (" + vd("1995") + ")."),
        "destrinchando": [
            "Arquitetura planejada em Bretton Woods: FMI, BIRD e uma " + azb("Organização Internacional do "
            "Comércio (OIC)") + ". A " + azb("Carta de Havana") + " (" + vd("1948") + ") criaria a OIC, mas o "
            "Congresso dos EUA não a ratificou, e o governo Truman desistiu em " + vd("1950") + ".",
            "O " + azb("GATT") + " — negociado em Genebra em " + vd("1947") + " por " + vd("23") + " países, "
            "como capítulo de política comercial antecipado da Carta — entrou em vigor em "
            + vd("1º/1/1948") + " pelo Protocolo de Aplicação Provisória e acabou sendo o único pilar "
            "comercial do sistema.",
            "Por isso os membros eram “partes contratantes”, não “membros”; o secretariado vinha de uma "
            "comissão interina da OIC; a solução de controvérsias dependia de consenso (a parte perdedora podia "
            "bloquear o relatório).",
            "A " + azb("OMC") + ", criada pelo Acordo de Marraqueche (" + vd("abril de 1994") + ", fim da Rodada "
            "Uruguai) e em funcionamento desde " + vd("1º/1/1995") + ", é organização formal, com personalidade "
            "jurídica e solução de controvérsias com consenso negativo. O texto do GATT sobrevive como "
            + azb("GATT 1994") + ", um dos acordos anexos.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de manual. O detalhe que derruba o candidato apressado é "
                       "achar que o GATT foi uma organização formal desde 1947; a ressalva “não se "
                       "constituindo… como organismo formal” é exatamente o ponto verdadeiro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O GATT foi criado como organização internacional formal, posteriormente transformada na "
            "OMC.”</i> → ERRADO (troca de conceito: era acordo provisório, sem personalidade jurídica)",
            "<i>“Com a criação da OMC, o texto do GATT foi revogado.”</i> → ERRADO (sobrevive como GATT 1994)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O GATT é lançado em 1947 como carta de intenções, sem oficialização institucional, o "
                             "que é feito em 1994, na Rodada Uruguai, com a criação da OMC."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0973
    {
        "id": "ECO-E1-0973-1", "fonte_ref": "E1-0973", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": True,
        "comando": "Acerca das negociações agrícolas no sistema multilateral de comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A Rodada Uruguai produziu o primeiro acordo multilateral voltado para o comércio "
                      "internacional de produtos agrícolas. No tocante ao acesso aos mercados, tarifas foram "
                      "convertidas em cotas, e, em relação ao apoio doméstico, buscou-se reduzir subsídios, que "
                      "elevam os preços internacionais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Rodada Uruguai produziu o primeiro acordo multilateral voltado para o comércio "
                       "internacional de produtos agrícolas. No tocante ao acesso aos mercados, ")
                    + vm("tarifas foram convertidas em cotas") + az(", e, em relação ao apoio doméstico, "
                    "buscou-se reduzir subsídios, que ") + vm("elevam") + az(" os preços internacionais.")),
        "poucas": ("Na " + azb("tarificação") + " da Rodada Uruguai, " + vd("cotas e outras barreiras viraram "
                   "tarifas") + " (não o contrário). E subsídios " + vd("reduzem") + " os preços "
                   "internacionais, ao estimular produção e excedentes."),
        "destrinchando": [
            "O " + azb("Acordo sobre Agricultura") + " (Rodada Uruguai, " + vd("1986–94") + ") foi, de fato, o "
            "primeiro acordo multilateral específico para o comércio agrícola, organizado em três pilares: "
            "acesso a mercados, apoio doméstico e subsídios à exportação.",
            azb("Tarificação") + ": cotas, licenças, gravames variáveis e demais barreiras não tarifárias foram "
            "convertidos em " + azb("tarifas equivalentes") + " e consolidados, para depois serem reduzidos "
            "(em média " + vd("36%") + " nos desenvolvidos, em 6 anos). Tarifa é mais transparente e "
            "negociável que cota.",
            "Para não fechar mercados com tarifas altíssimas, criaram-se " + azb("cotas tarifárias") + ": um "
            "volume entra com tarifa baixa e o excedente paga a tarifa cheia — é daí que vem a confusão do item.",
            "Subsídio à produção ou à exportação baixa o custo do produtor, expande a oferta e "
            + vd("deprime o preço mundial") + " — prejudica exportadores sem subsídio. Por isso o Brasil "
            "combate os subsídios agrícolas dos desenvolvidos.",
        ],
        "dissecando": (cz("[inversão]") + " Duas inversões sobre um início verdadeiro: a direção da conversão "
                       "(cotas → tarifas) e o efeito do subsídio sobre o preço mundial. O nome técnico "
                       "“tarificação” já entrega a direção: tudo vira <b>tarifa</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No Acordo sobre Agricultura, as barreiras não tarifárias foram convertidas em tarifas "
            "consolidadas, processo conhecido como tarificação.”</i> → CERTO",
            "<i>“Os subsídios agrícolas dos países desenvolvidos beneficiam os exportadores agrícolas sem "
            "subsídio, ao elevarem os preços mundiais.”</i> → ERRADO (inversão: deprimem os preços)",
        ])],
        "reescrita": ("A Rodada Uruguai produziu o primeiro acordo multilateral voltado para o comércio "
                      "internacional de produtos agrícolas. No tocante ao acesso aos mercados, " + hl("cotas foram "
                      "convertidas em tarifas") + ", e, em relação ao apoio doméstico, buscou-se reduzir "
                      "subsídios, que " + hl("reduzem") + " os preços internacionais."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Subsídios reduzem os preços internacionais ao baratear a produção; o Acordo sobre "
                             "Agricultura ampliou o acesso a mercados, disciplinou o apoio doméstico e limitou "
                             "subsídios à exportação; cotas foram convertidas em tarifas (“tarificação”)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0974
    {
        "id": "ECO-E1-0974-1", "fonte_ref": "E1-0974", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_OMC,
        "rotulo_item": "Item",
        "assertiva": ("Na Rodada de Desenvolvimento de Doha de 2001, os ministros das relações exteriores e de "
                      "comércio dos diferentes países buscaram a liberalização comercial e o crescimento "
                      "econômico, com especial atenção às necessidades dos países em desenvolvimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na Rodada de Desenvolvimento de Doha de <u>2001</u>, os ministros das relações exteriores "
                      "e de comércio dos diferentes países buscaram a liberalização comercial e o crescimento "
                      "econômico, com especial atenção às <u>necessidades dos países em desenvolvimento</u>."),
        "poucas": ("A Declaração Ministerial de Doha (" + vd("novembro de 2001") + ") lançou a "
                   + azb("Agenda de Desenvolvimento de Doha") + ", que pôs as necessidades dos países em "
                   "desenvolvimento no centro da liberalização."),
        "destrinchando": [
            "A IV Conferência Ministerial da OMC, em Doha (Catar), lançou a rodada dois meses depois do 11 de "
            "Setembro, num clima de reafirmação do multilateralismo e após o fracasso de Seattle (" + vd("1999")
            + ").",
            "O mandato incluía agricultura, serviços, acesso a mercados industriais (NAMA), regras "
            "(antidumping, subsídios), facilitação de comércio, e reafirmava o " + azb("tratamento especial e "
            "diferenciado") + ". Na mesma reunião, a " + azb("Declaração sobre TRIPS e Saúde Pública")
            + " reconheceu o direito de licenciar compulsoriamente medicamentos — vitória brasileira.",
            "A ênfase no desenvolvimento ajuda a explicar o impasse: os países em desenvolvimento cobravam "
            "concessões agrícolas dos ricos sem contrapartida equivalente em indústria e serviços, e o prazo "
            "original (" + vd("2005") + ") nunca foi cumprido.",
            "⏳ (out/2026) A rodada nunca foi formalmente concluída; desde Nairóbi (" + vd("2015") + ") os "
            "membros divergem sobre a manutenção do mandato de Doha, e as negociações migraram para acordos "
            "plurilaterais e temas pontuais.",
        ],
        "dissecando": (cz("[literalidade]") + " Item que parafraseia a própria Declaração de Doha. A armadilha "
                       "estaria em pensar no fracasso da rodada: o item fala dos <b>objetivos</b> declarados, não "
                       "dos resultados."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " foi protagonista da " + rx("Declaração sobre TRIPS e Saúde Pública")
                + " (Doha, " + vd("2001") + "), na esteira do programa brasileiro de combate à aids e da "
                "disputa com os EUA sobre patentes de medicamentos."]),
            ("😈 Para dificultar", [
                "<i>“A Rodada Doha, concluída em 2005, atendeu às principais demandas agrícolas dos países em "
                "desenvolvimento.”</i> → ERRADO (dado alterado: a rodada não foi concluída)",
            ]),
        ],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A preocupação com o desenvolvimento foi a marca da rodada e pode estar na base de seu "
                             "fracasso em conciliar interesses nacionais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00183
    {
        "id": "ECO-E2-L00183-1", "fonte_ref": "E2-L00183", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_1,
        "rotulo_item": "Item",
        "assertiva": ("As cotas de importação são um exemplo de instrumento tarifário cujo objetivo é o de proteger "
                      "a indústria local."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As cotas de importação são um exemplo de instrumento ") + vm("tarifário") + az(" cujo "
                    "objetivo é o de proteger a indústria local.")),
        "poucas": ("A cota limita a " + azb("quantidade") + " importada; não é imposto sobre o preço. É, por "
                   "isso, " + azb("barreira não tarifária") + " — embora proteja a indústria local, como diz o "
                   "item."),
        "destrinchando": [
            azb("Instrumentos tarifários") + ": impostos de importação — " + azb("ad valorem") + " (percentual "
            "sobre o valor), " + azb("específicos") + " (valor por unidade física) e mistos. Agem pelo preço.",
            azb("Instrumentos não tarifários") + ": cotas (limite de quantidade), licenças de importação, "
            "restrições voluntárias de exportação, barreiras técnicas e sanitárias, exigências de conteúdo local, "
            "compras governamentais preferenciais. Agem pela quantidade ou pelo acesso.",
            "Efeito da cota: com a oferta importada travada, o preço interno sobe; o produtor doméstico ganha, o "
            "consumidor perde, há peso morto e surge a " + azb("renda de cota") + " — que fica com quem detém as "
            "licenças, salvo se o governo as leiloar.",
            "Híbrido que confunde: a " + azb("cota tarifária") + " (<i>tariff-rate quota</i>) aplica tarifa "
            "baixa dentro de um volume e tarifa alta acima dele. Mesmo ela é, juridicamente, um regime "
            "<b>tarifário</b> — a cota de importação pura, não.",
            "Na OMC, o art. XI do GATT proíbe, em regra, " + azb("restrições quantitativas") + "; daí a "
            "preferência pela tarifa e a tarificação agrícola da Rodada Uruguai.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca a classificação (não tarifário → tarifário) e mantém "
                       "o objetivo verdadeiro (proteger a indústria) para dar credibilidade. Critério de bolso: "
                       "se age sobre o preço por imposto, é tarifário; se age sobre a quantidade, não é."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As cotas de importação são barreiras não tarifárias que, ao limitar a quantidade importada, "
            "elevam o preço interno do bem.”</i> → CERTO",
            "<i>“As cotas de importação, por definição, geram receita para o governo do país importador.”</i> → "
            "ERRADO (só se as licenças forem leiloadas)",
        ])],
        "reescrita": ("As cotas de importação são um exemplo de instrumento " + hl("não tarifário") + " cujo "
                      "objetivo é o de proteger a indústria local."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Cota é barreira não tarifária: restringe quantidade, não é imposto sobre preço. "
                             "Protege ao reduzir a oferta importada e elevar o preço interno, gerando renda de "
                             "cota."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00184
    {
        "id": "ECO-E2-L00184-1", "fonte_ref": "E2-L00184", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_1,
        "rotulo_item": "Item",
        "assertiva": ("A proibição de entrada de carne bovina produzida em determinado local é exemplo típico de "
                      "barreira técnica, instrumento não tarifário, que visa à defesa da sociedade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A proibição de entrada de carne bovina produzida em determinado local é exemplo típico de "
                      "<u>barreira técnica</u>, instrumento <u>não tarifário</u>, que visa à defesa da "
                      "sociedade."),
        "poucas": ("Proibir carne de certa origem é medida " + azb("não tarifária") + " de natureza técnico-"
                   "sanitária, justificada pela proteção da saúde — no sentido amplo usado no Brasil, uma "
                   + azb("barreira técnica") + "."),
        "destrinchando": [
            "No uso corrente (manuais e governo brasileiro), “barreiras técnicas” abrange normas, regulamentos "
            "técnicos e exigências sanitárias e fitossanitárias que condicionam a entrada de produtos.",
            "Na OMC, a classificação é mais fina: o " + azb("Acordo SPS") + " cobre medidas para proteger a vida "
            "e a saúde humana, animal e vegetal (ex.: veto à carne de região com febre aftosa ou vaca louca); o "
            + azb("Acordo TBT") + " cobre regulamentos técnicos e normas em geral (rotulagem, especificações, "
            "padrões de segurança). O próprio TBT exclui de seu alcance as medidas SPS.",
            "Legitimidade: a medida é admitida se tiver " + vd("base científica") + " e avaliação de risco, "
            "seguir padrões internacionais (OIE/OMSA, para saúde animal) ou justificá-los, e não discriminar "
            "arbitrariamente. Admite-se a " + azb("regionalização") + ": proibir só a carne de áreas afetadas, "
            "não de todo o país.",
            "Risco: a mesma medida pode ser " + azb("protecionismo disfarçado") + " — por isso o Acordo SPS "
            "exige justificativa científica e permite contestação no Órgão de Solução de Controvérsias.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item usa “barreira técnica” no sentido amplo; "
                       "tecnicamente, o veto sanitário à carne é medida <b>SPS</b>. A banca considerou o "
                       "enquadramento genérico aceitável: o que decide é “instrumento não tarifário” e a "
                       "finalidade de proteção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A proibição de entrada de carne bovina por razões sanitárias é exemplo de barreira tarifária "
            "ad valorem.”</i> → ERRADO (troca de conceito: não incide sobre o preço)",
            "<i>“Pelo Acordo SPS, medidas sanitárias dispensam fundamentação científica quando visam à defesa "
            "da saúde.”</i> → ERRADO (exige base científica)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["típico"], "dificuldade": 1,
        "comentario_fonte": ("Proibir carne bovina de determinada origem é medida não tarifária ligada a requisitos "
                             "técnicos/sanitários; enquadra-se como TBT e, mais precisamente, SPS quando o motivo "
                             "é risco à saúde."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0943-1 (medidas sanitárias e fitossanitárias como barreira não "
                    "tarifária)"],
    },
    # ------------------------------------------------------------------ E2-L00185
    {
        "id": "ECO-E2-L00185-1", "fonte_ref": "E2-L00185", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_1,
        "rotulo_item": "Item",
        "assertiva": ("O subsídio à exportação eleva o excedente do produtor à custa da redução do excedente do "
                      "consumidor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O subsídio à exportação <u>eleva</u> o excedente do produtor à custa da <u>redução</u> do "
                      "excedente do consumidor."),
        "poucas": ("O subsídio faz a venda externa render Pm + s; o produtor só vende internamente a esse preço, "
                   "e o " + vd("preço doméstico sobe") + ": o " + azb("produtor ganha") + ", o "
                   + azb("consumidor perde") + " (e o governo paga a conta)."),
        "destrinchando": [
            "Mecanismo (país pequeno): com subsídio s por unidade exportada, o preço interno sobe de Pm para "
            + vd("Pm + s") + ". Produção ↑, consumo doméstico ↓, exportações ↑.",
            "Contabilidade de bem-estar: consumidores perdem a faixa entre os preços à esquerda da demanda; "
            "produtores ganham a faixa à esquerda da oferta (maior que a perda dos consumidores); o governo "
            "gasta s × exportações. " + azb("Resultado líquido negativo") + ": o custo fiscal supera o ganho "
            "líquido privado, deixando dois triângulos de " + azb("peso morto") + ".",
            "Logo, o ganho do produtor vem de <b>duas</b> fontes: parte é transferência do consumidor doméstico, "
            "parte vem do Tesouro. O item destaca a primeira, o que não o torna errado.",
            "País grande: as exportações maiores derrubam o preço mundial — perda adicional de termos de troca, "
            "em benefício dos consumidores estrangeiros.",
            vm("Regra-âncora: subsídio à exportação = espelho da tarifa de exportação — preço interno sobe, "
               "produtor ganha, consumidor e Tesouro perdem."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item é verdadeiro, ainda que incompleto (omite o custo "
                       "fiscal). O risco é confundir com o subsídio à <b>produção</b> em economia fechada, que "
                       "beneficia o consumidor. Pista: “à exportação” → o preço interno sobe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O subsídio à exportação eleva tanto o excedente do produtor quanto o do consumidor "
            "doméstico.”</i> → ERRADO (troca de conceito: isso vale para subsídio à produção em economia "
            "fechada)",
            "<i>“O ganho do produtor com o subsídio à exportação é integralmente custeado pelo consumidor "
            "doméstico.”</i> → ERRADO (modulador absoluto: parte é custo fiscal)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["à custa de"], "dificuldade": 1,
        "comentario_fonte": ("O subsídio eleva o preço recebido pelo produtor, incentiva a produção e desvia oferta "
                             "do mercado interno, pressionando o preço doméstico para cima: aumenta o excedente do "
                             "produtor e reduz o do consumidor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: na fonte, “excedente do produto” (erro evidente de digitação por “produtor”)",
                    "quase_duplicata: ECO-E1-0951-1, ECO-E2-L00201-1 (subsídio à exportação e excedente do "
                    "consumidor)"],
    },
    # ------------------------------------------------------------------ E2-L00186
    {
        "id": "ECO-E2-L00186-1", "fonte_ref": "E2-L00186", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_1,
        "rotulo_item": "Item",
        "assertiva": ("Ceteris paribus, o efeito de uma tarifa aplicada ao comércio tende a ter um efeito mais "
                      "intenso no longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Ceteris paribus, o efeito de uma tarifa aplicada ao comércio tende a ter um efeito mais "
                       "intenso no ") + vm("longo") + az(" prazo.")),
        "poucas": ("O efeito da tarifa sobre o saldo comercial é mais forte no " + azb("curto prazo") + ": com o "
                   "tempo, a " + azb("apreciação cambial") + " que ela provoca barateia as demais importações e "
                   "encarece as exportações, anulando o ganho."),
        "destrinchando": [
            "Curto prazo: a tarifa encarece o importado, as importações caem e o saldo comercial melhora; há "
            "menos demanda por moeda estrangeira (ou mais oferta líquida de divisas).",
            "Ajuste: com câmbio flexível, a moeda nacional se " + azb("valoriza") + ". Os demais importados "
            "ficam mais baratos e os exportadores perdem competitividade — o saldo volta ao nível determinado "
            "por " + vd("S − I") + ", que a tarifa não alterou.",
            "Longo prazo: sobra só a mudança de <b>composição</b> (mais produção do bem protegido, menos dos "
            "exportáveis) e a perda de eficiência; o efeito sobre o saldo se dissipa.",
            "Com câmbio fixo, o Banco Central impede a apreciação e o efeito pode persistir — por isso o "
            "<i>ceteris paribus</i> do item é lido, na tradição de prova, com câmbio flexível.",
        ],
        "dissecando": (cz("[inversão]") + " Troca curto por longo prazo. Leitura esperada: efeito sobre o saldo "
                       "externo, neutralizado pelo câmbio. Atenção: numa leitura microeconômica (elasticidades "
                       "maiores no longo prazo), o efeito sobre <b>quantidades</b> do bem protegido poderia "
                       "crescer; o gabarito pressupõe a leitura macroeconômica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio flexível, os efeitos de uma tarifa sobre a balança comercial tendem a ser anulados no "
            "longo prazo pela apreciação cambial.”</i> → CERTO",
            "<i>“A tarifa deprecia a moeda nacional e, assim, reforça seu efeito sobre a balança no longo "
            "prazo.”</i> → ERRADO (inversão: a moeda se aprecia)",
        ])],
        "reescrita": ("Ceteris paribus, o efeito de uma tarifa aplicada ao comércio tende a ter um efeito mais "
                      "intenso no " + hl("curto") + " prazo."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a", "ceteris paribus"], "dificuldade": 2,
        "comentario_fonte": ("No curto prazo, as tarifas preservam reservas, as divisas ficam abundantes e a moeda "
                             "nacional se valoriza; no longo prazo, a valorização torna as importações competitivas "
                             "e anula o efeito tarifário."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0933-1, ECO-E1-0909-1 (tarifa neutralizada pelo câmbio no longo "
                    "prazo)"],
    },
    # ------------------------------------------------------------------ E2-L00199
    {
        "id": "ECO-E2-L00199-1", "fonte_ref": "E2-L00199", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_5,
        "rotulo_item": "Item",
        "assertiva": ("A adoção de cotas de importação aumenta o bem-estar nacional, ao passo que a adoção de uma "
                      "tarifa específica sobre importações aumenta o excedente do consumidor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção de cotas de importação ") + vm("aumenta") + az(" o bem-estar nacional, ao passo "
                    "que a adoção de uma tarifa específica sobre importações ") + vm("aumenta") + az(" o "
                    "excedente do consumidor.")),
        "poucas": ("Em país pequeno, a cota " + azb("reduz") + " o bem-estar nacional (peso morto, e a renda de "
                   "cota pode ir para fora), e a tarifa " + azb("reduz") + " o excedente do consumidor (preço "
                   "interno maior)."),
        "destrinchando": [
            "Tarifa específica (valor fixo por unidade, ex.: R$ 5/kg): o preço interno sobe em t; o consumidor "
            "compra menos e paga mais — " + vd("excedente do consumidor ↓") + ". Quem ganha: produtor doméstico "
            "e governo (receita).",
            "Cota: limita a quantidade importada e eleva o preço interno. Consumidor perde, produtor ganha, há "
            "os mesmos dois triângulos de " + azb("peso morto") + " da tarifa equivalente, e o retângulo vira "
            + azb("renda de cota") + ". Bem-estar nacional: cai pelo peso morto; cai ainda mais se a renda for "
            "para estrangeiros (restrição voluntária de exportação).",
            "Única exceção teórica: país grande, em que a restrição derruba o preço mundial e o ganho de "
            "termos de troca supera o peso morto. O item não oferece essa condição.",
            vm("Regra-âncora: proteção (tarifa ou cota) → consumidor sempre perde; produtor ganha; bem-estar "
               "nacional cai no país pequeno."),
        ],
        "dissecando": (cz("[inversão]") + " Dois sinais invertidos, um em cada oração. O item não tem parte "
                       "verdadeira: basta lembrar que toda proteção encarece o bem para o consumidor e gera "
                       "peso morto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A adoção de cotas de importação reduz o bem-estar nacional, e a de uma tarifa específica reduz "
            "o excedente do consumidor.”</i> → CERTO",
            "<i>“A tarifa específica, por ser fixa por unidade, não afeta o preço interno do bem.”</i> → ERRADO "
            "(eleva o preço interno em t)",
        ])],
        "reescrita": ("A adoção de cotas de importação " + hl("reduz") + " o bem-estar nacional, ao passo que a "
                      "adoção de uma tarifa específica sobre importações " + hl("reduz") + " o excedente do "
                      "consumidor."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Cotas tendem a reduzir o bem-estar e podem transferir renda via renda de cota; a "
                             "tarifa específica eleva o preço doméstico e reduz o excedente do consumidor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00200
    {
        "id": "ECO-E2-L00200-1", "fonte_ref": "E2-L00200", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_5,
        "rotulo_item": "Item",
        "assertiva": ("Uma tarifa específica sobre importações reduz o excedente do produtor, ao passo que a adoção "
                      "de cotas de importação aumenta esse excedente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma tarifa específica sobre importações ") + vm("reduz") + az(" o excedente do produtor, ")
                    + vm("ao passo que") + az(" a adoção de cotas de importação aumenta esse excedente.")),
        "poucas": ("Tarifa e cota " + azb("elevam") + " o excedente do produtor doméstico — ambas sobem o preço "
                   "interno. O item inverte o efeito da tarifa e cria um contraste que não existe."),
        "destrinchando": [
            "Com a tarifa, o preço interno sobe de Pm para " + vd("Pm + t") + "; o produtor doméstico vende mais "
            "e a preço maior: seu excedente cresce pela faixa entre os dois preços, à esquerda da oferta.",
            "Com a cota, o mecanismo é o mesmo por outro caminho: a quantidade importada é travada, o preço "
            "interno sobe e o produtor ganha a mesma faixa (se a cota for equivalente à tarifa).",
            "A diferença entre os instrumentos não está no produtor nem no consumidor, mas no retângulo: "
            + azb("receita") + " (tarifa) × " + azb("renda de cota") + " (cota).",
            "Proteção é, por definição, transferência do consumidor para o produtor doméstico — é por isso que "
            "setores organizados fazem lobby por ela (" + oc("Olson") + ", lógica da ação coletiva: ganhos "
            "concentrados, perdas difusas).",
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " A 2ª oração é verdadeira (cota eleva o excedente do "
                       "produtor); o erro está na 1ª, e o “ao passo que” fabrica uma oposição inexistente. 🔥 "
                       "Itens em par tarifa × cota quase sempre testam se o candidato sabe que os efeitos sobre "
                       "excedentes são iguais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tanto a tarifa quanto a cota de importação elevam o excedente do produtor doméstico.”</i> → "
            "CERTO",
            "<i>“A tarifa eleva o excedente do produtor, e a cota, por gerar renda de cota, reduz esse "
            "excedente.”</i> → ERRADO (nexo indevido: a renda de cota não sai do produtor)",
        ])],
        "reescrita": ("Uma tarifa específica sobre importações " + hl("aumenta") + " o excedente do produtor, "
                      + hl("assim como") + " a adoção de cotas de importação aumenta esse excedente."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["ao passo que"], "dificuldade": 1,
        "comentario_fonte": ("A tarifa específica aumenta o excedente do produtor e reduz o do consumidor; cotas "
                             "também elevam o preço interno e o excedente do produtor; a assertiva inverte o efeito "
                             "tarifário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0937-1 (tarifa eleva o excedente do produtor)"],
    },
    # ------------------------------------------------------------------ E2-L00201
    {
        "id": "ECO-E2-L00201-1", "fonte_ref": "E2-L00201", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_5,
        "rotulo_item": "Item",
        "assertiva": ("Uma tarifa específica sobre importações reduz o excedente do consumidor, ao passo que a "
                      "adoção de um subsídio à exportação também diminui esse excedente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma tarifa específica sobre importações <u>reduz</u> o excedente do consumidor, ao passo que "
                      "a adoção de um subsídio à exportação <u>também diminui</u> esse excedente."),
        "poucas": ("Os dois instrumentos " + vd("elevam o preço interno") + ": a tarifa encarece o importado; o "
                   "subsídio desvia oferta para fora. Em ambos, o " + azb("consumidor doméstico perde") + "."),
        "destrinchando": [
            azb("Tarifa de importação") + " (país importador): preço interno sobe a Pm + t → consumo cai → "
            "excedente do consumidor ↓; produtor e governo ganham; peso morto.",
            azb("Subsídio à exportação") + " (país exportador): o produtor só vende internamente se receber "
            "Pm + s → preço interno sobe → consumo cai → excedente do consumidor ↓; produtor ganha; governo "
            "<b>gasta</b>; peso morto.",
            "Simetria útil: tarifa de importação e subsídio à exportação favorecem o produtor doméstico e "
            "prejudicam o consumidor; tarifa de exportação e subsídio à importação fazem o oposto.",
            "Diferença fiscal: a tarifa arrecada; o subsídio custa ao Tesouro — por isso o subsídio à "
            "exportação gera perda nacional maior por real de proteção, e a OMC o proíbe para bens industriais "
            "(Acordo SMC) e, desde " + vd("2015") + ", para agrícolas.",
            vm("Regra-âncora: tudo o que eleva o preço interno (tarifa de importação, subsídio à exportação, "
               "cota) reduz o excedente do consumidor."),
        ],
        "dissecando": (cz("[literalidade]") + " O “ao passo que” sugere contraste, mas o item o neutraliza com "
                       "“também” — os dois efeitos têm o mesmo sinal. Quem confunde subsídio à exportação com "
                       "subsídio à produção (que barateia o bem) marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O subsídio à exportação, ao contrário da tarifa de importação, eleva o excedente do consumidor "
            "doméstico.”</i> → ERRADO (inversão: também o reduz)",
            "<i>“A tarifa de exportação reduz o preço interno e eleva o excedente do consumidor doméstico.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["também"], "dificuldade": 1,
        "comentario_fonte": ("A tarifa específica eleva o preço doméstico e reduz o excedente do consumidor; o "
                             "subsídio à exportação desloca oferta para o exterior e eleva o preço doméstico, "
                             "reduzindo também o excedente do consumidor, com ganho do produtor e custo fiscal."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0951-1, ECO-E2-L00185-1 (subsídio à exportação reduz o excedente do "
                    "consumidor)"],
    },
]
