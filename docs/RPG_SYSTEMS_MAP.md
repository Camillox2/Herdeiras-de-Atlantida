# Herdeiras de Atlântida — mapa de sistemas do RPG

Este documento transforma a referência de aventura/RPG/VN em um produto verificável. A prioridade não é copiar outro jogo: é cobrir o mesmo tipo de fantasia de exploração, missões, relacionamentos, evolução e mundo vivo com identidade própria greco-atlante.

## Norte de qualidade

- Mundo: pixel art mediterrânea coesa, com leitura clara de caminhos, portas e água.
- Controle: resposta imediata, colisão previsível, quatro direções e escala consistente.
- Vida: água, vento, folhas, pássaros, luzes, áudio, rotinas e falas contextuais.
- História: escolhas com consequência, romance lento, afinidade legível e finais condicionais.
- RPG: exploração, combate, equipamentos, recursos, economia, segredos e progressão.
- Conforto: 960×540 a 2560×1440, janela/sem bordas/tela cheia, teclado e controle.

## Matriz de sistemas

| Pilar | Sistema | Estado atual | Próxima definição de pronto |
|---|---|---|---|
| Controle | Movimento em quatro direções | Implementado e coberto por regressão | Controle, remapeamento e corrida com stamina |
| Controle | Colisões de cenário/NPC/água | Implementado no vertical slice | Migrar áreas finais para polígonos e teste por mapa |
| Controle | Interação contextual | Implementado com prompt `[E]` | Ícones de controle e prioridades acessíveis |
| Mundo | Kallípolis, Ágora, Nereu, Pensão, Cisterna | Jogáveis | Mais interiores, transições e mapa-múndi |
| Mundo | Água/vento/fauna/partículas | Implementado no vertical slice | Clima, horário e variação regional |
| Mundo | Moradores e rotas | Implementado com falas | Agenda diária, casas, trabalho e reação à história |
| Narrativa | Diálogo paginado | Implementado | Histórico, velocidade de texto, autoplay e skip lido |
| Narrativa | Escolhas e afinidade | Implementado para Ariane/Nerissa | Estado individual das seis heroínas e consequências cruzadas |
| Narrativa | Main quest | Prólogo jogável | Capítulos, estados de falha e recapitulação |
| Narrativa | Side quests | Estrutura parcial | Quadro de missões, objetivos opcionais e recompensas únicas |
| Romance | Rotas individuais | Fundação de afinidade | 5 eventos por heroína antes de romance explícito |
| Romance | Final solo ou harém | Regra definida | Harém somente com afinidade mínima das seis e conflitos resolvidos |
| RPG | Combate por turnos | Protótipo jogável | Status, habilidades, inimigos, chefes, feedback e balanceamento |
| RPG | Vida, Essência e Foco | Implementado | Curva de evolução e efeitos de equipamento |
| RPG | Inventário/equipamentos | Implementado | Slots, comparação, uso, descarte e itens de missão protegidos |
| RPG | Níveis/XP/atributos | Pendente | Árvore compacta sem protagonista invencível no começo |
| RPG | Magia da Marca | Primeiro poder implementado | Escolas ligadas às Moiras, custo e riscos narrativos |
| Economia | Ouro e recompensas | Implementado | Lojas, preços, venda, reputação e fontes/sumidouros equilibrados |
| Recursos | Madeira, pedra, minério, ervas, relíquias | Pendente | Coleta contextual sem grind e receitas com função narrativa |
| Construção | Base própria | Pendente | Reforma por cômodos, decoração e eventos das companheiras |
| Grupo | Formação de party | Pendente | Duas companheiras, funções de campo e diálogos reativos |
| Grupo | Roupas cosméticas | Pendente | Desbloqueio por evento e retratos/sprites sincronizados |
| Atividades | Pesca | Pendente | Minigame curto, coleção e segredos aquáticos |
| Atividades | Corrida/arena/puzzles/furtividade | Pendente | Um protótipo de cada antes de expandir conteúdo |
| Exploração | Segredos e baús | Primeiro baú/reliquias | Linguagem visual consistente e registro de descoberta |
| Exploração | Viagem rápida | Pendente | Desbloqueio diegético e retorno sem quebrar missões |
| UX | Mapa, bolsa, vínculos e pausa | Implementado | Journal unificado, filtros e marcadores de missão |
| UX | Configuração gráfica | Implementado com Aplicar/Cancelar | Áudio, acessibilidade, idioma e remapeamento |
| Sistema | Save/load | Implementado | Três slots, autosave, backup e migração de versão |
| Sistema | Resoluções 16:9 | Implementado | Teste visual automatizado em cinco resoluções |
| Sistema | Música por região | Quatro temas originais | Crossfade, volume e stingers de evento/combate |
| Sistema | Efeitos e ambiência | Primeira camada | Passos por material, mar, mercado, interior e cisterna |

## Ordem de produção

### P0 — vertical slice confiável

1. Movimento, colisão, portas, diálogo, progressão e configurações sem bloqueios.
2. Kallípolis viva: moradores, água, partículas, áudio, prompts e objetivos claros.
3. Fluxo completo Lysandra → Pólemon → caixa → Ariane → Coletor → Cisterna → Nereu.
4. Save seguro, reinício e regressão automática.

### P1 — RPG completo do Capítulo 1

1. Diário de missões e mapa com marcadores opcionais.
2. Combate refatorado, XP, quatro habilidades e três famílias de inimigos.
3. Loja, coleta, crafting curto e equipamentos comparáveis.
4. Agenda de NPCs, ciclo de horário e clima mediterrâneo.
5. Primeiros eventos de afinidade das seis heroínas.

### P2 — retenção e personalização

1. Base reformável com quartos, biblioteca, oficina e jardim.
2. Party, roupas e conversas reativas durante exploração.
3. Pesca, arena, corrida, furtividade e puzzles como atividades opcionais.
4. Viagem rápida e novas ilhas/cidades.

### P3 — fechamento narrativo

1. Rotas individuais completas e conflitos entre afinidades.
2. Finais solo, amizade, sacrifício e harém condicionado.
3. New Game+, conquistas, galeria e recapitulação de escolhas.

## Critérios de aceite por mapa

- O jogador nunca entra em água ou parede além do limite dos pés.
- Toda porta utilizável apresenta prompt e leva a um ponto distante da saída.
- Há pelo menos três fontes de movimento ambiental visíveis em dez segundos.
- Há pelo menos três NPCs não essenciais com rota, nome e fala própria.
- Música e ambiência começam sem ação do jogador e mudam com a região.
- A missão principal pode ser concluída sem consultar um guia externo.
- Toda resolução mantém 16:9, texto legível e pixel art sem deformação.
- Nenhuma conversa reabre com o mesmo toque usado para fechá-la.
