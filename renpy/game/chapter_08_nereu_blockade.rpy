label chapter_08_start:
    if not chapter_07_completed:
        jump chapter_07_start

    scene bg nereu
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 8{/size}\n{size=30}O Porto Fechado{/size}"

    "Nereu cheirava a sal, corda molhada e pão que não chegaria a tempo. Três navios de abastecimento aguardavam fora das correntes da cidade, enquanto uma linha de embarcações sem bandeira bloqueava a entrada."
    "A capitã Nerissa acompanhava tudo da torre do cais. Não parecia assustada. Parecia alguém a quem o medo tinha dado trabalho demais para fazer."

    show nerissa neutral at portrait_left
    show ivo wary at portrait_bust_right

    nerissa "Se eu abrir as correntes, podemos trazer comida e também os homens do Coletor."
    ivo "Se não abrir?"
    nerissa "O mercado fica sem grãos em quatro dias. Em cinco, a cidade começa a procurar culpados."
    "No convés mais distante, uma criança agitou uma lanterna. Não era sinal de ataque. Era um pedido para voltar para casa."

    show ariane neutral at portrait_center
    ariane "A liga aprendeu rápido. Não precisa conquistar uma cidade se conseguir fazê-la escolher crueldade sozinha."
    nerissa "Meu pai fechou estes portões uma vez. Duas mil pessoas ficaram do lado errado. Eu não vou repetir a história dele."

    menu:
        "Como Ivo ajuda Nerissa a lidar com o bloqueio?"

        "Propor uma inspeção pública dos navios antes de abrir o porto.":
            $ nereu_decision = "inspecao"
            $ trusted_nerissa_command = True
            $ nerissa_affinity += 2
            $ ivo_honesty += 1
            ivo "Não esconda a decisão. Chame pescadores, médicos e famílias para verem cada porão. Se houver uma armadilha, ela não fica nas mãos de uma pessoa só."
            "Nerissa olhou para a cidade abaixo, calculando a resistência que uma verdade visível poderia criar."
            nerissa "Você faz democracia parecer uma operação militar. Eu respeito isso."

        "Mandar um barco pequeno resgatar primeiro os civis.":
            $ nereu_decision = "resgate"
            $ nerissa_affinity += 1
            $ ivo_compassion += 2
            ivo "Antes de decidir sobre carga, tiramos as pessoas da linha de fogo."
            "Nerissa hesitou apenas para dar uma ordem precisa. Um barco leve saiu pelos canais laterais, sem bandeira, e voltou com crianças, idosos e três tripulantes exaustos."

        "Procurar a marca dos sinos no farol de Nereu.":
            $ nereu_decision = "sinos"
            $ ivo_courage += 2
            ivo "Kallípolis ensinou uma coisa: alguém quer que a multidão sinta medo antes de saber por quê."
            "Dentro do farol, Ivo encontrou um sino de bronze preso à lente. A inscrição não invocava maré; invocava suspeita. Cada toque fazia qualquer sussurro parecer confissão."

    "Um conselheiro surgiu na escada da torre trazendo uma carta lacrada. A proposta era simples: entregar Nerissa ao bloqueio e os navios entrariam sem inspeção."
    "A praça explodiu em vozes. Alguns pediam que ela aceitasse. Outros pediam guerra. Nenhum deles precisava estar na ponte quando a primeira flecha voasse."
    show nerissa embarrassed at portrait_emphasis_left
    nerissa "Eu treinei a vida inteira para dar ordens. Ninguém me ensinou a aceitar que algumas pessoas vão me odiar mesmo quando faço o certo."
    ivo "Talvez fazer o certo não seja escolher quem fica com raiva. Talvez seja não deixar que a raiva escolha por você."

    menu:
        "Nerissa pede uma resposta direta. Ivo diz:"

        "Abra o porto com a cidade como testemunha.":
            $ trusted_nerissa_command = True
            $ nerissa_affinity += 2
            $ ivo_courage += 1
            ivo "Abre. Mas não para eles. Abre para todos que puderem ver e impedir que uma mentira assuma o controle."
            "Nerissa tomou a trompa de comando. A voz dela percorreu os muros sem pedir que acreditassem nela; pediu que viessem olhar."

        "Mantenha fechado até tirar o sino do farol.":
            $ ivo_honesty += 1
            $ nerissa_affinity += 1
            ivo "Um porto aberto sob encantamento não é escolha. Desarma a mentira, então chama a cidade."
            nerissa "Cautela sem abandono. É mais difícil do que parece."

        "Não entregue a própria vida por uma proposta do Coletor.":
            $ nerissa_affinity += 2
            $ ivo_compassion += 1
            ivo "Ele quer que você aceite ser a culpa visível. Não dá esse presente a ele."
            "Nerissa soltou uma risada curta, quase irritada por precisar ouvir aquilo. Depois rasgou a carta ao meio."

    "Ao meio-dia, as correntes se abriram. A inspeção revelou sacos de farinha, remédios e, sob uma lona, uma caixa de sinos de bronze. Pólemon tinha razão: o bloqueio não precisava de soldados para vencer; precisava que alguém entrasse em pânico primeiro."
    "Nerissa ordenou que a caixa fosse exibida na praça, não escondida. Quando a multidão viu o mecanismo, a suspeita perdeu parte da sua magia."

    show nerissa neutral at portrait_left
    nerissa "Meu pai achava que um capitão protege fechando portões."
    ivo "E você?"
    nerissa "Acho que protege ensinando pessoas a ver o que está tentando assustá-las."
    ariane "Uma frase muito boa. Anota antes que Pólemon tente vender como slogan."

    "No fundo da caixa havia um mapa parcial, marcado com duas rotas: as estufas de Asterion e uma estrada seca rumo ao deserto das estátuas."
    nerissa "Mélia vai precisar de ajuda. E alguém está levando sinos para longe do mar."
    ivo "Então seguimos antes que outra cidade precise escolher sozinha."

    $ chapter_08_completed = True
    jump chapter_08_summary


label chapter_08_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 8{/size}\n\n{size=30}Nereu abriu os portões sem abrir mão de si mesma.{/size}"

    "Vínculo com Nerissa: [bond_rank(nerissa_affinity)]."
    "A próxima rota aponta para Asterion e para uma ameaça que cresce sob as raízes."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 9 — As Raízes que Lembram":
            jump chapter_09_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_08_summary

        "Recomeçar o Capítulo 8":
            jump chapter_08_start

        "Voltar ao menu principal":
            return
