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


label sensual_nerissa_bath:
    if not persistent.sensual_mode:
        return

    scene cg sensual_nerissa_bath
    with dissolve
    play ambience "audio/ambience/harbor_night.wav" fadeout 0.5 fadein 0.5

    "Em Nereu, Nerissa conhece uma varanda de banho acima do porto. O lugar é discreto, mas a vista é ampla demais para permitir que qualquer um finja não sentir o mar."
    nerissa "Eu costumava vir aqui para pensar nas decisões que ainda não tinha tomado. Hoje eu preferi não trazer nenhuma."
    ivo "Posso ficar mesmo sem uma pauta?"
    nerissa "Pode. Acho que essa é a primeira vez que estou pedindo isso sem transformar em ordem."
    "Ivo estende a toalha, e Nerissa a aceita sorrindo de um jeito que seria fácil perder se ele ainda estivesse procurando uma vitória. Os dois conversam baixo, entre os reflexos azuis da água."
    nerissa "Ficar perto de alguém não precisa ser uma estratégia. Ainda estou aprendendo."
    ivo "Eu também. Podemos aprender devagar."
    "Quando os primeiros sinos do porto soam, ela não se apressa para vestir a armadura de comandante. Apenas segura a mão dele e olha o céu clarear."
    return


label sensual_melia_spring:
    if not persistent.sensual_mode:
        return

    scene cg sensual_melia_spring
    with dissolve
    play ambience "audio/ambience/observatory_stars.wav" fadeout 0.5 fadein 0.5

    "Mélia encontra uma nascente escondida no jardim de Asterion, onde a água morna corre entre raízes luminosas. Ela diz que as plantas não contam segredos, mas sorri como quem espera que Ivo não teste a teoria."
    melia "Trouxe uma flor. Não como presente. Ela fica melhor fora da terra por alguns minutos."
    ivo "Então hoje somos os dois tentando ficar bem fora do lugar de costume."
    "Mélia aceita a flor de volta e aproxima a mão da dele, esperando que ele feche a distância por escolha própria."
    melia "Gosto quando você pergunta sem transformar tudo em obrigação."
    ivo "Gosto quando você me deixa escolher onde ficar."
    "A água reflete os dois entre folhas e lanternas. Por alguns minutos, nada precisa crescer depressa — nem a confiança, nem o futuro."
    return
