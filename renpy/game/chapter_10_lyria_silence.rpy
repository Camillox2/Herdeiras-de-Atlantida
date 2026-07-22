label chapter_10_start:
    if not chapter_09_completed:
        jump chapter_09_start

    scene bg lyria_temple
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 10{/size}\n{size=30}A Voz que Não se Curva{/size}"

    if melia_crisis == "":
        call crisis_melia
    call late_consequence_ch10

    "Lýria não fora destruída; isso teria sido mais simples. As ruas estavam cheias, janelas abertas e braseiros acesos — mas ninguém cantava. Até os vendedores anunciavam peixe com gestos, como se a própria voz pudesse denunciá-los."
    "Nas colunas do Templo das Marés, placas de bronze declaravam que qualquer canção não autorizada seria tratada como traição."

    show lyra worried at portrait_left
    show ivo wary at portrait_bust_right

    lyra "O Coletor não precisa tirar minha voz. Basta fazer todos terem medo dela."
    ivo "E os sacerdotes aceitaram isso?"
    lyra "Alguns estão assustados. Outros sempre quiseram uma regra que deixasse a cidade silenciosa quando fosse conveniente."
    "Mikon esperava perto da escadaria, com uma capa azul e um sino quebrado enrolado em pano."
    mikon "Eles prenderam três aprendizes por cantar para acalmar crianças durante a tempestade. Dizem que a música abriu as correntes."
    lyra "Não foi a música. Foi o medo que a cidade deixou crescer em torno dela."

    menu:
        "Como Ivo começa a ajudar Lyra?"

        "Pedir que Mikon leve os aprendizes para um lugar seguro.":
            $ lyria_response = "abrigo"
            $ ivo_compassion += 2
            $ lyra_affinity += 1
            ivo "Primeiro tiramos as pessoas da prisão. Depois discutimos a lei que chamou cuidado de crime."
            "Mikon assentiu e usou um corredor de serviço. Lyra não o interrompeu; apenas viu alguém mais jovem escolher coragem sem precisar cantar."

        "Questionar a lei diante do templo, sem provocar uma multidão.":
            $ lyria_response = "publico"
            $ ivo_honesty += 2
            ivo "Se eles dizem que a canção é perigosa, que expliquem quem ela feriu e quem lucra com o silêncio."
            "A pergunta circulou pela praça. Não como grito, mas como algo mais difícil de ignorar: uma dúvida dita em voz alta."

        "Investigar o sino quebrado que Mikon trouxe.":
            $ lyria_response = "sino"
            $ ivo_courage += 2
            "Dentro do bronze havia um fio de seda negra. Não era do Coletor: era o mesmo material das faixas usadas pelos magistrados do templo."
            lyra "Alguém daqui não apenas aceitou o medo. Ajudou a fabricá-lo."

    "Na câmara inferior, Lyra encontrou os três aprendizes sentados em silêncio diante de uma bacia vazia. Ela não tentou fazê-los cantar. Sentou no chão ao lado deles."
    show lyra embarrassed at portrait_emphasis_left
    lyra "Quando eu tinha a idade de vocês, disseram que minha voz era uma chave. Eu passei anos tentando ser uma porta fechada."
    ivo "E agora?"
    lyra "Agora estou cansada de ser a fechadura de alguém."

    "O sacerdote Hieron não estava ali. Em seu lugar, uma comissão de cidadãos aguardava acima, pronta para exigir que Lyra se calasse para sempre ou cantasse sob controle. Duas formas diferentes de pedir que ela não fosse pessoa."

    "Sob as placas do templo, os sinos proibidos começam a vibrar. Eles não pedem uma canção; pedem que alguém decida quem tem direito a ser ouvido."
    call juramento_confronto("Sinos do silêncio", 3, "Lyra", "song")
    if combat_result == "won":
        $ lyra_affinity += 1
        lyra "Você não abafou o ruído. Deu a cada voz um lugar onde ela não precisava gritar."
    else:
        $ ivo_integrity -= 1
        lyra "Nós passamos, mas alguns deles ainda vão chamar controle de paz. A conversa não termina aqui."

    menu:
        "Lyra pergunta o que Ivo faria no lugar dela."

        "Dizer que ela não precisa provar nada cantando.":
            $ trusted_lyra_leadership = True
            $ lyra_affinity += 2
            $ ivo_compassion += 1
            ivo "Eu não faria por você. Se a resposta for silêncio, ela precisa ser sua. Se for música, também."
            "Lyra fechou os olhos. Pela primeira vez, o silêncio ao redor dela pareceu escolha, não prisão."

        "Dizer que ela pode cantar uma nota que não pertença ao templo.":
            $ trusted_lyra_leadership = True
            $ lyra_affinity += 2
            $ ivo_courage += 1
            ivo "Se você cantar, não canta para obedecer nem para convencer. Canta algo que eles não possam possuir."
            lyra "Uma nota sem dono."
            ivo "Parece um bom começo."

        "Pedir que ela transforme a comissão em testemunha, não júri.":
            $ lyra_affinity += 1
            $ ivo_honesty += 1
            ivo "Mostra a eles o que o silêncio custa. Mas não deixa que decidam quem você é."
            lyra "Você sempre transforma uma conversa em plano de cerco?"
            ivo "Só as conversas perigosas."

    "Na praça, os magistrados ordenaram que Lyra entregasse a lira. Ela caminhou até o centro sem pressa. Ivo ficou perto o bastante para que ela soubesse que não estava sozinha, mas longe o bastante para que ninguém confundisse proteção com comando."
    show lyra neutral at portrait_left
    lyra "Esta cidade me pediu para ser remédio quando estava com medo e veneno quando queria controlar alguém. Hoje, eu não serei nenhum dos dois."
    "Ela tocou uma nota. Apenas uma."
    "Não houve feitiço, onda ou revelação forçada. A nota era pequena e humana. Pessoas começaram a lembrar de quem haviam deixado de ouvir: filhos, parceiros, vizinhos, a si mesmas."
    "Os sinos de bronze escondidos sob as placas da lei racharam ao mesmo tempo."

    collector "Uma cidade não precisa amar uma corrente para continuar presa a ela."
    lyra "E uma cidade não precisa de permissão para aprender diferente."
    "A sombra se desfez. Os aprendizes começaram a cantar, baixo demais para ser hino e forte demais para ser proibido."

    mikon "O que fazemos com os magistrados?"
    lyra "Nós os ouvimos. Depois os julgamos pelo que fizeram, não pelo medo que alegam sentir."
    ivo "Você acabou de virar a pessoa que eles estavam tentando impedir que existisse."
    show lyra embarrassed at portrait_emphasis_left
    lyra "É um hábito novo. Vou precisar praticar."

    "Quando a música voltou às ruas, a muda de Asterion respondeu dentro da bolsa de Mélia. Uma folha apontou para o norte, onde as muralhas de Akris já estavam recebendo sinais do próximo ataque."

    $ chapter_10_completed = True
    jump chapter_10_summary


label chapter_10_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 10{/size}\n\n{size=30}Lýria voltou a cantar sem pedir permissão.{/size}"

    "Vínculo com Lyra: [bond_rank(lyra_affinity)]."
    "A próxima rota retorna a Akris, onde as muralhas começaram a receber sinais de guerra."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 11 — A Muralha e o Cerco":
            jump chapter_11_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_10_summary

        "Recomeçar o Capítulo 10":
            jump chapter_10_start

        "Voltar ao menu principal":
            return
