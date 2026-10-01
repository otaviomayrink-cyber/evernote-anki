# 🗃️ Especificação do JSONL e do Relatório — Notas de Questões (-Q) — v2
*Complementa a Folha -Q v3 e o Protocolo de Gráficos v1. Define a base de dados de itens (JSONL), os relatórios de passada e de lote e as lições. Anexar a todo prompt de consolidação de questões.*

**Novidades da v2**: campos `figuras` e `figuras_fonte` (§2.1); alertas `texto_reconstruido`, `banca_provavel`, `figura_conjectural`, `figura_irrecuperavel`, `transcricao_incoerente`, `teste_importacao`, `qualidade_fonte`; `versao_folha = "Q-v3"`; relatórios e verificação com as figuras (§4, §5).

---

## 1. O que é o JSONL
- **Não é um relatório; é a base de dados.** Um arquivo de texto com **uma linha por item**, cada linha um objeto JSON com todos os campos do item.
- Tudo sai dele: as notas -Q (HTML e ENEX), o relatório e as lições. Se a Folha mudar, as notas podem ser regeneradas a partir do JSONL sem reescrever o conteúdo.
- É **acumulativo**: cada passada produz um JSONL; no fim do lote, eles se juntam num JSONL-mestre da matéria; com o tempo, os mestres formam a base do caderno inteiro.

**Nomes de arquivo**
- Por passada: `{SIGLA}-Q_passada{NN}.jsonl` (ex.: `HB-Q_passada03.jsonl`)
- Mestre da matéria: `{SIGLA}-Q_mestre.jsonl`
- Codificação UTF-8; um objeto por linha; sem vírgula entre linhas.

## 2. Campos
| Campo | Tipo | Valores / regra |
|---|---|---|
| `id` | texto | `{SIGLA}-{linha de origem}-{n}` — ex.: `HB-R0123-1`. Único em todo o caderno. |
| `materia` | texto | Sigla da v9: PORT, HB, HM, PI, DIP, ECO, GEO, D.CONST, D.ADMIN… |
| `passada` | inteiro | Nº da passada que produziu o item |
| `versao_folha` | texto | `Q-v3` |
| `nota_destino` | texto | Id da nota (ex.: `07-A`) ou `TRIAGEM` |
| `subtema` | texto | Nome do H2 (sem emoji) |
| `tipo` | texto | `C/E` · `ME` · `EXERC` · `DISC` |
| `banca` | texto | Normalizada (Folha -Q §3.1) |
| `prova` | texto | `Órgão/Cargo/Ano` como na fonte, ou vazio |
| `ano` | inteiro/nulo | Ano da prova |
| `cacd` | booleano | Item de prova do CACD/IRBr (inclui TPS e Bolsa-Prêmio) |
| `errei` | booleano | Vinha marcado com ❌ na fonte |
| `comando` | texto | Comando completo |
| `excerto` | HTML | Texto motivador recortado |
| `assertiva` | HTML | Assertiva ou enunciado + alternativas, fiel |
| `gabarito` | texto | `CERTO` · `ERRADO` · `ANULADO` · `A`–`E` · `RESPOSTA` |
| `gabarito_origem` | texto | `fonte` · `oficial` (fonte do caderno divergia e prevaleceu o oficial) · `resolvido` (fonte sem gabarito) |
| `status` | texto | `normal` · `contestavel` · `anulado` · `alterado` (gabarito oficial mudou) · `desatualizado` |
| `tipo_erro` | lista | 1–2 códigos da taxonomia (Folha -Q §4), o principal primeiro; na ME, o da alternativa-chave |
| `moduladores` | lista | Palavras-gatilho da assertiva: "sempre", "apenas", "pode", "em regra"… |
| `dificuldade` | inteiro | 1 (direto) · 2 (exige domínio) · 3 (fino, polêmico ou raro) — estimada |
| `modulos` | lista | Módulos opcionais usados: `panorama`, `autores`, `base_normativa`, `brasil`, `mnemonico`, `para_dificultar`, `carta_manga` |
| `autores` | lista | Autores e obras citados no comentário |
| `normas` | lista | Dispositivos citados (ex.: "CF/88, art. 4º, IX") |
| `temas_discursiva` | lista | Temas de discursiva para os quais o item fornece argumento (frases curtas) |
| `comentario_fonte` | texto | Resumo fiel do comentário original (vazio se não havia) |
| `qualidade_fonte` | texto | `bom` · `raso` · `com_erro` · `ausente` |
| `verso_html` | HTML | Verso completo, como renderizado |
| `alertas` | lista | `contestavel: …` · `texto_parcial: …` · `texto_irrecuperavel: …` · `texto_reconstruido: …` · `banca_confirmada: …` · `banca_provavel: …` · `destino_sugerido: …` · `redirecionado: …` · `duplicata: …` · `figura_conjectural: …` · `figura_irrecuperavel: …` · `transcricao_incoerente: …` · `teste_importacao: …` · `qualidade_fonte: …` (erro do comentário de origem que vale registrar) · `quase_duplicata: …` (item irmão de outra prova/redação, com o id) · `texto_corrigido: …` (erro evidente de digitação corrigido na assertiva) · `dado_aproximado: …` (regra de bolso ou número sem fonte oficial) · `nota_redacao: …` (observação editorial que não cabe nos tipos anteriores) |
| `figuras` | lista | Figuras **do card** (§2.1) |
| `figuras_fonte` | lista | Imagens **da fonte** e o destino de cada uma (§2.1) |

### 2.1 Figuras
Cada elemento de `figuras` (o que está no card):
| Campo | Valor |
|---|---|
| `id` | `{id do item}-F{n}` (frente) ou `-V{n}` (verso); figura compartilhada leva o id do primeiro item |
| `lado` | `frente` · `verso` |
| `tipo` | `modelo` · `paineis` · `dados` · `tabela` · `formula` |
| `fidelidade` | `fiel` · `conjectural` · `didatica` |
| `legenda` | a legenda exibida no card |
| `md5` | hash do PNG (o mesmo do `<en-media>`) |
| `png` | nome do arquivo |
| `spec` | a spec JSON completa — **é a fonte**: com ela a figura é re-renderizada sem a IA |

Cada elemento de `figuras_fonte` (o que havia na fonte): `ref` (ex.: `IMAGEM 109`, `image (4).png`), `tipo_fonte` (`GRÁFICO`, `DIAGRAMA`, `TABELA`, `FÓRMULA`, `TEXTO`, `MAPA`, `DECORATIVA`, `QUESTÃO EM IMAGEM`), `lado`, `acao` (`redesenhada` · `transcrita_html` · `texto` · `absorvida` · `cortada` · `irrecuperavel`, com observação entre parênteses quando útil).

## 3. Como usar o JSONL
- **Perguntar**: anexar o JSONL numa sessão e perguntar em linguagem natural — "em quais itens de PEB do CACD pós-2015 eu errei por meia-verdade?", "liste os anulados de HB com o motivo". A resposta sai de um script, não de memória.
- **Planilha**: pedir a conversão para `.xlsx`/CSV (uma coluna por campo) para filtrar e ordenar à mão.
- **Painel**: alimentar o CACD Cockpit com ❌ por tema e por tipo de erro.
- **Treino dirigido**: gerar notas ou simulados só com um recorte (ex.: todos os itens `GENERALIZACAO` de DIP).
- **Regenerar**: se a Folha mudar, remontar as notas a partir do JSONL; se a paleta ou o estilo dos gráficos mudar, re-renderizar as figuras a partir de `figuras[].spec` (`qgraf.py arquivo.jsonl`).
- **Melhorar o prompt**: os campos `qualidade_fonte`, `gabarito_origem` e `alertas` mostram onde o processo tropeça.

## 4. Relatórios
Três produtos, em Markdown:

### 4.1 Mini-relatório de passada (ao fim de cada passada)
Curto, no chat e em arquivo `{SIGLA}-Q_passada{NN}_relatorio.md`:
- Cards por nota, por banca e por tipo; itens da Triagem com destino sugerido.
- ⚠️ contestáveis, 🔧 gabaritos resolvidos ou trocados pelo oficial, ⏳ desatualizados, 📄 textos irrecuperáveis.
- 📈 Figuras: geradas (frente × verso; fiel × conjectural × didática), imagens da fonte por ação (redesenhada, transcrita, absorvida, cortada, irrecuperável), enunciados reconstruídos e imagens a reenviar.
- Resultado da verificação (contrato e revisão amostral).
- O que falta: passadas restantes e notas afetadas.

### 4.2 📊 Relatório do lote (ao fim da última passada, sobre o JSONL-mestre)
`{SIGLA}-Q_relatorio_do_lote.md`
1. **Panorama** — total de itens; CERTO × ERRADO × ANULADO × ME; tipos; bancas; CACD × demais CEBRASPE × outras bancas × cursos; distribuição por ano (e, no CACD, por edição).
2. **Mapa temático** — itens por nota e por subtema (tabela); 🔥 os 15 subtemas mais cobrados; ⬜ lacunas (notas e subtemas do índice sem nenhum item); proporção CACD por tema.
3. **Como os itens são fabricados** — frequência de cada código da taxonomia, no geral e só no CACD; para cada código, 1 item-exemplo (id + 1 linha); moduladores mais frequentes e o gabarito típico associado a cada um (ex.: "exclusivamente" → ERRADO em x%).
4. **Seu desempenho** — itens ❌ por nota, por subtema e por código da taxonomia; taxa de ❌ por código (onde você cai mais, relativamente); lista dos 20 itens ❌ mais instrutivos para revisão.
5. **Polêmicos** — contestáveis, anulados, alterados e desatualizados, com id, prova, motivo e resposta mais defensável.
6. **Qualidade da fonte** — distribuição de `qualidade_fonte`; gabaritos resolvidos e trocados pelo oficial; padrões de erro recorrentes nos comentários de origem (ex.: "curso X classifica gerúndio como adjunto").
6-bis. **Figuras** — itens com figura na frente por tema (onde a matéria é mais gráfica); modelos de gráfico mais usados; figuras conjecturais pendentes de conferência; transcrições incoerentes corrigidas.
7. **Sugestões para o prompt** — o que a execução revelou (ambiguidades da Folha, rótulos da taxonomia pouco usados ou insuficientes, módulos que não renderam, tempo e volume por passada) e ajustes propostos para a próxima matéria.

### 4.3 🎓 Lições do lote
`{SIGLA}-Q_licoes.md` — o que se aprende com o conjunto, escrito para estudo:
1. **Como a banca pensa nesta matéria** — os 8 a 12 padrões de construção mais recorrentes, cada um com: o padrão, um item real do lote, como reconhecer e o gabarito típico.
2. **Checklist de resolução** — 8 a 12 perguntas a fazer diante de qualquer item da matéria.
3. **Os conceitos mais cobrados** — os 10–15 conceitos ou fatos centrais, com uma linha de revisão cada e os ids dos itens.
4. **Confusões clássicas** — pares que a banca troca (conceito × conceito, autor × autor, data × data), com a distinção em uma linha.
5. **Lições para a discursiva**:
   - temas das objetivas que mais se repetem e são candidatos a discursiva;
   - para cada um: tese central, 3–5 argumentos, autores e dados utilizáveis (tirados dos cards) e um esqueleto de resposta;
   - erros conceituais das objetivas que também derrubam nota na discursiva;
   - orientação de estrutura e de vocabulário técnico para a matéria.
6. **Plano de revisão** — ordem sugerida de estudo a partir dos ❌ e das lacunas.

## 5. Verificação dos dados
Antes de gerar os relatórios, um script (`verificar_q.py`) confere: ids únicos; campos obrigatórios preenchidos; valores dentro das listas fechadas; `tipo_erro` presente em todo C/E e ME; coerência entre `gabarito`, `status` e `alertas`; toda figura com `id`, `lado`, `tipo`, `fidelidade`, `legenda`, `md5` e `spec`; toda figura `conjectural` com alerta `figura_conjectural`; toda figura de verso presente no `verso_html`; número de registros igual ao de cards nas notas; contagens do relatório batendo com o JSONL. Todos os números dos relatórios saem do script, nunca de estimativa.
