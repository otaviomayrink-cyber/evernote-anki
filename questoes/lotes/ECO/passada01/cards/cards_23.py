"""Cards da passada 01 de ECO — lote de redação 23 (notas 10, 11 e 12: oligopólios, jogos e falhas de mercado)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "cb": "🧮 Cournot e Bertrand",
    "stack": "🥇 Stackelberg e liderança",
    "cartel": "🤝 Cartel e conluio",
    "conc": "📏 Concentração e outras teorias",
    "nash": "♟️ Equilíbrio de Nash e dominância",
    "seq": "🔁 Jogos sequenciais e repetidos",
    "ext": "🌫️ Externalidades e Coase",
    "bp": "🏞️ Bens públicos e comuns",
}

CMD_RT = "Sobre as diferentes estruturas de mercado, julgue as afirmações a seguir."
CMD_TJPA_ESTR = ("No que se refere a estruturas de mercado, cadeias e redes produtivas, competitividade e "
                 "estratégia empresarial, julgue os itens seguintes.")
CMD_NIDI_JUN = ("A partir dos conceitos e das teorias usuais de concorrência perfeita, monopólio e oligopólio, "
                "julgue (C ou E) os itens que se seguem.")
CMD_NIDI_ESTR = ("Considerando as diversas estruturas de mercado, suas semelhanças e diferenças, julgue (C ou E) os "
                 "itens a seguir.")
CMD_JB_OUT = ("A teoria dos mercados estuda como os agentes econômicos interagem em diferentes estruturas de "
              "mercado [...]. Considerando a relação entre o Estado e diferentes estruturas de mercado existente "
              "numa economia mista, julgue certo ou errado (C ou E) as assertivas a seguir.")
CMD_COASE = "Com base nos trechos a seguir, julgue o item."
EXCERTO_COASE_1 = (
    "<p><i>Trecho 1: Caso Cooke versus Forbes. Um dos processos na tecelagem de tapetes de fibra de cacau [Cooke] "
    "era imergi-lo em um líquido alvejante e, depois, pendurá-lo para secagem. Vapores de um produtor de sulfato "
    "de amônia [Forbes] tinham o efeito de transformar a cor brilhosa do tapete em uma cor escurecida e fosca. (…) "
    "Uma ação foi ajuizada para impedir a manufatura de emitir tais vapores. Os advogados do réu argumentaram que, "
    "se o autor “não usasse um líquido alvejante específico, as fibras não seriam afetadas; que seu método de "
    "produção era atípico, contrário ao costume do comércio (…)”. O juiz explanou: “parece-me claro que uma pessoa "
    "tem o direito de, na sua propriedade, realizar um processo de manufatura em que se usa cloreto de estanho, ou "
    "qualquer outro tipo de corante metálico, e que seu vizinho não tem a liberdade para inundar o ambiente com gás "
    "que vai interferir na sua manufatura. Se isto pode ser imputado ao seu vizinho, então, compreendo eu, "
    "claramente ele terá o direito de vir aqui e pedir ajuda”.</i></p>")
EXCERTO_COASE_2 = (
    "<p><i>Trecho 2: (…) Com efeito, as propostas de solução do problema da poluição causada pela fumaça, bem como "
    "de outros problemas similares, feitas por meio da tributação, se sustenta com dificuldades advindas dos "
    "problemas relativos ao cálculo, da diferença entre dano médio e dano marginal e das inter-relações entre os "
    "danos causados a diversas propriedades etc.</i></p>"
    '<p><span style="color: rgb(160, 160, 160);">R. H. Coase. O problema do custo social. In: Journal of Law and '
    "Economics. 1960 (traduzido e adaptado).</span></p>")
ALERTA_2023 = ("banca_provavel: não confirmada — a fonte só traz o ano (2023); a classificação sugere prova do "
               "CACD, sem confirmação")
CMD_SEMI = "Julgue o item a seguir, relativo à classificação dos bens públicos, semipúblicos e meritórios."
CMD_FALHAS = "Julgue o item a seguir, relativo às falhas de mercado e à classificação dos bens."

ALERTA_E1_CACD = ("banca_provavel: CEBRASPE (estilo e ano compatíveis com a prova do CACD; a fonte só traz o ano, "
                  "sem órgão) — não confirmada")

CARDS = [
    # ------------------------------------------------------------------ E2-L00868
    {
        "id": "ECO-E2-L00868-1", "fonte_ref": "E2-L00868", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação às estruturas de mercado, julgue (C ou E) os itens que se seguem.",
        "rotulo_item": "Item",
        "assertiva": ("Todo cartel é estável a longo prazo devido aos ganhos superiores de todas as empresas que "
                      "dele fazem parte."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Todo cartel é estável") + az(" a longo prazo ") + vm("devido") + az(" aos ganhos "
                    "superiores de todas as empresas que dele fazem parte.")),
        "poucas": ("O cartel é " + azb("intrinsecamente instável") + ": o lucro conjunto é maior, mas cada membro "
                   "ganha ainda mais se <b>trair</b> o acordo sozinho (produzir acima da cota ou cortar preço)."),
        "destrinchando": [
            azb("Cartel") + " = acordo, explícito ou tácito, entre concorrentes para fixar preços, cotas de "
            "produção ou dividir mercados. Na prática, as empresas tentam agir como um " + azb("monopolista "
            "multiplanta") + ": restringem a quantidade e elevam o preço até perto do de monopólio.",
            "O ganho conjunto existe — é o que motiva o acordo. O problema é individual: ao preço alto do cartel, "
            "cada firma tem RMg individual > CMg; vender uma unidade a mais (ou dar um desconto discreto) eleva o "
            "<b>seu</b> lucro à custa dos demais. É a estrutura do " + azb("dilema dos prisioneiros") + ": "
            "trair é a estratégia dominante no jogo de uma rodada.",
            "Por isso a teoria parte da hipótese de " + vm("instabilidade") + ": para durar, o cartel precisa "
            "<b>detectar</b> e <b>punir</b> a trapaça. Condições que ajudam: poucas firmas e alta concentração; "
            "barreiras à entrada; produto e custos homogêneos; demanda inelástica e estável; interação repetida "
            "com ameaça crível de retaliação; preços transparentes.",
            "Exemplo clássico: a " + azb("OPEP") + ", cujas cotas são frequentemente descumpridas por membros que "
            "produzem acima do combinado. No " + rx("Brasil") + ", cartel é infração à ordem econômica (Lei "
            "12.529/2011) e crime (Lei 8.137/1990), investigado pelo " + rx("CADE") + ".",
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " O “todo” e o “estável a longo prazo” "
                       "transformam a exceção (cartéis duradouros) em regra; e o nexo “devido aos ganhos "
                       "superiores” ignora que é justamente o ganho de trair que desestabiliza. Pista: cartel + "
                       "“estável” quase sempre é armadilha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Mesmo que o lucro conjunto do cartel supere o da competição, cada membro tem incentivo "
            "individual a expandir a produção além da cota.”</i> → CERTO",
            "<i>“A estabilidade de um cartel é favorecida por demanda muito elástica.”</i> → ERRADO (inversão: "
            "favorece-a a demanda inelástica)",
        ])],
        "reescrita": (hl("Um cartel tende a ser instável") + " a longo prazo, " + hl("apesar") + " dos ganhos "
                      "superiores de todas as empresas que dele fazem parte" + hl(", porque cada uma ganha ainda "
                      "mais traindo o acordo") + "."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["todo"], "dificuldade": 1,
        "comentario_fonte": ("Definição de cartel (acordos para mimetizar o monopólio); a teoria supõe "
                             "instabilidade pelo incentivo a burlar; lista de fatores que favorecem cartéis."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00994
    {
        "id": "ECO-E2-L00994-1", "fonte_ref": "E2-L00994", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Em relação à microeconomia, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("A promoção da concorrência por meio da regulação se justifica em mercados contestáveis, em que "
                      "a probabilidade de entrada de novas empresas que possam competir em igualdade de condições é "
                      "reduzida."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A promoção da concorrência por meio da regulação ") + vm("se justifica") + az(" em mercados "
                    "contestáveis, em que a probabilidade de entrada de novas empresas que possam competir em "
                    "igualdade de condições é ") + vm("reduzida") + az(".")),
        "poucas": ("Mercado " + azb("contestável") + " é justamente aquele em que a entrada (e a saída) é livre e "
                   "sem custo: a ameaça de entrantes disciplina os incumbentes, e a regulação para promover "
                   "concorrência se torna <b>desnecessária</b>."),
        "destrinchando": [
            "A " + azb("teoria dos mercados contestáveis") + " é de " + oc("Baumol, Panzar e Willig") + " (1982). "
            "Tese: o que disciplina preços não é o <b>número</b> de firmas, mas a <b>ameaça de entrada</b>. "
            "Mesmo um monopolista cobra preço próximo do custo médio se qualquer lucro extraordinário atrair um "
            "entrante instantâneo (estratégia <i>hit and run</i>, “bater e correr”).",
            "Condições do mercado perfeitamente contestável: entrantes com acesso à mesma tecnologia e custos; "
            "ausência de barreiras à entrada; " + azb("custos irrecuperáveis (sunk costs) nulos") + ", de modo que "
            "sair não custa nada; incumbente incapaz de reagir antes que o entrante lucre.",
            "Consequência normativa: em mercado contestável, a estrutura concentrada não é, por si, problema — "
            "a política pública deve <b>remover barreiras</b> (licenças, custos afundados), não fixar preços ou "
            "multiplicar firmas. Exemplo de livro: rotas aéreas, em que o avião (ativo móvel) pode ser realocado "
            "de rota.",
            "O item inverte a definição: mercado com entrada <b>difícil</b> é o oposto do contestável. Ali, sim, "
            "a regulação ou a defesa da concorrência podem se justificar.",
            vm("Regra-âncora: contestável = entrada e saída livres e sem custo → a concorrência potencial basta."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O item cola no rótulo “contestável” a "
                       "característica do mercado <b>não</b> contestável (entrada improvável) e tira a conclusão "
                       "regulatória correspondente a este último. Pista: “contestável” vem de “contestar” — o "
                       "mercado pode ser disputado a qualquer momento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em mercados perfeitamente contestáveis, mesmo um monopolista tende a cobrar preço próximo do custo "
            "médio.”</i> → CERTO",
            "<i>“A contestabilidade de um mercado aumenta com os custos irrecuperáveis exigidos dos "
            "entrantes.”</i> → ERRADO (inversão: custos afundados reduzem a contestabilidade)",
        ])],
        "reescrita": ("A promoção da concorrência por meio da regulação " + hl("não") + " se justifica em mercados "
                      "contestáveis, em que a probabilidade de entrada de novas empresas que possam competir em "
                      "igualdade de condições é " + hl("elevada") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Teoria dos mercados contestáveis (Baumol): estruturas concentradas se comportam "
                             "competitivamente quando há poucas barreiras à entrada e à saída; a competição "
                             "potencial disciplina a conduta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01199
    {
        "id": "ECO-E2-L01199-1", "fonte_ref": "E2-L01199", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Quanto às estruturas de mercado, julgue (C ou E) os itens subsequentes.",
        "rotulo_item": "Item",
        "assertiva": ("Um oligopólio é um tipo de concorrência estável, em que os concorrentes cooperam para manter "
                      "os preços elevados por meio de restrições à quantidade produzida para o mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um oligopólio é um tipo de concorrência ") + vm("estável, em que os concorrentes cooperam")
                    + az(" para manter os preços elevados por meio de restrições à quantidade produzida para o "
                         "mercado.")),
        "poucas": ("O item descreve um <b>cartel bem-sucedido</b>, não o oligopólio em geral. O oligopólio é "
                   "marcado pela " + azb("tensão entre cooperação e interesse próprio") + ": coludir rende mais, "
                   "mas cada firma tem incentivo a trair."),
        "destrinchando": [
            azb("Oligopólio") + " = poucas firmas, com " + azb("interdependência estratégica") + ": o lucro de "
            "cada uma depende do que as rivais fazem. Daí a teoria dos jogos ser a ferramenta natural.",
            "Dois desfechos possíveis: (1) " + azb("colusão") + " — as firmas agem como um monopolista, restringem "
            "a quantidade e repartem o lucro de monopólio; (2) " + azb("comportamento não cooperativo") + " — "
            "Cournot (quantidades), Bertrand (preços), Stackelberg (líder e seguidora), com lucros menores.",
            "A colusão é instável: ao preço alto, cada firma ganha produzindo além da cota. É o "
            + azb("dilema dos prisioneiros") + " — o equilíbrio de Nash do jogo de uma rodada é trair, embora "
            "ambas prefiram cooperar.",
            "Logo, “cooperar para manter preços elevados” é uma <b>possibilidade</b> dentro do oligopólio, não a "
            "sua definição; e “estável” é exatamente o que essa cooperação costuma não ser.",
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " Define o gênero (oligopólio) pela "
                       "espécie (cartel) e ainda lhe atribui estabilidade. Pista: a definição de oligopólio não "
                       "precisa de cooperação — só de poucas firmas interdependentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No oligopólio, há incentivo à colusão, mas também incentivo individual a desviar do "
            "acordo.”</i> → CERTO",
            "<i>“No oligopólio de Bertrand com produto homogêneo, as firmas cooperam e mantêm o preço de "
            "monopólio.”</i> → ERRADO (troca de modelo: em Bertrand o preço cai ao custo marginal)",
        ])],
        "reescrita": ("Um oligopólio é um tipo de concorrência " + hl("instável, em que os concorrentes podem "
                      "cooperar") + " para manter os preços elevados por meio de restrições à quantidade "
                      "produzida para o mercado" + hl(", mas cada um tem incentivo a trair o acordo") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Tensão entre cooperação e interesse próprio; colusão bem-sucedida ou trapaça; o "
                             "oligopólio não é um tipo de concorrência estável."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01202
    {
        "id": "ECO-E2-L01202-1", "fonte_ref": "E2-L01202", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Quanto às estruturas de mercado, julgue (C ou E) os itens subsequentes.",
        "rotulo_item": "Item",
        "assertiva": "Um cartel tende a ser duradouro se a demanda pelo seu produto for expressa por uma curva horizontal.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um cartel tende a ser ") + vm("duradouro") + az(" se a demanda pelo seu produto for expressa "
                                                                        "por uma curva horizontal.")),
        "poucas": ("Demanda horizontal = " + azb("perfeitamente elástica") + ": qualquer aumento de preço zera as "
                   "vendas. O cartel não tem poder de mercado para explorar — e tende a <b>não</b> durar."),
        "destrinchando": [
            "O objetivo do cartel é subir o preço acima do custo marginal restringindo a quantidade. Isso só "
            "compensa se a quantidade cair pouco quando o preço sobe, isto é, se a demanda for "
            + azb("inelástica") + ".",
            "Com demanda horizontal (ε → ∞), o mercado só aceita um preço; cobrar um centavo a mais faz os "
            "compradores migrarem para substitutos. O lucro extra do cartel é nulo, e não há o que repartir.",
            "Pelo índice de " + oc("Lerner") + ", (P − CMg)/P = 1/|ε|: com |ε| infinita, a margem possível é "
            + vd("zero") + ". Quanto menos elástica a demanda, maior o poder de mercado que o cartel pode exercer.",
            "Em " + oc("Pindyck e Rubinfeld") + ", o sucesso do cartel pede duas condições: organização estável "
            "(membros que cumprem o acordo) e " + azb("potencial de poder de monopólio") + " — demanda total "
            "pouco elástica e controle da maior parte da oferta (ou oferta de fora do cartel inelástica). É o "
            "contraste clássico entre a OPEP dos anos 1970 (petróleo, demanda inelástica no curto prazo) e o "
            "fracassado cartel do cobre (CIPEC).",
        ],
        "dissecando": (cz("[inversão]") + " Troca a condição favorável (demanda inelástica, curva íngreme) pela "
                       "mais desfavorável possível (curva horizontal). Pista: “horizontal” em prova de micro é "
                       "sinônimo de concorrência perfeita — o oposto de poder de mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um cartel tende a ter mais sucesso quanto menos elástica for a demanda pelo seu produto.”</i> → "
            "CERTO",
            "<i>“Se a oferta dos produtores de fora do cartel for muito elástica, o cartel terá maior poder "
            "de mercado.”</i> → ERRADO (inversão: oferta externa elástica corrói o poder do cartel)",
        ])],
        "reescrita": ("Um cartel tende a " + hl("não") + " ser duradouro se a demanda pelo seu produto for expressa "
                      "por uma curva horizontal."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Demanda horizontal = infinitamente elástica; isso dificulta o cartel, que não tende "
                             "a ser duradouro."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01407
    {
        "id": "ECO-E2-L01407-1", "fonte_ref": "E2-L01407", "destino": "10", "subtema": H2["cartel"],
        "tipo": "DISC", "banca": "Intensivo MM", "prova": "Intensivo Pré-TPS/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Responda à questão a seguir, sobre os oligopólios.",
        "rotulo_item": "Questão",
        "assertiva": "Quando um oligopólio pode ter lucros de monopólio?",
        "gabarito": "RESPOSTA", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Quando as firmas coludem — formam um cartel, explícito ou tácito — e agem como um único "
                      "monopolista: escolhem a quantidade total em que a receita marginal do mercado iguala o custo "
                      "marginal, cobram o preço de monopólio e repartem o lucro. Para isso o acordo precisa ser "
                      "sustentável: poucas firmas, barreiras à entrada, demanda inelástica e meios de detectar e "
                      "punir quem trapaceia (interação repetida)."),
        "poucas": ("Só pela " + azb("colusão") + ": o lucro de monopólio é o teto do lucro conjunto, e o "
                   "oligopólio o alcança quando as firmas maximizam esse lucro juntas, como um monopolista "
                   "multiplanta."),
        "destrinchando": [
            "Lucro conjunto máximo = lucro de monopólio: escolher Q total com " + vd("RMg(Q) = CMg") + " e "
            "repartir a produção entre as plantas igualando os custos marginais. Qualquer outra configuração "
            "(Cournot, Stackelberg, Bertrand) dá lucro conjunto menor.",
            "Ordem dos resultados com produto homogêneo e custos iguais: lucro conjunto " + vd("cartel > "
            "Cournot > Bertrand = 0") + "; preço na ordem inversa da quantidade total.",
            "O obstáculo é o " + azb("incentivo a trair") + ": ao preço de monopólio, cada firma ganha produzindo "
            "um pouco mais. No jogo de uma rodada, a colusão desmorona (dilema dos prisioneiros).",
            "O que torna a colusão sustentável: jogo " + azb("repetido indefinidamente") + " com firmas pacientes "
            "e estratégias de gatilho (" + azb("teorema folk") + "); poucas firmas; barreiras à entrada; produto "
            "homogêneo e custos parecidos; preços observáveis; demanda inelástica e estável.",
            "Colusão tácita (sem acordo explícito, por " + azb("liderança ou sinalização de preços") + ") também "
            "pode aproximar o resultado de monopólio, mas costuma ser mais frágil.",
        ],
        "dissecando": (cz("[discursiva curta]") + " Em C/E, a banca transforma a pergunta em itens do tipo "
                       "“o equilíbrio de Cournot pode dar lucro maior que o cartel” (ERRADO) ou “o cartel é estável "
                       "porque todos ganham” (ERRADO: há incentivo a trair)."),
        "modulos": [("🃏 Carta na manga", [
            "Para o examinador, a resposta completa tem duas camadas: <b>o que</b> (colusão: agir como monopolista, "
            "RMg = CMg) e <b>como sustentar</b> (detecção + punição crível em jogo repetido). Citar o dilema dos "
            "prisioneiros e o teorema folk mostra domínio do tema."])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso sem texto: só uma imagem decorativa (dois personagens de mãos dadas).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 326", "tipo_fonte": "DECORATIVA", "lado": "verso", "acao": "cortada"}],
        "alertas": ["nota_redacao: resposta-modelo resolvida pelo redator (o verso da fonte tinha só uma imagem "
                    "decorativa)"],
    },
    # ------------------------------------------------------------------ E2-L01411
    {
        "id": "ECO-E2-L01411-1", "fonte_ref": "E2-L01411", "destino": "10", "subtema": H2["cartel"],
        "tipo": "ME", "banca": "CESGRANRIO", "prova": "IPEA/Técnico de Planejamento e Pesquisa/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": "Leia o enunciado a seguir e assinale a opção correta.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Questão",
        "assertiva": ("Dentre os principais fatores que favorecem a coordenação oligopolística que viabiliza a "
                      "formação de cartéis, estão"
                      "</p><p>(A) a presença de associações patronais; a presença de canais de distribuição "
                      "similares; a abrangência geográfica de mercados indefinida.</p>"
                      "<p>(B) a facilidade para detecção de desvios de conduta; a repetição sistemática da "
                      "interação entre firmas do cartel; a preferência por lucros imediatos em relação a lucros "
                      "futuros.</p>"
                      "<p>(C) a existência de produtos substitutos; os anúncios públicos de preços; as condições "
                      "estáveis da demanda.</p>"
                      "<p>(D) a existência de contatos entre rivais em outros mercados; os reduzidos diferenciais "
                      "de eficiência entre as empresas; o caráter crível da ameaça de punição ao desvio de "
                      "condutas.</p>"
                      "<p>(E) as barreiras estruturais à entrada; a homogeneidade de produto; a elevada "
                      "elasticidade-preço da demanda."),
        "gabarito": "D", "gabarito_origem": "fonte", "status": "normal",
        "anotada": ("❌ " + az("(A) a presença de associações patronais; a presença de canais de distribuição "
                               "similares; a abrangência geográfica de mercados ") + vm("indefinida")
                    + "</p><p>❌ " + az("(B) a facilidade para detecção de desvios de conduta; a repetição "
                                        "sistemática da interação entre firmas do cartel; a preferência por "
                                        "lucros ") + vm("imediatos em relação a lucros futuros")
                    + "</p><p>❌ " + az("(C) ") + vm("a existência de produtos substitutos") + az("; os anúncios "
                                        "públicos de preços; as condições estáveis da demanda")
                    + "</p><p>✅ " + az("(D) a existência de contatos entre rivais em outros mercados; os "
                                        "reduzidos diferenciais de eficiência entre as empresas; o caráter crível "
                                        "da ameaça de punição ao desvio de condutas")
                    + "</p><p>❌ " + az("(E) as barreiras estruturais à entrada; a homogeneidade de produto; a ")
                    + vm("elevada") + az(" elasticidade-preço da demanda")),
        "poucas": ("A única alternativa em que <b>os três</b> fatores favorecem a coordenação é a " + vd("D")
                   + ": contato multimercado, firmas de eficiência parecida e punição crível ao desvio. Nas "
                   "demais, ao menos um fator atrapalha o cartel."),
        "destrinchando": [
            "Teste para cada fator: ele facilita <b>chegar</b> a um acordo, <b>detectar</b> a trapaça ou "
            "<b>punir</b> quem trapaceia? Se sim, favorece a coordenação. Basta um fator contrário para "
            "eliminar a alternativa.",
            "(A) ❌ Associações patronais e canais de distribuição similares até facilitam contatos e "
            "monitoramento; mas um " + azb("mercado de contornos geográficos indefinidos") + " dificulta saber "
            "quem são os rivais e o que cada um cobra — atrapalha a coordenação.",
            "(B) ❌ Detecção fácil de desvios e interação repetida favorecem; mas a " + azb("preferência por "
            "lucros imediatos") + " (impaciência, desconto alto do futuro) é o que <b>destrói</b> o cartel: "
            "o ganho de trair hoje passa a valer mais que a punição de amanhã.",
            "(C) ❌ " + azb("Substitutos") + " elevam a elasticidade da demanda e limitam o preço do cartel. Já "
            "anúncios públicos de preços e demanda estável <b>favorecem</b> a coordenação (preço transparente "
            "e desvio fácil de detectar) — uma das resoluções da fonte dizia o contrário, por engano.",
            "(D) ✅ " + azb("Contato multimercado") + ": rivais que se encontram em vários mercados podem punir "
            "o desvio em qualquer um deles e se conhecem melhor. " + azb("Eficiências parecidas") + ": custos "
            "semelhantes facilitam acertar um preço comum (a firma de custo baixo não quer o preço da de custo "
            "alto). " + azb("Ameaça crível de punição") + ": é o que torna a cooperação um equilíbrio no jogo "
            "repetido.",
            "(E) ❌ Barreiras à entrada e produto homogêneo favorecem; " + vm("demanda elástica não") + ": "
            "com ela, subir o preço derruba as vendas e cada membro tem mais a ganhar cortando o preço.",
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Cada distrator mistura dois fatores verdadeiros com "
                       "um invertido (lucros <b>imediatos</b>, demanda <b>elástica</b>, existência de "
                       "<b>substitutos</b>). 🔥 Lista de fatores de cartel é tema recorrente — e o examinador "
                       "costuma esconder a inversão no último elemento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A preferência por lucros futuros em relação a lucros imediatos favorece a sustentação do "
            "cartel.”</i> → CERTO",
            "<i>“Grandes diferenças de eficiência entre as empresas facilitam a fixação de um preço "
            "comum.”</i> → ERRADO (inversão: dificultam)",
        ])],
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Gabarito D. Comentário de professor sobre favorecimento “direto” da formação de "
                             "cartéis, com análise de cada alternativa; resolução de IA que afirma, por engano, "
                             "que anúncios públicos de preços e demanda estável dificultam a coordenação; "
                             "observação de aluno sobre a demanda elástica na alternativa E."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 327", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído (alternativas a partir do verso)"},
                          {"ref": "IMAGEM 328-334", "tipo_fonte": "DIAGRAMA/TEXTO/GRÁFICO/MAPA/DECORATIVA",
                           "lado": "verso", "acao": "cortadas (conteúdo absorvido no 📖 ou decorativo)"}],
        "alertas": ["texto_reconstruido: frente era imagem descrita em uma linha; as cinco alternativas vêm "
                    "literalmente do comentário do verso, e o comando foi completado a partir de bancos de "
                    "questões — conferir a redação exata do enunciado com a IMAGEM 327",
                    "banca_confirmada: CESGRANRIO, Concurso Nacional Unificado 2024 (IPEA, Técnico de "
                    "Planejamento e Pesquisa), conforme bancos de questões",
                    "qualidade_fonte: uma das resoluções afirma que anúncios públicos de preços e demanda estável "
                    "dificultam a coordenação — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L01727
    {
        "id": "ECO-E2-L01727-1", "fonte_ref": "E2-L01727", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("Na teoria do duopólio, tanto o modelo de Cournot como o de Stackelberg caracterizam-se por "
                      "cada firma buscando maximizar seu lucro a partir da sua função de reação, com a diferença de "
                      "que o primeiro a determinação da quantidade é simultânea e, no segundo, há uma firma líder "
                      "que escolhe a quantidade primeiro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na teoria do duopólio, tanto o modelo de Cournot como o de Stackelberg caracterizam-se por "
                      "cada firma buscando maximizar seu lucro <u>a partir da sua função de reação</u>, com a "
                      "diferença de que o primeiro a determinação da quantidade é <u>simultânea</u> e, no "
                      "segundo, há uma firma líder que escolhe a quantidade <u>primeiro</u>."),
        "poucas": ("Ambos são duopólios em " + azb("quantidades") + " com funções de reação; Cournot é "
                   + vd("simultâneo") + ", Stackelberg é " + vd("sequencial") + " (a líder move primeiro, "
                   "antecipando a reação da seguidora)."),
        "destrinchando": [
            azb("Função de reação") + " (ou de melhor resposta): a quantidade que maximiza o lucro de uma firma "
            "para cada quantidade da rival. Com P = a − b(q₁ + q₂) e custo c: q₁ = (a − c − bq₂)/2b.",
            oc("Cournot") + " (1838): as duas escolhem ao mesmo tempo, cada uma tomando a quantidade da outra "
            "como dada. Equilíbrio = interseção das duas funções de reação, que é um " + azb("equilíbrio de "
            "Nash") + ". No caso linear simétrico, cada uma produz (a − c)/3b.",
            oc("Stackelberg") + " (1934): a líder escolhe primeiro, <b>incorporando</b> a função de reação da "
            "seguidora no seu problema; a seguidora observa e responde sobre a própria função de reação. "
            "Resultado linear: líder (a − c)/2b, seguidora (a − c)/4b — a líder produz e lucra mais que em "
            "Cournot (" + azb("vantagem do primeiro a jogar") + ").",
            "Comparação: quantidade total Stackelberg (3/4 da competitiva) > Cournot (2/3) > monopólio (1/2); "
            "o preço segue a ordem inversa.",
            "Rigor: em Stackelberg, a líder não está “sobre” a sua própria função de reação — ela escolhe um "
            "ponto da função de reação da seguidora. O item fala em maximizar “a partir da sua função de "
            "reação” num sentido amplo, e a banca o aceitou.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Reproduz a distinção de manual (simultâneo × "
                       "sequencial) em redação truncada (“o primeiro a determinação”), o que leva o candidato "
                       "a procurar erro onde não há. A variável de escolha (quantidade nos dois) está "
                       "correta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Stackelberg, a firma líder escolhe o preço, e a seguidora, a quantidade.”</i> → "
            "ERRADO (troca de variável: ambas escolhem quantidades)",
            "<i>“No modelo de Stackelberg, a líder obtém lucro maior que no equilíbrio de Cournot.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Ambos são modelos de competição por quantidade com funções de reação; Cournot "
                             "simultâneo (equilíbrio de Nash na interseção); Stackelberg com líder que antecipa a "
                             "reação da seguidora e lucra mais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01729
    {
        "id": "ECO-E2-L01729-1", "fonte_ref": "E2-L01729", "destino": "10", "subtema": H2["cb"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Bertrand é um modelo de duopólio caracterizado pela concorrência de preços com "
                      "produto homogêneo, sendo por isto caracterizado pelo preço cobrado pelas firmas acima do "
                      "custo marginal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de Bertrand é um modelo de duopólio caracterizado pela concorrência de preços com "
                       "produto homogêneo, sendo por isto caracterizado pelo preço cobrado pelas firmas ")
                    + vm("acima do") + az(" custo marginal.")),
        "poucas": ("No " + azb("paradoxo de Bertrand") + ", duas firmas com produto homogêneo e custos iguais "
                   "baixam o preço até " + vd("P = CMg") + ": resultado de concorrência perfeita, lucro econômico "
                   "zero."),
        "destrinchando": [
            "Hipóteses de " + oc("Bertrand") + " (1883): produto idêntico, firmas escolhem <b>preços</b> "
            "simultaneamente, consumidores compram tudo de quem cobra menos (empate divide o mercado), custo "
            "marginal constante e igual, capacidade ilimitada.",
            "Raciocínio: se a rival cobra P > CMg, cobrar P − ε captura o mercado inteiro e quase dobra o lucro. "
            "A rival faz o mesmo. A guerra de preços só para em " + vd("P₁ = P₂ = CMg") + " — único equilíbrio de "
            "Nash, pois ninguém ganha subindo (perde tudo) nem descendo (prejuízo).",
            "O “paradoxo”: bastam " + vd("duas") + " firmas para o resultado competitivo, ao contrário de "
            "Cournot, em que o preço fica acima do CMg e só converge a ele com muitas firmas.",
            "Como escapar do paradoxo (e então P > CMg): " + azb("produto diferenciado") + " (Bertrand com "
            "diferenciação); " + azb("restrição de capacidade") + " (" + oc("Kreps e Scheinkman") + ": escolher "
            "capacidade e depois preço reproduz Cournot); custos diferentes (a firma mais eficiente cobra um "
            "pouco abaixo do CMg da rival); jogo repetido com colusão.",
            vm("Regra-âncora: Bertrand + produto homogêneo + custos iguais → P = CMg, lucro zero."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A primeira parte (preços, produto homogêneo) é a "
                       "definição correta; o erro foi enxertado na conclusão, que importa o resultado de Cournot. "
                       "O “sendo por isto” é a pista: justamente por competir em preço com produto idêntico, o "
                       "preço cai ao custo marginal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Bertrand com produtos diferenciados, as firmas podem cobrar preços acima do custo "
            "marginal.”</i> → CERTO",
            "<i>“No modelo de Bertrand com produto homogêneo, o preço converge ao custo marginal apenas quando o "
            "número de firmas tende ao infinito.”</i> → ERRADO (troca de modelo: isso é Cournot; em Bertrand "
            "bastam duas)",
        ])],
        "reescrita": ("O modelo de Bertrand é um modelo de duopólio caracterizado pela concorrência de preços com "
                      "produto homogêneo, sendo por isto caracterizado pelo preço cobrado pelas firmas "
                      + hl("igual ao") + " custo marginal."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Paradoxo de Bertrand: competição em preços com produto homogêneo leva a P = CMg e "
                             "lucro zero; o trecho errado é “acima do custo marginal”."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00007
    {
        "id": "ECO-E3-L00007-1", "fonte_ref": "E3-L00007", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ-PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": "Acerca dos conceitos fundamentais de microeconomia, julgue os itens que se seguem.",
        "rotulo_item": "Item",
        "assertiva": ("A formação de grupos de produtores que atuam coletivamente, coordenando preços e níveis de "
                      "produção para maximizar o lucro em conjunto, promove maior eficiência econômica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A formação de grupos de produtores que atuam coletivamente, coordenando preços e níveis de "
                       "produção para maximizar o lucro em conjunto, promove ") + vm("maior") + az(" eficiência "
                                                                                                   "econômica.")),
        "poucas": ("O item descreve um " + azb("cartel") + ": ao agir como monopolista, ele restringe a produção "
                   "e eleva o preço acima do custo marginal, gerando " + azb("peso morto") + " — <b>menos</b> "
                   "eficiência, não mais."),
        "destrinchando": [
            "Eficiência alocativa exige " + vd("P = CMg") + ": produz-se cada unidade cujo valor para o "
            "consumidor (preço) supera o custo de produzi-la. É o resultado da concorrência perfeita.",
            "O cartel maximiza o lucro <b>conjunto</b>: escolhe a quantidade em que a receita marginal do mercado "
            "iguala o custo marginal (qm), menor que a competitiva (qc), e cobra pm > CMg.",
            "Efeitos de bem-estar: parte do excedente do consumidor vira lucro do cartel (" + azb("transferência")
            + ", não perda); e as trocas entre qm e qc, que valiam mais do que custavam, deixam de existir — o "
            + azb("peso morto") + ", perda líquida para a sociedade.",
            "Por isso o cartel é tratado como a infração mais grave ao direito da concorrência. No " + rx("Brasil")
            + ", é infração à ordem econômica (Lei 12.529/2011, art. 36) e crime (Lei 8.137/1990), com acordos "
            "de leniência conduzidos pelo " + rx("CADE") + ".",
            "Ressalva que não salva o item: alguns arranjos cooperativos entre empresas (joint ventures de P&amp;D, "
            "padronização) podem gerar eficiências; mas coordenar <b>preços e quantidades</b> para maximizar o "
            "lucro conjunto é o núcleo do cartel.",
        ],
        "grafico_verso": "ECO-E3-L00007-1-V1",
        "dissecando": (cz("[troca de conceito]") + " Confunde maximizar o <b>lucro</b> conjunto com maximizar o "
                       "<b>bem-estar</b>. A descrição do cartel é perfeita; só a conclusão foi invertida. "
                       "🔥 A CEBRASPE costuma descrever o cartel sem nomeá-lo, para testar se o candidato o "
                       "reconhece."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A formação de cartéis transfere excedente dos consumidores para os produtores e gera perda de "
            "peso morto.”</i> → CERTO",
            "<i>“O peso morto do cartel corresponde a todo o excedente perdido pelos consumidores.”</i> → ERRADO "
            "(parte é transferência para os produtores)",
        ])],
        "reescrita": ("A formação de grupos de produtores que atuam coletivamente, coordenando preços e níveis de "
                      "produção para maximizar o lucro em conjunto, promove " + hl("menor") + " eficiência "
                      "econômica."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Seis resoluções concordantes: a assertiva descreve um cartel, que reduz a produção, "
                             "eleva o preço acima do custo marginal e gera peso morto; combatido pelo direito "
                             "antitruste."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00020
    {
        "id": "ECO-E3-L00020-1", "fonte_ref": "E3-L00020", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ-PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA_ESTR,
        "rotulo_item": "Item",
        "assertiva": ("A integração vertical, ao eliminar o problema da dupla imposição de margens, é benéfica "
                      "tanto para os produtores como para os consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A integração vertical, <u>ao eliminar o problema da dupla imposição de margens</u>, é "
                      "benéfica <u>tanto para os produtores como para os consumidores</u>."),
        "poucas": ("Com poder de mercado em dois elos da cadeia, cada um aplica seu markup — a " + azb("dupla "
                   "marginalização") + ". Integrados, cobram uma margem só: o " + vd("preço final cai") + " e o "
                   + vd("lucro conjunto sobe") + "."),
        "destrinchando": [
            "Cenário: um fabricante monopolista vende o insumo a um varejista também monopolista. O fabricante "
            "cobra do varejista um preço acima do seu custo marginal; o varejista trata esse preço como custo e "
            "aplica <b>outra</b> margem sobre ele. O preço final fica acima até do preço de um monopolista "
            "integrado.",
            "Por quê: cada elo ignora que a sua margem reduz as vendas — e o lucro — do outro (uma "
            + azb("externalidade vertical") + "). A firma integrada internaliza esse efeito e escolhe o preço "
            "de monopólio uma vez só.",
            "Resultado (análise de " + oc("Spengler") + ", 1950): preço menor, quantidade maior, lucro conjunto "
            "maior e excedente do consumidor maior — um raro caso de " + vd("ganha-ganha") + " entre empresa e "
            "consumidor.",
            "Alternativas contratuais que fazem o mesmo sem fusão: tarifa em duas partes (o fabricante vende ao "
            "custo marginal e cobra uma taxa fixa), franquia, preço de revenda máximo.",
            "Contrapeso que a defesa da concorrência analisa: a integração vertical também pode gerar "
            + azb("fechamento de mercado") + " (<i>foreclosure</i>), ao negar insumo ou acesso a rivais. A "
            "afirmação do item vale <b>na lógica da dupla margem</b>, que é o que ela explicita.",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Parece exagerado dizer que uma concentração "
                       "beneficia “tanto” produtores “como” consumidores, mas é o resultado-padrão do modelo. O "
                       "item se protege com a oração causal: o benefício decorre de eliminar a dupla margem, não "
                       "da integração em qualquer circunstância."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A integração vertical, ao eliminar a dupla marginalização, eleva o preço final ao "
            "consumidor.”</i> → ERRADO (inversão: o preço cai)",
            "<i>“A integração vertical pode prejudicar a concorrência ao dificultar o acesso de rivais a insumos "
            "essenciais.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Seis resoluções concordantes: a dupla marginalização ocorre com poder de mercado em "
                             "elos sucessivos; a integração internaliza a margem, reduz o preço e eleva o lucro "
                             "conjunto; uma delas lembra o risco de fechamento de mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00104
    {
        "id": "ECO-E3-L00104-1", "fonte_ref": "E3-L00104", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUN,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de oligopólio com empresa líder, o preço de equilíbrio que vigora no mercado é "
                      "aquele que maximiza os lucros da empresa dominante. Subtraindo da demanda total de mercado a "
                      "quantidade ofertada por esta empresa, encontra-se a quantidade que é abastecida pelo "
                      "conjunto de todas as empresas seguidoras."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de oligopólio com empresa líder, o preço de equilíbrio que vigora no mercado é "
                      "aquele que <u>maximiza os lucros da empresa dominante</u>. Subtraindo da demanda total de "
                      "mercado a quantidade ofertada por esta empresa, encontra-se a quantidade que é abastecida "
                      "pelo conjunto de todas as empresas seguidoras."),
        "poucas": ("No " + azb("modelo da empresa dominante") + ", a líder fixa o preço que maximiza o seu lucro "
                   "sobre a " + azb("demanda residual") + "; a esse preço, a franja competitiva supre o que "
                   "falta: " + vd("Q mercado = Q líder + Q franja") + "."),
        "destrinchando": [
            "Estrutura: uma firma grande (custos menores ou maior escala) e muitas pequenas, a " + azb("franja "
            "competitiva") + ", que agem como tomadoras de preço e ofertam onde P = CMg delas.",
            "Passo 1 — a líder calcula a sua " + azb("demanda residual") + ": a cada preço, demanda de mercado "
            "menos a oferta da franja. Passo 2 — age como monopolista sobre ela: " + vd("RMg residual = CMg "
            "líder") + ", o que dá Q líder e, na demanda residual, o preço P*. Passo 3 — ao preço P*, a franja "
            "oferta a sua parte, e a soma iguala a demanda de mercado.",
            "Exemplo numérico do gráfico: mercado Q = 120 − 10p, franja Qf = 2p, CMg da líder = 4. Residual: "
            "Q = 120 − 12p; RMg = 4 → " + vd("Q líder = 36, P* = 7") + "; mercado demanda " + vd("50")
            + "; a franja supre " + vd("14") + " (= 50 − 36), exatamente o que diz o item.",
            "Não confundir com " + oc("Stackelberg") + " em quantidades (duopólio, líder antecipa a função de "
            "reação da seguidora): aqui a variável é o preço e a franja não tem poder de mercado. Uma das "
            "resoluções da fonte chama o modelo de “Stackelberg em preços” — rótulo impreciso.",
            "Casos reais citados: a Arábia Saudita como <i>swing producer</i> na OPEP; grandes siderúrgicas "
            "diante de produtoras menores. Se a líder for muito eficiente, pode fixar um " + azb("preço-limite")
            + " que expulsa a franja.",
        ],
        "grafico_verso": "ECO-E3-L00104-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item descreve o modelo pelo avesso — em vez de "
                       "“demanda residual = mercado − franja”, diz “franja = mercado − líder” —, o que leva "
                       "o candidato a enxergar inversão. No equilíbrio, as duas contas são a mesma identidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo da empresa dominante, as empresas seguidoras fixam o preço, e a líder abastece a "
            "demanda remanescente.”</i> → ERRADO (troca de ator: quem fixa o preço é a líder)",
            "<i>“A demanda residual da empresa dominante é obtida subtraindo-se da demanda de mercado a oferta "
            "das seguidoras a cada preço.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Modelo de liderança de preço / empresa dominante: a líder maximiza sobre a demanda "
                             "residual (mercado − franja) e a franja abastece o restante; uma resolução o chama de "
                             "Stackelberg e vê “inversão lógica sutil” no item, sem alterar o gabarito; tabelas "
                             "comparativas de modelos de oligopólio."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 70", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 71-72", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 73-75", "tipo_fonte": "TEXTO/TABELA", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00105
    {
        "id": "ECO-E3-L00105-1", "fonte_ref": "E3-L00105", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUN,
        "rotulo_item": "Item",
        "assertiva": ("O sucesso de um cartel requer duas condições. Primeiro, a demanda de mercado deve ser "
                      "elástica e, além disso, o cartel deve ser capaz de controlar a maior parte da oferta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O sucesso de um cartel requer duas condições. Primeiro, a demanda de mercado deve ser ")
                    + vm("elástica") + az(" e, além disso, o cartel deve ser capaz de controlar a maior parte da "
                                          "oferta.")),
        "poucas": ("A demanda precisa ser " + azb("inelástica") + ": só assim subir o preço não derruba as "
                   "vendas. A segunda condição (controlar a maior parte da oferta) está correta."),
        "destrinchando": [
            "Paráfrase de " + oc("Pindyck e Rubinfeld") + " (<i>Microeconomia</i>, seção sobre cartéis): o "
            "sucesso exige (1) uma organização estável, com membros que concordem com preço e produção e os "
            "cumpram; e (2) " + azb("potencial de poder de monopólio") + " — demanda total pouco elástica e "
            "controle de quase toda a oferta (ou oferta de fora do cartel inelástica).",
            "Por que inelástica: o cartel age como monopolista; o markup ótimo é dado por (P − CMg)/P = "
            + vd("1/|ε|") + ". Com demanda elástica, o preço quase não pode subir acima do custo; com demanda "
            "inelástica, sobe muito com pouca perda de vendas.",
            "Por que controlar a oferta: se produtores de fora do cartel puderem expandir a produção quando o "
            "preço sobe, eles ocupam o mercado e corroem o lucro do acordo.",
            "Ilustração clássica: a " + azb("OPEP") + " nos anos 1970 (petróleo com demanda e oferta não-OPEP "
            "inelásticas no curto prazo) × o " + azb("CIPEC") + ", cartel do cobre, que fracassou porque a "
            "demanda era elástica (substituição por alumínio, sucata) e a oferta externa reagia.",
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " Uma palavra trocada (elástica × inelástica) numa "
                       "frase que, no resto, reproduz o manual. 🔥 Elasticidade da demanda e poder de mercado "
                       "são cobrados juntos: monopólio, cartel e tributação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um cartel tem mais chance de sucesso se a oferta dos produtores que não participam dele for "
            "inelástica.”</i> → CERTO",
            "<i>“Basta que o cartel controle a maior parte da oferta para que seja bem-sucedido, "
            "independentemente da elasticidade da demanda.”</i> → ERRADO (restrição indevida: a demanda também "
            "precisa ser inelástica)",
        ])],
        "reescrita": ("O sucesso de um cartel requer duas condições. Primeiro, a demanda de mercado deve ser "
                      + hl("inelástica") + " e, além disso, o cartel deve ser capaz de controlar a maior parte da "
                      "oferta."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Pindyck, seção 12.6: a demanda deve ser inelástica; com demanda elástica, o "
                             "aumento de preço derruba a quantidade e limita o ganho; controlar a oferta está "
                             "correto."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 76", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (referência ao manual)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00306
    {
        "id": "ECO-E3-L00306-1", "fonte_ref": "E3-L00306", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": True,
        "comando": CMD_NIDI_ESTR,
        "rotulo_item": "Item",
        "assertiva": ("Em mercados com poucas empresas competidoras, a sinalização de preços é uma estratégia de "
                      "acordo explícito que visa assegurar a estabilidade do setor, garantindo que o equilíbrio seja "
                      "atingido num nível de preços que seja lucrativo para as empresas e não inunde o mercado com "
                      "excesso de bens ofertados."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em mercados com poucas empresas competidoras, a sinalização de preços é uma estratégia de ")
                    + vm("acordo explícito") + az(" que visa assegurar a estabilidade do setor, ") + vm("garantindo")
                    + az(" que o equilíbrio seja atingido num nível de preços que seja lucrativo para as empresas "
                         "e não inunde o mercado com excesso de bens ofertados.")),
        "poucas": ("A " + azb("sinalização de preços") + " é forma de " + azb("colusão tácita") + " (implícita): "
                   "a firma anuncia um preço e espera que as rivais a sigam, <b>sem</b> acordo nem comunicação "
                   "direta — e sem garantia de que sigam."),
        "destrinchando": [
            "Oligopolistas enfrentam o dilema dos prisioneiros: todos ganhariam com preços altos, mas ninguém "
            "sabe se as rivais vão acompanhar. A sinalização resolve parte do problema sem acordo: uma firma "
            "(em geral a líder) anuncia publicamente um reajuste e observa; se as outras seguem, o novo patamar "
            "se firma; se não, ela recua.",
            "Variante próxima: a " + azb("liderança de preço") + " — uma firma muda o preço regularmente e as "
            "demais acompanham. É o padrão descrito por " + oc("Pindyck e Rubinfeld") + " ao lado da demanda "
            "quebrada (rigidez de preços) e do cartel.",
            azb("Colusão explícita") + " (cartel) = comunicação direta e compromisso entre concorrentes "
            "(reuniões, trocas de mensagens, cotas). " + azb("Colusão tácita") + " = coordenação por observação "
            "mútua de condutas públicas, sem pacto. A primeira é ilícita <i>per se</i>; a segunda, mais difícil "
            "de provar, porque o mero " + azb("paralelismo consciente") + " de preços não basta para condenar.",
            "No " + rx("Brasil") + ", o " + rx("CADE") + " trata a troca de informações sensíveis e certos "
            "anúncios de preços futuros como possíveis condutas facilitadoras de coordenação (Lei 12.529/2011, "
            "art. 36), mas a sinalização, em si, não é um acordo.",
            "Segundo erro: a sinalização <b>aumenta a probabilidade</b> de coordenação, mas não “garante” "
            "equilíbrio algum — rivais podem não seguir, e o incentivo a desviar continua lá.",
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " Troca “tácito” por “explícito” e "
                       "converte uma tentativa de coordenação em garantia de resultado. Pista: “sinalizar” é "
                       "comunicar <b>sem falar</b> com o rival — se houvesse acordo, não seria preciso sinalizar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A sinalização de preços é uma forma de colusão implícita, em que uma empresa anuncia um "
            "comportamento e espera que as concorrentes a acompanhem.”</i> → CERTO",
            "<i>“Por constituir acordo formal entre concorrentes, a sinalização de preços é sempre punida como "
            "cartel.”</i> → ERRADO (troca de conceito e modulador absoluto: é coordenação tácita)",
        ])],
        "reescrita": ("Em mercados com poucas empresas competidoras, a sinalização de preços é uma estratégia de "
                      + hl("coordenação tácita (acordo implícito)") + " que visa assegurar a estabilidade do setor, "
                      + hl("buscando") + " que o equilíbrio seja atingido num nível de preços que seja lucrativo "
                      "para as empresas e não inunde o mercado com excesso de bens ofertados."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["garantindo"], "dificuldade": 2,
        "comentario_fonte": ("Sinalização de preços é acordo implícito (uma empresa anuncia e espera que as "
                             "outras sigam); três resoluções de IA concordantes, com quadro tácito × explícito, "
                             "papel do CADE e crítica ao “garantindo”."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 412-413", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00307
    {
        "id": "ECO-E3-L00307-1", "fonte_ref": "E3-L00307", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": True,
        "comando": CMD_NIDI_ESTR,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado oligopolista em que ocorra um equilíbrio de Cournot, é possível que as empresas "
                      "obtenham um lucro maior do que em uma estrutura de cartel."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um mercado oligopolista em que ocorra um equilíbrio de Cournot, ") + vm("é possível")
                    + az(" que as empresas obtenham um lucro ") + vm("maior") + az(" do que em uma estrutura de "
                                                                                 "cartel.")),
        "poucas": ("O cartel escolhe o lucro conjunto <b>máximo</b> (o de monopólio); qualquer outro resultado — "
                   "Cournot inclusive — dá lucro conjunto " + vd("menor") + ". Logo não é possível."),
        "destrinchando": [
            "Cartel = maximização do lucro <b>conjunto</b>: é o problema do monopolista multiplanta. Por "
            "definição, nenhuma outra combinação de quantidades rende mais ao grupo.",
            oc("Cournot") + ": cada firma maximiza o <b>próprio</b> lucro tomando a quantidade da rival como dada. "
            "Ao expandir, ela reduz o preço também para a rival e ignora esse custo — uma "
            + azb("externalidade negativa") + " entre as firmas. Resultado: quantidade total maior, preço menor, "
            "lucro conjunto menor.",
            "Exemplo do gráfico (P = 30 − Q, custo zero): Cournot → 10 + 10 = 20 unidades, P = 10, lucro "
            "conjunto " + vd("200") + "; cartel → 15 unidades, P = 15, lucro " + vd("225") + "; competitivo → 30 "
            "unidades, P = 0, lucro zero.",
            "Hierarquia com produto homogêneo e custos iguais: lucro conjunto " + vd("cartel > Stackelberg > "
            "Cournot > Bertrand (= 0)") + ". O “custo” do cartel não é lucro menor, é a " + azb("instabilidade")
            + ": cada membro ganha individualmente se trair (no exemplo, quem mantém 7,5 vê a rival responder com "
            "11,25 e lucrar mais).",
            "Ressalva que não salva o item: uma firma <b>individual</b> pode lucrar mais em Cournot do que "
            "recebendo uma cota muito desigual do cartel; mas o item fala das empresas, e o lucro do cartel "
            "pode sempre ser repartido de modo a deixar todas melhor.",
        ],
        "grafico_verso": "ECO-E3-L00307-1-V1",
        "dissecando": (cz("[inversão · nexo indevido]") + " O “é possível” soa prudente (modulador relativo), "
                       "mas o resultado é impossível por construção. 🔥 Itens de oligopólio adoram a escala "
                       "cartel × Cournot × Bertrand: memorize a ordem dos lucros e das quantidades."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio de Cournot, a quantidade total produzida é maior e o preço é menor do que no "
            "cartel.”</i> → CERTO",
            "<i>“No equilíbrio de Cournot, o preço iguala o custo marginal.”</i> → ERRADO (troca de modelo: isso "
            "é Bertrand com produto homogêneo)",
        ])],
        "reescrita": ("Em um mercado oligopolista em que ocorra um equilíbrio de Cournot, " + hl("não é possível")
                      + " que as empresas obtenham um lucro " + hl("conjunto") + " maior do que em uma estrutura de "
                      "cartel."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["é possível"], "dificuldade": 1,
        "comentario_fonte": ("Cartel maximiza o lucro conjunto; Cournot gera produção maior e lucro conjunto "
                             "menor (externalidade não internalizada); hierarquia cartel > Cournot > Bertrand; "
                             "gráfico das curvas de reação com equilíbrios de Cournot, conluio e competitivo; "
                             "quadros comparativos dos modelos de duopólio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 415", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00307-1-V1)"},
                          {"ref": "IMAGEM 414, 416-418", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00412
    {
        "id": "ECO-E3-L00412-1", "fonte_ref": "E3-L00412", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_JB_OUT,
        "rotulo_item": "Item",
        "assertiva": ("As externalidades positivas podem surgir em oligopólios quando empresas colaboram em "
                      "inovações, criando novos produtos ou serviços que beneficiam não apenas os consumidores "
                      "diretos, mas também outras empresas e setores da economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As externalidades positivas <u>podem</u> surgir em oligopólios quando empresas colaboram em "
                      "inovações, criando novos produtos ou serviços que beneficiam não apenas os consumidores "
                      "diretos, mas também <u>outras empresas e setores da economia</u>."),
        "poucas": ("Inovação gera " + azb("transbordamentos (spillovers)") + ": o conhecimento criado por uma "
                   "empresa beneficia terceiros que não pagaram por ele — é uma " + azb("externalidade positiva")
                   + ", e pode nascer em oligopólios."),
        "destrinchando": [
            azb("Externalidade positiva") + " = benefício que uma atividade gera a quem não participa da "
            "transação nem paga por ele. Conhecimento é o caso típico: é não rival e difícil de excluir "
            "(engenharia reversa, mobilidade de pessoal, imitação, publicações).",
            "Hipótese de " + oc("Schumpeter") + " (<i>Capitalismo, Socialismo e Democracia</i>, 1942): grandes "
            "empresas com poder de mercado têm lucros e escala para financiar P&amp;D; a " + azb("destruição "
            "criadora") + " mostra que a concentração pode ser o preço da inovação. A concorrência perfeita, com "
            "lucro econômico zero, deixa pouco para investir em pesquisa.",
            "Colaboração entre empresas de um oligopólio (" + azb("joint ventures") + " e consórcios de P&amp;D, "
            "padrões técnicos comuns) pode ampliar esses transbordamentos: o padrão GSM ou o USB beneficiaram "
            "fabricantes de aparelhos, desenvolvedores e setores inteiros.",
            "Consequência de política: como o inovador não captura todo o ganho social, o mercado investe "
            + vm("menos") + " em P&amp;D do que o ótimo — daí patentes, subsídios e fomento público à pesquisa.",
            "Contrapeso: a mesma colaboração pode servir de fachada para coordenação de preços; por isso a "
            "defesa da concorrência examina acordos de cooperação caso a caso.",
        ],
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " O “podem” protege o item, e ele contraria "
                       "a ideia de que oligopólio só traz perda de bem-estar. A banca testa se o candidato "
                       "conhece o argumento schumpeteriano e o conceito de transbordamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os transbordamentos tecnológicos fazem o investimento privado em P&amp;D tender a superar o nível "
            "socialmente ótimo.”</i> → ERRADO (inversão: tende a ficar abaixo)",
            "<i>“Para Schumpeter, o poder de mercado pode favorecer a inovação ao gerar lucros que financiam "
            "P&amp;D.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("Hipótese schumpeteriana: lucros extraordinários financiam P&D; inovações geram "
                             "spillovers para outros setores; quatro resoluções concordantes com exemplos de "
                             "tecnologia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 578", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00413
    {
        "id": "ECO-E3-L00413-1", "fonte_ref": "E3-L00413", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_JB_OUT,
        "rotulo_item": "Item",
        "assertiva": ("Os oligopólios são, em geral, prejudiciais ao bem-estar social, pois a ausência de "
                      "competição que os caracteriza dificulta a geração de externalidades positivas, uma vez que "
                      "um acordo de competição sustentável entre as empresas é altamente instável."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os oligopólios ") + vm("são, em geral, prejudiciais") + az(" ao bem-estar social, pois a ")
                    + vm("ausência de competição que os caracteriza dificulta a geração de externalidades "
                         "positivas") + az(", uma vez que um acordo de competição sustentável entre as empresas é "
                                           "altamente instável.")),
        "poucas": ("Três problemas: oligopólio não se caracteriza por “ausência de competição” (há competição "
                   + azb("estratégica") + "); pode gerar " + azb("externalidades positivas") + " via inovação; "
                   "e o efeito sobre o bem-estar depende do caso, não é “em geral” negativo."),
        "destrinchando": [
            "Oligopólio = poucas firmas <b>interdependentes</b>. Elas competem, e às vezes ferozmente: guerra de "
            "preços (" + oc("Bertrand") + ", que leva a P = CMg com duas firmas), disputa por quantidades "
            "(Cournot), por qualidade, marca, inovação.",
            "Visão estática × dinâmica: no curto prazo, o poder de mercado tende a gerar preço acima do custo "
            "marginal e peso morto; no longo prazo, lucros e escala podem financiar P&amp;D e gerar "
            + azb("transbordamentos tecnológicos") + " (hipótese de " + oc("Schumpeter") + ").",
            "Por isso a análise antitruste moderna não condena a estrutura em si: avalia barreiras à entrada, "
            "risco de colusão, eficiências e potencial inovador. Concentração não é sinônimo de ineficiência.",
            "A oração final é verdadeira isoladamente — acordos de colusão tendem a ser instáveis —, mas não "
            "sustenta a conclusão: instabilidade do conluio significa <b>mais</b> competição, não menos.",
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " Empilha uma generalização (“em geral, "
                       "prejudiciais”), uma premissa falsa (“ausência de competição”) e um nexo causal que não "
                       "fecha. Item gêmeo do que afirma que oligopólios <b>podem</b> gerar externalidades "
                       "positivas por inovação (CERTO): lidos juntos, um desmente o outro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Oligopólios podem gerar perdas estáticas de bem-estar e, ao mesmo tempo, ganhos dinâmicos "
            "associados à inovação.”</i> → CERTO",
            "<i>“Por haver poucas empresas, não há competição entre os oligopolistas.”</i> → ERRADO (há "
            "competição estratégica)",
        ])],
        "reescrita": ("Os oligopólios " + hl("não são, necessariamente,") + " prejudiciais ao bem-estar social, "
                      "pois a " + hl("competição estratégica que os caracteriza pode conviver com a geração de "
                      "externalidades positivas") + ", uma vez que um acordo de competição sustentável entre as "
                      "empresas é altamente instável."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["em geral"], "dificuldade": 2,
        "comentario_fonte": ("Generalização indevida; há competição estratégica (Cournot, Bertrand); oligopólios "
                             "podem ser fonte de inovação e externalidades positivas; trade-off entre perdas "
                             "estáticas e ganhos dinâmicos; quatro resoluções concordantes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 579-580", "tipo_fonte": "TEXTO/TABELA", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0232
    {
        "id": "ECO-E1-0232-1", "fonte_ref": "E1-0232", "destino": "11", "subtema": H2["nash"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo à teoria dos jogos aplicada a mercados.",
        "rotulo_item": "Item",
        "assertiva": ("Mercados com poucos atores, em que a interdependência de ações é uma característica marcante, "
                      "podem ser representados como um jogo, cujo resultado, associado a uma estratégia, é "
                      "denominado playoff. Considera-se relativamente mais fácil utilizar a forma estratégica em "
                      "situações em que um jogador (empresa) deva agir sem o conhecimento da ação de seu "
                      "concorrente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Mercados com poucos atores, em que a interdependência de ações é uma característica "
                       "marcante, podem ser representados como um jogo, cujo resultado, associado a uma estratégia, "
                       "é denominado ") + vm("playoff") + az(". Considera-se relativamente mais fácil utilizar a "
                       "forma estratégica em situações em que um jogador (empresa) deva agir sem o conhecimento da "
                       "ação de seu concorrente.")),
        "poucas": ("O ganho associado a cada combinação de estratégias chama-se " + azb("payoff") + " (não "
                   "“playoff”, que é fase eliminatória de campeonato). A segunda frase é correta: a forma "
                   "estratégica é a representação natural dos jogos <b>simultâneos</b>."),
        "destrinchando": [
            "Elementos de um jogo: " + azb("jogadores") + ", " + azb("estratégias") + " e " + azb("payoffs")
            + " — o resultado (lucro, utilidade) de cada jogador para cada combinação de estratégias. Para "
            "firmas, o payoff é o lucro (" + oc("Pindyck e Rubinfeld") + ").",
            azb("Forma estratégica") + " (ou normal): matriz de payoffs, com as estratégias de cada jogador nas "
            "linhas e colunas. Serve aos jogos em que cada um decide <b>sem observar</b> a escolha do outro — "
            "jogos simultâneos, como o dilema dos prisioneiros ou o duopólio de Cournot.",
            azb("Forma extensiva") + ": árvore de decisão, com a ordem dos lances e o que cada jogador sabe em "
            "cada nó. É a adequada aos jogos " + azb("sequenciais") + " (Stackelberg, dissuasão de entrada), "
            "resolvidos por indução retroativa.",
            "Por isso a 2ª frase do item é verdadeira: quando a empresa age sem conhecer a ação da rival, a "
            "matriz basta e é mais simples de usar. O erro do item está só no termo “playoff”.",
            "Correção de leitura: uma resolução corrente deste item afirma que a 2ª frase também estaria errada "
            "(“é mais difícil decidir sem conhecer a ação do rival”). Isso confunde a dificuldade de <b>decidir</b> "
            "com a adequação da <b>representação</b>; não é o que o item diz.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Erro de vocabulário plantado num termo parecido (payoff × "
                       "playoff). A 2ª frase, tecnicamente correta, funciona como distração: quem a julga pelo "
                       "senso comum (“sem informação é mais difícil”) acerta o gabarito pelo motivo errado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Jogos sequenciais são mais bem representados na forma extensiva, por meio de uma árvore de "
            "decisão.”</i> → CERTO",
            "<i>“A forma estratégica é a representação adequada quando uma empresa observa a decisão da rival "
            "antes de agir.”</i> → ERRADO (troca de conceito: isso pede a forma extensiva)",
        ])],
        "reescrita": ("Mercados com poucos atores, em que a interdependência de ações é uma característica marcante, "
                      "podem ser representados como um jogo, cujo resultado, associado a uma estratégia, é "
                      "denominado " + hl("payoff") + ". Considera-se relativamente mais fácil utilizar a forma "
                      "estratégica em situações em que um jogador (empresa) deva agir sem o conhecimento da ação "
                      "de seu concorrente."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["relativamente"], "dificuldade": 2,
        "comentario_fonte": ("O termo correto é payoff (definição de Pindyck e Rubinfeld); a fonte também afirma "
                             "que a 2ª frase estaria errada, porque seria mais difícil decidir sem conhecer a ação "
                             "do concorrente, e menciona equilíbrio de Nash."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_E1_CACD,
                    "qualidade_fonte: a fonte considera falsa também a 2ª frase; a forma estratégica (normal) é a "
                    "representação própria de jogos simultâneos, de modo que só o termo “playoff” torna o item "
                    "ERRADO — gabarito mantido, justificativa corrigida"],
    },
    # ------------------------------------------------------------------ E2-L01660
    {
        "id": "ECO-E2-L01660-1", "fonte_ref": "E2-L01660", "destino": "11", "subtema": H2["seq"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": "A respeito dos conceitos e teorias da microeconomia, julgue os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando a teoria dos jogos na análise de um duopólio, uma vez no equilíbrio cooperativo "
                      "com a formação de cartel, ambas as firmas têm incentivo a burlar e aumentar seus lucros, o "
                      "que pode ser contornado se o jogo for repetido infinitamente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando a teoria dos jogos na análise de um duopólio, uma vez no equilíbrio cooperativo "
                      "com a formação de cartel, <u>ambas as firmas têm incentivo a burlar</u> e aumentar seus "
                      "lucros, o que <u>pode</u> ser contornado se o jogo for <u>repetido infinitamente</u>."),
        "poucas": ("No cartel, trair é a melhor resposta de cada firma (" + azb("dilema dos prisioneiros")
                   + "). Com repetição " + vd("infinita") + " (ou indefinida) e firmas pacientes, a ameaça de "
                   "punição futura pode sustentar a cooperação."),
        "destrinchando": [
            "Jogo de uma rodada: se a rival cumpre a cota, produzir mais eleva o meu lucro; se a rival trai, "
            "trair também me protege. Trair é " + azb("estratégia dominante") + " para as duas, e o equilíbrio "
            "de Nash é o pior para o grupo.",
            "Jogo " + azb("repetido infinitamente") + ": entram estratégias que condicionam o futuro ao "
            "presente. " + azb("Gatilho") + " (<i>grim trigger</i>): coopero enquanto você cooperar; se trair, "
            "volto à competição para sempre. " + azb("Olho por olho") + " (<i>tit-for-tat</i>): repito o seu "
            "último lance — estratégia que venceu os torneios de " + oc("Axelrod") + ".",
            "Condição: o ganho único de trair hoje tem de ser menor que o valor presente das perdas futuras. "
            "Isso exige " + azb("fator de desconto") + " alto (firmas pacientes, juros baixos, interação "
            "frequente). Resultado geral: " + azb("teorema folk") + ".",
            "Repetição <b>finita</b> e conhecida não basta: na última rodada todos traem; antecipando isso, "
            "traem na penúltima, e assim por diante (indução retroativa). Daí o item exigir repetição infinita "
            "— ou com fim incerto.",
            "Leitura prática: cartéis duram mais onde a interação é frequente, os preços são observáveis e a "
            "punição é crível (poucas firmas, produto homogêneo).",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " Reproduz o roteiro de manual (incentivo a "
                       "trair → repetição infinita) e se protege com “pode ser contornado”. Quem lembra só da "
                       "instabilidade do cartel marca ERRADO; o detalhe da repetição infinita salva o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o jogo for repetido um número finito e conhecido de vezes, a cooperação é sustentável em "
            "todas as rodadas.”</i> → ERRADO (indução retroativa: trai-se desde a 1ª rodada)",
            "<i>“Em jogos repetidos indefinidamente, a cooperação é mais fácil de sustentar quanto mais as "
            "firmas valorizam o futuro.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Cada firma tem incentivo a trapacear (dilema dos prisioneiros); repetição infinita "
                             "permite estratégias de gatilho/tit-for-tat; teorema folk com taxa de desconto "
                             "baixa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01728
    {
        "id": "ECO-E2-L01728-1", "fonte_ref": "E2-L01728", "destino": "11", "subtema": H2["nash"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("O equilíbrio de Nash em um jogo de duopólio é um equilíbrio de estratégias dominantes, porém "
                      "será um equilíbrio instável, caso o jogo não tenha repetição infinita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O equilíbrio de Nash em um jogo de duopólio ") + vm("é um equilíbrio de estratégias "
                    "dominantes") + az(", ") + vm("porém será um equilíbrio instável, caso") + az(" o jogo não "
                                                                                          "tenha repetição "
                                                                                          "infinita.")),
        "poucas": ("Dois erros: o " + azb("equilíbrio de Nash") + " não exige estratégias dominantes (todo "
                   "equilíbrio em dominantes é Nash, não o contrário); e ele é estável por definição — ninguém "
                   "ganha desviando sozinho —, com ou sem repetição."),
        "destrinchando": [
            azb("Equilíbrio de Nash") + " (" + oc("John Nash") + ", 1950): combinação de estratégias em que "
            "cada jogador faz o melhor que pode <b>dado o que os outros fazem</b>. Nenhum tem incentivo a "
            "mudar unilateralmente.",
            azb("Equilíbrio em estratégias dominantes") + ": cada jogador tem uma estratégia que é a melhor "
            "<b>qualquer que seja</b> a do outro. É mais exigente — e mais raro. Relação: " + vm("dominantes ⊂ "
            "Nash") + ".",
            "Exemplos: no dilema dos prisioneiros, o Nash é também em dominantes (trair). No duopólio de "
            "Cournot, não: a melhor quantidade de cada firma depende da quantidade da rival (função de "
            "reação), e o equilíbrio é Nash sem dominância. Na batalha dos sexos, há dois equilíbrios de Nash "
            "e nenhuma estratégia dominante.",
            "Estabilidade: o Nash é, por construção, autossustentável. A repetição infinita não “estabiliza” o "
            "Nash do jogo de uma rodada; ela torna possíveis <b>outros</b> equilíbrios, como a cooperação do "
            "cartel (teorema folk). O que é instável sem repetição é a cooperação, não o Nash.",
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Funde dois conceitos vizinhos (Nash × "
                       "dominantes) e transfere ao equilíbrio de Nash a instabilidade que pertence ao "
                       "<b>cartel</b>. Pista: “equilíbrio instável” é quase uma contradição em termos para Nash."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todo equilíbrio em estratégias dominantes é um equilíbrio de Nash, mas nem todo equilíbrio de "
            "Nash envolve estratégias dominantes.”</i> → CERTO",
            "<i>“O equilíbrio de Cournot é um equilíbrio de estratégias dominantes.”</i> → ERRADO (é Nash sem "
            "dominância)",
        ])],
        "reescrita": ("O equilíbrio de Nash em um jogo de duopólio " + hl("não é necessariamente") + " um "
                      "equilíbrio de estratégias dominantes, " + hl("e é estável por definição, ainda que") + " o "
                      "jogo não tenha repetição infinita."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Dois erros: Nash não é necessariamente em estratégias dominantes (Cournot é exemplo); "
                             "Nash é estável por definição; repetição permite cooperação, mas não afeta a "
                             "estabilidade do Nash do jogo estático."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00021
    {
        "id": "ECO-E3-L00021-1", "fonte_ref": "E3-L00021", "destino": "11", "subtema": H2["seq"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ-PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_ESTR,
        "rotulo_item": "Item",
        "assertiva": ("Na análise da estratégia empresarial em jogos sequenciais, é mais vantajoso para uma empresa "
                      "aguardar a decisão de sua concorrente para fins de maximizar seus lucros."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na análise da estratégia empresarial em jogos sequenciais, ") + vm("é") + az(" mais "
                       "vantajoso para uma empresa ") + vm("aguardar a decisão de sua concorrente") + az(" para fins de maximizar "
                                                                                       "seus lucros.")),
        "poucas": ("Em jogos sequenciais, a regra é a " + azb("vantagem do primeiro a jogar") + " (<i>first-mover "
                   "advantage</i>): quem age antes cria um fato consumado e condiciona a resposta do rival. "
                   "Esperar não é, em geral, melhor."),
        "destrinchando": [
            azb("Jogo sequencial") + ": os jogadores agem em ordem, e quem vem depois observa o lance anterior. "
            "Representa-se na forma extensiva (árvore) e resolve-se por " + azb("indução retroativa") + ": "
            "primeiro a melhor resposta do último, depois a escolha de quem antecipa essa resposta.",
            "Caso-padrão: " + oc("Stackelberg") + ". A líder escolhe a quantidade sabendo como a seguidora "
            "reagirá; ao produzir mais, força a rival a produzir menos. No caso linear, a líder produz o dobro "
            "da seguidora e lucra mais que em Cournot.",
            "O ingrediente é o " + azb("compromisso crível") + ": capacidade instalada, investimento "
            "irreversível, anúncio público. Exemplo de " + oc("Pindyck e Rubinfeld") + ": a incumbente que "
            "expande capacidade para dissuadir a entrada de um rival.",
            "Há exceções — " + azb("vantagem do segundo a jogar") + ": competição em preços com produtos "
            "diferenciados (quem anuncia o preço primeiro pode ser rebaixado), mercados com muita incerteza "
            "(o seguidor aprende com os erros do pioneiro). Por isso o item erra ao transformar a exceção em "
            "regra.",
        ],
        "dissecando": (cz("[inversão · modulador absoluto]") + " Inverte a vantagem típica (primeiro × segundo "
                       "a jogar) e a enuncia sem ressalva (“é mais vantajoso”). Pista: em prova, jogo sequencial "
                       "+ empresa remete a Stackelberg, cujo ponto é justamente a vantagem da líder."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em jogos sequenciais, a empresa que move primeiro pode obter vantagem ao assumir um "
            "compromisso crível que condiciona a resposta da rival.”</i> → CERTO",
            "<i>“Em jogos sequenciais, mover primeiro é sempre a melhor estratégia.”</i> → ERRADO (modulador "
            "absoluto: há casos de vantagem do segundo a jogar)",
        ])],
        "reescrita": ("Na análise da estratégia empresarial em jogos sequenciais, " + hl("costuma ser") + " mais "
                      "vantajoso para uma empresa " + hl("mover primeiro, antes de sua concorrente,") + " para fins "
                      "de maximizar seus lucros."),
        "tipo_erro": ["INVERSAO", "GENERALIZACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Seis resoluções concordantes: vantagem do primeiro a mover (Stackelberg, compromisso "
                             "crível); há casos de vantagem do segundo, mas não é a regra."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0218 (1)
    {
        "id": "ECO-E1-0218-1", "fonte_ref": "E1-0218", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": True,
        "comando": CMD_COASE, "excerto": EXCERTO_COASE_1,
        "rotulo_item": "Item",
        "assertiva": ("O problema apresentado no primeiro trecho, que se refere ao julgamento do processo de Cooke "
                      "contra Forbes, é conhecido como externalidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O problema apresentado no primeiro trecho, que se refere ao julgamento do processo de Cooke "
                      "contra Forbes, é conhecido como <u>externalidade</u>."),
        "poucas": ("Os vapores de Forbes estragam os tapetes de Cooke, que não participa da produção nem é "
                   "compensado: custo imposto a terceiro fora do mercado = " + azb("externalidade negativa")
                   + "."),
        "destrinchando": [
            azb("Externalidade") + ": efeito da atividade de um agente sobre o bem-estar ou a produção de outro, "
            "que não passa pelo sistema de preços. Negativa (poluição, ruído) ou positiva (vacina, pesquisa); "
            "de produção ou de consumo.",
            "No caso: o custo privado de Forbes não inclui o dano aos tapetes; o " + azb("custo marginal "
            "social") + " supera o privado, e a fábrica produz (e polui) mais do que o socialmente ótimo.",
            "O caso é um dos que " + oc("Ronald Coase") + " analisa em “O problema do custo social” (1960), "
            "texto que reformulou o tema: em vez de perguntar “como impedir A de prejudicar B”, Coase propõe "
            "ver o problema como <b>recíproco</b> — impedir o dano a B também impõe um custo a A. Os advogados "
            "de Forbes usam exatamente esse argumento (o alvejante de Cooke é que seria atípico).",
            "Soluções tradicionais: " + oc("Pigou") + " (tributo igual ao dano marginal) ou regulação; "
            "solução coasiana: definir direitos de propriedade e deixar as partes negociarem.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de reconhecimento: o texto descreve um dano a terceiro sem "
                       "compensação de mercado, e o item dá o nome. A dificuldade está no texto longo, que "
                       "distrai com detalhes jurídicos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O problema descrito constitui externalidade positiva, pois a decisão judicial gera benefícios "
            "a terceiros.”</i> → ERRADO (sinal trocado: o dano é custo imposto a Cooke)",
            "<i>“Para Coase, problemas como o descrito têm natureza recíproca.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Os trechos tratam de externalidades: a emissão do gás afeta quem não participa do "
                             "ato original; externalidade negativa pela qual o juiz admite compensação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_E1_CACD],
    },
    # ------------------------------------------------------------------ E1-0218 (2)
    {
        "id": "ECO-E1-0218-2", "fonte_ref": "E1-0218", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": True,
        "comando": CMD_COASE, "excerto": EXCERTO_COASE_1,
        "rotulo_item": "Item",
        "assertiva": ("A solução para o problema apresentado no primeiro trecho, de acordo com o teorema de Coase, "
                      "é a correta atribuição dos direitos de propriedade envolvidos no caso, desde que não haja "
                      "custos de transação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A solução para o problema apresentado no primeiro trecho, de acordo com o teorema de Coase, "
                      "é a <u>correta atribuição dos direitos de propriedade</u> envolvidos no caso, <u>desde que "
                      "não haja custos de transação</u>."),
        "poucas": ("Pelo " + azb("teorema de Coase") + ", com " + vd("custos de transação nulos") + " e direitos "
                   "de propriedade bem definidos, a negociação privada leva à solução eficiente — a externalidade "
                   "se resolve sem tributo nem regulação."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "pelo teorema, a eficiência é alcançada <b>qualquer que seja</b> a parte a quem se "
                          "atribui o direito — não existe uma atribuição “correta” do ponto de vista da "
                          "eficiência; o que importa é que o direito seja <b>claro</b>. O gabarito CERTO lê "
                          "“correta atribuição” como “definição clara”; uma leitura literal (um titular "
                          "específico seria o correto) tornaria o item ERRADO.")],
        "destrinchando": [
            "Enunciado usual: se os " + azb("direitos de propriedade") + " estão bem definidos e os "
            + azb("custos de transação") + " são nulos, as partes negociam até a alocação eficiente, "
            "<b>independentemente</b> de a quem o direito foi dado. A atribuição muda a <b>distribuição</b> "
            "(quem paga a quem), não a eficiência.",
            "No caso: se Cooke tem direito ao ar limpo, Forbes pode comprá-lo (pagar para poluir) quando o seu "
            "lucro com a fábrica superar o dano; se Forbes tem direito de emitir, Cooke pode pagar para que ele "
            "reduza as emissões quando o dano superar o lucro. Nos dois casos, prevalece o uso de maior valor.",
            "Custos de transação = custos de identificar as partes, negociar, redigir e fazer cumprir o acordo. "
            "Com muitas vítimas (poluição urbana), são altos e o teorema não se aplica: daí o papel do Estado e "
            "das soluções pigouvianas.",
            "Lição institucional de " + oc("Coase") + " (Nobel de 1991): como os custos de transação são "
            "positivos no mundo real, a <b>forma</b> como o direito e o Judiciário alocam direitos importa — "
            "deveriam atribuí-los a quem os valoriza mais. Origem da " + azb("análise econômica do direito") + ".",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz as duas condições do teorema (direitos "
                       "definidos + custo de transação zero). O ponto sensível é o adjetivo “correta”: a banca "
                       "costuma testar se o candidato sabe que a alocação inicial é irrelevante para a "
                       "eficiência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o teorema de Coase, a eficiência só é alcançada se o direito for atribuído à parte "
            "prejudicada pela externalidade.”</i> → ERRADO (restrição indevida: qualquer atribuição serve)",
            "<i>“Com custos de transação elevados, a negociação privada pode não alcançar a solução "
            "eficiente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["desde que"], "dificuldade": 2,
        "comentario_fonte": ("Afirma que, quando não se consegue definir claramente os direitos de propriedade, as "
                             "partes devem negociar formas de compensação, internalizando a externalidade; o "
                             "pleiteante busca o Judiciário para definir os direitos."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_E1_CACD,
                    "contestavel: a classificação marcava o gabarito como incerto; a fonte dá “Correto”, mas o "
                    "teorema dispensa uma atribuição “correta” (basta que seja clara) — gabarito da fonte mantido",
                    "qualidade_fonte: o comentário de origem inverte a condição do teorema (fala em direitos que "
                    "não se consegue definir claramente) — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0218 (3)
    {
        "id": "ECO-E1-0218-3", "fonte_ref": "E1-0218", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": True,
        "comando": CMD_COASE, "excerto": EXCERTO_COASE_1,
        "rotulo_item": "Item",
        "assertiva": ("O teorema de Coase permite inferir que, eliminados os custos de transação, seria possível "
                      "Cooke vender para Forbes o seu direito a ter ar limpo, de modo que este pudesse emitir os "
                      "vapores de sulfato de amônia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O teorema de Coase permite inferir que, <u>eliminados os custos de transação</u>, seria "
                      "<u>possível</u> Cooke vender para Forbes o seu direito a ter ar limpo, de modo que este "
                      "pudesse emitir os vapores de sulfato de amônia."),
        "poucas": ("Se o direito ao ar limpo é de Cooke (como sugere o juiz), ele pode " + azb("negociá-lo")
                   + ": Forbes paga para poluir sempre que o seu ganho com a produção superar o dano aos "
                   "tapetes. É a lógica de mercado do " + azb("teorema de Coase") + "."),
        "destrinchando": [
            "Direito de propriedade é transacionável. O juiz entende que o vizinho não pode “inundar o "
            "ambiente com gás”: o direito inicial fica com Cooke. Com custos de transação nulos, as partes "
            "trocam esse direito se isso aumentar o ganho conjunto.",
            "Exemplo numérico: se emitir os vapores vale " + vd("100") + " para Forbes e o dano a Cooke é "
            + vd("60") + ", qualquer pagamento entre 60 e 100 deixa ambos melhor — Cooke vende o direito, e a "
            "fábrica opera. Se o dano fosse 150, nenhum acordo sairia, e o ar continuaria limpo.",
            "O resultado eficiente (o uso de maior valor) seria o mesmo se o direito fosse de Forbes: aí Cooke "
            "pagaria para que ele parasse, quando o dano superasse o lucro. Só a distribuição de renda muda.",
            "Mercados de licenças de emissão negociáveis (<i>cap and trade</i>) são a aplicação de política "
            "pública da mesma ideia: definir direitos de poluir e deixá-los ser comprados e vendidos.",
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Soa estranho “vender o direito ao ar "
                       "limpo”, e o candidato tende a ver nisso um absurdo ético; mas é exatamente a "
                       "implicação do teorema. O “seria possível” e o “eliminados os custos de transação” "
                       "protegem o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teorema de Coase implica que Cooke jamais aceitaria vender o seu direito, pois o dano é "
            "irreparável.”</i> → ERRADO (o acordo sai se o ganho de Forbes superar o dano)",
            "<i>“Licenças de emissão negociáveis aplicam a lógica de Coase à política ambiental.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["seria possível"],
        "dificuldade": 2,
        "comentario_fonte": ("A negociação direta entre as partes delimita os direitos e permite acordar uma "
                             "compensação; o mercado atinge o equilíbrio ótimo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [ALERTA_E1_CACD,
                    "nota_redacao: a classificação marcava o gabarito como incerto; adotado o “Correto” do verso, "
                    "coerente com o teorema"],
    },
    # ------------------------------------------------------------------ E1-0219
    {
        "id": "ECO-E1-0219-1", "fonte_ref": "E1-0219", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": True,
        "comando": CMD_COASE, "excerto": EXCERTO_COASE_2,
        "rotulo_item": "Item",
        "assertiva": "No segundo trecho, faz-se referência ao tributo (ou imposto) Tobin.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No segundo trecho, faz-se referência ao tributo (ou imposto) ") + vm("Tobin") + az("."),
        "poucas": ("O trecho critica o " + azb("imposto pigouviano") + " — tributar a fumaça pelo dano que causa —, "
                   "não a taxa " + oc("Tobin") + ", que incide sobre transações cambiais."),
        "destrinchando": [
            oc("Arthur Pigou") + " (<i>The Economics of Welfare</i>, 1920): externalidade negativa → tributo "
            "por unidade igual ao " + azb("dano marginal") + " no ponto ótimo. O imposto faz o custo privado "
            "igualar o custo social e o poluidor internaliza o dano.",
            "Crítica de " + oc("Coase") + " (1960), resumida no trecho: calcular esse tributo exige conhecer o "
            "dano <b>marginal</b> (não o médio) e as interações entre danos a várias propriedades — informação "
            "que o governo raramente tem. Além disso, o problema é recíproco, e o tributo pode induzir ajustes "
            "ineficientes.",
            azb("Taxa Tobin") + ": proposta de " + oc("James Tobin") + " (1972) de um imposto pequeno sobre "
            "operações de câmbio para “jogar areia nas engrenagens” dos fluxos especulativos de curto prazo. "
            "Nada a ver com poluição.",
            "Outros nomes que a banca pode trocar: imposto " + azb("Ramsey") + " (tributação ótima com "
            "alíquotas inversas à elasticidade), " + azb("taxa Pigou") + " (externalidades), " + azb("imposto "
            "inflacionário") + " (senhoriagem).",
        ],
        "dissecando": (cz("[troca de ator]") + " Troca o autor associado ao instrumento. Pista no próprio texto: "
                       "“tributação” como solução para a “poluição causada pela fumaça” é a assinatura de Pigou; "
                       "Tobin é sempre câmbio e capital especulativo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No segundo trecho, Coase aponta dificuldades da tributação pigouviana, como a distinção entre "
            "dano médio e dano marginal.”</i> → CERTO",
            "<i>“O imposto pigouviano ótimo deve igualar o dano médio causado pela externalidade.”</i> → ERRADO "
            "(dado alterado: dano marginal)",
        ])],
        "reescrita": "No segundo trecho, faz-se referência ao tributo (ou imposto) " + hl("pigouviano") + ".",
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Trata-se do imposto pigouviano, que busca compensar o custo social das "
                             "externalidades negativas; o mercado produz em excesso o bem poluente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_E1_CACD],
    },
    # ------------------------------------------------------------------ E1-0252
    {
        "id": "ECO-E1-0252-1", "fonte_ref": "E1-0252", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("Quando o preço de equilíbrio não considera custos impostos pela transação a agentes "
                      "terceiros, não envolvidos diretamente na transação em estudo, ocorre externalidade negativa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando o preço de equilíbrio <u>não considera custos impostos</u> pela transação a agentes "
                      "<u>terceiros</u>, não envolvidos diretamente na transação em estudo, ocorre externalidade "
                      "negativa."),
        "poucas": ("É a definição de " + azb("externalidade negativa") + ": custo que recai sobre quem está fora "
                   "da transação e que o preço de mercado não incorpora. Resultado: " + azb("custo marginal "
                   "social > custo marginal privado") + " e produção excessiva."),
        "destrinchando": [
            "Comprador e vendedor só levam em conta os próprios custos e benefícios. Se a produção impõe custos "
            "a terceiros (poluição de um rio que prejudica pescadores, ruído, congestionamento), esses custos "
            "ficam fora do preço.",
            "Graficamente: a oferta reflete o " + azb("CMg privado") + "; somando o dano marginal a terceiros, "
            "obtém-se o " + azb("CMg social") + ", acima dela. O mercado produz qₘ, onde a demanda corta a "
            "oferta privada; o ótimo social é q* < qₘ, onde a demanda corta o CMg social.",
            "As unidades entre q* e qₘ custam à sociedade mais do que valem para os consumidores: é o "
            + azb("peso morto") + " da externalidade. O preço de mercado fica " + vm("baixo demais") + " e a "
            "quantidade, alta demais.",
            "Espelho: na " + azb("externalidade positiva") + " (vacinação, educação, P&amp;D), o benefício "
            "marginal social supera o privado, e o mercado produz <b>menos</b> que o ótimo.",
            "Correções: imposto pigouviano igual ao dano marginal; regulação de quantidade; licenças "
            "negociáveis; negociação coasiana, se os custos de transação forem baixos.",
        ],
        "grafico_verso": "ECO-E1-0252-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " Reescreve a definição de manual (“custos impostos a terceiros "
                       "não refletidos no preço”) com palavras próprias. O risco está em confundir com "
                       "externalidade positiva ou com custo de transação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença de externalidade negativa na produção, o mercado produz quantidade inferior à "
            "socialmente ótima.”</i> → ERRADO (inversão: produz em excesso)",
            "<i>“Na externalidade negativa, o custo marginal social supera o custo marginal privado.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Definição de externalidade negativa (custos a terceiros não refletidos no preço), "
                             "exemplos da fábrica que polui o rio e da indústria de detergentes; CMgS > CMgP e "
                             "produção acima do ótimo; espelho da externalidade positiva."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (87).png, image (85).png", "tipo_fonte": "não preservadas",
                           "lado": "verso", "acao": "irrecuperavel (mecanismo redesenhado em ECO-E1-0252-1-V1)"}],
        "alertas": [ALERTA_2023],
    },
    # ------------------------------------------------------------------ E1-0253
    {
        "id": "ECO-E1-0253-1", "fonte_ref": "E1-0253", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_FALHAS,
        "rotulo_item": "Item",
        "assertiva": "Bens rivais são uma falha de mercado relativa a marcas concorrentes de um mesmo produto.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Bens rivais ") + vm("são uma falha de mercado relativa a marcas concorrentes de um mesmo "
                                            "produto") + az(".")),
        "poucas": ("" + azb("Rivalidade") + " é uma característica do <b>consumo</b> do bem (o que eu consumo "
                   "deixa de estar disponível para você), não uma falha de mercado nem uma questão de marcas."),
        "destrinchando": [
            azb("Bem rival") + ": o consumo por um agente reduz a quantidade disponível para os demais (uma "
            "maçã, um litro de gasolina). " + azb("Bem não rival") + ": o consumo de um não reduz o dos outros "
            "(a luz do farol, um sinal de rádio, uma ideia).",
            "Combinado com a " + azb("excludabilidade") + " (é possível impedir quem não paga?), dá a "
            "classificação de quatro casas: privado (rival e excludente), público (não rival e não "
            "excludente), " + azb("recurso comum") + " (rival e não excludente: peixes no mar) e "
            + azb("bem de clube") + " ou monopólio natural (não rival e excludente: TV por assinatura).",
            "A maior parte dos bens é rival — e o mercado os aloca bem. As " + azb("falhas de mercado") + " são "
            "outras: bens públicos, externalidades, poder de mercado, informação assimétrica. Rivalidade só "
            "se liga a falha quando combinada com não exclusão: a " + azb("tragédia dos comuns") + " (sobre-"
            "exploração).",
            "Marcas concorrentes do mesmo produto têm a ver com estrutura de mercado (concorrência "
            "monopolística, diferenciação), não com rivalidade no consumo.",
            "Nota: um dos comentários da fonte mistura o conceito econômico de bem público com o jurídico "
            "(bens de uso comum, inalienabilidade) — são noções distintas; na economia, “público” se define "
            "por não rivalidade e não exclusão, não pela titularidade estatal.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Usa “rival” no sentido coloquial (concorrente) para "
                       "fabricar uma definição falsa e ainda a rotula de falha de mercado. Pista: rivalidade "
                       "descreve o consumo, não a oferta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens rivais e não excludentes, como os estoques pesqueiros em alto-mar, tendem à "
            "sobre-exploração.”</i> → CERTO",
            "<i>“A rivalidade no consumo é, por si só, uma falha de mercado.”</i> → ERRADO (troca de conceito: "
            "é a característica da maioria dos bens privados)",
        ])],
        "reescrita": ("Bens rivais " + hl("são aqueles cujo consumo por um agente reduz a quantidade disponível "
                      "para os demais, característica que não constitui, por si só, falha de mercado") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Vários comentários: rivalidade é característica do bem, não falha de mercado; falhas "
                             "são externalidades, bens públicos, assimetria, monopólio; um deles mistura o conceito "
                             "jurídico de bem público (inalienabilidade, impenhorabilidade); outro chama bens "
                             "rivais de falha de mercado."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_2023,
                    "qualidade_fonte: um dos comentários afirma que “bens rivais são uma falha de mercado” e outro "
                    "confunde bem público econômico com bem público jurídico — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0254
    {
        "id": "ECO-E1-0254-1", "fonte_ref": "E1-0254", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("Um bem público é uma falha de mercado originada pela produção do bem pelo setor público, ou "
                      "seja, pelo governo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um bem público é uma falha de mercado ") + vm("originada pela produção do bem pelo setor "
                                                                      "público, ou seja, pelo governo") + az(".")),
        "poucas": ("Bem público se define pelas características do consumo — " + azb("não rivalidade") + " e "
                   + azb("não exclusão") + " —, não por quem o produz. A falha vem do " + azb("carona") + ", e "
                   "a provisão estatal é a <b>resposta</b> a ela, não a causa."),
        "destrinchando": [
            "Definição (" + oc("Samuelson") + ", 1954): bem público puro é não rival (o consumo de um não reduz "
            "o dos demais) e não excludente (não se pode impedir quem não paga de usufruir). Exemplos: defesa "
            "nacional, iluminação pública, farol.",
            "Por que é falha de mercado: sem exclusão, cada um prefere esperar que os outros paguem — o "
            + azb("problema do carona") + " (<i>free rider</i>). A disposição a pagar fica oculta, e a "
            "provisão privada é insuficiente ou nula.",
            "Por isso o governo costuma prover (ou financiar com impostos) esses bens. Mas a causalidade é a "
            "inversa da do item: o bem é público pela natureza; a produção estatal é a solução.",
            "Provisão ótima: como todos consomem a mesma unidade, soma-se " + azb("verticalmente") + " a "
            "disposição marginal a pagar: Σ BMg = CMg (condição de Samuelson). Nos bens privados, a soma é "
            "horizontal.",
            "Contraexemplos que a banca usa: o governo produz bens privados (energia, correios, crédito de "
            "bancos públicos), e há bens públicos providos privadamente (software livre, sinal aberto de TV "
            "financiado por anúncios).",
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Confunde o sentido econômico de “público” "
                       "(característica do bem) com o jurídico/administrativo (de propriedade ou produção "
                       "estatal) e inverte causa e solução. A 1ª parte (“é uma falha de mercado”) é verdadeira "
                       "e serve de isca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens públicos são não rivais e não excludentes, o que dá origem ao problema do carona.”</i> → "
            "CERTO",
            "<i>“Todo bem produzido pelo governo é um bem público.”</i> → ERRADO (modulador absoluto: o governo "
            "também produz bens privados)",
        ])],
        "reescrita": ("Um bem público é uma falha de mercado " + hl("decorrente de suas características de não "
                      "rivalidade e não exclusão, que levam ao problema do carona, e não da sua produção pelo "
                      "governo") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O erro é associar a falha à produção pelo governo; bens públicos são não exclusivos "
                             "e não rivais; carona; o governo provê por isso; um comentário reescreve o item de "
                             "forma confusa (agentes que não querem pagar pela produção estatal)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (84).png", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo coberto pelo texto)"}],
        "alertas": [ALERTA_2023],
    },
    # ------------------------------------------------------------------ E1-0321
    {
        "id": "ECO-E1-0321-1", "fonte_ref": "E1-0321", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_SEMI,
        "rotulo_item": "Item",
        "assertiva": "Temos como exemplo de bem semipúblico ou meritório a defesa nacional.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Temos como exemplo de bem ") + vm("semipúblico ou meritório") + az(" a defesa "
                                                                                          "nacional.")),
        "poucas": ("A defesa nacional é o exemplo clássico de " + azb("bem público puro") + ": não rival e não "
                   "excludente. Meritórios são bens como " + vd("educação e saúde") + ", que podem ser vendidos "
                   "no mercado, mas que o Estado oferta por seu valor social."),
        "destrinchando": [
            azb("Bem público puro") + ": todos os habitantes são protegidos ao mesmo tempo (não rival) e não "
            "há como excluir quem não paga impostos (não excludente). Só o Estado consegue financiá-lo, por "
            "tributação compulsória.",
            azb("Bens semipúblicos ou meritórios") + " (" + oc("Musgrave") + "): bens que <b>podem</b> ser "
            "providos pelo mercado — há rivalidade e é possível excluir quem não paga —, mas que o Estado "
            "oferta (total ou parcialmente) porque geram " + azb("externalidades positivas") + " ou porque a "
            "sociedade julga que todos devem tê-los, independentemente da renda.",
            "Exemplos de meritórios: " + rx("educação básica, saúde pública (SUS), merenda escolar, "
            "vacinação, habitação popular") + ". O consumo individual traz benefício também a terceiros "
            "(população mais instruída e saudável).",
            "Nas funções do governo de Musgrave, a provisão de bens públicos e meritórios pertence à "
            + azb("função alocativa") + "; ao lado dela, a distributiva e a estabilizadora.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca o exemplo-modelo de uma categoria pelo de outra. "
                       "Teste rápido: dá para excluir alguém da defesa nacional? Não — então não é semipúblico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A educação pública é exemplo de bem semipúblico ou meritório.”</i> → CERTO",
            "<i>“A defesa nacional é bem público por ser produzida pelo governo.”</i> → ERRADO (nexo indevido: é "
            "público por ser não rival e não excludente)",
        ])],
        "reescrita": ("Temos como exemplo de bem " + hl("público puro") + " a defesa nacional."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A defesa nacional é bem público puro: não rival e não excludente.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (76).jpeg", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo coberto pelo texto)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0322
    {
        "id": "ECO-E1-0322-1", "fonte_ref": "E1-0322", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_SEMI,
        "rotulo_item": "Item",
        "assertiva": "Temos como exemplo de bem semipúblico ou meritório: a utilização de um parque/praça na cidade.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Temos como exemplo de bem ") + vm("semipúblico ou meritório") + az(": a utilização de um "
                                                                                           "parque/praça na "
                                                                                           "cidade.")),
        "poucas": ("Praça e parque abertos são " + azb("bens públicos") + " (locais): ninguém é excluído e, até "
                   "lotar, o uso de um não atrapalha o de outro. Não se encaixam no conceito de bem "
                   + azb("meritório") + " (educação, saúde)."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "parte da literatura chama de “semipúblicos” os " + azb("bens públicos impuros") + " "
                          "— não excludentes, mas sujeitos a congestionamento —, categoria em que um parque "
                          "lotado poderia caber. O gabarito ERRADO segue a leitura mais usual, em que "
                          "“semipúblico” é sinônimo de “meritório” (Musgrave), e o parque, bem público local.")],
        "destrinchando": [
            "Parque ou praça abertos: " + azb("não excludentes") + " (acesso livre) e " + azb("não rivais")
            + " até o ponto de congestionamento. São " + azb("bens públicos locais") + ": beneficiam sobretudo "
            "os moradores de uma área, por isso costumam ser providos pelos municípios.",
            "Com lotação, surge rivalidade parcial: é o " + azb("bem público congestionável") + " (ou "
            "impuro). Se se cobrar ingresso, passa a " + azb("bem de clube") + " (excludente e não rival até a "
            "capacidade).",
            azb("Bens meritórios") + " são outra coisa: bens privados por natureza (rivais e excludentes) que o "
            "Estado oferta por considerar que todos devem consumi-los — educação, saúde, vacinação. O critério é "
            "o <b>mérito social</b> do consumo, não a impossibilidade de excluir.",
            "Quadro-resumo: defesa nacional e iluminação → públicos puros; parque, rua sem pedágio → públicos "
            "locais/congestionáveis; escola e hospital públicos → meritórios; peixes no mar → recurso comum.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mesmo molde do item sobre a defesa nacional: oferece um "
                       "exemplo de outra categoria. Pista: o parque não é bem privado oferecido pelo Estado por "
                       "mérito — é acesso livre, típico de bem público."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um parque público sujeito a lotação nos fins de semana é exemplo de bem público "
            "congestionável.”</i> → CERTO",
            "<i>“Bens meritórios são, por definição, não rivais e não excludentes.”</i> → ERRADO (troca de "
            "conceito: essa é a definição de bem público puro)",
        ])],
        "reescrita": ("Temos como exemplo de bem " + hl("público (local)") + ": a utilização de um parque/praça na "
                      "cidade."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Parque público é bem público local, com rivalidade limitada (pode lotar) e não "
                             "excludente."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (81).jpeg", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo coberto pelo texto)"}],
        "alertas": ["contestavel: “semipúblico” às vezes designa bem público impuro (congestionável), categoria em "
                    "que o parque caberia; gabarito ERRADO da fonte mantido pela leitura semipúblico = meritório"],
    },
    # ------------------------------------------------------------------ E1-0323
    {
        "id": "ECO-E1-0323-1", "fonte_ref": "E1-0323", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo aos bens públicos e às externalidades.",
        "rotulo_item": "Item",
        "assertiva": ("No que se refere à promoção da mudança tecnológica, a pesquisa básica é um bem público. Isso "
                      "significa que as despesas com pesquisa e desenvolvimento para invenções ou inovações nunca "
                      "foram fontes de externalidades."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No que se refere à promoção da mudança tecnológica, a pesquisa básica é um bem público. "
                       "Isso significa que as despesas com pesquisa e desenvolvimento para invenções ou inovações ")
                    + vm("nunca foram") + az(" fontes de externalidades.")),
        "poucas": ("A 1ª frase está certa; a conclusão, invertida. Justamente por ser bem público, o conhecimento "
                   "gerado pela pesquisa " + azb("transborda") + " para terceiros: P&amp;D é fonte clássica de "
                   + azb("externalidades positivas") + "."),
        "destrinchando": [
            "Conhecimento científico é " + azb("não rival") + " (um teorema serve a todos ao mesmo tempo) e "
            "dificilmente " + azb("excludente") + " (publicações, imitação, mobilidade de pesquisadores). "
            "Pesquisa básica é, assim, bem público.",
            "Consequência: quem financia a pesquisa captura só parte do ganho social, e o resto beneficia "
            "outras empresas e setores — " + azb("transbordamentos (spillovers)") + ". O retorno social da "
            "P&amp;D supera o privado, e o mercado investe " + vm("menos") + " que o ótimo.",
            "Respostas de política: financiamento público direto (universidades, institutos), subsídios e "
            "incentivos fiscais à P&amp;D, patentes (exclusão temporária para restaurar o incentivo). No "
            + rx("Brasil") + ": CNPq, CAPES, FINEP, Embrapa e a Lei do Bem (Lei 11.196/2005).",
            "Nas teorias de crescimento endógeno (" + oc("Romer") + ", 1990), esses transbordamentos de "
            "conhecimento sustentam o crescimento de longo prazo.",
        ],
        "dissecando": (cz("[contradição · modulador absoluto]") + " A 2ª frase contradiz a 1ª: se é bem "
                       "público, gera externalidades. O “nunca” é a bandeira vermelha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por ser bem público, a pesquisa básica tende a ser subprovida pelo mercado.”</i> → CERTO",
            "<i>“As patentes eliminam por completo as externalidades da pesquisa.”</i> → ERRADO (modulador "
            "absoluto: a patente divulga o conhecimento e só restringe o uso comercial por um prazo)",
        ])],
        "reescrita": ("No que se refere à promoção da mudança tecnológica, a pesquisa básica é um bem público. Isso "
                      "significa que as despesas com pesquisa e desenvolvimento para invenções ou inovações "
                      + hl("são importantes") + " fontes de externalidades " + hl("positivas") + "."),
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["nunca"], "dificuldade": 1,
        "comentario_fonte": ("Pesquisas básicas geram muitas externalidades positivas ao disseminar conhecimento "
                             "útil a múltiplos agentes."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
