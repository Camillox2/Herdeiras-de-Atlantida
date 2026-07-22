style default:
    font gui.text_font
    size gui.text_size
    color gui.text_color

style say_window:
    background Solid("#07131de8")
    xalign 0.5
    yalign 0.98
    xsize 1780
    ysize 300
    padding (52, 32)

style say_label:
    size gui.name_text_size
    color "#8de7f2"
    bold True

style say_dialogue:
    size gui.text_size
    color "#f1f7fa"
    line_spacing 8

style choice_vbox:
    xalign 0.5
    yalign 0.72
    spacing 18

style choice_button:
    background Solid("#0b2335e8")
    hover_background Solid("#164a63f2")
    selected_background Solid("#1a5d75f2")
    xsize 1320
    padding (34, 20)

style choice_button_text:
    xalign 0.5
    text_align 0.5
    size 31
    color "#e8f4f8"
    hover_color "#ffffff"

style nav_button:
    background Solid("#081d2dcf")
    hover_background Solid("#15546ddf")
    xsize 420
    padding (28, 15)

style nav_button_text:
    xalign 0.5
    size 31
    color "#d8edf4"
    hover_color "#ffffff"

style menu_title:
    size 72
    color "#e8f7fb"
    outlines [(3, "#06111acc", 0, 2)]

style menu_subtitle:
    size 28
    color "#bcd6df"

style panel:
    background Solid("#07131de8")
    padding (42, 36)

style relationship_name:
    size 32
    color "#eaf7fa"

style relationship_value:
    size 28
    color "#8de7f2"
