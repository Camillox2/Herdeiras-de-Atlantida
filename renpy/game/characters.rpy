define ivo = Character("Ivo", color="#d7e7ff", image="ivo")
define ariane = Character("Ariane", color="#71b9ff", image="ariane")
define nerissa = Character("Nerissa", color="#9ed6ec", image="nerissa")
define melia = Character("Mélia", color="#87d492", image="melia")
define lyra = Character("Lyra", color="#f0c76d", image="lyra")
define thalia = Character("Thalia", color="#ef8d82", image="thalia")
define cassia = Character("Cássia", color="#bba0df", image="cassia")
define lysandra = Character("Lysandra", color="#dfb48a", image="lysandra")
define polemon = Character("Pólemon", color="#e2c06f", image="polemon")
define collector = Character("Coletor", color="#d8848f", image="collector")
define moira_voice = Character("Voz", color="#7ce8ef")
define mikon = Character("Mikon", color="#a8d8ef")
define hieron = Character("Hieron", color="#d7b976")
define oren = Character("Oren", color="#c5d1d8")
define thoughts = Character(None, what_prefix="{i}", what_suffix="{/i}", window_style="say_window")

image bg title = Transform("images/backgrounds/title_kallipolis.png", size=(1920, 1080))
image bg kallipolis = Transform("images/backgrounds/bg_kallipolis.png", size=(1920, 1080))
image bg pensao = Transform("images/backgrounds/bg_pensao.png", size=(1920, 1080))
image bg agora = Transform("images/backgrounds/bg_agora.png", size=(1920, 1080))
image bg cisterna = Transform("images/backgrounds/bg_cisterna.png", size=(1920, 1080))
image bg nereu = Transform("images/backgrounds/bg_nereu.png", size=(1920, 1080))
image bg asterion = Transform("images/backgrounds/bg_asterion.png", size=(1920, 1080))
image bg lyria_temple = Transform("images/backgrounds/bg_lyria_temple.png", size=(1920, 1080))
image bg akris_fortress = Transform("images/backgrounds/bg_akris_fortress.png", size=(1920, 1080))
image bg nix_observatory = Transform("images/backgrounds/bg_nix_observatory.png", size=(1920, 1080))
image bg sunken_hall = Transform("images/backgrounds/bg_sunken_hall.png", size=(1920, 1080))
image bg kallipolis_storm = Transform("images/backgrounds/bg_kallipolis_storm.png", size=(1920, 1080))
image bg mirror_island = Transform("images/backgrounds/bg_mirror_island.png", size=(1920, 1080))

# CGs narrativos, compostos para preservar uma área de leitura na parte inferior.
image cg final_judgment = Transform("images/cgs/cg_final_judgment.png", size=(1920, 1080))
image cg ariane_balcony = Transform("images/cgs/cg_ariane_balcony.png", size=(1920, 1080))
image cg cassia_stars = Transform("images/cgs/cg_cassia_stars.png", size=(1920, 1080))
image cg kiss_ariane = Transform("images/cgs/cg_kiss_ariane.png", size=(1920, 1080))
image cg kiss_nerissa = Transform("images/cgs/cg_kiss_nerissa.png", size=(1920, 1080))
image cg kiss_melia = Transform("images/cgs/cg_kiss_melia.png", size=(1920, 1080))
image cg kiss_lyra = Transform("images/cgs/cg_kiss_lyra.png", size=(1920, 1080))
image cg kiss_thalia = Transform("images/cgs/cg_kiss_thalia.png", size=(1920, 1080))
image cg kiss_cassia = Transform("images/cgs/cg_kiss_cassia.png", size=(1920, 1080))
image cg arrival = Transform("images/cgs/cg_arrival.png", size=(1920, 1080))
image cg asterion_roots = Transform("images/cgs/cg_asterion_roots.png", size=(1920, 1080))
image cg akris_siege = Transform("images/cgs/cg_akris_siege.png", size=(1920, 1080))

image ivo neutral = "images/characters/ivo.png"
image ivo wary = "images/characters/ivo_wary.png"

image lysandra neutral = "images/characters/lysandra.png"
image lysandra skeptical = "images/characters/lysandra_skeptical.png"
image polemon neutral = "images/characters/polemon.png"
image polemon guarded = "images/characters/polemon_guarded.png"
image collector neutral = "images/characters/collector.png"
image collector command = "images/characters/collector_command.png"

image ariane neutral = "images/characters/ariane.png"
image ariane embarrassed = "images/characters/ariane_embarrassed.png"
image ariane concerned = "images/characters/ariane_concerned.png"

image nerissa neutral = "images/characters/nerissa.png"
image nerissa embarrassed = "images/characters/nerissa_embarrassed.png"

image melia neutral = "images/characters/melia.png"
image melia embarrassed = "images/characters/melia_embarrassed.png"
image lyra neutral = "images/characters/lyra.png"
image lyra embarrassed = "images/characters/lyra_embarrassed.png"
image lyra worried = "images/characters/lyra_worried.png"
image thalia neutral = "images/characters/thalia.png"
image thalia embarrassed = "images/characters/thalia_embarrassed.png"
image thalia defensive = "images/characters/thalia_defensive.png"
image cassia neutral = "images/characters/cassia.png"
image cassia embarrassed = "images/characters/cassia_embarrassed.png"
image cassia vision = "images/characters/cassia_vision.png"

transform portrait_left:
    subpixel True
    xalign 0.18
    yalign 1.06
    zoom 0.52
    yoffset 0
    block:
        ease 3.0 yoffset -6
        ease 3.0 yoffset 0
        repeat

transform portrait_center:
    subpixel True
    xalign 0.5
    yalign 1.06
    zoom 0.54
    yoffset 0
    block:
        ease 3.0 yoffset -6
        ease 3.0 yoffset 0
        repeat

transform portrait_right:
    subpixel True
    xalign 0.82
    yalign 1.06
    zoom 0.52
    yoffset 0
    block:
        ease 3.0 yoffset -6
        ease 3.0 yoffset 0
        repeat

transform portrait_enter_right:
    subpixel True
    xalign 1.15
    yalign 1.06
    zoom 0.52
    alpha 0.0
    parallel:
        ease 0.42 xalign 0.82 alpha 1.0
    parallel:
        block:
            ease 3.0 yoffset -6
            ease 3.0 yoffset 0
            repeat

transform portrait_enter_left:
    subpixel True
    xalign -0.15
    yalign 1.06
    zoom 0.52
    alpha 0.0
    parallel:
        ease 0.42 xalign 0.18 alpha 1.0
    parallel:
        block:
            ease 3.0 yoffset -6
            ease 3.0 yoffset 0
            repeat

transform portrait_emphasis_left:
    subpixel True
    xalign 0.18
    yalign 1.06
    zoom 0.54
    yoffset 0
    ease 0.10 yoffset -12
    ease 0.12 yoffset 0
    block:
        ease 3.0 yoffset -6
        ease 3.0 yoffset 0
        repeat

transform portrait_emphasis_right:
    subpixel True
    xalign 0.82
    yalign 1.06
    zoom 0.54
    yoffset 0
    ease 0.10 yoffset -12
    ease 0.12 yoffset 0
    block:
        ease 3.0 yoffset -6
        ease 3.0 yoffset 0
        repeat

# Ivo e Ariane foram ilustrados como bustos, não como silhuetas de corpo inteiro.
# Mantê-los em uma transformação própria evita que pareçam maiores que quem divide a cena.
transform portrait_bust_left:
    subpixel True
    xalign 0.18
    yalign 1.06
    zoom 0.46
    yoffset 0
    block:
        ease 3.0 yoffset -5
        ease 3.0 yoffset 0
        repeat

transform portrait_bust_center:
    subpixel True
    xalign 0.5
    yalign 1.06
    zoom 0.47
    yoffset 0
    block:
        ease 3.0 yoffset -5
        ease 3.0 yoffset 0
        repeat

transform portrait_bust_right:
    subpixel True
    xalign 0.82
    yalign 1.06
    zoom 0.46
    yoffset 0
    block:
        ease 3.0 yoffset -5
        ease 3.0 yoffset 0
        repeat

transform portrait_bust_enter_right:
    subpixel True
    xalign 1.15
    yalign 1.06
    zoom 0.46
    alpha 0.0
    parallel:
        ease 0.42 xalign 0.82 alpha 1.0
    parallel:
        block:
            ease 3.0 yoffset -5
            ease 3.0 yoffset 0
            repeat

transform portrait_bust_emphasis_right:
    subpixel True
    xalign 0.82
    yalign 1.06
    zoom 0.48
    yoffset 0
    ease 0.10 yoffset -10
    ease 0.12 yoffset 0
    block:
        ease 3.0 yoffset -5
        ease 3.0 yoffset 0
        repeat
