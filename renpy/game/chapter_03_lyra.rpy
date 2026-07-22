label chapter_03_start:
    if not chapter_02_completed:
        jump chapter_02_start

    scene bg lyria_temple
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 3{/size}\n{size=30}A Canção que Não Termina{/size}"

    show lyra neutral at portrait_left
    show ivo wary at portrait_bust_right

    "Lýria fora construída para que o mar pudesse ser escutado sem precisar ser enfrentado. Naquela hora, porém, as ondas abaixo dos penhascos batiam no compasso insistente de uma respiração presa."
    "No centro do templo, uma jovem cantava para um círculo de água imóvel. A voz era baixa, quase íntima; ainda assim, fazia as chamas dos braseiros se inclinarem para ela como quem escuta uma ordem."

    lyra "Não entrem no círculo."
    ivo "Essa é uma forma bastante direta de dar boas-vindas."
    lyra "Não é uma recepção. É um pedido."

    "A canção cessou por meio segundo. Das pedras molhadas, dezenas de vozes repetiram a última nota — umas velhas, outras infantis, todas cansadas."
    show lyra worried at portrait_left
    lyra "Se elas aprenderem uma voz nova, talvez nunca mais se calem."

    show ariane neutral at portrait_center
    ariane "Nerissa disse que uma cantora estava prestes a ser silenciada. Não mencionou um coro enterrado sob um templo."
    lyra "Nerissa costuma omitir a parte que faz pessoas sensatas fugirem."

    "Um rapaz de túnica azul surgiu no alto da escadaria, sem fôlego e com uma tira de pergaminho apertada nas duas mãos."
    mikon "Lyra! O Conselho fechou os portões. O ancião Hieron quer a cerimônia antes da lua atingir a água."
    lyra "Então ele não quer uma cerimônia. Quer uma coleira."
    mikon "Ele diz que a sua canção vai revelar quem trouxe a maldição."
    "Mikon olhou para a Marca no pulso de Ivo e percebeu tarde demais que havia sido indelicado."

    menu:
        "Como Ivo responde ao aviso de Mikon?"

        "Pedir que Mikon conte tudo, sem punir o medo dele.":
            $ protected_mikon = True
            $ ivo_compassion += 2
            $ lyra_affinity += 1
            ivo "Você veio avisar, mesmo sabendo que podia ser visto. Isso basta por enquanto. O que Hieron pretende fazer?"
            mikon "Forçá-la a cantar a nota de abertura. Ela faz as vozes dizerem nomes. Depois ele escolhe quem culpar."
            lyra "E cada nome dito acorda outra memória no fundo."

        "Exigir saber por que o Conselho teme Lyra.":
            $ lyria_choice = "verdade"
            $ ivo_honesty += 2
            ivo "Ninguém prende uma cantora por medo de música. O que a voz dela mostra?"
            mikon "As últimas palavras que as pessoas esconderam. Não mentiras. As coisas que elas não conseguiram dizer."
            lyra "É por isso que chamam de bênção quando precisam de mim e de maldição quando precisam me controlar."

        "Usar humor para tirar Mikon do pânico.":
            $ lyria_choice = "humor"
            $ ivo_humor += 2
            ivo "Ótimo. Um conselho, um ritual e um nome assustador. Pelo menos a arquitetura é bonita."
            "Mikon riu sem querer. Lyra quase sorriu, mas a nota sob a água vacilou e ela retomou a canção antes que o silêncio crescesse."

    show ariane embarrassed at portrait_emphasis_left
    ariane "Esse é o momento em que eu digo que temos um plano?"
    ivo "Temos?"
    ariane "Não. Mas eu gosto de ver se você aprende."
    hide ariane

    lyra "A primeira nota não acorda apenas as vozes. Ela abre uma memória que chamamos de Refrão."
    lyra "Quando eu era criança, minha mãe cantou para ele. Depois passou três anos acordando toda noite e perguntando por um homem que morreu antes de me conhecer."
    ivo "Você não quer repetir isso."
    lyra "Eu não quero que ninguém use minha voz para repetir isso. Há diferença."

    menu:
        "O que Ivo oferece a Lyra antes da cerimônia?"

        "Dizer que ela pode escolher não cantar.":
            $ trusted_lyra_song = True
            $ lyra_affinity += 2
            $ ivo_compassion += 1
            ivo "Se eles fecharem os portões, nós abrimos outra saída. Mas a escolha de cantar é sua."
            "Lyra observou Ivo como se aquela frase fosse uma língua que ela conhecia, mas nunca tinha ouvido dirigida a ela."
            lyra "Você fala como alguém que teve a própria escolha roubada."

        "Pedir que ela ensine a Ivo a ouvir o Refrão.":
            $ lyria_choice = "ouvir"
            $ lyra_affinity += 1
            $ ivo_courage += 2
            ivo "Se a Marca reage às memórias, talvez eu consiga dividir o peso."
            lyra "Ou talvez o Refrão encontre em você uma porta grande demais para fechar."
            ivo "Ainda assim, quero entender a porta antes que alguém a derrube."

        "Pedir que Ariane cuide de Lyra enquanto ele distrai o Conselho.":
            $ ariane_affinity += 2
            $ lyra_affinity += 1
            ivo "Não vou deixá-la sozinha com homens que chamam coerção de dever. Ariane, fica com ela."
            ariane "Eu já pretendia. Mas é bom saber que seu senso de autopreservação não apagou completamente."

    "O sino do templo tocou. Não houve vento, mas os estandartes azuis se ergueram de uma vez, apontando para a câmara inferior."
    "Hieron desceu os degraus cercado por guardas. Não trazia arma alguma; carregava apenas um cálice de prata, o tipo de objeto que tentava parecer inocente até que alguém o usasse para dar uma ordem."
    hieron "Lyra. Pela segurança de Lýria, comece a nota."
    lyra "Pela segurança de Lýria, diga a verdade: você tem medo do que ela vai mostrar sobre você."
    "O ancião olhou para Mikon. Dois guardas avançaram, e o rapaz recuou até a borda do círculo."

    menu:
        "Quando o Conselho tenta levar Mikon, Ivo escolhe:"

        "Colocar-se entre os guardas e o rapaz.":
            $ protected_mikon = True
            $ ivo_courage += 2
            ivo "Ele não é uma prova. E ela não é uma ferramenta."
            "A Marca de Ivo brilhou em azul sob a manga. Os guardas pararam não por respeito, mas porque a água ao redor de seus pés começou a subir."

        "Mandar Mikon fugir enquanto Ariane cria uma distração.":
            $ ariane_affinity += 1
            $ ivo_humor += 1
            ivo "Mikon, escadas. Ariane, a parte barulhenta."
            ariane "Finalmente uma instrução com meu nome."
            "Uma lâmpada caiu, o pátio mergulhou em sombras e Mikon desapareceu por uma passagem lateral."

        "Forçar Hieron a explicar o cálice diante de todos.":
            $ ivo_honesty += 2
            ivo "Antes da música, explique o que está no cálice. Se isto é proteção, não deve haver problema em dizer."
            "O silêncio de Hieron respondeu antes dele. Lyra reconheceu o líquido: água das memórias, concentrada para prender uma voz à vontade de quem a oferecesse."
            lyra "Você nunca quis que eu cantasse. Quis que eu não pudesse parar."

    "A primeira voz do Refrão ergueu-se do espelho d'água. Não pediu permissão. Apenas disse, com a voz de Ivo:"
    moira_voice "Eu voltei tarde demais."
    "Ivo viu o convés do navio desaparecendo sob ondas negras. Viu também a figura mais velha que surgira no primeiro Eco, segurando uma corda cortada e chorando como se soubesse exatamente quem seria perdido."
    "Lyra levou as duas mãos à garganta. A nota que ela guardava havia se transformado numa pergunta."

    menu:
        "Dentro do Refrão, Ivo decide o que dividir:"

        "Oferecer a própria memória do naufrágio.":
            $ ivo_honesty += 2
            $ lyra_affinity += 2
            ivo "Se ele quer uma verdade, começa pela minha. Mas eu escolho contar."
            "A água subiu até os joelhos de Ivo e mostrou o naufrágio sem cortar nenhum detalhe. Lyra cantou ao redor da lembrança, não para apagá-la, mas para impedir que ela o definisse por inteiro."

        "Pedir que Lyra cante apenas uma nota livre.":
            $ trusted_lyra_song = True
            $ lyra_affinity += 2
            $ ivo_compassion += 1
            ivo "Não precisa resolver a cidade. Canta uma nota que seja sua. Só sua."
            "Lyra fechou os olhos. A nota que surgiu não vinha do fundo, nem do Conselho. Era imperfeita, humana e tão clara que as vozes enterradas se calaram para escutá-la."

        "Segurar Ariane e manter o grupo ancorado no presente.":
            $ ariane_affinity += 2
            $ ivo_courage += 1
            "Ivo procurou a mão de Ariane antes de procurar respostas. Mélia segurou o outro pulso dele, e Lyra ouviu, no silêncio entre três respirações, uma harmonia que o Refrão não conseguia possuir."

    show lyra embarrassed at portrait_emphasis_left
    lyra "Eu... consigo ouvi-las sem obedecer."
    "O cálice de prata rachou. Hieron caiu de joelhos, não ferido, mas privado da máscara de calma. A água mostrou a todos o que ele escondera: não um crime grandioso, e sim o medo covarde de ter perdido a filha para a mesma canção e transformado esse luto em controle."
    hieron "Eu só queria que ninguém mais desaparecesse."
    lyra "Então deveria ter começado perguntando quem queria ficar."

    "Os guardas baixaram as armas. Mikon voltou da escadaria com os sinos da cidade tocando atrás dele, não como alarme, mas como resposta."
    mikon "Os portões estão abertos. O Conselho não consegue mais fingir que isso foi uma cerimônia privada."

    show lyra neutral at portrait_left
    lyra "Eu não vou fugir de Lýria. Mas também não vou continuar presa a ela."
    ivo "Então vem conosco até descobrir onde termina uma coisa e começa a outra."
    lyra "Esse convite precisa ser menos bonito da próxima vez. Fica mais difícil recusar."

    "Antes de partir, Mélia encontrou uma marca nova no chão do templo: uma espada atravessando uma coroa partida. Ariane a reconheceu antes de Ivo perguntar."
    ariane "Thalia. A herdeira das muralhas. Se o símbolo apareceu aqui, ela não está esperando ser encontrada."
    lyra "Nem parece ser o tipo de pessoa que gosta de esperar."

    $ chapter_03_completed = True
    if "Lyra" not in unlocked_gallery:
        $ unlocked_gallery.append("Lyra")
    jump chapter_03_summary


label chapter_03_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 3{/size}\n\n{size=30}A canção não foi silenciada. Ela foi escolhida.{/size}"

    "Vínculo com Lyra: [bond_rank(lyra_affinity)]."
    "A próxima rota aponta para Thalia e a fortaleza de Akris."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 4 — A Muralha que Escolhe":
            jump chapter_04_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_03_summary

        "Recomeçar o Capítulo 3":
            jump chapter_03_start

        "Voltar ao menu principal":
            return
