# Notas de questões (-Q) — protocolo, scripts e testes

Tudo o que é preciso para consolidar as notas de questões objetivas do caderno CACD, **inclusive com gráficos**.

## Documentos (`docs/`) — versões vigentes
| Documento | Papel |
|---|---|
| `Prompt_Consolidacao_Q_v3.md` | o prompt de cada lote (Fases 0, 0.5, 1 e 2) |
| `Folha_de_Estilo_Notas_de_Questoes_v3.md` | **o que** o card precisa ser (v2 + §10 Figuras e gráficos) |
| `Especificacao_JSONL_e_Relatorio_Notas_Q_v2.md` | a base de dados (JSONL), relatórios e verificação (v1 + campos de figuras) |
| `Protocolo_de_Graficos_v1.md` | **como** tratar imagens e gerar gráficos: decisão, spec JSON, modelos, lint, revisão visual, teste de importação |
| `Folha_de_Estilo_Caderno_CACD_v9.md` | HTML seguro, ENEX, cores, emojis (sem mudanças; cópia de referência) |

Anexar a cada sessão de lote: o prompt preenchido, os quatro documentos e um zip desta pasta.

## Scripts
| Script | Faz |
|---|---|
| `inventario/inventariar_figuras.py` | Fase 0: inventaria as imagens dos cadernos (`.md` com transcrições, `.html` sem as imagens) e lista as imagens de frente a reenviar |
| `graficos/qgraf.py` (+ `modelos.py`) | spec JSON → PNG no estilo do caderno; calcula interseções e áreas; confere rótulos, geometria e as checagens econômicas; `--galeria` para revisão visual |
| `montar_nota_q.py` | fonte dos cards → JSONL + HTML + ENEX com as figuras embutidas (`<en-media>` + `<resource>`) |
| `verificar_q.py` | contrato da Folha -Q v3 §9 (inclusive figuras) e verificação do JSONL |

```bash
pip install -r questoes/requirements.txt
python3 questoes/graficos/qgraf.py questoes/teste_graficos/specs -o /tmp/fig --galeria
python3 questoes/montar_nota_q.py questoes/teste_graficos/cards_teste.py --titulo "00-TESTE-GRAF-1 - Obj." \
    --sigla ECO --passada 0 --specs questoes/teste_graficos/specs -o questoes/teste_graficos/entrega
python3 questoes/verificar_q.py questoes/teste_graficos/entrega/*.enex \
    --jsonl questoes/teste_graficos/entrega/ECO-Q_passada00.jsonl
```

## Teste de gráficos de Economia (`teste_graficos/`)
13 itens reais dos cadernos ECO 1–3, escolhidos para cobrir cada situação de figura:

| Card | Situação testada | Figura |
|---|---|---|
| T01 | gráfico na **frente** (conjectural) + painéis no verso (movimento × deslocamento) | F1, V1 |
| T02 | mesma figura de frente compartilhada por item irmão; verso com deslocamento oposto | F1, V1 |
| T03 | tabela da frente como **PNG** (alternativa) | F1 |
| T04 | **fórmula** na frente transcrita como texto; verso com eixos numéricos e checagem do excedente = 135 | V1 |
| T05 | tabelamento com checagem Qᴰ − Qˢ = 40 | V1 |
| T06 | IS-LM na frente; deslocamento da LM no verso (modelo pronto) | F1, V1 |
| T07 | curva não linear feita com primitivas (LM com trecho plano: armadilha da liquidez) | V1 |
| T08 | isoquantas na frente, conjecturais (valores não preservados) | F1 |
| T09 | exercício aberto (EXERC) com o modelo de tributo | V1 |
| T10 | áreas em letra (A–G) reconstruídas pela convenção do livro-texto | F1 |
| T11 | Solow com regra de ouro, item ❌ | V1 |
| T12 | **frente que era só imagem** (caderno 1): enunciado reconstruído + antes × depois no verso | V1 |
| T13 | tabela da frente em **HTML aninhada**, com transcrição incoerente corrigida; barras com dados reais | V1 |

Entrega em `teste_graficos/entrega/`: o ENEX para importar, o HTML de pré-visualização, o JSONL e `figuras/galeria.html`.
Depois de importar, preencher o checklist do Protocolo §7.

## Inventário dos cadernos ECO (`inventario/`)
- `ECO-Q_figuras_inventario.csv` — 1.770 ocorrências de imagem nos três cadernos, com lado, tipo e ação sugerida.
- `ECO-Q_imagens_a_reenviar.csv` — as 36 imagens de **frente** do caderno 1 (exportado sem a pasta de imagens), pelo nome do arquivo; 28 delas são questões que existem só como imagem.
