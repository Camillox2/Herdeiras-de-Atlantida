define config.name = _("Herdeiras de Atlântida")
define config.version = "0.1.0-vn"
define build.name = "HerdeirasDeAtlantidaVN"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = "audio/music/kallipolis_harbor.wav"
define config.enter_transition = Dissolve(0.25)
define config.exit_transition = Dissolve(0.25)
define config.intra_transition = Dissolve(0.15)
define config.after_load_transition = Dissolve(0.25)
define config.end_game_transition = Fade(0.5, 0.0, 0.5)

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

define config.save_directory = "HerdeirasDeAtlantidaVN-2026"
define config.default_music_volume = 0.65
define config.default_sfx_volume = 0.70

default preferences.text_cps = 35
default preferences.afm_time = 12

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("game/cache/**", None)
    build.classify("game/saves/**", None)
    build.documentation("*.md")
