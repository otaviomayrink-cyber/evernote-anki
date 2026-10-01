# PROMPT — Consolidação das Notas de Questões Objetivas (-Q) — v3
*v3 = v2 + figuras e gráficos (Folha -Q v3 §10 e Protocolo de Gráficos v1). Trechos novos marcados com 📈.*

Você é meu editor-chefe na reforma do meu caderno de estudos para o CACD e concursos correlatos (banca principal: CEBRASPE). Anexei:

1. o(s) arquivo(s) com as questões objetivas de {MATÉRIA — SIGLA} — `.md` já convertido (imagens transcritas em `[[IMAGEM n · TIPO: X]]`) e/ou `.html` exportado do Evernote (imagens só referenciadas); a maioria já traz comentário;
2. a Folha de Estilo das Notas de Questões **v3** — seguir integralmente;
3. a Especificação do JSONL e do Relatório **v2** — seguir integralmente;
4. a Folha de Estilo v9 (HTML seguro, ENEX, cores, emojis), que complementa a Folha -Q;
5. 📈 o **Protocolo de Gráficos v1** e o zip `questoes/` (scripts `qgraf.py`, `modelos.py`, `montar_nota_q.py`, `verificar_q.py`, `inventariar_figuras.py`) — seguir integralmente;
6. (opcional) ficha de bibliografia da matéria (obras e autores-chave);
7. (opcional, a partir da 2ª passada) o plano do lote (`{SIGLA}-Q_plano.json`), os JSONL das passadas anteriores e o zip de scripts e specs da passada anterior;
8. (opcional) HTMLs ou ENEX de notas -Q já existentes, que devem receber o material novo sem duplicar;
9. 📈 (opcional) as imagens de frente reenviadas, com os nomes da lista `{SIGLA}-Q_imagens_a_reenviar.csv`.

PARÂMETROS DO LOTE (preencha)

* Matéria / sigla: {ex.: Economia — ECO}
* Bancas prioritárias: {ex.: CEBRASPE (CACD); demais como multibanca}
* Itens de outras matérias: {direcionar se estiverem no índice | mandar para 🧹 Triagem}
* Notas -Q já existentes a mesclar: {nenhuma | lista}
* Referência temporal: {ex.: legislação e dados vigentes em out/2026; marcar ⏳ o que envelheceu}
* 📈 Tabela da frente: {HTML aninhada | PNG} — conforme o teste de importação (Protocolo §7); até o teste, HTML
* Passada atual: {Fase 0 | Fase 0.5 | passada NN}

ÍNDICE DA MATÉRIA (mapa de destino)
Cada linha: `id — emoji Título`. O título da nota -Q no Evernote será `{id}-1 - Obj.`.

```
COLAR AQUI O ÍNDICE DA MATÉRIA

```

O QUE FAZER
O arquivo pode vir bagunçado: a numeração e o título das notas antigas não indicam o tema. Trate o arquivo inteiro como um blocão único e direcione cada item pelo conteúdo que ele testa (Folha -Q §8).

FASE 0 — Diagnóstico e plano (aguarde minha aprovação)
Rodada sobre o arquivo inteiro, mesmo que a execução vá em várias passadas.

* (a) Inventário: nº de questões e de itens julgáveis após desmembramento; distribuição por banca, tipo (C/E, ME, EXERC, DISC) e origem (CACD × demais); com e sem gabarito; com e sem comentário; itens marcados ❌; duplicatas prováveis.
* (a-bis) 📈 Inventário de figuras (script `inventariar_figuras.py`): imagens por lado (frente/verso) e tipo; ação sugerida para cada uma (Protocolo §2); itens cuja frente depende de figura; **lista de imagens de frente a reenviar** (`{SIGLA}-Q_imagens_a_reenviar.csv`), com nome do arquivo e o começo do verso para eu localizar.
* (b) Mapa de destino: tabela `nota → nº de itens → H2 propostos`, incluindo a 🧹 Triagem com o motivo de cada item e os itens de outras matérias.
* (c) Problemas: textos motivadores irrecuperáveis, gabaritos ausentes ou contestáveis, itens possivelmente desatualizados; 📈 figuras de frente irrecuperáveis sem reenvio e transcrições de imagem insuficientes para julgar o item.
* (d) Plano de passadas: divisão em passadas de 600 a 800 itens, seguindo os blocos do índice, com a estimativa de sessões. 📈 Notas muito gráficas (ex.: oferta e demanda, IS-LM) contam em dobro na estimativa de esforço.
* (e) Entregáveis da Fase 0: `{SIGLA}-Q_mapa_de_itens.csv` (item → destino, subtema, banca, gabarito, alertas, 📈 figuras da frente e ação), `{SIGLA}-Q_plano.json` (lista fixa de H2 por nota e itens de cada passada) e os dois CSV de figuras.

FASE 0.5 — Amostra de teste (aguarde minha aprovação)
Antes de executar qualquer passada completa:

* Produza 12 a 15 cards cobrindo: C/E certo; C/E errado (inclusive uma meia-verdade); ME; item do CACD; item polêmico ou anulado; item com texto motivador longo; item ❌; e, entre eles, ao menos uma vez cada módulo que a matéria costuma pedir.
* 📈 Na matéria com figuras, a amostra cobre também: gráfico na frente (fiel e conjectural); gráfico didático no verso; tabela na frente (HTML aninhada **e** PNG, um card de cada); dados reais em barras; fórmula transcrita; enunciado reconstruído.
* Entregue em uma nota HTML e um ENEX de teste (título `00-TESTE-1 - Obj.`), mais as linhas correspondentes do JSONL e a 📈 galeria das figuras (`galeria.html`).
* O ENEX de teste serve também para eu verificar, na importação real, se a linha de separação `<hr/>` dentro da célula sobrevive (Folha -Q §3.2 ③) e 📈 o checklist do Protocolo §7 (imagens, larguras, tabela HTML × PNG, legibilidade no celular). Se algo não sobreviver, adote a alternativa prevista.
* Eu aprovo ou peço ajustes em uma linha; ajustes aprovados valem para todas as passadas.

FASE 1 — Execução da passada (autônoma, sem me pedir "siga")

1. Extração estruturada no JSONL (Especificação §2), um registro por item. Desmembre questões com vários itens; recupere textos motivadores referidos; deduplique. 📈 Registre `figuras_fonte` de cada item.
2. Gabarito: o oficial da fonte. Sem gabarito: resolva e marque `gabarito_origem: resolvido`. Gabarito que parece errado: mantenha o oficial e registre ⚠️; se o gabarito do meu caderno diverge do oficial comprovado, vale o oficial (`gabarito_origem: oficial`). Pesquise quando precisar (lei, jurisprudência, doutrina, dado, gabarito definitivo).
3. Redação dos cards (Folha -Q §3–§5):
   * verso = gabarito → assertiva anotada (azul/vermelho) → separação → 🎯 → (⚠️ ⏳ 🏛️) → 📖 Destrinchando o tema → 📈 No gráfico (se houver) → 🧐 Dissecando a redação → módulos (0 a 3) → ✍️ Reescrita correta por último;
   * comentário recheado segundo as três perguntas da Folha -Q §5, calibrado pelo tamanho do item;
   * o comentário da fonte é insumo: aproveite, corrija, amplie, funda — não reproduza a assertiva no comentário;
   * taxonomia (§4) em todo C/E e ME;
   * marca ❌ preservada antes do cabeçalho.
4. 📈 Figuras (Folha -Q §10; Protocolo §1–§6):
   * decida a ação de cada imagem (Protocolo §2) e aplique o teste do quadro-negro aos gráficos de verso (máx. 1 por card);
   * escreva uma **spec JSON** por figura (nunca código de plotagem), com `legenda`, `fidelidade` e, no verso, as `checar` do que o comentário afirma; prefira os modelos prontos;
   * rode `qgraf.py` até zerar erros; checagem que falha → reveja o **comentário** antes do desenho;
   * **abra e confira cada PNG** (Protocolo §6): 100% das figuras de frente; no verso, 100% nas duas primeiras passadas da matéria, depois 30%;
   * tabelas da frente: transcreva e confira as identidades; incoerência → corrija e registre `transcricao_incoerente`;
   * frente que era só imagem: use a imagem reenviada; sem ela, reconstrua só com segurança (`texto_reconstruido`) ou mande para a 🧹 Triagem.
5. Montagem de uma nota -Q por destino (índice com contagens, H2 do plano, ordem de bancas) com `montar_nota_q.py`. Se houver nota -Q existente, mescle sem apagar nem duplicar.
6. Verificação:
   * `verificar_q.py` (contrato da Folha -Q §9, incluindo os itens 14–19 de figuras, e Especificação §5) em todas as notas, até zerar os alertas;
   * revisão independente por amostragem de ~10% dos cards (gabarito, fidelidade, conteúdo);
   * revisão de todas as reescritas dos itens ERRADO e de todas as assertivas anotadas dos ERRADO (os trechos vermelhos correspondem exatamente ao que a reescrita corrige?);
   * 📈 revisão visual das figuras conforme o item 4.
7. Entrega da passada:
   * um HTML e um `.enex` por nota -Q, com título `{id}-1 - Obj.`, sem tags, XML validado, 📈 figuras embutidas;
   * um `.enex` consolidado da passada;
   * `{SIGLA}-Q_passada{NN}.jsonl` (com `figuras[].spec`);
   * zip com os scripts, os arquivos-fonte dos cards, 📈 as specs, os PNG e a galeria;
   * mini-relatório de passada (Especificação §4.1), 📈 com o bloco de figuras.

FASE 2 — Fechamento do lote (na última passada, ou numa sessão própria com todos os JSONL anexados)

1. Unir os JSONL das passadas em `{SIGLA}-Q_mestre.jsonl` e verificar (Especificação §5).
2. Gerar o 📊 Relatório do lote (Especificação §4.2, 📈 incluindo o 6-bis) e as 🎓 Lições do lote (§4.3), com todos os números calculados por script.
3. Entregar os dois relatórios e o JSONL-mestre.

REGRAS INVIOLÁVEIS

* Card autossuficiente: nada de "o texto acima" ou "a questão anterior".
* Nenhum item é descartado silenciosamente. O que não couber vai para a 🧹 Triagem; o que for ilegível é listado nela.
* Não invente dados de prova (órgão, ano, cargo), autores, obras ou citações. Sem dado, omita.
* Fidelidade à assertiva e ao gabarito oficiais. Correções ficam no comentário, nunca no enunciado.
* Marca ❌ da fonte preservada, antes do cabeçalho, sem trocar o emoji.
* ✍️ Reescrita correta sempre como último bloco do verso.
* HTML seguro para Evernote (Folha v9 §8); tabela de 2 colunas a 1400px.
* Tabela sem linha de título: nada de primeira linha "Enunciado | Resposta" ou "Frente | Verso", nem `<th>`/`<thead>`. Toda linha vira flashcard, então a tabela começa direto pela primeira questão.
* Título da nota no ENEX: `{id}-1 - Obj.` — e só isso.
* 📈 Nenhuma imagem de terceiros e nenhum `[Imagem não reproduzida]` em card: figura é redesenho próprio a partir de spec, ou o item vai para a Triagem.
* 📈 A figura da frente não entrega o gabarito; a do verso só entra se passar no teste do quadro-negro.
* 📈 Dados de gráfico só da fonte ou de fonte oficial citada; figura deduzida é sempre marcada como conjectural.
