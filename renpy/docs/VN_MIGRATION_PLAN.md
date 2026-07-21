# Plano de migração — RPG Godot para VN Ren'Py

## Decisão

A adaptação Ren'Py não substitui o RPG. Ela vive na branch `renpy-vn`, enquanto a `main` preserva o projeto Godot.

## Escopo removido

- movimentação e colisão;
- exploração top-down;
- combate;
- vida, essência e equipamentos;
- inventário e baús;
- NPCs com rotas;
- shaders e configurações gráficas específicas do Godot;
- objetivos físicos e marcadores de mapa.

## Escopo mantido

- universo greco-atlante;
- prólogo e continuidade em Nereu;
- seis heroínas;
- escolhas;
- afinidade;
- traços de personalidade de Ivo;
- consequências entre capítulos;
- finais individuais, amizade e final conjunto condicionado;
- retratos, expressões, música e cenários.

## Estrutura narrativa recomendada

1. Prólogo — A Marca das Moiras.
2. Capítulo 1 — As Velas Azuis de Nereu.
3. Capítulo 2 — O Jardim de Mélia.
4. Capítulo 3 — A Canção de Lyra.
5. Capítulo 4 — A Arena de Thalia.
6. Capítulo 5 — A Coroa de Cassia.
7. Capítulo 6 — O Juramento de Ariane.
8. Capítulo final — As Herdeiras de Atlântida.

## Regras de escolhas

- escolhas menores definem personalidade e alteram falas;
- escolhas médias modificam afinidade e cenas;
- escolhas críticas criam flags permanentes;
- afinidade não deve ser a única condição de rota;
- finais conjuntos exigem confiança, conflitos resolvidos e consentimento de todas as envolvidas.

## Próximo trabalho

- testar a build no launcher;
- revisar posicionamento e escala dos retratos;
- importar fundos premium;
- criar CG do despertar da Marca;
- escrever o primeiro arco de Nereu;
- criar sistema de capítulos e galeria persistente.
