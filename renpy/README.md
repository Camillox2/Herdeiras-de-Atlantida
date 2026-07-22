# Herdeiras de Atlântida — Visual Novel

Esta pasta contém a adaptação em Ren'Py, mantida separada do RPG em Godot.

## Segurança do projeto original

- A branch `main` continua sendo o RPG em Godot.
- A branch `renpy-vn` contém a adaptação narrativa.
- Nenhum arquivo do RPG precisa ser removido para desenvolver ou testar a VN.

## Abrir no Ren'Py

1. Instale o Ren'Py 8.5.3 ou outra versão estável compatível da série 8.
2. Abra o Ren'Py Launcher.
3. Escolha **Adicionar projeto existente**.
4. Selecione a pasta `renpy` deste repositório.
5. Clique em **Iniciar projeto**.

## Versão atual — 0.2.0 Prólogo

O prólogo foi reescrito como uma visual novel completa, de Kallípolis até a entrada em Nereu.

Inclui:

- três atos narrativos com começo, tensão e revelação final;
- mistério do naufrágio e do antigo portador da Marca;
- Ariane confirmada como uma das seis herdeiras;
- Nerissa apresentada como a herdeira das marés;
- escolhas que alteram falas e relações posteriores;
- confiança de Lysandra e respeito de Pólemon;
- afinidade com Ariane e primeira impressão de Nerissa;
- quatro traços de personalidade de Ivo;
- resumo personalizado ao final do prólogo;
- tela de vínculos que retorna corretamente ao menu final;
- save, load, histórico e preferências;
- cenários, retratos e músicas reaproveitados do RPG;
- sem movimentação, combate, inventário ou estatísticas de RPG.

## Estrutura

- `game/script.rpy`: entrada do jogo;
- `game/chapter_00_prologue.rpy`: prólogo completo;
- `game/characters.rpy`: personagens e imagens;
- `game/variables.rpy`: escolhas, afinidade, traços e consequências;
- `game/screens.rpy`: interface;
- `game/styles.rpy`: identidade visual;
- `game/images/`: assets necessários à VN;
- `docs/`: plano narrativo e direção de arte.

## Próximos marcos

1. Executar uma rodada visual no Ren'Py Launcher e conferir posicionamento dos retratos.
2. Substituir os cenários herdados pelos fundos premium 1920×1080.
3. Criar CGs fiéis aos retratos oficiais.
4. Escrever o Capítulo 1 — As Velas Azuis de Nereu.
5. Expandir afinidades e rotas das seis heroínas.
