# Ecos de escolhas antigas. Estes momentos não concedem pontos: tornam as
# decisões já feitas visíveis quando o mundo volta a cobrar por elas.

label late_consequence_ch07:
    show ariane neutral at portrait_left
    show ivo wary at portrait_bust_right
    if told_ariane_everything:
        ariane "Quando você me contou a verdade na pensão, eu achei que estava me dando um problema. Agora vejo que me deu tempo para não enfrentar isso sozinha."
        ivo "Eu quase não contei."
        ariane "Quase não constrói ponte nenhuma. Você contou. Lembra disso quando a cidade pedir atalhos."
    elif hid_heirs_from_ariane or hid_third_echo:
        ariane "Se você souber de outra visão, não espere ela virar desastre para me chamar."
        ivo "Eu queria proteger você."
        ariane "Então me dê informação. Não uma gaiola com boas intenções."
    hide ariane
    hide ivo
    return

label late_consequence_ch08:
    show nerissa neutral at portrait_left
    show ivo wary at portrait_bust_right
    if trusted_nerissa_with_coin:
        nerissa "Você entregou a moeda quando ainda não tinha motivo para confiar em mim. Por isso os capitães ouviram quando pedi que esperassem."
        "Os navios no horizonte mantêm as velas baixas. Uma chance pequena de conversa ainda existe."
    else:
        nerissa "Da última vez, você guardou o que podia ter dividido. Hoje eu preciso de um motivo melhor para abrir o porto."
        ivo "Você vai ter um."
        nerissa "Então faça ele existir antes de pedir que eu aposte uma cidade."
    hide nerissa
    hide ivo
    return

label late_consequence_ch10:
    show lyra worried at portrait_left
    show ivo wary at portrait_bust_right
    if trusted_lyra_song and protected_mikon:
        lyra "Mikon perguntou se ainda pode cantar perto de você. Eu disse que pode."
        "Não é perdão completo; é uma voz a mais disposta a atravessar a praça quando o silêncio parece mais seguro."
    else:
        lyra "Uma cidade aprende rápido quem é ouvido apenas quando convém. Não peça coragem de crianças se os adultos ainda escolhem o silêncio."
        ivo "Eu sei."
        lyra "Saber é o começo. Não use como final."
    hide lyra
    hide ivo
    return

label late_consequence_ch09:
    show melia neutral at portrait_left
    show ivo wary at portrait_bust_right
    if heard_melia_name:
        melia "Você ouviu meu nome antes de me conhecer e mesmo assim esperou que eu dissesse quem era. Aqui, isso não acontece muito."
        ivo "Eu já tinha decidido que profecia não é apresentação."
    else:
        melia "Raízes odeiam ser arrancadas por quem ainda não sabe o nome da árvore. Hoje vamos aprender devagar."
    hide melia
    hide ivo
    return

label late_consequence_ch11:
    show thalia defensive at portrait_left
    show ivo wary at portrait_bust_right
    if saved_akris_scouts and trusted_thalia_with_map:
        thalia "Os batedores voltaram porque você não tratou gente como peça de mapa. Hoje eles abriram um corredor antes do rumor chegar."
        "Uma patrulha acende lanternas na estrada da encosta: uma rota existe porque, antes, alguém foi escolhido para voltar."
    else:
        thalia "Não tenho batedores suficientes para prometer que conheço a estrada. Isso é o que escolhas antigas fazem: deixam buracos onde uma certeza deveria estar."
        ivo "Então não vou pedir certeza. Só um plano que admita o buraco."
    hide thalia
    hide ivo
    return

label late_consequence_ch12:
    show cassia vision at portrait_left
    show ivo wary at portrait_bust_right
    if trusted_cassia_vision and trusted_cassia_truth:
        cassia "Você acreditou na minha visão sem transformá-la em sentença. Por isso eu vou mostrar o que ainda não consigo calcular."
        "Cássia abre o astrolábio. Pela primeira vez, ela não procura uma resposta que Ivo possa carregar sozinho."
    elif kept_future_secret:
        cassia "Segredos úteis ainda são segredos. Eu sei porque passei anos chamando os meus de prudência."
        ivo "E o que fazemos agora?"
        cassia "Dizemos a verdade antes que ela vire arquitetura."
    else:
        cassia "A ilha vai mostrar versões de nós que se parecem demais com desculpas. Não aceite a mais confortável só porque ela usa o seu rosto."
    hide cassia
    hide ivo
    return

label late_consequence_ch13:
    if legacy_score() >= 8:
        "Quando o Abismo chama, seis respostas chegam antes do medo: uma rota de Nerissa, sementes de Mélia, vozes de Lyra, vigias de Thalia, um cálculo incompleto de Cássia e uma chave de Ariane. Ninguém entrega a solução; todos entregam presença."
    elif legacy_score() <= 2:
        "O Abismo responde com os silêncios que Ivo deixou crescer. As herdeiras ainda estão ali, mas cada uma mede a distância antes de oferecer a mão. A travessia será possível — só não será gratuita."
    else:
        "O grupo chega ao Abismo com acordos imperfeitos, mas reais. Ainda há perguntas que ninguém quer fazer; desta vez, porém, ninguém finge que elas não existem."
    return
