label chapter_06_start:
    if not chapter_05_completed:
        jump chapter_05_start

    scene bg sunken_hall
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 6{/size}\n{size=30}O Juramento das Moiras{/size}"

    "O Salão Afundado não ficava sob o mar como uma ruína. Ficava dentro de uma pausa: a água curvava-se ao redor dos arcos e não atravessava a linha dourada desenhada no chão."
    "Seis cadeiras de mármore cercavam a mesa central. Nenhuma tinha nome. Cada uma guardava apenas um símbolo: onda, raiz, voz, muralha, estrela e chama."

    show ariane neutral at portrait_left
    show ivo wary at portrait_bust_center
    show nerissa neutral at portrait_right

    nerissa "Eu odeio quando uma profecia acerta a decoração."
    ariane "Você veio mesmo assim."
    nerissa "Vim porque ninguém deveria receber um convite do Coletor sem ter alguém por perto para dizer que é uma péssima ideia."
    ivo "Essa função parece muito disputada."
    ariane "Você não imagina."

    "A porta de água se abriu mais uma vez. Mélia entrou carregando uma raiz enrolada em pano úmido; Lyra, com a mão sobre a lira; Thalia, sem a máscara no rosto; e Cassia, com o astrolábio apagado pela primeira vez."
    hide nerissa
    show melia neutral at portrait_left
    show lyra neutral at portrait_center
    show thalia neutral at portrait_right

    melia "A raiz me trouxe até aqui. Não porque queria. Porque reconheceu o caminho."
    lyra "Minha canção fez as correntes pararem. Elas estavam esperando pessoas, não um navio."
    thalia "A passagem para Akris fechou depois que atravessamos. Isso não é uma reunião. É uma armadilha com cadeiras bonitas."
    cassia "Pode ser os dois."

    hide melia
    show cassia vision at portrait_left
    show ivo neutral at portrait_bust_right
    cassia "O futuro se divide aqui em muitas linhas. Em todas elas, alguém tenta decidir qual de nós deve carregar a culpa."
    ivo "E em alguma delas ninguém carrega?"
    cassia "Há uma. Ela é curta, difícil e não parece com as histórias que os homens escrevem sobre heróis."

    menu:
        "Antes de tocar a mesa, Ivo escolhe o que dizer às herdeiras:"

        "Ninguém será usado para salvar o resto.":
            $ assembly_choice = "ninguem"
            $ ivo_compassion += 2
            $ ariane_affinity += 1
            $ nerissa_affinity += 1
            $ melia_affinity += 1
            $ lyra_affinity += 1
            $ thalia_affinity += 1
            $ cassia_affinity += 1
            ivo "Se esta mesa exige que uma de vocês vire sacrifício, então a mesa está errada. Encontramos outra resposta."
            "Ninguém aplaudiu. Mas seis pessoas que tinham passado tempo demais sendo tratadas como destino ergueram os olhos ao mesmo tempo."

        "A verdade importa, mesmo quando separa o grupo.":
            $ assembly_choice = "verdade"
            $ ivo_honesty += 2
            $ ariane_affinity += 2
            $ cassia_affinity += 1
            ivo "Eu não prometo que será fácil. Prometo que não vou esconder o que sei só para manter todos confortáveis."
            ariane "Perigoso. Mas honesto."
            cassia "A primeira previsão útil da noite."

        "Cada uma pode partir se quiser.":
            $ assembly_choice = "escolha"
            $ ivo_courage += 1
            $ lyra_affinity += 2
            $ thalia_affinity += 1
            ivo "Ninguém me deve companhia. Fiquem porque querem, não porque uma ruína fez um desenho bonito."
            lyra "Isso é estranhamente gentil para alguém no centro de um ritual."
            thalia "Também é uma boa forma de descobrir quem fica."

    "A Marca de Ivo tocou a mesa. As seis cadeiras responderam, não com correntes, mas com memórias."
    "Ariane viu a noite em que escolhera uma família para salvar e outra para abandonar. Nerissa viu o porto fechado por ordem do pai. Mélia viu sementes guardadas no lugar de pessoas. Lyra ouviu todas as últimas palavras que tentara esquecer. Thalia viu o irmão na ponte. Cassia viu versões de si mesma fugindo antes de conhecer qualquer uma delas."
    "E Ivo viu a cidade de onde viera antes do mar. Uma rua comum, luzes de carros no asfalto molhado, um quarto pequeno e a sensação terrível de que ele já não cabia naquela vida sem negar todas as pessoas que agora o olhavam."

    show ariane embarrassed at portrait_left
    ariane "Você nunca contou de onde realmente veio."
    ivo "Eu não tinha certeza se importava."
    nerissa "Importa para você. Isso costuma ser suficiente."
    show cassia neutral at portrait_right
    cassia "A porta entre mundos não o trouxe para substituir ninguém. Trouxe porque alguém do outro lado recusou uma escolha que esta história precisava repetir."

    "A água além dos arcos escureceu. A máscara do Coletor surgiu refletida no chão, grande demais para pertencer a uma única pessoa."
    collector "Vocês chamam de escolha aquilo que é apenas medo de assumir poder. Sentem-se. Escolham uma guardiã. As outras cidades serão poupadas."
    thalia "E depois você escolhe a próxima coisa que ela terá de perder."
    collector "Depois ela aprende."

    menu:
        "O Coletor exige uma guardiã. O grupo responde:"

        "Recusar a cadeira central e dividir o juramento.":
            $ first_arc_completed = True
            $ ivo_compassion += 1
            $ melia_affinity += 1
            $ lyra_affinity += 1
            ivo "Não existe uma guardiã. Existem seis pessoas que podem dizer não."
            "Mélia pousou a raiz no centro; Lyra cantou uma nota livre; Thalia colocou a máscara na mesa; Cassia girou o astrolábio; Nerissa derramou uma gota do mar de Nereu; Ariane cortou a própria fita vermelha em seis partes."

        "Usar a Marca como âncora, mas sem escolher uma herdeira.":
            $ first_arc_completed = True
            $ ivo_courage += 2
            $ ariane_affinity += 1
            $ thalia_affinity += 1
            ivo "A Marca me trouxe até vocês. Ela não manda em vocês. Se alguém precisa ficar no centro, sou eu — e ainda assim, só com a permissão de todas."
            "Ariane foi a primeira a tocar o pulso de Ivo. As outras se aproximaram não para obedecer, mas para tirar da Marca o direito de ser a única âncora."

        "Pedir que cada uma escolha uma condição para continuar.":
            $ first_arc_completed = True
            $ ivo_honesty += 1
            $ cassia_affinity += 1
            $ nerissa_affinity += 1
            ivo "Não faço promessas por vocês. Digam o que precisa ser verdade para esta aliança existir."
            nerissa "Nenhum segredo usado como arma."
            melia "Nenhuma vida tratada como ferramenta."
            lyra "Nenhuma voz forçada a cantar."
            thalia "Nenhuma ordem acima de quem vai sofrer a consequência."
            cassia "Nenhuma previsão acima de uma escolha presente."
            ariane "E ninguém fica sozinho quando o medo pedir isolamento."

    "A mesa dividiu-se em seis linhas de luz e apagou a sombra do Coletor. Não o destruiu. Apenas tornou impossível para ele fingir que a vontade de seis pessoas podia ser resumida por uma única coroa."
    collector "Então vocês escolheram guerra."
    ivo "Não. Escolhemos não ser seu mecanismo."

    "A voz dele desapareceu. O Salão ficou quieto por tempo suficiente para que todos ouvissem a água voltando a se mover fora dos arcos."
    show lyra embarrassed at portrait_left
    show ivo neutral at portrait_bust_center
    show thalia embarrassed at portrait_right
    lyra "Então... e agora?"
    thalia "Agora fortalecemos cidades, encontramos aliados e descobrimos onde ele guarda o rosto quando não usa máscara."
    nerissa "E alguém vai precisar aprender a cozinhar para sete pessoas."
    ivo "Eu votei pela parte sem guerra."
    ariane "Você perdeu por unanimidade."

    "As seis cadeiras permaneceram vazias. Isso era importante. Não eram tronos; eram lugares que só teriam sentido enquanto quem se sentasse ali pudesse se levantar depois."

    $ chapter_06_completed = True
    $ first_arc_completed = True
    jump chapter_06_summary


label chapter_06_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO ARCO I{/size}\n\n{size=30}As herdeiras não aceitaram um destino. Construíram uma aliança.{/size}"

    "Os vínculos que você construiu continuarão a influenciar cenas, rotas e o desfecho futuro."
    "O próximo arco começa com as cidades reagindo ao juramento e com a caçada ao Coletor."

    menu:
        "O que deseja fazer?"

        "Continuar para o Arco II — A Cidade que Escolhe":
            jump chapter_07_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_06_summary

        "Recomeçar o Capítulo 6":
            jump chapter_06_start

        "Voltar ao menu principal":
            return
