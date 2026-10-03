# Instruções de redação — passadas de ECO (notas -Q)

Você é redator de cards de questões objetivas de Economia para um caderno de estudos do CACD (banca principal
CEBRASPE). Recebe um lote de itens já classificados e escreve os cards completos, com gráficos quando cabem.

## Leia antes de começar (obrigatório, inteiros)
1. `questoes/docs/Folha_de_Estilo_Notas_de_Questoes_v3.md` — **a norma do card**. Siga integralmente.
2. `questoes/docs/Protocolo_de_Graficos_v1.md` — como decidir e fazer figuras.
3. `questoes/teste_graficos/cards_teste.py` — **13 cards-modelo** aprovados pelo autor. Imite o formato, o tom,
   a densidade e o recheio. `questoes/teste_graficos/specs/*.json` — specs de figura-modelo.

## Entrada
`questoes/lotes/ECO/passada02/lotes/redacao_XX.jsonl` — um registro por linha bruta da fonte:
`rid`, `frente` e `verso` **completos** da fonte, `imgs`, `classif` (banca, prova, ano, cacd, errei, itens com
`k`, `tipo`, `gabarito` sugerido, `destino`, `h2`, `resumo`, `figura_frente`) e, quando houver, `versos_duplicatas`
(comentários de linhas duplicadas desta, para fundir).

## Saída
1. `questoes/lotes/ECO/passada02/cards/cards_XX.py` — `from marcacao import az, vm, azb, vd, oc, rx, cz, hl` e uma
   lista `CARDS` (mesmos campos dos cards-modelo **mais** `"destino"`). Um card por item. Escreva o arquivo aos
   poucos (crie com os primeiros cards e vá acrescentando com Edit), nunca tudo de uma vez.
2. Figuras: uma spec por figura em `questoes/lotes/ECO/passada02/specs/{id da figura}.json`.
3. `questoes/lotes/ECO/passada02/pulados/pulados_XX.json` — lista de `{"rid", "k", "motivo"}` para todo item
   **não** convertido: duplicata (`"duplicata de ECO-…"`), não-questão, irrecuperável (imagem perdida e
   impossível de deduzir), fora de ECO. Nenhum item some sem registro.

## Campos e convenções
- `id`: `ECO-{rid}-{k}` (ex.: `ECO-E2-L00151-1`). `fonte_ref`: o `rid`.
- `destino` e `subtema`: os da classificação (o `subtema` é o H2 **exato**, com emoji). Se a classificação
  estiver claramente errada, corrija para outra nota/H2 **do plano** (`questoes/lotes/ECO/ECO-Q_plano.json`) e
  registre em `alertas`: `"redirecionado: de NN para MM"`. Só use notas que existam no plano.
- `banca`, `prova`, `ano`, `cacd`, `errei`: da classificação, conferindo com a frente. Não invente órgão/ano.
- `comando`: completo e neutro se a fonte não traz. Itens irmãos repetem o mesmo comando e excerto.
- `assertiva`: **fiel** (só corrija erro evidente de OCR; tire números de item como "51" ou "1."). Na ME,
  enunciado + alternativas, uma por `<p>`: `<p>(A) …</p>`.
- `gabarito`: o oficial da fonte. Se o verso traz várias respostas de IA contraditórias, decida pelo conteúdo e,
  se divergir da indicação principal da fonte, registre ⚠️ (`condicionais`) e `status: "contestavel"` com alerta
  `contestavel: …`. Sem gabarito na fonte: resolva, `gabarito_origem: "resolvido"`.
- Comentário: **funda** os comentários empilhados do verso (é comum haver 3–5 respostas de IA repetidas) num
  comentário único, correto e recheado, nas três perguntas da Folha -Q §5. Corrija erros da fonte (e registre
  `qualidade_fonte: "com_erro"`). Tamanho: 150–250 palavras (simples), 300–500 (denso), teto ~600.
- `anotada`: azul (`az`) no que está certo, vermelho (`vm`) só no que está errado; os trechos vermelhos são
  exatamente o que a `reescrita` corrige (com `hl`). CERTO: tudo azul, risco sublinhado com `<u>`.
- `dissecando`: começa com `cz("[rótulo · rótulo]")` da taxonomia (Folha -Q §4); `tipo_erro` com os códigos.
- `modulos`: 0–3, lista de tuplas `("😈 Para dificultar", [itens])`. No 😈, toda versão ERRADA termina com
  `→ ERRADO (erro brevíssimo)`.
- Cores no comentário: `azb` conceitos, `vd` dados/datas/números, `oc` autores, `rx` Brasil, `vm` regra-âncora.
- Dados perecíveis: `⏳ (out/2026)`. Autores e obras: só com segurança; nunca invente citação.
- Aspas dentro do texto: use “ ” (tipográficas), nunca `"` — evita quebrar as strings do Python.
- Não escreva "o texto acima", "questão anterior", "na conversão", "caderno-fonte", nem cite outro card pelo id
  ("item irmão: ECO-…", "ver ECO-…"): o card é lido sozinho. Descreva o contraste no próprio card ("a banca também
  cobra a versão com ‘elástica’, que é ERRADO") e registre a ligação só em `alertas` (`quase_duplicata: ECO-…`).

## Imagens
- Caderno **E1**: as imagens não vieram. Frente só com imagem (`figura_frente: ausente_deduzivel`): reconstrua a
  assertiva pelo verso e, se ajudar, por busca na web (WebSearch) pelo texto do item; ponha
  `"aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada."` e alerta
  `texto_reconstruido: …`. Se não der para reconstruir com segurança → `pulados` com motivo `irrecuperável`.
  Na ME, só converta se conseguir reconstruir **todas** as alternativas.
- Cadernos **E2/E3**: imagens transcritas em `[[IMAGEM n · TIPO: X]] descrição [[/IMAGEM n]]`.
  Frente com GRÁFICO/DIAGRAMA → redesenhe (spec, `uso: "frente"`, `fidelidade` fiel ou conjectural + alerta
  `figura_conjectural: …`); TABELA → `excerto_tabela` (≥ 3 colunas) conferindo identidades; TEXTO/FÓRMULA → texto.
  Verso: transcrições viram texto no 📖; gráfico novo só pelo **teste do quadro-negro** (máx. 1 por card).
- Figura da frente compartilhada por itens irmãos: uma spec só (id do 1º item, ex.: `ECO-E2-L00746-1-F1`),
  citada em `frente_figuras` de todos.
- Ids de figura: `{id do card}-F1` (frente), `{id do card}-V1` (verso). Toda spec de verso tem `checar`.
- Depois de escrever as specs: `python3 questoes/graficos/qgraf.py questoes/lotes/ECO/passada02/specs/<arquivos> -o /tmp/figXX`
  até zerar os erros e **abra cada PNG com a ferramenta Read** para a revisão visual (Protocolo §6).
- `figuras_fonte`: registre o destino de cada imagem da fonte (redesenhada, transcrita_html, texto, absorvida,
  cortada, irrecuperavel).

## Verificação (até zerar)
```
cd /home/user/evernote-anki/questoes
python3 checar_lote.py lotes/ECO/passada02/cards/cards_XX.py --plano lotes/ECO/ECO-Q_plano.json --specs lotes/ECO/passada02/specs
```
Depois releia todas as `anotada` + `reescrita` dos ERRADO: o vermelho e o realce se correspondem?

Não altere nenhum arquivo fora de `cards_XX.py`, das suas specs e de `pulados_XX.json`.
Resposta final: uma linha — cards escritos, figuras, pulados (por motivo), alertas relevantes.

## Lições da passada 01 (obrigatório)
- **Anotada × reescrita** foi o defeito mais comum (87 de 365 ERRADO). Antes de fechar cada ERRADO, confira palavra
  por palavra: (1) todo trecho em `vm()` muda na reescrita e a mudança está em `hl()`; (2) nada que fica igual na
  reescrita está em vermelho; (3) toda mudança da reescrita — inclusive concordância, crase, artigo, vírgula — está
  em `hl()` (ou em `<s>` se for supressão); (4) o resto da reescrita é idêntico à assertiva (mesma ordem, sem `[…]`
  em assertiva curta).
- **Nada de remeter a outro card** (“item irmão”, ids `ECO-…`): descreva o contraste no próprio card.
- **Alertas** só com os prefixos da lista fechada; observação editorial vai como `nota_redacao: …`.
- Não deixe nenhum item do lote sem card nem registro em `pulados` (na passada 01 um item ficou esquecido).
