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
]
