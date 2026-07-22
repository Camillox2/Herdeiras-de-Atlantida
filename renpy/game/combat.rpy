# Confrontos de Juramento: escolhas táticas curtas, cada uma adaptada ao lugar
# e à herdeira presente. Não há grind, nem derrota automática.

label juramento_confronto(enemy_name, enemy_resolve, companion_name, style="base", focus_limit=3):
    $ combat_focus_limit = focus_limit
    $ combat_focus = focus_limit
    $ combat_enemy = enemy_resolve
    $ combat_companion = companion_name
    $ combat_style = style
    $ combat_phase = "Fase I — Resistir juntos" if style == "final" else ""
    $ combat_result = ""
    $ profile = combat_profile_for(style)
    $ combat_action_labels = profile["labels"]
    $ combat_action_texts = profile["texts"]
    show screen combat_hud(enemy_name)

    while combat_focus > 0 and combat_enemy > 0:
        menu:
            "Confronto: qual é a próxima ação de Ivo?"

            "[combat_action_labels[0]]":
                $ combat_enemy -= 1
                $ ivo_compassion += 1
                "[combat_action_texts[0]]"

            "[combat_action_labels[1]]":
                $ combat_enemy -= 2
                $ combat_focus -= 1
                $ ivo_honesty += 1
                "[combat_action_texts[1]]"

            "[combat_action_labels[2]]":
                $ combat_focus = min(combat_focus_limit, combat_focus + 1)
                $ combat_enemy -= 1
                $ ivo_courage += 1
                "[combat_action_texts[2]]"

        if combat_style == "final" and combat_enemy > 0 and combat_enemy <= 3 and combat_phase == "Fase I — Resistir juntos":
            $ combat_phase = "Fase II — Recusar a cadeira"
            $ combat_focus = min(combat_focus_limit, combat_focus + 1)
            "A cadeira sétima muda de forma e oferece a Ivo uma vitória rápida em troca de uma ausência. As seis herdeiras respondem antes dele: ninguém será deixado como preço."

    hide screen combat_hud
    if combat_enemy <= 0:
        $ combat_result = "won"
        "A ameaça recua quando percebe que não consegue separar o grupo em peças úteis."
    else:
        $ combat_result = "strained"
        "O grupo não cai, mas o inimigo deixa uma marca no terreno. A vitória terá de ser cobrada mais tarde."
    return
