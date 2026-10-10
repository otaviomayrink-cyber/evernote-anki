"""Cards do lote de redação 24 — ECO, passada 03 (itens de provas diferentes antes fundidos como duplicatas)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ppc": "📏 Câmbio nominal × real e PPC",
    "cepal": "🌎 CEPAL e termos de troca",
    "par": "🔗 Paridades e repasse cambial",
    "novas": "🔬 Novas teorias do comércio",
    "bw": "🏦 Bretton Woods",
    "glob": "🌐 Globalização e vulnerabilidade",
    "tar": "🧾 Tarifas",
    "omc": "🏛️ Política comercial e OMC",
}

CARDS = [
    # ------------------------------------------------------------------ E2-L01045 (cf. E2-L00487)
    {
        "id": "ECO-E2-L01045-1", "fonte_ref": "E2-L01045", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Em relação à macroeconomia aberta, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Suponha que a inflação no Brasil seja igual a 5% e que a inflação externa seja igual a 1%. "
                      "Considerando a versão relativa da paridade do poder de compra e que essas variações são "
                      "pequenas, para que a taxa real de câmbio se mantenha em equilíbrio e constante, a variação "
                      "da taxa de câmbio nominal deve ser igual a -4%."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Suponha que a inflação no Brasil seja igual a 5% e que a inflação externa seja igual a "
                       "1%. Considerando a versão relativa da paridade do poder de compra e que essas variações "
                       "são pequenas, para que a taxa real de câmbio se mantenha em equilíbrio e constante, a "
                       "variação da taxa de câmbio nominal deve ser igual a ") + vm("-4%") + az(".")),
        "poucas": ("PPC relativa: " + vd("%ΔE ≈ π − π* = 5% − 1% = +4%") + ". A moeda do país com mais inflação "
                   "precisa se " + azb("depreciar") + " (E sobe), não se apreciar."),
        "destrinchando": [
            "Câmbio real: " + vd("q = E · P*/P") + ". Em variações pequenas, %Δq ≈ %ΔE + π* − π. Para q "
            "constante (%Δq = 0): " + vd("%ΔE = π − π*") + " — é a " + azb("PPC relativa") + ".",
            "Com os dados: %ΔE = 5% − 1% = " + vd("+4%") + ". O real deve perder cerca de 4% de valor frente "
            "à moeda externa (ex.: de R$ 5,00 para R$ 5,20 por dólar) para compensar o fato de os preços "
            "brasileiros subirem 4 pontos a mais.",
            "Se E caísse 4% (o −4% do item), o efeito seria dobrado na direção errada: %Δq ≈ −4% + 1% − 5% = "
            + vd("−8%") + " — " + azb("apreciação real") + " de cerca de 8%, com perda de competitividade.",
            "Atenção ao sinal conforme a convenção: com E = R$/US$ (cotação do incerto, padrão no Brasil), "
            "depreciação é variação <b>positiva</b>. A conta exata (sem aproximação) seria (1,05/1,01) − 1 ≈ "
            "3,96%; o enunciado autoriza a aproximação ao dizer que as variações são pequenas.",
            vm("Regra-âncora: mais inflação em casa → E sobe na medida do diferencial (%ΔE = π − π*)."),
        ],
        "dissecando": (cz("[dado alterado · inversão]") + " Número certo, sinal trocado: a banca aposta em quem "
                       "faz π* − π ou confunde depreciação com variação negativa. Pista: o país com inflação "
                       "maior nunca vê sua moeda se fortalecer sob PPC."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a variação da taxa de câmbio nominal deve ser de aproximadamente +4%, o que corresponde a uma "
            "depreciação nominal do real.”</i> → CERTO",
            "<i>“…a taxa real de câmbio deve se depreciar 4%.”</i> → ERRADO (sob PPC o real fica constante; quem "
            "varia é o nominal)",
        ])],
        "reescrita": ("Suponha que a inflação no Brasil seja igual a 5% e que a inflação externa seja igual a 1%. "
                      "Considerando a versão relativa da paridade do poder de compra e que essas variações são "
                      "pequenas, para que a taxa real de câmbio se mantenha em equilíbrio e constante, a variação "
                      "da taxa de câmbio nominal deve ser igual a " + hl("+4%") + "."),
        "tipo_erro": ["DADO_ALTERADO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Inflação doméstica maior → o real deve depreciar: aumento da taxa de câmbio (+4% = "
                             "5% − 1%), não queda. PPC absoluta (E = P/P*) e relativa: e = EP*/P constante ⇒ "
                             "%e = %E + %P* − %P = 0 ⇒ %E = %P − %P* = 4%."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 180", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 181", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00487-1 (mesmo item em outra lista Nabuco)"],
    },
    # ------------------------------------------------------------------ E2-L01159 (cf. E1-0906)
    {
        "id": "ECO-E2-L01159-1", "fonte_ref": "E2-L01159", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Com relação às teorias do comércio internacional, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a visão de Prebisch, as recorrentes crises, nas nações periféricas, causadas pelo "
                      "desequilíbrio dos balanços de pagamentos, decorreram, em parte, do fato de às elevadas "
                      "elasticidades-renda da demanda de importações terem-se contraposto as baixas "
                      "elasticidades-renda das exportações da periferia, o que contribuía para a deterioração dos "
                      "termos de troca desses países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a visão de Prebisch, as recorrentes crises, nas nações periféricas, causadas "
                      "pelo desequilíbrio dos balanços de pagamentos, decorreram, <u>em parte</u>, do fato de às "
                      "<u>elevadas</u> elasticidades-renda da demanda de importações terem-se contraposto as "
                      "<u>baixas</u> elasticidades-renda das exportações da periferia, o que contribuía para a "
                      "deterioração dos termos de troca desses países."),
        "poucas": ("A periferia importa manufaturados de " + azb("alta elasticidade-renda") + " e exporta "
                   "primários de " + azb("baixa elasticidade-renda") + ": quando a renda cresce, as importações "
                   "sobem mais que as exportações — " + azb("estrangulamento externo") + " e termos de troca "
                   "piores."),
        "destrinchando": [
            "Assimetria de elasticidades: se a periferia cresce, sua demanda por manufaturados importados cresce "
            "<b>mais</b> que proporcionalmente; se o centro cresce, sua demanda por primários da periferia cresce "
            "<b>menos</b> que proporcionalmente. Mesmo com as duas regiões crescendo ao mesmo ritmo, as "
            "importações da periferia avançam mais rápido que suas exportações.",
            "Consequências: (1) déficits recorrentes no " + azb("balanço de pagamentos") + " e crises cambiais — "
            "o crescimento periférico esbarra na falta de divisas (" + azb("restrição externa") + "); (2) excesso "
            "de oferta de primários e excesso de demanda por manufaturados no mercado mundial, o que pressiona os "
            + azb("termos de troca") + " contra a periferia.",
            "A ideia foi depois formalizada na " + azb("lei de Thirlwall") + " (" + oc("A. P. Thirlwall") + ", "
            + vd("1979") + "): a taxa de crescimento compatível com o equilíbrio externo é a razão entre o "
            "crescimento das exportações e a elasticidade-renda das importações.",
            "Daí a prescrição de " + oc("Prebisch") + " e da " + azb("CEPAL") + ": industrializar para substituir "
            "importações de alta elasticidade-renda e diversificar a pauta exportadora.",
            vm("Regra-âncora: importações de alta elasticidade-renda × exportações de baixa = estrangulamento "
               "externo da periferia."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " As elasticidades estão no lugar certo "
                       "(elevadas nas importações da periferia, baixas nas exportações) e o “em parte” protege o "
                       "nexo causal. A armadilha usual é trocar os adjetivos — o que tornaria o item ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…do fato de às baixas elasticidades-renda da demanda de importações terem-se contraposto as "
            "elevadas elasticidades-renda das exportações da periferia…”</i> → ERRADO (inversão)",
            "<i>“As crises de balanço de pagamentos na periferia decorreram exclusivamente da deterioração dos "
            "termos de troca.”</i> → ERRADO (modulador absoluto)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["em parte"], "dificuldade": 2,
        "comentario_fonte": ("Excesso de demanda da periferia por manufaturados importados do centro, de alta "
                             "elasticidade-renda, e oferta excedente de primários de baixa elasticidade-renda "
                             "produzidos pela periferia: tendência à deterioração dos termos de troca."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0906-1 (mesmo item, reutilizado em lista Nabuco)",
                    "quase_duplicata: ECO-E1-0896-1, ECO-E1-0675-1 (elasticidades dos primários na tese cepalina)"],
    },
    # ------------------------------------------------------------------ E2-L01234 (cf. E2-L00638)
    {
        "id": "ECO-E2-L01234-1", "fonte_ref": "E2-L01234", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Com base nos conceitos de macroeconomia aberta, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Supondo que os títulos dos países A e B sejam substitutos perfeitos e paguem, respectivamente, "
                      "5% a.a. e 6% a.a. de taxa de juros, então o mercado de câmbio prevê implicitamente que a "
                      "moeda do país A irá se depreciar em relação à moeda do país B em 1% no próximo ano."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Supondo que os títulos dos países A e B sejam substitutos perfeitos e paguem, "
                       "respectivamente, 5% a.a. e 6% a.a. de taxa de juros, então o mercado de câmbio prevê "
                       "implicitamente que a moeda do país A irá se ") + vm("depreciar") + az(" em relação à moeda "
                       "do país B em 1% no próximo ano.")),
        "poucas": ("A moeda que paga " + azb("menos juros") + " precisa ter " + vm("apreciação") + " esperada para "
                   "compensar: ΔE<sup>e</sup> (A por B) = 5% − 6% = " + vd("−1%") + " → A se aprecia 1%."),
        "destrinchando": [
            "Do ponto de vista de A, com E = unidades de A por unidade de B: " + vd("i<sub>A</sub> = i<sub>B</sub> "
            "+ ΔE<sup>e</sup>") + " → 5% = 6% + ΔE<sup>e</sup> → " + vd("ΔE<sup>e</sup> = −1%") + ". E cai: é "
            "preciso menos moeda A por moeda B — A se " + vd("aprecia") + ".",
            "Intuição: aplicar em A rende 1 p.p. a menos. Para que alguém aceite manter títulos de A, a moeda A "
            "precisa valorizar-se cerca de 1%, de modo que o retorno total em moeda comum seja o mesmo.",
            "Se o mercado esperasse depreciação de A, aplicar em A seria duplamente pior (juro menor e perda "
            "cambial): ninguém compraria títulos de A, e a paridade estaria violada.",
            "“Substitutos perfeitos” é a hipótese que elimina o prêmio de risco e autoriza a paridade descoberta "
            "pura.",
            vm("Regra-âncora: juro maior → depreciação esperada; juro menor → apreciação esperada."),
        ],
        "dissecando": (cz("[inversão]") + " O número (1%) está certo; o sentido está invertido. O examinador conta "
                       "com quem calcula o diferencial e atribui a depreciação ao país errado. Teste: a moeda de "
                       "<b>maior</b> juro é a que se espera que deprecie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o mercado prevê implicitamente que a moeda do país B irá se depreciar em relação à moeda do "
            "país A em cerca de 1% no próximo ano.”</i> → CERTO",
            "<i>“…prevê que a moeda do país A irá se apreciar em 11%.”</i> → ERRADO (dado alterado: somou as taxas "
            "em vez de subtrair)",
        ])],
        "reescrita": ("Supondo que os títulos dos países A e B sejam substitutos perfeitos e paguem, respectivamente, "
                      "5% a.a. e 6% a.a. de taxa de juros, então o mercado de câmbio prevê implicitamente que a "
                      "moeda do país A irá se " + hl("apreciar") + " em relação à moeda do país B em 1% no próximo "
                      "ano."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Paridade descoberta: ΔE<sup>e</sup> = 5% − 6% = −1%. Espera-se que a moeda do país A "
                             "se aprecie em 1% em relação à moeda do país B."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 214", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00638-1 (mesmo item em outra lista Nabuco)"],
    },
    # ------------------------------------------------------------------ E3-L00219 (cf. E1-0858)
    {
        "id": "ECO-E3-L00219-1", "fonte_ref": "E3-L00219", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": "Acerca da teoria do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Quando um país apresenta economias de escala em determinado setor, nem os preços dos "
                      "produtos nem a remuneração dos fatores são suficientes para prever o padrão de comércio com "
                      "seus parceiros comerciais. Isso ocorre porque a presença de rendimentos crescentes de escala "
                      "permite ao país reduzir os custos médios ao aumentar o volume produzido e isso fará com que "
                      "passe a ser exportador líquido dos produtos desse setor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando um país apresenta economias de escala em determinado setor, <u>nem os preços dos "
                      "produtos nem a remuneração dos fatores são suficientes</u> para prever o padrão de comércio "
                      "com seus parceiros comerciais. Isso ocorre porque a presença de rendimentos crescentes de "
                      "escala permite ao país reduzir os custos médios ao aumentar o volume produzido e isso fará "
                      "com que passe a ser exportador líquido dos produtos desse setor."),
        "poucas": ("Com " + azb("rendimentos crescentes") + ", quem produz mais tem custo médio menor: a "
                   "especialização pode ser decidida por " + vd("história, tamanho do mercado e pioneirismo")
                   + ", e não só por preços autárquicos ou dotações de fatores."),
        "destrinchando": [
            "Nos modelos clássicos (" + oc("Ricardo") + ", " + oc("Heckscher-Ohlin") + "), basta comparar "
            "preços relativos de autarquia (ou dotações e remunerações de fatores) para prever quem exporta "
            "o quê. Isso supõe " + azb("retornos constantes") + ".",
            "Com " + azb("economias de escala") + ", o custo médio cai com o volume. Quem sai na frente — por "
            "acaso histórico, mercado interno grande ou política industrial — ganha escala, barateia o produto "
            "e consolida a liderança (" + azb("vantagem do pioneiro") + ", " + azb("path dependence") + "). "
            "Dois países idênticos podem especializar-se de modos diferentes, e o padrão resultante não se "
            "deduz dos fundamentos iniciais.",
            "Exemplos clássicos: a indústria de relógios na Suíça, o polo de semicondutores no Vale do Silício, "
            "a disputa Airbus × Boeing — vantagens " + azb("criadas") + ", e não herdadas.",
            "Base teórica: " + oc("Paul Krugman") + " (1979, 1980; Nobel " + vd("2008") + "), com escala "
            "interna e concorrência monopolística; " + azb("economias externas") + " (clusters) produzem o mesmo "
            "efeito de travamento. É também o fundamento da " + azb("política comercial estratégica") + ".",
            "Leitura do “fará com que passe a ser exportador líquido”: é a tendência do modelo para o país que "
            "obtém a escala no setor; o essencial do item é a imprevisibilidade a partir de preços e fatores.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item afirma que os determinantes clássicos "
                       "“não bastam”, o que soa como heresia para quem estudou só H-O — e é a tese da nova "
                       "teoria. O “nem… nem…” não é modulador absoluto aqui: diz que não são suficientes, não "
                       "que são irrelevantes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com economias de escala, o padrão de comércio é integralmente determinado pela dotação relativa "
            "de fatores.”</i> → ERRADO (contradição: a escala e a história também decidem)",
            "<i>“Na presença de rendimentos crescentes, países com dotações idênticas podem ter ganhos com o "
            "comércio ao se especializarem em produtos diferentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["nem… nem…", "suficientes"],
        "dificuldade": 2,
        "comentario_fonte": ("Base da nova teoria do comércio (Krugman): com economias de escala, o comércio não é "
                             "determinado por vantagens comparativas (dotação de fatores), mas pela história ou por "
                             "acidentes históricos que permitiram a uma indústria crescer primeiro, reduzir custos e "
                             "dominar o mercado global (vantagem do pioneiro)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0858-1, ECO-E3-L00257-1 (mesmo item em outros simulados)",
                    "texto_corrigido: OCR da fonte (“economías”, “liquido”) corrigido para “economias”, “líquido”"],
    },
    # ------------------------------------------------------------------ E3-L00257 (cf. E1-0858)
    {
        "id": "ECO-E3-L00257-1", "fonte_ref": "E3-L00257", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": ("No que diz respeito à Teoria do Comércio Internacional, julgue certo ou errado (C ou E) o "
                    "item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Quando um país apresenta economias de escala em determinado setor, nem os preços dos "
                      "produtos nem a remuneração dos fatores são suficientes para prever o padrão de comércio com "
                      "seus parceiros comerciais. Isso ocorre porque a presença de rendimentos crescentes de escala "
                      "permite ao país reduzir os custos médios ao aumentar o volume produzido e isso fará com que "
                      "passe a ser exportador líquido dos produtos desse setor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando um país apresenta economias de escala em determinado setor, <u>nem os preços dos "
                      "produtos nem a remuneração dos fatores são suficientes</u> para prever o padrão de comércio "
                      "com seus parceiros comerciais. Isso ocorre porque a presença de rendimentos crescentes de "
                      "escala permite ao país reduzir os custos médios ao aumentar o volume produzido e isso fará "
                      "com que passe a ser exportador líquido dos produtos desse setor."),
        "poucas": ("Com " + azb("rendimentos crescentes") + ", quem produz mais tem custo médio menor: a "
                   "especialização pode ser decidida por " + vd("história, tamanho do mercado e pioneirismo")
                   + ", e não só por preços autárquicos ou dotações de fatores."),
        "destrinchando": [
            "Nos modelos clássicos (" + oc("Ricardo") + ", " + oc("Heckscher-Ohlin") + "), basta comparar "
            "preços relativos de autarquia (ou dotações e remunerações de fatores) para prever quem exporta "
            "o quê. Isso supõe " + azb("retornos constantes") + ".",
            "Com " + azb("economias de escala") + ", o custo médio cai com o volume. Quem sai na frente — por "
            "acaso histórico, mercado interno grande ou política industrial — ganha escala, barateia o produto "
            "e consolida a liderança (" + azb("vantagem do pioneiro") + ", " + azb("path dependence") + "). "
            "Dois países idênticos podem especializar-se de modos diferentes, e o padrão resultante não se "
            "deduz dos fundamentos iniciais.",
            "Exemplos clássicos: a indústria de relógios na Suíça, o polo de semicondutores no Vale do Silício, "
            "a disputa Airbus × Boeing — vantagens " + azb("criadas") + ", e não herdadas.",
            "Base teórica: " + oc("Paul Krugman") + " (1979, 1980; Nobel " + vd("2008") + "), com escala "
            "interna e concorrência monopolística; " + azb("economias externas") + " (clusters) produzem o mesmo "
            "efeito de travamento. É também o fundamento da " + azb("política comercial estratégica") + ".",
            "Leitura do “fará com que passe a ser exportador líquido”: é a tendência do modelo para o país que "
            "obtém a escala no setor; o essencial do item é a imprevisibilidade a partir de preços e fatores.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item afirma que os determinantes clássicos "
                       "“não bastam”, o que soa como heresia para quem estudou só H-O — e é a tese da nova "
                       "teoria. O “nem… nem…” não é modulador absoluto aqui: diz que não são suficientes, não "
                       "que são irrelevantes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com economias de escala, o padrão de comércio é integralmente determinado pela dotação relativa "
            "de fatores.”</i> → ERRADO (contradição: a escala e a história também decidem)",
            "<i>“Na presença de rendimentos crescentes, países com dotações idênticas podem ter ganhos com o "
            "comércio ao se especializarem em produtos diferentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["nem… nem…", "suficientes"],
        "dificuldade": 2,
        "comentario_fonte": ("Crítica aos modelos de abundância de fatores: com economias de escala, preços e "
                             "fatores não bastam; custos médios caem com a produção; acidentes históricos, política "
                             "industrial e tamanho do mercado doméstico decidem; dois países idênticos podem se "
                             "especializar de modo diferente (nova teoria do comércio, Krugman, 1979)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0858-1, ECO-E3-L00219-1 (mesmo item em outros simulados)"],
    },
    # ------------------------------------------------------------------ E3-L00274 (cf. E1-0464)
    {
        "id": "ECO-E3-L00274-1", "fonte_ref": "E3-L00274", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": "Acerca do sistema monetário internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na Conferência de Bretton Woods, Keynes, como representante do Reino Unido, teve papel "
                      "ativo e central na construção de uma governança financeira global. Nessa conferência, Keynes "
                      "sugeriu um regime de taxas de câmbio flutuantes como forma de apoiar o crescimento do "
                      "comércio internacional, que foi fundamental para a recuperação econômica do pós-guerra."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na Conferência de Bretton Woods, Keynes, como representante do Reino Unido, teve papel "
                       "ativo e central na construção de uma governança financeira global. Nessa conferência, "
                       "Keynes sugeriu um regime de taxas de câmbio ") + vm("flutuantes")
                    + az(" como forma de apoiar o crescimento do comércio internacional, que foi fundamental para "
                         "a recuperação econômica do pós-guerra.")),
        "poucas": ("Keynes e White defendiam " + azb("câmbio fixo, porém ajustável") + " (<i>adjustable peg</i>). "
                   "A diferença entre eles estava no meio de liquidação: " + vd("bancor") + " (Keynes) × "
                   + vd("dólar conversível em ouro") + " (White)."),
        "destrinchando": [
            "Contexto: a experiência dos anos 1930 — desvalorizações competitivas (“empobrecer o vizinho”), "
            "controles, blocos comerciais, colapso do comércio — convenceu britânicos e americanos de que o "
            "pós-guerra exigia " + azb("estabilidade cambial") + " com alguma flexibilidade. Ninguém, em 1944, "
            "propunha flutuação generalizada.",
            azb("Plano Keynes") + " (Reino Unido): " + vd("União Internacional de Compensação") + " (<i>International "
            "Clearing Union</i>), com uma moeda contábil supranacional, o " + vd("bancor") + "; saldos de "
            "deficitários e superavitários penalizados de forma <b>simétrica</b>; grandes facilidades de "
            "saque. Interesse de um país devedor e com reservas escassas.",
            azb("Plano White") + " (EUA, " + oc("Harry Dexter White") + "): um fundo de estabilização com "
            "cotas, recursos limitados, ajuste a cargo do deficitário e o dólar conversível em ouro no centro. "
            "Interesse do grande credor. Prevaleceu: daí o " + azb("FMI") + " e o padrão " + vd("ouro-dólar")
            + " (US$ 35 por onça).",
            "O regime acordado: paridades fixas em relação ao dólar (margem de 1%), alteráveis em caso de "
            + azb("desequilíbrio fundamental") + " do balanço de pagamentos, com consulta ao FMI; controles de "
            "capital permitidos. A flutuação generalizada só veio com o colapso do sistema (1971–1973) e foi "
            "legalizada pelos Acordos da Jamaica (1976).",
            "A primeira oração do item está certa: " + oc("Keynes") + " chefiou a delegação britânica e foi o "
            "principal formulador intelectual da conferência, ainda que derrotado no desenho final.",
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " Primeira frase verdadeira (o papel de "
                       "Keynes), segunda com o regime trocado. Pista: o objetivo declarado em Bretton Woods era "
                       "<b>evitar</b> a instabilidade cambial do entreguerras; “flutuante” contradiz o próprio "
                       "espírito da conferência. 🔥 Itens sobre os planos costumam trocar bancor × dólar ou "
                       "inverter Keynes × White."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tanto o plano de Keynes quanto o de White previam taxas de câmbio fixas, mas ajustáveis.”</i> → "
            "CERTO",
            "<i>“O plano de Keynes atribuía exclusivamente aos países deficitários o ônus do ajuste externo.”</i> "
            "→ ERRADO (inversão: o ajuste seria simétrico; o ônus no deficitário era a lógica do plano White)",
        ])],
        "reescrita": ("Na Conferência de Bretton Woods, Keynes, como representante do Reino Unido, teve papel ativo "
                      "e central na construção de uma governança financeira global. Nessa conferência, Keynes "
                      "sugeriu um regime de taxas de câmbio " + hl("fixas, porém ajustáveis,") + " como forma de "
                      "apoiar o crescimento do comércio internacional, que foi fundamental para a recuperação "
                      "econômica do pós-guerra."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Keynes defendeu câmbio fixo, porém ajustável (adjustable peg), e uma moeda contábil "
                             "internacional (bancor) numa união de compensação; White propôs o dólar conversível em "
                             "ouro. Flutuação contrariava o objetivo de evitar as desvalorizações competitivas dos "
                             "anos 1930 (vários comentários empilhados, convergentes)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 380", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 381", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia o enunciado)"}],
        "alertas": ["quase_duplicata: ECO-E1-0464-1 (mesmo item em outra prova)",
                    "quase_duplicata: ECO-E2-L00361-1, ECO-E2-L00486-1 (planos Keynes × White)",
                    "nota_redacao: a frente traz o enunciado-base da “Questão 61” truncado na fonte; comando "
                    "neutro"],
    },
    # ------------------------------------------------------------------ E3-L00292 (cf. E1-0372)
    {
        "id": "ECO-E3-L00292-1", "fonte_ref": "E3-L00292", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Tendo em vista que o movimento internacional de capitais tem recebido grande atenção da "
                    "literatura, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Embora sejam determinantes expressivos do desempenho econômico dos países, as tendências, "
                      "flutuações e composição dos fluxos internacionais de capitais têm baixíssimo impacto nas "
                      "diretrizes ou escolhas de política econômica em uma economia aberta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Embora sejam determinantes expressivos do desempenho econômico dos países, as tendências, "
                       "flutuações e composição dos fluxos internacionais de capitais têm ") + vm("baixíssimo")
                    + az(" impacto nas diretrizes ou escolhas de política econômica em uma economia aberta.")),
        "poucas": ("Em economia aberta, os fluxos de capitais " + azb("condicionam") + " a política econômica: "
                   "afetam câmbio, juros, inflação, reservas e custo da dívida, e restringem a autonomia "
                   "monetária (" + azb("trilema") + ")."),
        "destrinchando": [
            "Contabilmente, o fluxo de capital é a " + azb("poupança externa") + " que financia o déficit em "
            "transações correntes: S + (M − X) = I. Quando o fluxo seca, o país precisa gerar superávit "
            "externo à força — com desvalorização e recessão.",
            azb("Trilema") + " (trindade impossível, a partir de " + oc("Mundell-Fleming") + "): não se têm, ao "
            "mesmo tempo, câmbio fixo, livre mobilidade de capitais e política monetária autônoma. Com capital "
            "livre, ou o câmbio flutua (e os fluxos movem o câmbio) ou os juros ficam presos aos externos.",
            "A " + azb("composição") + " importa: IED é estável; portfólio e dívida de curto prazo são voláteis "
            "e sujeitos a " + azb("sudden stops") + ". Muita dívida de curto prazo em moeda estrangeira "
            "aumenta a vulnerabilidade e exige mais reservas.",
            "Na prática, os governos reagem aos fluxos: juros altos para atrair ou reter capital, intervenções "
            "e swaps cambiais, acúmulo de reservas, medidas macroprudenciais, controles de capital (o "
            + rx("IOF sobre ingressos de 2009–2013, no Brasil") + "), comunicação com os mercados. O "
            + azb("fear of floating") + " (" + oc("Calvo e Reinhart") + ") mostra países que dizem flutuar mas "
            "intervêm por medo dos efeitos cambiais.",
            vm("Regra-âncora: com mobilidade de capitais, os fluxos externos restringem as escolhas de "
               "política monetária, cambial e fiscal."),
        ],
        "dissecando": (cz("[contradição · juízo indevido]") + " A concessiva inicial é verdadeira e prepara a "
                       "armadilha: se os fluxos determinam o desempenho econômico, não podem ser irrelevantes "
                       "para a política econômica. O superlativo “baixíssimo” entrega o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com livre mobilidade de capitais e câmbio fixo, a política monetária perde autonomia.”</i> → "
            "CERTO",
            "<i>“A composição dos fluxos de capitais é irrelevante para a vulnerabilidade externa, que depende "
            "apenas do volume total.”</i> → ERRADO (dívida de curto prazo é mais volátil que IED)",
        ])],
        "reescrita": ("Embora sejam determinantes expressivos do desempenho econômico dos países, as tendências, "
                      "flutuações e composição dos fluxos internacionais de capitais têm " + hl("elevado")
                      + " impacto nas diretrizes ou escolhas de política econômica em uma economia aberta."),
        "tipo_erro": ["CONTRADICAO", "JUIZO_INDEVIDO"], "moduladores": ["baixíssimo"], "dificuldade": 1,
        "comentario_fonte": ("Em economia aberta, os fluxos de capitais condicionam fortemente a política "
                             "econômica (trilema de Mundell-Fleming): afetam câmbio, juros, inflação, reservas, "
                             "regulação prudencial e controles de capital; a composição (IED × carteira × dívida de "
                             "curto prazo) altera a vulnerabilidade a sudden stops."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 401", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia o enunciado)"}],
        "alertas": ["quase_duplicata: ECO-E1-0372-1 (mesmo item em outra prova)",
                    "nota_redacao: item 3 da “Questão 65” do simulado; o enunciado-base vem truncado na fonte"],
    },
    # ------------------------------------------------------------------ E3-L00293 (cf. E1-0373)
    {
        "id": "ECO-E3-L00293-1", "fonte_ref": "E3-L00293", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Tendo em vista que o movimento internacional de capitais tem recebido grande atenção da "
                    "literatura, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Um dos problemas mais preocupantes do movimento internacional de capital ocorre quando a "
                      "saída dos fluxos se dá repentinamente, pressionando o câmbio e colocando em risco a "
                      "manutenção da estabilidade financeira. Em países que fizeram a liberalização financeira "
                      "com implementação de políticas para limitar o excesso de volatilidade, as regulações "
                      "prudenciais desempenham papel fundamental e preventivo na contenção desses riscos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um dos problemas mais preocupantes do movimento internacional de capital ocorre quando a "
                      "saída dos fluxos se dá <u>repentinamente</u>, pressionando o câmbio e colocando em risco a "
                      "manutenção da estabilidade financeira. Em países que fizeram a liberalização financeira "
                      "com implementação de políticas para limitar o excesso de volatilidade, as "
                      "<u>regulações prudenciais</u> desempenham papel fundamental e <u>preventivo</u> na "
                      "contenção desses riscos."),
        "poucas": ("A " + azb("parada súbita") + " (sudden stop) deprecia o câmbio e ameaça bancos e empresas "
                   "endividados em moeda estrangeira; a " + azb("regulação prudencial") + " reduz o acúmulo de "
                   "riscos no boom e amortece a reversão."),
        "destrinchando": [
            azb("Sudden stop") + " (" + oc("Guillermo Calvo") + "): interrupção abrupta dos ingressos, ou fuga, "
            "após uma onda de entrada. O câmbio dispara; quem tem dívida em dólar e receita em moeda local "
            "(" + azb("descasamento cambial") + ") vê o passivo crescer de uma vez; o crédito seca; bancos e "
            "empresas quebram.",
            "Canais para a estabilidade financeira: inflação pela desvalorização, balanços com dívida em moeda "
            "estrangeira, queda do preço dos ativos, aperto de liquidez. Exemplos: México (1994–95), Ásia "
            "(1997), Rússia (1998), " + rx("Brasil (1999)") + ", Argentina (2001).",
            azb("Regulação prudencial e macroprudencial") + ": limites à posição cambial dos bancos, "
            "requerimentos de capital e de liquidez (Basileia), compulsórios sobre captações externas, "
            "restrições ao descasamento, colchões contracíclicos. Atua <b>antes</b> da crise, contendo o "
            "endividamento arriscado nos anos de bonança.",
            "Casos citados: o " + azb("encaje") + " chileno dos anos 1990 (depósito não remunerado sobre "
            "ingressos de curto prazo); no " + rx("Brasil") + ", IOF sobre ingressos e compulsório sobre "
            "posições vendidas em câmbio dos bancos (2009–2011), além de swaps cambiais e reservas elevadas. "
            "Em 2012 o " + azb("FMI") + " passou a aceitar medidas de gestão de fluxos de capital em certas "
            "circunstâncias (<i>institutional view</i>).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item longo e descritivo, com moduladores moderados (“um dos "
                       "problemas”, “papel fundamental”). A banca costuma errar trocando “preventivo” por "
                       "“exclusivamente corretivo” ou dizendo que a liberalização eliminou o risco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma vez concluída a liberalização financeira, as regulações prudenciais tornam-se "
            "dispensáveis, pois o mercado disciplina a volatilidade.”</i> → ERRADO (juízo indevido)",
            "<i>“Descasamentos cambiais em balanços de bancos e empresas amplificam os efeitos de uma parada "
            "súbita de capitais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["um dos", "fundamental"], "dificuldade": 1,
        "comentario_fonte": ("Sudden stops (Calvo) pressionam o câmbio, encarecem o financiamento externo e, com "
                             "descasamento cambial, ameaçam bancos e empresas; regulações prudenciais e "
                             "macroprudenciais (exigências de capital, limites de posição cambial, encajes como no "
                             "Chile, Brasil pós-2008) atuam preventivamente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0373-1 (mesmo item em outra prova)",
                    "nota_redacao: item 4 da “Questão 65” do simulado; o enunciado-base vem truncado na fonte"],
    },
    # ------------------------------------------------------------------ E3-L00466 (cf. E1-0933)
    {
        "id": "ECO-E3-L00466-1", "fonte_ref": "E3-L00466", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": ("No que se refere à economia internacional e suas teorias de comércio, julgue o item a "
                    "seguir."),
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
        "comentario_fonte": ("Com câmbio flexível (Mundell-Fleming), a tarifa reduz importações só de início; a "
                             "entrada de divisas aprecia a moeda, barateia os demais importados e fere as "
                             "exportações, anulando o ganho; no longo prazo o saldo é dado por S − I = NX. Efeitos "
                             "de curto prazo anulados no longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 669", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 670", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (sequência IS-LM-BP descrita no 📖)"},
                          {"ref": "IMAGEM 671", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia o enunciado)"}],
        "alertas": ["quase_duplicata: ECO-E1-0933-1 (mesmo item em outra prova)",
                    "quase_duplicata: ECO-E2-L00186-1, ECO-E1-0909-1 (tarifa neutralizada pelo câmbio)"],
    },
    # ------------------------------------------------------------------ E3-L00467 (cf. E1-0904)
    {
        "id": "ECO-E3-L00467-1", "fonte_ref": "E3-L00467", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Acerca das teorias de comércio internacional e do sistema multilateral de comércio, julgue o "
                    "item a seguir."),
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
        "comentario_fonte": ("Art. XXIV do GATT 1994 (e art. V do GATS): acordos regionais são exceção admitida à "
                             "nação mais favorecida, desde que cubram “substancialmente todo o comércio” entre as "
                             "partes (não a totalidade das linhas tarifárias) e não elevem barreiras contra "
                             "terceiros; exceções setoriais limitadas (agrícolas sensíveis) são aceitas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 672", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E1-0904-1 (mesmo item em outra prova)"],
    },
]
