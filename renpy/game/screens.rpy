screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        vbox:
            spacing 10

            if who is not None:
                text who id "who" style "say_label"

            text what id "what" style "say_dialogue"

screen input(prompt):
    style_prefix "input"

    window:
        style "say_window"

        vbox:
            spacing 20
            text prompt
            input id "input"

screen choice(items):
    style_prefix "choice"
    modal True
    zorder 250

    # Menus recebem também a pergunta como um item sem ação. Separá-la das
    # opções impede que ela vire um botão e se misture visualmente à escolha.
    add Solid("#06131ed9")

    frame:
        style "choice_panel"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 22

            for item in items:
                if item.action:
                    textbutton item.caption action item.action style "choice_button"
                else:
                    text item.caption style "choice_caption"

style choice_panel is frame:
    xsize 1360
    background Solid("#0a2233f5")
    padding (52, 42)

style choice_caption is text:
    font gui.interface_text_font
    size 42
    color "#ffe1a3"
    xalign 0.5
    text_align 0.5
    layout "subtitle"
    line_spacing 8

style choice_button is button:
    xfill True
    yminimum 96
    background Solid("#123653")
    hover_background Solid("#1d6685")
    selected_background Solid("#214b68")
    padding (34, 22)

style choice_button_text is text:
    font gui.interface_text_font
    size 32
    color "#f3fbff"
    hover_color "#ffffff"
    xalign 0.5
    text_align 0.5
    layout "subtitle"
    line_spacing 6

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            xalign 0.5
            yalign 0.995
            spacing 18

            textbutton _("Voltar") action Rollback()
            textbutton _("Histórico") action ShowMenu("history")
            textbutton _("Salvar") action ShowMenu("save")
            textbutton _("Carregar") action ShowMenu("load")
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Pular") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Vínculos") action Show("relationships")
            textbutton _("Menu") action ShowMenu("preferences")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

screen navigation():
    vbox:
        spacing 16

        if main_menu:
            textbutton _("Continuar") style "nav_button" action Continue()
            textbutton _("Começar") style "nav_button" action Start()
            textbutton _("Carregar") style "nav_button" action ShowMenu("load")
        else:
            textbutton _("Histórico") style "nav_button" action ShowMenu("history")
            textbutton _("Salvar") style "nav_button" action ShowMenu("save")
            textbutton _("Carregar") style "nav_button" action ShowMenu("load")
            textbutton _("Vínculos") style "nav_button" action Show("relationships")

        textbutton _("Galeria") style "nav_button" action ShowMenu("cg_gallery")
        textbutton _("Preferências") style "nav_button" action ShowMenu("preferences")
        textbutton _("Sobre") style "nav_button" action ShowMenu("about")

        if _in_replay:
            textbutton _("Encerrar replay") style "nav_button" action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Menu principal") style "nav_button" action MainMenu()

        textbutton _("Sair") style "nav_button" action Quit(confirm=not main_menu)

screen main_menu():
    tag menu

    add gui.main_menu_background
    add Solid("#0209128a")

    frame:
        style "main_menu_panel"
        xalign 0.09
        yalign 0.5

        vbox:
            spacing 20

            text "Herdeiras de Atlântida" style "menu_title"
            text "PRIMEIRA TEMPORADA" style "menu_kicker"
            text "Seis herdeiras. Um juramento.\nNenhuma escolha sem consequência." style "menu_subtitle"

            null height 22
            use navigation

    text "Uma visual novel de fantasia mediterrânea" style "menu_footer" xalign 0.95 yalign 0.95

style main_menu_panel is frame:
    xsize 700
    background Solid("#071827e8")
    padding (58, 56)

style menu_kicker is text:
    font gui.interface_text_font
    size 22
    color "#e9bd67"
    kerning 4

style menu_footer is text:
    font gui.interface_text_font
    size 20
    color "#c8ddea"
    outlines [(2, "#02101a", 0, 0)]

screen history():
    tag menu
    add gui.game_menu_background

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1720
        ysize 900

        vbox:
            spacing 20

            hbox:
                xfill True
                text _("Histórico") style "menu_title"
                textbutton _("Voltar") action Return() xalign 1.0

            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                yinitial 1.0

                vbox:
                    spacing 24

                    for h in _history_list:
                        vbox:
                            if h.who:
                                text h.who style "say_label"
                            text h.what style "say_dialogue"

screen save():
    tag menu
    use file_slots(_("Salvar"))

screen load():
    tag menu
    use file_slots(_("Carregar"))

screen file_slots(title):
    add gui.game_menu_background

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1720
        ysize 900

        vbox:
            spacing 24

            hbox:
                xfill True
                text title style "menu_title"
                textbutton _("Voltar") action Return() xalign 1.0

            grid 3 2:
                spacing 22

                for slot in range(1, 7):
                    button:
                        xsize 520
                        ysize 310
                        background Solid("#0a2233dc")
                        hover_background Solid("#15516add")
                        action FileAction(slot)

                        vbox:
                            spacing 12
                            add FileScreenshot(slot) xalign 0.5
                            text FileTime(slot, format=_("%d/%m/%Y  %H:%M"), empty=_("Espaço vazio")) xalign 0.5
                            text FileSaveName(slot) xalign 0.5

screen preferences():
    tag menu
    add gui.game_menu_background

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1500
        ysize 820

        vbox:
            spacing 30

            hbox:
                xfill True
                text _("Preferências") style "menu_title"
                textbutton _("Voltar") action Return() xalign 1.0

            text _("Exibição") style "say_label"
            hbox:
                spacing 18
                textbutton _("Janela") action Preference("display", "window")
                textbutton _("Tela cheia") action Preference("display", "fullscreen")

            text _("Velocidade do texto") style "say_label"
            bar value Preference("text speed")

            text _("Avanço automático") style "say_label"
            bar value Preference("auto-forward time")

            text _("Música") style "say_label"
            bar value Preference("music volume")

            text _("Efeitos") style "say_label"
            bar value Preference("sound volume")

            text _("Conteúdo") style "say_label"
            if persistent.sensual_mode:
                textbutton _("Cenas sensuais: ATIVADAS") action ToggleField(persistent, "sensual_mode")
                text _("Extensões românticas opcionais aparecem apenas em rotas com consentimento e vínculo alto.") style "menu_subtitle"
            else:
                textbutton _("Cenas sensuais: DESATIVADAS") action ToggleField(persistent, "sensual_mode")
                text _("O jogo segue a versão romântica padrão, sem extensões sensuais.") style "menu_subtitle"

            text _("Acessibilidade") style "say_label"
            hbox:
                spacing 18
                textbutton _("Alternar auto") action Preference("auto-forward", "toggle")
                textbutton _("Sem transições") action Preference("transitions", "none")

screen cg_gallery():
    tag menu
    add gui.game_menu_background
    add Solid("#020912b8")

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1720
        ysize 900

        vbox:
            spacing 26

            hbox:
                xfill True
                vbox:
                    text _("Galeria de Memórias") style "menu_title"
                    text _("Cenas liberadas durante a jornada.") style "menu_subtitle"
                textbutton _("Voltar") action Return() xalign 1.0

            viewport:
                ysize 650
                draggable True
                mousewheel True
                scrollbars "vertical"

                grid 3 6:
                    spacing 28
                    use cg_card("O Julgamento", "O Julgamento", "cg final_judgment", "images/cgs/cg_final_judgment.png")
                    use cg_card("O Verão Escolhido", "O Verão Escolhido", "cg collective_thermal", "images/cgs/cg_collective_thermal.png")
                    use cg_card("Beijo Coletivo — Ariane", "Beijo Coletivo — Ariane", "cg collective_kiss_ariane", "images/cgs/cg_collective_kiss_ariane.png")
                    use cg_card("Beijo Coletivo — Nerissa", "Beijo Coletivo — Nerissa", "cg collective_kiss_nerissa", "images/cgs/cg_collective_kiss_nerissa.png")
                    use cg_card("Beijo Coletivo — Mélia", "Beijo Coletivo — Mélia", "cg collective_kiss_melia", "images/cgs/cg_collective_kiss_melia.png")
                    use cg_card("Beijo Coletivo — Lyra", "Beijo Coletivo — Lyra", "cg collective_kiss_lyra", "images/cgs/cg_collective_kiss_lyra.png")
                    use cg_card("Beijo Coletivo — Thalia", "Beijo Coletivo — Thalia", "cg collective_kiss_thalia", "images/cgs/cg_collective_kiss_thalia.png")
                    use cg_card("Beijo Coletivo — Cássia", "Beijo Coletivo — Cássia", "cg collective_kiss_cassia", "images/cgs/cg_collective_kiss_cassia.png")
                    use cg_card("Ariane — Varanda", "Ariane — Varanda", "cg ariane_balcony", "images/cgs/cg_ariane_balcony_v2.png")
                    use cg_card("Cássia — Estrelas", "Cássia — Estrelas", "cg cassia_stars", "images/cgs/cg_cassia_stars.png")
                    use cg_card("Ariane — Beijo", "Ariane — Beijo", "cg kiss_ariane", "images/cgs/cg_kiss_ariane.png")
                    use cg_card("Nerissa — Beijo", "Nerissa — Beijo", "cg kiss_nerissa", "images/cgs/cg_kiss_nerissa.png")
                    use cg_card("Mélia — Beijo", "Mélia — Beijo", "cg kiss_melia", "images/cgs/cg_kiss_melia.png")
                    use cg_card("Lyra — Beijo", "Lyra — Beijo", "cg kiss_lyra", "images/cgs/cg_kiss_lyra.png")
                    use cg_card("Thalia — Beijo", "Thalia — Beijo", "cg kiss_thalia", "images/cgs/cg_kiss_thalia.png")
                    use cg_card("Cássia — Beijo", "Cássia — Beijo", "cg kiss_cassia", "images/cgs/cg_kiss_cassia.png")
                    use cg_card("A Chegada", "A Chegada", "cg arrival", "images/cgs/cg_arrival_v2.png")
                    use cg_card("As Raízes", "As Raízes que Lembram", "cg asterion_roots", "images/cgs/cg_asterion_roots.png")
                    use cg_card("O Cerco de Akris", "O Cerco de Akris", "cg akris_siege", "images/cgs/cg_akris_siege.png")
                    use cg_card("Ariane — A Verdade", "Ariane — A Verdade", "cg crisis_ariane", "images/cgs/cg_crisis_ariane.png")
                    use cg_card("Nerissa — A Quarentena", "Nerissa — A Quarentena", "cg crisis_nerissa", "images/cgs/cg_crisis_nerissa.png")
                    use cg_card("Lyra — A Voz", "Lyra — A Voz", "cg crisis_lyra", "images/cgs/cg_crisis_lyra.png")
                    use cg_card("Thalia — A Muralha", "Thalia — A Muralha", "cg crisis_thalia", "images/cgs/cg_crisis_thalia.png")
                    use cg_card("Cássia — A Profecia", "Cássia — A Profecia", "cg crisis_cassia", "images/cgs/cg_crisis_cassia.png")
                    use cg_card("Oryx — A Revelação", "Oryx — A Revelação", "cg oryx_revelation", "images/cgs/cg_oryx_revelation.png")

screen cg_card(unlock_key, caption, cg, thumbnail):
    vbox:
        spacing 12
        if unlock_key in unlocked_cgs:
            imagebutton:
                idle Transform(thumbnail, size=(500, 281))
                hover Transform(thumbnail, size=(520, 292))
                action Show("cg_viewer", cg=cg)
            text caption xalign 0.5
        else:
            frame:
                xsize 500
                ysize 281
                background Solid("#0b2334")
                text _("Memória bloqueada") xalign 0.5 yalign 0.5
            text _("???") xalign 0.5

screen cg_viewer(cg):
    modal True
    zorder 300
    add Solid("#000000ef")
    add cg
    textbutton _("Fechar") action Hide("cg_viewer") xalign 0.96 yalign 0.05

screen about():
    tag menu
    add gui.game_menu_background

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1420
        ysize 760

        vbox:
            spacing 24

            hbox:
                xfill True
                text _("Sobre") style "menu_title"
                textbutton _("Voltar") action Return() xalign 1.0

            text "[config.name!t]"
            text _("Versão [config.version!t]")
            text _("Uma visual novel de fantasia mediterrânea sobre escolhas, memória e vínculos.")
            text _("Esta temporada contém o prólogo, quinze capítulos e rotas de epílogo.")
            text _("As rotas românticas dependem de afinidade e de escolhas feitas ao longo da jornada.")

screen relationships(close_action=Hide("relationships")):
    modal True
    zorder 200

    add Solid("#020912cc")

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 820

        vbox:
            spacing 25

            hbox:
                xfill True
                text _("Vínculos") style "menu_title"
                textbutton _("Fechar") action close_action xalign 1.0

            for person, points in [
                ("Ariane", ariane_affinity),
                ("Nerissa", nerissa_affinity),
                ("Mélia", melia_affinity),
                ("Lyra", lyra_affinity),
                ("Thalia", thalia_affinity),
                ("Cássia", cassia_affinity),
            ]:
                hbox:
                    xfill True
                    text person style "relationship_name"
                    text "[bond_rank(points)]" style "relationship_value" xalign 1.0

            null height 16
            text _("Traço predominante de Ivo: [dominant_trait()]") style "say_label"
            text _("Rastro do juramento: [integrity_rank(ivo_integrity)]") style "say_label"
            text _("Legado das escolhas: [legacy_rank(legacy_score())]") style "say_label"
            text _("Rupturas de rota: [crisis_break_count()]") style "say_label"

screen combat_hud(enemy_name):
    zorder 180
    frame:
        xalign 0.5
        yalign 0.04
        xsize 900
        background Solid("#071827e8")
        padding (24, 14)
        hbox:
            xfill True
            vbox:
                text _("CONFRONTO DE JURAMENTO") style "menu_kicker"
                text enemy_name style "say_label"
            vbox:
                xalign 1.0
                if combat_phase:
                    text "[combat_phase]" style "menu_kicker" xalign 1.0
                text _("Foco: [combat_focus]/[combat_focus_limit]") xalign 1.0
                text _("Pressão inimiga: [combat_enemy]") xalign 1.0

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add Solid("#020912cc")

    frame:
        style "panel"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 28
            text message xalign 0.5 text_align 0.5

            hbox:
                xalign 0.5
                spacing 30
                textbutton _("Sim") action yes_action
                textbutton _("Não") action no_action

screen skip_indicator():
    zorder 100

    frame:
        background Solid("#081d2de8")
        xalign 0.98
        yalign 0.05
        padding (20, 12)

        text _("Pulando")

screen notify(message):
    zorder 100

    frame:
        background Solid("#081d2de8")
        xalign 0.5
        yalign 0.08
        padding (24, 14)

        text message
