label chapter_05_start:
    if not chapter_04_completed:
        jump chapter_04_start

    scene bg nix_observatory
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 5{/size}\n{size=30}O Céu que Não Promete{/size}"

    "O Observatório de Nix não tinha teto. As constelações ocupavam a abóbada aberta como se o céu inteiro tivesse descido alguns metros para escutar. No chão, círculos de bronze giravam sozinhos sobre mosaicos roxos."
    "No centro de todos eles, uma mulher segurava um astrolábio contra o peito. Ela não olhou para os visitantes quando falou."

    show cassia vision at portrait_left
    show ivo wary at portrait_bust_right

    cassia "Vocês demoraram quatro dias, sete horas e uma decisão que não era inevitável."
    ivo "Você costuma receber gente assim?"
    cassia "Não. Normalmente eu finjo que ninguém chegou antes de saber se a presença delas melhora o futuro."
    "Ela ergueu os olhos. Havia medo neles, mas não o medo de quem esperava ser atacada. Era o medo de quem já vira o golpe acontecer."

    show thalia neutral at portrait_center
    thalia "Cassia de Nix. A mulher que o meu pai chamava quando queria que uma previsão dissesse o que ele já tinha decidido fazer."
    cassia "Seu pai odiava minhas previsões. Elas nunca concordavam com ele."
    thalia "Por isso mesmo."

    "O astrolábio de Cassia girou e projetou seis constelações sobre o chão. Uma era uma onda. Outra, uma raiz. Outra, uma muralha. As três últimas tremiam, incompletas, mas Ivo reconheceu o fio que ligava todas à Marca em seu pulso."
    cassia "A marca não trouxe você para cá. Ela impediu que você morresse em outro lugar."
    ivo "Isso deveria me tranquilizar?"
    cassia "Não. Eu não trabalho com tranquilidade."

    menu:
        "O que Ivo pergunta primeiro a Cassia?"

        "Por que ela não procurou as outras herdeiras antes.":
            $ nix_choice = "isolamento"
            $ cassia_affinity += 2
            $ ivo_honesty += 1
            ivo "Se você sabia sobre as seis, por que ficou aqui sozinha?"
            cassia "Porque toda vez que procurei uma de vocês, a visão terminava em perda. Depois comecei a achar que eu era a variável perigosa."
            ivo "Ou a única pessoa tentando impedir que alguém decidisse por elas."

        "O que exatamente aconteceu no naufrágio.":
            $ nix_choice = "naufragio"
            $ ivo_courage += 1
            ivo "Você disse que a Marca me impediu de morrer. O que ela tirou em troca?"
            cassia "Tempo. Não sei quanto. Na visão, você afunda e volta. Entre uma coisa e outra existe uma porta que nenhuma estrela consegue olhar por dentro."

        "Se o Coletor está vindo para Nix.":
            $ nix_choice = "coletor"
            $ ivo_compassion += 1
            ivo "Ele deixou cidades inteiras para trás. Por que o observatório?"
            cassia "Porque aqui existe a única máquina capaz de transformar possibilidades em instruções. E ele prefere um destino que possa vender."

    hide thalia
    show cassia neutral at portrait_left
    "Cassia levou o grupo até uma lente de cristal suspensa no ar. Dentro dela, Ivo viu uma versão da sala sem ninguém de pé. As constelações haviam caído sobre as pedras como cinzas."
    cassia "Esta é a visão que me fez parar de procurar vocês. Não é o futuro. É uma rota possível quando alguém acredita que a escolha já foi feita."
    ivo "E você acredita nisso?"
    cassia "Acredito que previsões são covardes. Elas mostram uma estrada e depois fingem que construíram o mundo."

    show ariane neutral at portrait_center
    ariane "Finalmente alguém nesta história falando com bom senso."
    cassia "Obrigada. Quem é você?"
    ariane "A pessoa que vai impedir você de se esconder atrás de frases bonitas."

    menu:
        "Diante da visão, Ivo escolhe:"

        "Pedir que Cassia mostre tudo, inclusive o pior.":
            $ trusted_cassia_vision = True
            $ cassia_affinity += 2
            $ ivo_honesty += 2
            ivo "Se ela pode nos ferir, eu prefiro conhecê-la inteira. Mas você não precisa carregar isso sozinha."
            "Cassia inclinou a lente. A visão revelou uma sombra com a máscara do Coletor diante de uma mesa de seis cadeiras. Em uma delas, havia uma faixa vermelha. Em outra, o mapa de cobre de Thalia."
            cassia "Ele não quer matar as herdeiras. Quer fazer uma de nós escolher as outras."

        "Destruir a lente antes que ela prenda todos à visão.":
            $ ivo_courage += 2
            $ cassia_affinity += 1
            ivo "Uma máquina que só mostra derrotas não merece ser altar."
            "Ivo ergueu a mão, mas Cassia segurou seu pulso. Não o impediu — apenas fez com que ele enxergasse as fissuras no cristal antes de quebrá-lo."
            cassia "Destrua se quiser. Só saiba que as respostas não vão desaparecer junto."
            "Ivo golpeou a borda. A lente se abriu em rachaduras luminosas, e as constelações enfim deixaram de obedecer ao desenho imposto."

        "Pedir que Ariane e Thalia ancorem o grupo no presente.":
            $ ariane_affinity += 1
            $ thalia_affinity += 1
            $ cassia_affinity += 1
            ivo "Ninguém olha sozinho. Se a visão tentar escolher um de nós, ela vai ter que encarar todos."
            "Ariane ficou à direita de Cassia; Thalia, à esquerda. Três mulheres que haviam passado a vida sendo tratadas como símbolos recusaram, em silêncio, a posição de peça."

    "As engrenagens do observatório pararam. Então voltaram a girar na direção errada. Uma estrela desenhada no teto se apagou, depois outra."
    moira_voice "A sexta cadeira observa."
    cassia "Não. Ela é observada."
    "Uma janela de sombra abriu-se sobre a lente. A voz do Coletor não atravessou a sala; atravessou a cabeça de cada pessoa nela."
    collector "Seis mulheres, seis cidades, seis medos. Vocês chamam isso de juramento. Eu chamo de mecanismo."
    collector "Tragam a Marca ao Salão Afundado, e cada uma poderá escolher o que salvar. Recusem, e o mar escolherá sem vocês."

    menu:
        "Como Ivo responde à proposta do Coletor?"

        "Recusar qualquer escolha que sacrifique alguém.":
            $ kept_future_secret = False
            $ ivo_compassion += 2
            ivo "Você oferece escolhas falsas e chama isso de liberdade. Não vamos dar nomes ao seu mecanismo."
            "A sombra sorriu sem boca. Cassia apertou o astrolábio, e uma das estrelas apagadas voltou a acender."

        "Aceitar ir ao Salão, mas não as regras dele.":
            $ kept_future_secret = True
            $ ivo_courage += 2
            ivo "Vamos até lá. Mas você não escolhe o tabuleiro, e não escolhe quem senta à mesa."
            collector "Todos dizem isso antes de perder algo."
            ivo "Então você vai aprender uma coisa nova."

        "Pedir a Cassia que esconda a visão mais perigosa por enquanto.":
            $ kept_future_secret = True
            $ cassia_affinity += 1
            ivo "Não precisamos despejar cada medo sobre o grupo no mesmo minuto. Guarda o que ainda não conseguimos carregar."
            cassia "Guardar não é mentir, se você pretende voltar para buscar."
            ivo "Eu pretendo."

    "A sombra desfez-se. No lugar dela, a lente agora mostrava o mar ao redor de uma ruína circular: o Salão Afundado. Sobre seis pedras, seis símbolos esperavam."
    show cassia vision at portrait_emphasis_left
    cassia "Ariane, Nerissa, Mélia, Lyra, Thalia e eu. O juramento não quer uma rainha. Quer testemunhas que se recusem a entregar umas às outras."
    ivo "E eu?"
    cassia "Você é a pergunta que o juramento tentou apagar."
    ivo "Isso também não me tranquiliza."
    show cassia embarrassed at portrait_emphasis_left
    cassia "Eu disse que não trabalho com tranquilidade. Mas posso trabalhar com companhia."

    "Cassia guardou o astrolábio, não como alguém que esconde uma arma, mas como quem finalmente admite que uma ferramenta pode ser compartilhada."
    "Nas paredes abertas do observatório, a primeira luz do amanhecer alcançou a constelação da coroa partida. Pela primeira vez, ela não parecia uma previsão de queda. Parecia uma pergunta esperando seis respostas."

    $ chapter_05_completed = True
    if "Cassia" not in unlocked_gallery:
        $ unlocked_gallery.append("Cassia")
    jump chapter_05_summary


label chapter_05_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 5{/size}\n\n{size=30}O futuro foi visto. Não foi aceito.{/size}"

    "Vínculo com Cassia: [bond_rank(cassia_affinity)]."
    "As seis herdeiras agora têm uma rota comum: o Salão Afundado."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 6 — O Juramento das Moiras":
            jump chapter_06_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_05_summary

        "Recomeçar o Capítulo 5":
            jump chapter_05_start

        "Voltar ao menu principal":
            return
