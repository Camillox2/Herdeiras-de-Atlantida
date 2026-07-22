label splashscreen:
    scene bg title
    with fade
    pause 1.0
    centered "{size=64}{color=#eaf8fb}Herdeiras de Atlântida{/color}{/size}\n{size=28}{color=#9fcbd8}Segredos do passado. Destinos entrelaçados.{/color}{/size}\n\n{size=20}{color=#d6e5ee}Clique para continuar{/color}{/size}"
    pause 1.5
    return

label start:
    $ quick_menu = True
    jump prologue_start
