# Suporte de resolucao

## Base visual

- Resolucao logica: `960x540` em proporcao 16:9.
- O Godot usa escala de `CanvasItem`, aspecto `keep` e estiramento fracionario.
- A arte e a HUD crescem juntas; personagens nao mudam de proporcao nem perdem o alinhamento com colisoes.
- O jogador pode escolher `Pixels nitidos` (filtro nearest) ou `Suavizacao HD` (filtro linear).

## Modos validados

| Resolucao | Escala sobre a base | Resultado esperado |
| --- | ---: | --- |
| 960x540 | 1x | Referencia de composicao e desempenho. |
| 1280x720 | 1,33x | Preenchimento 16:9 sem corte. |
| 1600x900 | 1,67x | Preenchimento 16:9 sem corte. |
| 1920x1080 | 2x | Escala integral e imagem nitida; validada em teste visual. |
| 2560x1440 | 2,67x | Preenchimento 16:9 com filtro escolhido pelo jogador. |

Proporcoes diferentes de 16:9 recebem barras discretas para preservar a composicao. No modo janela, uma resolucao maior que a area util do monitor e reduzida proporcionalmente e centralizada. `Aplicar` confirma a mudanca e grava a configuracao; `Cancelar` restaura o estado anterior.
