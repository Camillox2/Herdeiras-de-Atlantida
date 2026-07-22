label chapter_02_start:
    if not chapter_01_completed:
        jump chapter_01_start

    scene bg asterion
    with fade
    play music "audio/music/agora_of_columns.wav" fadein 1.2

    centered "{size=52}CAPÍTULO 2{/size}\n{size=30}O Jardim de Mélia{/size}"

    show melia neutral at portrait_left
    show ivo neutral at portrait_bust_center
    show ariane neutral at portrait_bust_right

    "Asterion não parecia uma cidade construída sobre a pedra, mas uma cidade que a pedra havia decidido proteger."
    "Jardins subiam pelas encostas em degraus verdes. Água corria por aquedutos de bronze, e cada estufa guardava plantas que Ivo não saberia nomear nem em outro mundo."

    melia "Não toquem nas flores azuis. Elas reconhecem pensamentos insistentes."
    ivo "Elas mordem?"
    melia "Pior. Elas mostram aquilo que você está tentando esquecer."
    show ariane embarrassed at portrait_bust_emphasis_right
    ariane "Finalmente uma planta com boas maneiras."

    "Mélia sorriu, mas não por muito tempo. No canteiro diante da estufa principal, as raízes de uma oliveira antiga tinham rompido o mármore e traçado o mesmo padrão de três fios no chão."

    show melia embarrassed at portrait_emphasis_left
    melia "Elas começaram ontem. Primeiro as folhas ficaram salgadas. Depois os jardineiros começaram a sonhar com uma cidade que nunca visitaram."
    ivo "Atlântida."
    melia "Eu não disse esse nome."

    show melia neutral at portrait_left
    ariane "Ela não precisava."

    "Uma menina correu pelo corredor de pedra carregando um vaso quebrado. Quando se aproximou das raízes, parou no meio do passo. Seu olhar ficou vazio, como se estivesse ouvindo alguém chamar debaixo da terra."
    "Mélia se ajoelhou diante dela e soprou um pó dourado sobre a água do vaso. A menina piscou, chorou uma vez e voltou a respirar."

    melia "As raízes não querem matar ninguém. Querem lembrar através de alguém."
    ivo "E o que acontece quando a lembrança encontra a pessoa errada?"
    melia "Ela vira destino."

    menu:
        "Diante da raiz aberta, Ivo escolhe:"

        "Ajudar Mélia a acalmar as raízes.":
            $ asterion_choice = "cuidar"
            $ melia_affinity += 2
            $ ivo_compassion += 1
            ivo "Se elas estão tentando falar, vamos impedir que precisem gritar."
            "Mélia colocou uma pequena lâmina de poda na mão de Ivo. Não era uma arma; era uma ferramenta precisa demais para permitir pressa."
            melia "Corte apenas o que já está morto. É assim que se protege algo vivo sem possuí-lo."

        "Perguntar de onde Mélia conhece o padrão.":
            $ asterion_choice = "verdade"
            $ melia_affinity += 1
            $ ivo_honesty += 2
            ivo "Você reconheceu a Marca antes de nos conhecer. Não vou fingir que não vi."
            "Mélia tocou uma folha azul entre dois dedos. A ponta dela escureceu, como se a planta tivesse aceitado a pergunta."
            melia "Minha mãe guardava sementes que não deviam sobreviver. Antes de morrer, disse que um dia alguém viria do mar carregando uma resposta que ninguém queria ouvir."

        "Pedir que Ariane mantenha os curiosos afastados.":
            $ asterion_choice = "proteger"
            $ ariane_affinity += 2
            $ ivo_courage += 1
            ivo "Se a raiz quer uma mente, não vamos dar a ela uma multidão."
            ariane "Finalmente uma instrução simples. Fique com a botânica. Eu cuido da parte em que ninguém se aproxima demais."
            "Ariane sumiu entre os arcos, deixando para trás dois guardas locais confusos demais para protestar."

    "Quando Ivo tocou a raiz, a Marca não queimou. Ela esfriou."
    "O jardim desapareceu por um instante, substituído por uma sala circular sob a água. Seis cadeiras cercavam uma mesa de pedra. Cinco estavam vazias. A sexta tinha ramos de oliveira crescendo através do assento."

    moira_voice "A curadora preservou a semente."
    moira_voice "A semente preservou o juramento."

    "Ivo retirou a mão antes de se afogar na lembrança. Mélia o segurou pelo pulso, firme o bastante para trazê-lo de volta, gentil o bastante para não fazê-lo se sentir salvo contra a vontade."

    show melia embarrassed at portrait_emphasis_left
    melia "Você viu alguma coisa?"

    menu:
        "O que Ivo revela a Mélia?"

        "Contar sobre as seis cadeiras e o juramento.":
            $ melia_affinity += 2
            $ ivo_honesty += 1
            ivo "Vi um lugar esperando por seis pessoas. E acho que você é uma delas."
            melia "Eu cuido de sementes. Não de coroas."
            ivo "Talvez seja exatamente por isso que a cadeira tinha raízes."

        "Contar apenas que a raiz respondeu à Marca.":
            $ melia_affinity += 1
            ivo "Ela respondeu a mim. Não sei se isso é bom."
            melia "Então não vamos chamá-lo de bom ainda. Vamos chamá-lo de verdadeiro e esperar para ver o que faz."

        "Perguntar se ela deseja saber antes de contar.":
            $ melia_affinity += 2
            $ ivo_compassion += 1
            ivo "A memória parece sua. Você quer ouvi-la?"
            "Mélia demorou a responder. Depois assentiu, sem fingir coragem onde ainda havia medo."
            melia "Quero. Mas não porque tenho direito. Porque, se eu for parte disso, alguém vai tentar escolher por mim."

    show melia neutral at portrait_left
    "Um sino soou no alto dos terraços. Ariane retornou com uma fita branca enrolada na mão. O selo de Nereu havia sido quebrado."

    ariane "Mensagem da capitã. O Conselho mandou uma embarcação para buscar vocês. E Pólemon mandou outra, sem assinatura."
    ivo "Duas ofertas no mesmo dia. Isso parece uma armadilha."
    melia "Em Asterion, chamamos isso de 'terça-feira'."

    "Ariane abriu a fita. A letra de Nerissa era curta: 'Não embarquem com Pólemon. Procurem a cantora antes que o templo a silencie.'"
    "Junto à assinatura, havia um desenho de sete notas e uma única palavra: Lýria."

    melia "Lyra. Ela canta no templo das marés altas."
    ivo "Mais uma herdeira?"
    melia "Mais uma pessoa. Não cometa o erro de trocar as duas coisas."

    $ chapter_02_completed = True
    if "Lyra" not in unlocked_gallery:
        $ unlocked_gallery.append("Lyra")
    jump chapter_02_summary


label chapter_02_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 2{/size}\n\n{size=30}A semente respondeu. A canção chamou.{/size}"

    "Vínculo com Mélia: [bond_rank(melia_affinity)]."
    "Ariane continua ao lado de Ivo: [bond_rank(ariane_affinity)]."
    "A próxima rota aponta para Lyra e o Templo das Marés Altas."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 3 — A Canção que Não Termina":
            jump chapter_03_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_02_summary

        "Recomeçar o Capítulo 2":
            jump chapter_02_start

        "Voltar ao menu principal":
            return
