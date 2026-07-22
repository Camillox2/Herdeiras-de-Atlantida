# Confrontos de Juramento: combate tático curto que privilegia escolhas e
# vínculos, em vez de grind. Cada ação tem custo, benefício e consequência.

label juramento_confronto(enemy_name, enemy_resolve, companion_name):
    $ combat_focus = 3
    $ combat_enemy = enemy_resolve
    $ combat_companion = companion_name
    $ combat_result = ""
    show screen combat_hud(enemy_name)

    while combat_focus > 0 and combat_enemy > 0:
        menu:
            "Confronto: qual é a próxima ação de Ivo?"

            "Ancorar o grupo — reduzir a pressão sem ferir ninguém.":
                $ combat_enemy -= 1
                $ ivo_compassion += 1
                "Ivo recusa o ritmo que o inimigo impõe. A linha de defesa se fecha, não como muralha, mas como promessa de que ninguém será deixado para trás."

            "Ler a abertura — atacar o mecanismo por trás da ameaça.":
                $ combat_enemy -= 2
                $ combat_focus -= 1
                $ ivo_honesty += 1
                "A Marca encontra o ponto onde o medo foi transformado em ordem. O golpe funciona, mas cobra concentração demais."

            "Proteger [combat_companion] — trocar vantagem por segurança.":
                $ combat_focus += 1
                $ combat_enemy -= 1
                $ ivo_courage += 1
                "Ivo escolhe a posição mais difícil e abre espaço para [combat_companion] respirar. A formação perde terreno, mas não perde ninguém."

    hide screen combat_hud
    if combat_enemy <= 0:
        $ combat_result = "won"
        "A ameaça recua quando percebe que não consegue separar o grupo em peças úteis."
    else:
        $ combat_result = "strained"
        "O grupo não cai, mas o inimigo deixa uma marca no terreno. A vitória terá de ser cobrada mais tarde."
    return
