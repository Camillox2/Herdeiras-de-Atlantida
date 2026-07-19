# Herdeiras de Atlantida — Roteiro de Producao

## Regra de qualidade

Nenhum mapa final usa uma imagem panoramica como chao ou mistura estilos de
packs. Cada area e um mapa de tiles em camadas, com arte mediterranea original,
sprites coerentes e pontos de interacao reais.

## Padrao tecnico de arte

| Categoria | Padrao de producao |
| --- | --- |
| Tile de mundo | 32 x 32 px, ortografico em tres quartos, pixel art nitida |
| Personagem no mundo | silhueta legivel de 48 x 64 px ou 64 x 80 px |
| Retrato de dialogo | 1024 px de altura, PNG com alpha, 8 expressoes para heroina |
| Animacao de caminhada | 4 direcoes x 4 frames, idle separado |
| Camadas de mapa | chao, detalhe, colisao, objetos baixos, objetos altos, teto |
| Iluminacao | PointLight2D, oclusao simples, shader leve para agua e noite |

## Fases e criterio de pronto

### Fase 1 — Fundacao de arte e tecnologia

- Organizar `assets/art/world`, `assets/art/characters`, `assets/art/ui` e `assets/art/vfx`.
- Definir paleta, escala, convencao de nomes e manifesto de licencas.
- Converter o render de exploracao para TileMapLayer, Camera2D, Y-sort e colisao por celula.

Pronto quando um mapa teste tiver camadas, colisao, profundidade e luz sem
dependencia de desenhos procedurais.

### Fase 2 — Kallipolis vertical slice

- Porto, mercado, pensao, praca, becos, farol, tres interiores e cais.
- Agua animada, lanternas, arvores, vegetacao, objetos, NPCs e placas.
- Missao de Lysandra, Polemon, caixa, Ariane e Coletor completa do inicio ao combate.

Pronto quando a primeira hora de jogo tiver uma cidade bonita, navegavel e com
exploracao significativa.

### Fase 3 — Ivo e Ariane

- Sprites de exploracao, idle, caminhada e combate.
- Retratos e oito expressoes de cada um.
- Animacoes de reacao, proximidade e eventos de afinidade.

Pronto quando ambos forem reconheciveis pelo sprite e pelo retrato, sem usar
marcadores de texto como substituto visual.

### Fase 4 — Cisterna Esquecida

- Tiles de ruina, agua, mosaico, portas, pontes, armadilhas e baus.
- Sombra da Cisterna, combate, ecos e magia de Ressonancia.
- Iluminacao azul, neblina, particulas e efeito de agua.

Pronto quando a dungeon tiver leitura espacial, recompensa e atmosfera propria.

### Fase 5 — Sistemas de RPG

- Combate, equipamentos, itens, loja, loot, magia, diario e save.
- VFX, SFX, feedback de dano, menus e acessibilidade de texto.
- Afinidade, escolhas persistentes e bloqueio etico da rota de harem por consentimento e afinidade alta.

### Fase 6 — Nereu e expansao

- Nova cidade, porto, navio, interiores e primeira rota maritima.
- Introducao de Nerissa, secundarios e proxima decisao de historia.
- Base reutilizavel para Asterion e Atlantida.

### Fase 7 — Fechamento da build

- Revisao de historia, continuidades, bugs, colisao, saves e performance.
- Teste de jornada completa, build Windows e publicacao.

## Asset backlog inicial

### Kallipolis

- 24 tiles de terreno, 18 de caminho/rua, 20 de agua/cais, 36 de construcao e 45 props.
- 5 fachadas, 3 interiores, 1 praca, 1 mercado e 1 cais completo.
- 12 NPCs de fundo com 3 variantes cada.

### Personagens principais

- Ivo: 16 frames de caminhada, 4 idle, 8 combate e 8 retratos.
- Ariane: 16 frames de caminhada, 4 idle, 8 combate e 8 retratos.
- Cada proxima heroina segue o mesmo padrao antes de receber rota romantica.

### VFX e audio

- Agua, espuma, luz de lanterna, poeira, folhas, magia, impacto e sombra.
- Passos por superficie, porto, mercado, interior, combate, magia e interface.
