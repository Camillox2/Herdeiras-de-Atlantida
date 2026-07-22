label chapter_11_start:
    if not chapter_10_completed:
        jump chapter_10_start

    scene bg akris_fortress
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 11{/size}\n{size=30}A Muralha e o Cerco{/size}"

    "Akris não estava sob ataque de um exército. Isso era o que tornava tudo pior. As estradas ao redor da fortaleza estavam vazias; eram as mensagens que chegavam sem parar. Cada uma dizia que a cidade vizinha havia se rendido. Cada uma exigia que Thalia fechasse os portões antes que o medo entrasse."

    show thalia defensive at portrait_left
    show ivo wary at portrait_bust_right

    thalia "Se eu fechar, as aldeias da encosta ficam do lado de fora. Se eu abrir, o Conselho diz que a cidade vira alvo."
    ivo "E o que você quer fazer?"
    thalia "Eu quero uma escolha que não termine com alguém contando mortos depois."
    "No pátio, famílias vindas das aldeias esperavam sob chuva fina. Dentro dos muros, soldados sem sono vigiavam as mesmas pessoas que deveriam proteger."

    show nerissa neutral at portrait_center
    nerissa "Os navios sem bandeira não existem. Minhas vigias verificaram três vezes. Alguém está usando os sinos para transformar rumor em estratégia."
    thalia "Então a cidade está pronta para se trancar por causa de uma guerra que ainda não chegou."
    nerissa "Uma guerra que ainda não chegou também pode matar muita gente. Só demora mais."

    menu:
        "O que Ivo propõe para Akris?"

        "Abrir um corredor protegido para as aldeias, com todos vendo a operação.":
            $ akris_siege_choice = "corredor"
            $ trusted_thalia_council = True
            $ thalia_affinity += 2
            $ ivo_compassion += 2
            ivo "Não abrimos o portão sem plano. Abrimos uma rota, com guardas, médicos e gente da cidade olhando."
            "Thalia marcou o caminho no mapa. Pela primeira vez naquela manhã, a mão dela parou de tremer antes de tocar a espada."

        "Fazer o Conselho enfrentar as famílias antes de votar pelo fechamento.":
            $ akris_siege_choice = "conselho"
            $ thalia_affinity += 1
            $ ivo_honesty += 2
            ivo "Se querem decidir quem fica do lado de fora, que tenham coragem de olhar essas pessoas nos olhos."
            "A sala do Conselho foi aberta para a praça. Alguns conselheiros odiaram a ideia. Isso não a tornou menos necessária."

        "Encontrar os sinos antes de mexer nos portões.":
            $ akris_siege_choice = "sinos"
            $ ivo_courage += 2
            ivo "O medo está sendo fabricado. Enquanto o mecanismo estiver funcionando, qualquer decisão parece errado."
            "Ivo e Nerissa encontraram três sinos dentro de carroças de provisões. Não havia invasores; havia pessoas comuns que tinham sido convencidas a entregar o próprio pânico."

    "No fim da tarde, uma flecha caiu no pátio trazendo uma faixa de seda negra. A mensagem não era ameaça. Era uma lista de nomes: os mesmos moradores que o Conselho usaria para justificar o fechamento."
    show thalia neutral at portrait_left
    thalia "Ele quer que eu escolha uma lista. Como se comandar fosse decidir qual perda parece mais aceitável."
    ivo "Você pode comandar de outro jeito."
    thalia "É fácil dizer quando não nasceu ouvindo que uma muralha só vale alguma coisa se nunca cede."
    ivo "Muralhas cedem. A diferença é se fazem isso para esmagar alguém ou para deixar alguém entrar."

    menu:
        "Thalia precisa dar a ordem final. Ivo diz:"

        "Você não precisa carregar a cidade sozinha.":
            $ trusted_thalia_council = True
            $ thalia_affinity += 2
            $ ivo_compassion += 1
            ivo "Chama as pessoas que vão ser afetadas. Deixa elas segurarem parte da decisão com você."
            "Thalia respirou fundo e chamou ferreiros, enfermeiras, batedores e mães para o pátio. Não pediu obediência. Pediu trabalho."

        "A ordem precisa proteger quem não tem voz no Conselho.":
            $ thalia_affinity += 1
            $ ivo_honesty += 1
            ivo "Se a cidade vai se lembrar de algo, que seja de você escolhendo os mais vulneráveis antes dos mais poderosos."
            thalia "Essa é uma ordem que eu consigo dar."

        "Use a muralha como abrigo, não como ameaça.":
            $ thalia_affinity += 1
            $ ivo_courage += 1
            ivo "Abre o corredor. Mostra que Akris ainda é forte o bastante para proteger sem virar prisão."
            "Thalia ergueu a mão. Os portões não se escancararam; abriram-se na largura exata de uma promessa que pretendia cumprir."

    "Quando as primeiras famílias atravessaram, nada explodiu. O exército imaginário não veio. Os sinos foram quebrados diante da cidade, e a lista do Coletor perdeu o poder de parecer destino."
    "Thalia ficou ao lado do portão até a última carroça passar. Depois tirou a máscara de bronze do cinto e a colocou sobre a mesa do Conselho."
    thalia "Guardem isto, se quiserem. Eu não vou mais comandar escondida atrás de uma pessoa que sobrevivia sem olhar para quem ficava."
    nerissa "Vai ser uma péssima política."
    thalia "Ainda bem."
    ivo "O que acontece agora?"
    thalia "Agora perguntamos quem está produzindo os sinos. E por que toda estrada leva para o mesmo ponto."

    "No mapa, um quarto lugar brilhou entre as cidades: uma ilha que não constava em rota alguma, coberta pelo mesmo símbolo da coroa partida. Cassia reconheceu a marca em uma carta enviada por pombo."
    thalia "Ela chama de Ilha do Espelho. Diz que o Coletor está procurando algo lá antes de nós."

    $ chapter_11_completed = True
    jump chapter_11_summary


label chapter_11_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 11{/size}\n\n{size=30}Akris abriu os portões sem se render ao medo.{/size}"

    "Vínculo com Thalia: [bond_rank(thalia_affinity)]."
    "A próxima rota aponta para Cassia e a Ilha do Espelho."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 12 — A Ilha do Espelho":
            jump chapter_12_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_11_summary

        "Recomeçar o Capítulo 11":
            jump chapter_11_start

        "Voltar ao menu principal":
            return
