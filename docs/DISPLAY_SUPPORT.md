# Suporte de resolucao

## Base visual

- Resolucao de design: 960x540 (16:9).
- O jogo usa `viewport` stretch com aspecto `keep` e escala inteira.
- Texturas usam filtro nearest; pixels nao recebem suavizacao acidental.

## Comportamento esperado

| Tela | Escala | Resultado |
| --- | --- | --- |
| 960x540 | 1x | Resolucao de referencia. |
| 1920x1080 | 2x | Pixels nitidos em tela cheia. |
| 2560x1440 | 2x | Pixels nitidos com barras discretas. |
| 3840x2160 | 4x | Pixels nitidos em tela cheia. |
| Proporcoes fora de 16:9 | inteira | Pillarbox ou letterbox preserva a arte sem deformar. |

O modo inteiro prioriza leitura de pixel art. Resolucaes que nao comportam uma escala inteira exibem barras em vez de borrar, esticar personagens ou distorcer a HUD.
