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

    frame:
        background Solid("#06131ec4")
        xalign 0.08
        yalign 0.5
        padding (48, 44)

        vbox:
            spacing 28

            text "Herdeiras de Atlântida" style "menu_title"
            text "Segredos do passado. Destinos entrelaçados." style "menu_subtitle"

            null height 16
            use navigation

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
            text _("Adaptação em visual novel do universo Herdeiras de Atlântida.")
            text _("A branch principal do repositório preserva o RPG original em Godot.")
            text _("Esta versão concentra-se em história, escolhas, vínculos e rotas narrativas.")

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
                ("Cassia", cassia_affinity),
            ]:
                hbox:
                    xfill True
                    text person style "relationship_name"
                    text "[bond_rank(points)]" style "relationship_value" xalign 1.0

            null height 16
            text _("Traço predominante de Ivo: [dominant_trait()]") style "say_label"

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
