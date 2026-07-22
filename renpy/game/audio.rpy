# Camada ambiental original: a trilha continua nos WAVs musicais existentes;
# este canal usa o controle de efeitos das Preferências.
init python:
    renpy.music.register_channel("ambience", "sfx", loop=True, tight=True)
