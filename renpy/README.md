# Herdeiras de Atlântida — Visual Novel

Esta pasta contém a adaptação em Ren'Py, mantida separada do RPG em Godot.

## Segurança do projeto original

- A branch `main` continua sendo o RPG em Godot.
- A branch `renpy-vn` contém a adaptação narrativa.
- Nenhum arquivo do RPG precisa ser removido para desenvolver ou testar a VN.

## Abrir no Ren'Py

1. Instale uma versão estável do Ren'Py 8.
2. Abra o Ren'Py Launcher.
3. Escolha **Adicionar projeto existente**.
4. Selecione a pasta `renpy` deste repositório.
5. Clique em **Iniciar projeto**.

## Estado desta primeira versão

- prólogo narrativo de Kallípolis até Nereu;
- escolhas de personalidade;
- afinidade com Ariane e Nerissa;
- finais e variações condicionais do prólogo;
- tela de vínculos;
- save, load e preferências;
- cenários, retratos e músicas reaproveitados do RPG;
- sem movimentação, combate, inventário ou estatísticas de RPG.

## Estrutura

- `game/script.rpy`: entrada do jogo;
- `game/chapter_00_prologue.rpy`: prólogo convertido;
- `game/characters.rpy`: personagens e imagens;
- `game/variables.rpy`: escolhas, afinidade e estados;
- `game/screens.rpy`: interface;
- `game/styles.rpy`: identidade visual;
- `game/images/`: cópias dos assets necessários à VN;
- `docs/`: plano narrativo e direção de arte.

## Próximos marcos

1. Revisar o texto do prólogo em jogo.
2. Substituir os cenários herdados pelos fundos premium 1920×1080.
3. Criar CGs dos momentos decisivos.
4. Escrever o Capítulo 1 em Nereu.
5. Expandir afinidades e rotas das seis heroínas.
