# Extensões opcionais: só são chamadas por rotas adultas já consolidadas e
# apenas quando a pessoa jogadora ativou o modo nas Preferências.

label sensual_ariane_bath:
    if not persistent.sensual_mode:
        return

    scene cg sensual_ariane_bath
    with dissolve
    play ambience "audio/ambience/harbor_night.wav" fadeout 0.5 fadein 0.5

    "Mais tarde, longe da praça, Ariane leva Ivo a uma pequena piscina termal que a pensão mantinha escondida entre colunas e buganvílias."
    ariane "Antes que você invente uma lenda: eu vim aqui porque queria silêncio. E porque queria sua companhia."
    ivo "Então eu fico. Do jeito que você quiser."
    "Ela aceita a xícara que ele oferece e deixa os dedos repousarem nos dele por um instante a mais do que o necessário. Não há pressa em transformar proximidade em promessa."
    ariane "É bom saber que posso pedir uma coisa simples sem o mundo desabar."
    ivo "E é bom saber que posso dizer sim sem precisar salvar ninguém primeiro."
    "Sob a lua, os dois permanecem juntos até a água perder o último reflexo das lanternas. Quando voltam, a cidade continua enorme — mas já não parece uma distância entre eles."
    return
