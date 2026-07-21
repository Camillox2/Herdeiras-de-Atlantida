define ivo = Character("Ivo", color="#d7e7ff", image="ivo")
define ariane = Character("Ariane", color="#71b9ff", image="ariane")
define nerissa = Character("Nerissa", color="#9ed6ec", image="nerissa")
define lysandra = Character("Lysandra", color="#dfb48a")
define polemon = Character("Pólemon", color="#e2c06f")
define collector = Character("Coletor", color="#d8848f")
define voice = Character("Voz", color="#7ce8ef")
define thoughts = Character(None, what_prefix="{i}", what_suffix="{/i}", window_style="say_window")

image bg title = im.Scale("images/backgrounds/title_kallipolis.png", 1920, 1080)
image bg kallipolis = im.Scale("images/backgrounds/bg_kallipolis.png", 1920, 1080)
image bg pensao = im.Scale("images/backgrounds/bg_pensao.png", 1920, 1080)
image bg agora = im.Scale("images/backgrounds/bg_agora.png", 1920, 1080)
image bg cisterna = im.Scale("images/backgrounds/bg_cisterna.png", 1920, 1080)
image bg nereu = im.Scale("images/backgrounds/bg_nereu.png", 1920, 1080)

image ivo neutral = "images/characters/ivo.png"

image ariane neutral = "images/characters/ariane.png"
image ariane embarrassed = "images/characters/ariane_embarrassed.png"

image nerissa neutral = "images/characters/nerissa.png"
image nerissa embarrassed = "images/characters/nerissa_embarrassed.png"

image melia neutral = "images/characters/melia.png"
image melia embarrassed = "images/characters/melia_embarrassed.png"
image lyra neutral = "images/characters/lyra.png"
image lyra embarrassed = "images/characters/lyra_embarrassed.png"
image thalia neutral = "images/characters/thalia.png"
image thalia embarrassed = "images/characters/thalia_embarrassed.png"
image cassia neutral = "images/characters/cassia.png"
image cassia embarrassed = "images/characters/cassia_embarrassed.png"

transform portrait_left:
    xalign 0.18
    yalign 1.0
    zoom 0.86

transform portrait_center:
    xalign 0.5
    yalign 1.0
    zoom 0.90

transform portrait_right:
    xalign 0.82
    yalign 1.0
    zoom 0.86

transform portrait_enter_right:
    xalign 1.15
    yalign 1.0
    zoom 0.86
    ease 0.35 xalign 0.82

transform portrait_enter_left:
    xalign -0.15
    yalign 1.0
    zoom 0.86
    ease 0.35 xalign 0.18
