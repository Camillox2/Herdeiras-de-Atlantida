label chapter_12_start:
    if not chapter_11_completed:
        jump chapter_11_start

    scene bg mirror_island
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 12{/size}\n{size=30}A Ilha do Espelho{/size}"

    call late_consequence_ch12

    "A Ilha do Espelho não aparecia em mapas porque não estava sempre no mesmo lugar. À noite, a lagoa refletia um céu que Nix nunca tinha visto; ao amanhecer, cada ruína mostrava uma versão do visitante que fizera uma escolha diferente."

    show cassia vision at portrait_left
    show ivo wary at portrait_bust_right

    cassia "Não olhe para a água por tempo demais. Ela não mostra desejos. Mostra justificativas."
    ivo "Qual é a diferença?"
    cassia "Desejos pedem. Justificativas fingem que não havia outra saída."
    "No espelho da lagoa, Ivo viu a si mesmo deixando Kallípolis sem olhar para trás. Na versão refletida, as cidades continuavam existindo — só que ninguém dizia seu nome."

    show ariane neutral at portrait_center
    ariane "Você está vendo alguma coisa útil?"
    ivo "Uma versão de mim com menos problemas."
    ariane "Parece claramente uma armadilha."

    "Cássia conduziu o grupo até uma coluna quebrada. Dentro dela havia uma máscara de bronze, menor que a do Coletor, coberta de inscrições que mudavam sempre que alguém tentava lê-las."
    cassia "O primeiro Coletor não era uma pessoa. Era um cargo. Um guardião criado para preservar cidades escolhendo qual delas podia ser sacrificada."
    ivo "E alguém decidiu que isso era uma boa ideia?"
    cassia "Alguém com medo suficiente para chamar crueldade de matemática."

    menu:
        "Como Ivo reage ao segredo da máscara?"

        "Perguntar por que Cássia nunca contou isso.":
            $ mirror_choice = "verdade"
            $ cassia_affinity += 2
            $ ivo_honesty += 1
            ivo "Você sabia que a máscara podia escolher pessoas. Por que me trouxe aqui sem dizer?"
            cassia "Porque eu não sabia se você ficaria. E porque parte de mim preferia uma mentira administrável a uma verdade que pudesse afastar todos."
            ivo "Então começa dizendo a verdade antes que a máscara use seu silêncio."

        "Focar em destruir a máscara antes que ela escolha outro hospedeiro.":
            $ mirror_choice = "destruir"
            $ ivo_courage += 2
            ivo "Cargo ou pessoa, isto não pode continuar procurando alguém para vestir."
            cassia "Destruir sem entender pode apenas espalhar a função. Mas concordo que não podemos deixá-la acordada."

        "Pedir que cada um diga o que viu no reflexo.":
            $ mirror_choice = "partilhar"
            $ cassia_affinity += 1
            $ ivo_compassion += 2
            ivo "A ilha se alimenta do que a gente esconde. Então não vamos dar isso de graça."
            "Ariane falou primeiro. Thalia falou por último. Cássia demorou, mas contou que vira a si mesma governando todas as cidades porque não confiava em ninguém mais para ver o futuro."

    "A máscara rachou. De dentro dela não saiu fumaça, mas uma sala antiga: seis pessoas sentadas ao redor de uma mesa, discutindo uma enchente que não podiam deter. Uma voz dizia que uma cidade precisava ser salva; outra respondia que nenhuma cidade valia uma criança deixada do lado de fora."
    "A figura que venceu não usava máscara. Usava a Marca que agora estava no pulso de Ivo."
    show cassia neutral at portrait_left
    cassia "O portador anterior escolheu uma cidade. O juramento foi criado para impedir que alguém voltasse a ter esse poder sozinho."
    ivo "E o Coletor quer me transformar nele."
    cassia "Quer que você acredite que não existe alternativa. É assim que a máscara entra."

    "A lagoa começou a subir pelas pedras, mostrando uma versão mais cruel da história: Ivo sentado na cadeira central do Salão Afundado; seis cidades ajoelhadas; cada herdeira em silêncio atrás dele."
    show cassia vision at portrait_emphasis_left
    cassia "Esta é a visão que eu escondi. Não porque ela seja inevitável. Porque eu tinha medo de que ela parecesse conveniente para alguém."

    menu:
        "Diante da pior visão, Ivo responde a Cássia:"

        "Obrigado por mostrar antes que ela virasse segredo.":
            $ trusted_cassia_truth = True
            $ cassia_affinity += 2
            $ ivo_compassion += 1
            ivo "Ter medo não torna você a máscara. Esconder para sempre talvez tornasse. Você mostrou. Isso muda tudo."
            "Cássia segurou o astrolábio com menos força. O reflexo de Ivo na lagoa deixou de usar coroa."

        "Vamos destruir a cadeira antes que alguém possa sentar nela.":
            $ trusted_cassia_truth = True
            $ ivo_courage += 2
            $ cassia_affinity += 1
            ivo "Se existe uma peça feita para reduzir seis pessoas a ferramentas, ela não merece ficar esperando alguém desesperado."
            "Ariane cortou a imagem com a fita vermelha. O reflexo se desfez em água comum, fria e sem autoridade."

        "A visão não decide quem eu vou ser.":
            $ ivo_honesty += 1
            $ cassia_affinity += 1
            ivo "Eu já vi versões minhas fazendo coisas que não quero. Isso só me mostra onde preciso prestar atenção."
            cassia "Essa é a resposta mais difícil de colocar em um mapa."

    "Sob a coluna, o grupo encontrou um disco de bronze com a rota de todos os sinos. Eles não formavam um cerco em torno das cidades. Formavam uma espiral em direção a um lugar só: o Abismo de Tálassa, onde o Salão Afundado tocava a corrente mais profunda do mar."
    ariane "É lá que ele quer ativar a máscara."
    cassia "Ou é lá que a máscara quer ativar alguém. Há diferença."
    ivo "Então chegamos antes e impedimos os dois."
    show cassia embarrassed at portrait_emphasis_left
    cassia "Você diz coisas impossíveis como se fossem uma agenda de viagem."
    ivo "Está funcionando até agora."
    cassia "Isso não é evidência."
    ariane "É um pouco de evidência."

    "Quando o grupo deixou a ilha, a lagoa devolveu apenas seus reflexos verdadeiros. Imperfeitos, cansados e sem coroas."

    $ chapter_12_completed = True
    jump chapter_12_summary


label chapter_12_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 12{/size}\n\n{size=30}A máscara não prevê o futuro. Ela tenta convencer alguém a repeti-lo.{/size}"

    "Vínculo com Cássia: [bond_rank(cassia_affinity)]."
    "A próxima rota leva ao Abismo de Tálassa, onde o Coletor prepara sua escolha final."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 13 — O Abismo de Tálassa":
            jump chapter_13_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_12_summary

        "Recomeçar o Capítulo 12":
            jump chapter_12_start

        "Voltar ao menu principal":
            return
