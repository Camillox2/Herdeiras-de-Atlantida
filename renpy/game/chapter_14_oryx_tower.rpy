label chapter_14_start:
    if not chapter_13_completed:
        jump chapter_13_start

    scene bg nix_observatory
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2
    play ambience "audio/ambience/observatory_stars.wav" fadeout 0.8 fadein 1.0

    centered "{size=52}CAPÍTULO 14{/size}\n{size=30}O Homem que Voltou Tarde Demais{/size}"

    if "Oryx — A Revelação" not in unlocked_cgs:
        $ unlocked_cgs.append("Oryx — A Revelação")
    scene cg oryx_revelation
    with dissolve
    play sound "audio/sfx/moiras_chime.wav"
    "A superfície negra entre as pedras devolve duas silhuetas que a mesma escolha poderia ter produzido. Ivo não olha para o reflexo por muito tempo."

    "A Torre de Oryx não tinha portas. Tinha uma escada que terminava em céu aberto e, no topo, uma lente voltada para uma estrela inexistente. Cássia jurou que a torre não podia estar de pé; ainda assim, cada degrau reconhecia os passos de Ivo antes que ele os desse."

    show cassia vision at portrait_left
    show ivo wary at portrait_bust_right

    cassia "Esta torre foi apagada dos registros depois da primeira interrupção do juramento."
    ivo "Então por que ela está aqui?"
    cassia "Porque alguma coisa passou anos querendo que você fizesse essa pergunta."
    "No centro do observatório, a máscara do Coletor flutuava sobre uma cadeira vazia. Desta vez, ela não falou com muitas vozes. Falou com uma só."

    collector "Você me reconhece."
    "A máscara se abriu. Do outro lado havia um homem mais velho, marcado pelo sal, com os olhos de Ivo e uma cicatriz atravessando o mesmo pulso esquerdo."
    ivo "Não."
    collector "Não ainda."

    show ariane neutral at portrait_center
    ariane "Aquele é..."
    cassia "Uma possibilidade preservada. Não um destino."
    "O homem sorriu sem alegria."
    collector "Eu também disse isso, no começo. Depois vi uma cidade afundar porque me recusei a escolher. Depois vi outra morrer porque escolhi tarde. Em algum momento, a culpa ficou mais fácil de carregar do que a dúvida."

    menu:
        "Diante do próprio futuro, Ivo pergunta:"

        "Quem você tentou salvar primeiro?":
            $ oryx_choice = "primeira"
            $ ivo_compassion += 1
            $ cassia_affinity += 1
            ivo "Não quero saber quem você sacrificou. Quero saber quem você pensou que estava salvando."
            collector "Uma criança em uma rua que você ainda não conhece. Eu a salvei. E depois usei aquela memória para justificar cada pessoa que deixei para trás."
            ivo "Então você não virou monstro porque não se importava. Virou porque decidiu que se importar bastava."

        "Por que trazer Ivo de outro mundo?":
            $ oryx_choice = "mundo"
            $ ivo_honesty += 2
            ivo "Você não podia me obrigar a repetir seu caminho, então me arrancou da minha vida?"
            collector "Eu abri a porta procurando uma versão de mim que ainda soubesse dizer não. Você caiu através dela antes que eu pudesse fechá-la."
            ivo "Isso não faz de mim sua correção. Faz de você responsável por me trazer."

        "O que você teme que aconteça se perder?":
            $ oryx_choice = "medo"
            $ ivo_courage += 1
            ivo "Não fala de ordem. Fala do que acontece quando você não controla mais ninguém."
            collector "Tudo o que tentei salvar me odeia. E talvez tenham razão."
            "Ariane não respondeu. Às vezes uma verdade precisava ficar no ar antes que alguém tentasse consertá-la."

    "A lente mostrou o passado do homem: Ivo mais velho diante de uma enchente, sozinho porque as seis herdeiras tinham sido separadas uma a uma por guerras, medos e promessas quebradas. A máscara lhe ofereceu uma cidade salva em troca de outra."
    "Ele aceitou. Depois aceitou de novo. A cada escolha, a máscara ficava mais fácil de vestir e as pessoas ficavam mais fáceis de transformar em números."
    collector "Eu não criei o mecanismo. Eu apenas fui o suficiente desesperado para fazê-lo funcionar."
    ivo "E agora quer que eu faça o mesmo antes de descobrir outra saída."
    collector "Quero que você me prove errado."

    "Um fragmento da máscara se desprende da lente e tenta repetir os gestos que fizeram o outro Ivo ceder. Cássia segura a respiração, esperando que desta vez a resposta seja escolha, não destino."
    call juramento_confronto("Fragmento da Máscara", 4, "Cássia", "stars")
    if combat_result == "won":
        $ cassia_affinity += 1
        cassia "Você acabou de transformar uma previsão em evidência. É bem diferente."
    else:
        $ ivo_integrity -= 1
        cassia "A máscara quase encontrou uma brecha. Não se castigue por ela; apenas não a chame de inevitável."

    menu:
        "Ivo responde à versão que falhou:"

        "Eu não vou ser você, mas não vou fingir que você não existe.":
            $ faced_future_ivo = True
            $ ivo_honesty += 2
            $ ariane_affinity += 1
            ivo "Se eu tratar você como monstro, aprendo nada. Se tratar como desculpa, repito tudo. Você é um aviso. Não é meu destino."
            collector "Essa é uma resposta que eu não consegui dar."

        "Entregue a máscara e venha responder pelo que fez.":
            $ faced_future_ivo = True
            $ ivo_courage += 2
            ivo "Você pode parar de decidir por cidades. Não apaga o passado, mas começa a devolvê-lo a quem pagou por ele."
            collector "Você ainda acredita que depois de escolhas suficientes existe um 'depois'."
            ivo "É por isso que estou aqui."

        "As seis herdeiras podem impedir o que você não conseguiu.":
            $ faced_future_ivo = True
            $ ariane_affinity += 1
            $ cassia_affinity += 1
            ivo "Você ficou sozinho e chamou isso de necessidade. Nós não vamos."
            "Ao redor de Ivo, as seis luzes do juramento apareceram. Não eram armas. Eram presenças que a máscara não conseguia converter em cadeira."

    "Por um instante, o homem mais velho pareceu livre da máscara. Ele olhou para o pulso de Ivo, depois para Ariane e Cássia."
    collector "A torre está segurando a porta entre os mundos. Se ela cair, você pode voltar."
    ivo "E você?"
    collector "Eu fico onde as minhas escolhas terminaram."
    cassia "Isso não é reparação. É fuga com poesia."
    "O homem riu, pela primeira vez como alguém real."
    collector "Você sempre foi mais difícil do que eu previa."

    "A torre começou a se desfazer. O fragmento da máscara não tentou atacar. Tentou alcançar a mão de Ivo, como se pedisse que ele aceitasse a solução rápida mais uma vez."
    "Ivo fechou os dedos, não para segurá-lo, mas para deixá-lo cair. Ariane cortou o fragmento com a fita vermelha; Cássia prendeu a poeira resultante num anel do astrolábio."
    "O futuro de Ivo não desapareceu. Apenas deixou de ocupar a cadeira do presente."

    collector "O Salão Afundado vai abrir uma última vez. Quando abrir, o juramento vai exigir não uma cidade — mas a verdade que cada um de vocês esconde de si mesma."
    "A imagem se partiu. No topo da torre, o céu voltou a ser apenas céu."

    $ chapter_14_completed = True
    jump chapter_14_summary


label chapter_14_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 14{/size}\n\n{size=30}O inimigo tinha o rosto de uma possibilidade. O presente ainda tem escolha.{/size}"

    "A próxima rota retorna ao Salão Afundado para o julgamento final do juramento."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 15 — O Julgamento do Juramento":
            jump chapter_15_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_14_summary

        "Recomeçar o Capítulo 14":
            jump chapter_14_start

        "Voltar ao menu principal":
            return
