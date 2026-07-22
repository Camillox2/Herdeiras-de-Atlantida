label chapter_15_start:
    if not chapter_14_completed:
        jump chapter_14_start

    scene bg sunken_hall
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    if "O Julgamento" not in unlocked_cgs:
        $ unlocked_cgs.append("O Julgamento")

    scene cg final_judgment
    with dissolve

    centered "{size=52}CAPÍTULO 15{/size}\n{size=30}O Julgamento do Juramento{/size}"

    "Quando o Salão Afundado abriu pela última vez, não havia máscara, cadeira ou inimigo à espera. Havia apenas as seis cadeiras vazias, o círculo de luz no chão e a água quieta demais para ser mar."
    "Cássia explicou que o juramento não julgava inocência. Julgava disposição: se cada pessoa continuaria tratando as outras como alguém inteiro quando a escolha se tornasse dolorosa."

    show ariane neutral at portrait_left
    show ivo neutral at portrait_bust_center
    show cassia neutral at portrait_right

    ariane "Então a ruína decidiu nos dar uma prova moral. Eu odeio quando prédios fazem isso."
    cassia "Não é o prédio. Somos nós usando o prédio como desculpa para perguntar o que evitamos."
    ivo "E se a resposta for ruim?"
    cassia "Então ela ainda é uma resposta. O perigo começa quando alguém tenta escondê-la em nome de todos."

    "O círculo acendeu. Cada cadeira mostrou uma memória, não como punição, mas como porta. Ariane viu a família que não conseguiu salvar. Nerissa, os portões fechados. Mélia, a primeira semente enterrada por medo. Lyra, uma voz proibida. Thalia, a ponte. Cássia, a versão de si mesma sozinha."

    menu:
        "O juramento pede a Ivo uma regra para o grupo. Ele escolhe:"

        "Nenhum segredo pode ser usado para tomar o lugar de uma escolha.":
            $ ivo_honesty += 2
            $ ending_route = "honestidade"
            ivo "Podemos guardar coisas por um tempo. Mas ninguém transforma silêncio em arma."
            "As seis cadeiras se aproximaram alguns centímetros, como se a própria sala aceitasse que confiança não era ausência de medo, e sim uma forma de voltar depois dele."

        "Ninguém será deixado para trás para tornar a decisão mais fácil.":
            $ ivo_compassion += 2
            $ ending_route = "compaixao"
            ivo "Não prometo que nunca vamos perder. Prometo que ninguém vira custo aceitável enquanto ainda houver alguém para tentar."
            "Mélia colocou a mão sobre a mesa. Uma raiz verde atravessou o mármore e floresceu entre os símbolos."

        "A responsabilidade fica com quem decide, nunca com quem sofre.":
            $ ivo_courage += 2
            $ ending_route = "responsabilidade"
            ivo "Quem dá uma ordem olha para quem vai pagar por ela. Se não consegue, não dá a ordem."
            "Thalia assentiu. Não como soldado diante de um comando, mas como alguém que reconhecia uma regra que teria mudado uma vida inteira."

    "As memórias não desapareceram. Tornaram-se suportáveis. Ariane deixou a fita vermelha na cadeira da chama; Nerissa derramou água na da onda; Mélia colocou uma semente na da raiz; Lyra pousou uma corda da lira na da voz; Thalia deixou a máscara sobre a muralha; Cássia alinhou o astrolábio à estrela."
    "A Marca de Ivo se abriu em sete fios. Um para cada herdeira. O último ficou no próprio pulso, não como coroa, mas como lembrança de que estar no centro não significava estar acima."

    show lyra neutral at portrait_left
    show thalia neutral at portrait_right
    lyra "E o homem da torre?"
    ivo "Ele continua sendo uma possibilidade."
    thalia "Então vamos garantir que não fique sozinho tempo suficiente para virar uma."

    "Do lado de fora, a água baixou. A torre de Oryx desapareceu no horizonte, mas as cidades continuavam ali: imperfeitas, assustadas e vivas. O Coletor não foi absolvido. Tampouco foi tratado como destino."
    "No lugar da sétima cadeira, o juramento deixou uma mesa simples com espaço para sete pessoas. Sem tronos. Sem ordens."

    $ chapter_15_completed = True
    jump ending_selector


label ending_selector:
    scene bg title
    with fade
    stop music fadeout 1.0

    centered "{size=54}EPÍLOGOS{/size}\n{size=30}Os vínculos construídos ao longo da jornada agora definem como Ivo segue em frente.{/size}"

    menu:
        "Qual futuro Ivo escolhe?"

        "Seguir sem romance, como parte da aliança.":
            $ ending_route = "alianca"
            jump ending_alliance

        "Escolher uma pessoa, se houver vínculo profundo.":
            jump ending_single_menu

        "Construir uma relação coletiva, se todas tiverem vínculo profundo.":
            if ariane_affinity >= 7 and nerissa_affinity >= 7 and melia_affinity >= 7 and lyra_affinity >= 7 and thalia_affinity >= 7 and cassia_affinity >= 7:
                $ ending_route = "coletiva"
                jump ending_collective
            else:
                "O grupo ainda não construiu confiança suficiente para uma relação coletiva. O juramento recusa transformar afinidade baixa em obrigação."
                jump ending_selector
