# Estado da build jogável

## O que já é jogável

- Tela de abertura e início de jornada.
- Exploração top-down em Kallípolis, Pensão dos Degraus, Ágora das Colunas, Cisterna e Nereu.
- Mapas exteriores ilustrados de forma coesa, com rotas caminháveis, colisões próprias e água animada com reflexos opcionais.
- Personagem com aceleração/desaceleração, varredura de colisão, deslizamento e dezesseis quadros cardinais na mesma escala visual dos NPCs.
- Moradores com rotas de vários pontos, pausas, falas e prioridade correta para personagens de missão; Mikon está visível e interativo.
- Gaivotas, folhas, pétalas, espuma, fonte em quatro fases e água com refracão/causticas em shader.
- Objetivo compacto, marcador animado, placas ilustradas e prompts contextuais `[E]` para portas, NPCs, itens e saídas.
- Diálogos paginados, escolhas ramificadas e afinidade com Ariane.
- Caixa selada, moeda de Atlântida e combate contra o Coletor.
- Transição para a Cisterna Esquecida.
- Coleta de três Ecos, porta de bronze e confronto com a Sombra da Cisterna.
- Combate por turnos com atacar, defender e focar.
- Equipamentos ativos: arma, armadura e relíquia.
- Magia de Ressonância desbloqueada pela Moeda de Atlântida; consome Essência, que é recuperada com Focar.
- Baú opcional na Cisterna Esquecida melhora arma e armadura; seus bônus entram no cálculo de dano e guarda.
- Efeitos sonoros CC0 para confirmação, interação e ataque e quatro temas musicais originais por região.
- Bolsa de itens, galeria de Vínculos e salvamento local.
- Menu de pausa navegável e configurações gráficas persistentes com Aplicar/Cancelar explícitos.
- Migração automática de posição para saves antigos que carreguem dentro de água, parede ou mobiliário.
- Modos janela, janela sem bordas e tela cheia; resoluções de 960×540 a 2560×1440.
- VSync, pixels nítidos/suavização HD, sombras, reflexos da água, luz mediterrânea e brilho.
- Chegada jogável a Nereu e primeiro diálogo ramificado com Nerissa.

## Controles

- `WASD` ou setas: mover e selecionar opções.
- `E` ou espaço: interagir e confirmar.
- `I`: abrir a bolsa.
- `J`: abrir Vínculos.
- `F5`: salvar.
- `M`: mapa e objetivo.
- `Esc`: pausa e configurações.

## Estrutura de conteúdo

- `assets/backgrounds/`: cenários originais de abertura e exploração.
- `assets/portraits/`: retratos-base e expressões de diálogo.
- `assets/kenney/`: kit CC0 usado como biblioteca de prototipagem.
- `scripts/`: lógica Godot.
- `scenes/`: cenas Godot.
- `docs/`: roteiro, licenças e documentação de produção.

## Escopo desta build

Esta é uma primeira build de prólogo com começo, meio e encerramento local: Kallípolis → Ágora → Cisterna Esquecida → chegada a Nereu. Os capítulos seguintes podem continuar a partir de Nereu sem quebrar saves nem os sistemas centrais.

O resultado da rodada de jogabilidade e regressão de 19/07/2026 está em [QA_2026-07-19.md](QA_2026-07-19.md).
