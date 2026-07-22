label chapter_07_start:
    if not chapter_06_completed:
        jump chapter_06_start

    scene bg kallipolis_storm
    with fade
    play music "audio/music/kallipolis_harbor.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}ARCO II — CAPÍTULO 7{/size}\n{size=30}A Cidade que Escolhe{/size}"

    "Kallípolis recebera o Juramento antes dos viajantes. Rumores chegaram de barco, de pombos e de pessoas que juravam ter visto seis luzes sobre o mar. Quando Ivo voltou, encontrou o cais tomado por chuva, filas de famílias e uma maré que subia sem obedecer à lua."

    show lysandra neutral at portrait_left
    show ivo wary at portrait_bust_right

    lysandra "Você escolheu uma semana péssima para virar lenda."
    ivo "Eu estava tentando voltar como cliente da pensão."
    lysandra "Clientes não trazem tempestades que chamam nomes."
    "Uma onda atingiu a muralha do cais. Entre os gritos, Ivo reconheceu uma voz infantil repetindo a mesma frase: 'A casa debaixo da água está abrindo'."

    show ariane neutral at portrait_center
    ariane "O Coletor está testando a cidade. Se a população entrar em pânico, alguém vai pedir uma salvadora."
    lysandra "E ele sabe exatamente quem apontar quando isso acontecer."

    menu:
        "O que Ivo prioriza no primeiro minuto da crise?"

        "Ajudar Lysandra a abrir a pensão como abrigo.":
            $ arc_2_priority = "abrigo"
            $ ivo_compassion += 2
            $ lysandra_trust += 2
            ivo "Paredes secas, sopa quente e nomes anotados. Primeiro ninguém fica sozinho na chuva."
            "Lysandra entregou uma chave a Ivo. Em minutos, quartos vazios viraram abrigo e a cozinha virou uma linha de trabalho."

        "Ir ao farol descobrir quem está chamando a maré.":
            $ arc_2_priority = "farol"
            $ ivo_courage += 2
            ariane "Finalmente uma decisão imprudente com utilidade."
            "No farol, Ivo encontrou marcas de bronze sob as lentes. Não eram um feitiço de ataque; eram uma convocação, feita para que o mar respondesse ao medo de quem a via."

        "Falar com a multidão antes que o pânico vire violência.":
            $ arc_2_priority = "multidao"
            $ ivo_honesty += 2
            ivo "Não tenho uma mentira bonita. Tenho mãos para ajudar e gente comigo que não vai abandonar vocês."
            "Não foi discurso de herói. Foi suficiente para que o primeiro homem largasse uma pedra, e para que outras pessoas começassem a carregar crianças em vez de culpar desconhecidos."

    hide lysandra
    show polemon guarded at portrait_left
    show ivo neutral at portrait_bust_right

    "Pólemon esperava sob um toldo rasgado, com água escorrendo do capuz e uma caixa de madeira aberta a seus pés. Dentro dela, dezenas de pequenos sinos de bronze vibravam sem tocar."
    polemon "Antes que me acuse, eu vim avisar. O Coletor espalhou esses sinos pelas cidades. Eles amplificam a pior coisa que uma multidão está pronta para acreditar."
    ivo "E você sabe disso porque?"
    polemon "Porque eu os transportei uma vez. Antes de entender o preço."
    "Ele não pediu perdão. Isso tornou a confissão mais difícil de ignorar."

    menu:
        "Ivo decide como lidar com Pólemon:"

        "Usar a informação dele, mas exigir que fique para reparar o dano.":
            $ trusted_polemon_again = True
            $ polemon_respect += 2
            $ ivo_honesty += 1
            ivo "Você conhece os sinos. Então vai ajudar a encontrar todos. Não como favor: como responsabilidade."
            polemon "Uma frase terrível para um mercador. Mas justa."

        "Mandá-lo embora e proteger a cidade sem ele.":
            $ trusted_polemon_again = False
            $ ivo_courage += 1
            ivo "Você avisou. Agora saia antes que alguém decida que a chuva é culpa sua também."
            "Pólemon assentiu, mas deixou o mapa dos sinos sobre a caixa. Algumas pessoas começavam a reparar mesmo sem saber como ficar."

        "Perguntar quem financia os sinos.":
            $ arc_2_priority = "financiador"
            $ polemon_respect += 1
            ivo "Bronze, navios, homens. O Coletor não faz isso sozinho. Quem compra a crise?"
            polemon "Uma liga de cidades que prefere um tirano previsível a seis mulheres com poder de dizer não. E alguém dentro de Kallípolis abriu os portões para eles."

    "Ao longe, o sino do farol tocou uma vez. A onda seguinte não veio. Em vez disso, a maré recuou, deixando no chão do cais uma única peça de bronze com o emblema da coroa partida."
    show collector command at portrait_left
    collector "Vocês salvaram uma noite. Agora tentem salvar uma cidade que acredita que precisa de mim."
    ariane "Ele não está escondendo a ameaça."
    ivo "Não. Está treinando as pessoas para aceitá-la."

    "Lysandra fechou a porta da pensão depois que a última criança encontrou uma cama. Pólemon marcou no mapa três cidades onde outros sinos haviam sido vistos. No alto do farol, a tempestade começava a ceder."
    lysandra "Então qual é o plano?"
    ivo "Não deixar que ele escolha quem fica com medo sozinho. Uma cidade de cada vez."
    ariane "Isso não é um plano."
    ivo "É o começo de um."
    ariane "Infelizmente, está ficando melhor nisso."

    $ chapter_07_completed = True
    jump chapter_07_summary


label chapter_07_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 7{/size}\n\n{size=30}O mar recuou. A ameaça não.{/size}"

    "Kallípolis resistiu esta noite. Três cidades ainda chamam por ajuda."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 8 — O Porto Fechado":
            jump chapter_08_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_07_summary

        "Recomeçar o Capítulo 7":
            jump chapter_07_start

        "Voltar ao menu principal":
            return
