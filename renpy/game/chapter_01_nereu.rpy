label chapter_01_start:
    if not prologue_completed:
        jump prologue_start

    scene bg nereu
    with fade
    play music "audio/music/nereu_blue_sails.wav" fadein 1.2

    centered "{size=52}CAPÍTULO 1{/size}\n{size=30}As Velas Azuis de Nereu{/size}"

    show nerissa neutral at portrait_left
    show ivo neutral at portrait_bust_center
    show ariane neutral at portrait_bust_right

    "Nereu recebia a madrugada como um navio recebe tempestade: sem apagar as luzes, sem admitir medo."
    "Nas pontes de mármore, guardas trocavam turnos em silêncio. Nos canais, pequenas velas azuis marcavam os barcos autorizados a cruzar depois do sino."

    nerissa "Vocês têm até o próximo sino para explicar por que a moeda respondeu a mim."
    ariane "É generoso. Em Kallípolis, ele teria até a próxima faca."
    nerissa "Kallípolis resolve problemas com pressa. Nereu prefere saber quem os criou."

    "Nerissa conduziu os dois por uma escadaria estreita, sem chamar escolta. O gesto parecia confiança até Ivo notar as portas fechando uma a uma atrás deles."

    ivo "Isto é uma conversa ou uma prisão educada?"
    nerissa "Se fosse prisão, eu não teria perguntado."
    ariane "E se fosse conversa, você não teria trancado as saídas."
    nerissa "Vocês duas têm uma definição excessivamente romântica de conversa."

    scene bg cisterna
    with dissolve
    play music "audio/music/cistern_forgotten_echoes.wav" fadeout 0.8 fadein 1.2

    show nerissa neutral at portrait_left
    show ivo neutral at portrait_bust_center
    show ariane neutral at portrait_bust_right

    "O arquivo das marés não ficava acima do mar, mas abaixo dele. Prateleiras de bronze surgiam entre colunas úmidas; em cada nicho, uma ampola guardava a última lembrança de alguém que havia morrido no oceano."
    "Ivo parou diante de uma fileira de frascos sem rótulo. Alguns brilhavam em azul. Um, ao fundo, brilhava com a mesma luz da moeda sob sua camisa."

    nerissa "Meu trabalho é impedir que memórias perigosas encontrem alguém disposto a usá-las."
    ivo "E a sua memória?"
    show ariane concerned at portrait_bust_right
    show nerissa embarrassed at portrait_emphasis_left
    nerissa "A minha não está em catálogo."

    "Ariane deixou a provocação passar. Era a primeira vez que Ivo a via respeitar um silêncio sem tentar vencê-lo."

    menu:
        "O que Ivo faz com a moeda?"

        "Entregar a moeda a Nerissa por um instante.":
            $ trusted_nerissa_with_coin = True
            $ nerissa_affinity += 2
            $ ivo_honesty += 1
            ivo "Se você quer que eu confie em Nereu, comece segurando o que todos estão tentando tirar de mim."
            show nerissa neutral at portrait_left
            nerissa "Confiança não é isto. Isto é risco."
            ivo "Às vezes é a mesma coisa."
            "Nerissa aceitou a moeda com as duas mãos. Ela não queimou. Apenas emitiu um pulso, como um coração que enfim reconhecesse o ritmo da cidade."

        "Manter a moeda escondida e pedir uma explicação.":
            $ ivo_courage += 1
            $ nerissa_affinity -= 1
            ivo "Já vi gente suficiente dizer que quer me proteger antes de pedir que eu entregue algo."
            nerissa "Cautela não é um crime."
            ariane "Em Nereu, essa frase provavelmente vem acompanhada de uma taxa."
            nerissa "Em Nereu, ela vem acompanhada de sobrevivência."

        "Pedir que Ariane decida com ele.":
            $ ariane_affinity += 2
            $ ivo_compassion += 1
            $ protected_ariane_in_nereu = True
            ivo "Não vou transformar a primeira pessoa que me ajudou em espectadora da minha decisão."
            show ariane embarrassed at portrait_bust_emphasis_right
            ariane "Você está aprendendo a dizer coisas perigosas com muita calma."
            nerissa "Uma boa qualidade. Só não a confunda com uma boa estratégia."

    show nerissa neutral at portrait_left
    show ariane neutral at portrait_bust_right

    "A moeda abriu uma linha de luz sobre a mesa de pedra. Não era um mapa inteiro, mas o traço de uma rota: Nereu, Asterion e uma terceira marca apagada por água salgada."
    "Ao lado de Asterion havia o desenho de uma folha com cinco nervuras."

    nerissa "O Jardim Suspenso. A marca de uma curadora chamada Mélia."
    ariane "Uma herdeira?"
    nerissa "Uma suspeita. Há diferença. É assim que se evita enterrar inocentes em nome de profecias."

    "Um alarme baixo atravessou a cisterna. As ampolas nas prateleiras vibraram, e a água entre as colunas recuou um palmo contra a gravidade."

    nerissa "Alguém abriu a comporta externa."
    ariane "O Coletor?"
    nerissa "Se for ele, chegou cedo demais. Se não for, chegou pior."

    menu:
        "A primeira pista exige uma escolha rápida."

        "Ajudar Nerissa a proteger o arquivo.":
            $ nereu_lead = "arquivo"
            $ nerissa_affinity += 2
            $ ivo_compassion += 1
            ivo "Se essas memórias caírem nas mãos erradas, não haverá cidade para investigar depois."
            nerissa "Finalmente alguém que entende prioridade. Fique perto de mim."
            "Ivo e Nerissa empurraram a grade de bronze enquanto Ariane cortava os fios de uma runa sabotada. Água gelada subiu pelos degraus e recuou quando a moeda brilhou contra a palma de Ivo."

        "Seguir Ariane pelo corredor que leva à comporta.":
            $ nereu_lead = "comporta"
            $ ariane_affinity += 2
            $ ivo_courage += 1
            ivo "Quem abriu a comporta pode saber por que a moeda reagiu."
            ariane "Isso foi quase um plano. Estou orgulhosa."
            "Os dois encontraram uma lâmina presa na roda da comporta. O metal estava coberto pelo símbolo dos seis riscos — mas a assinatura fora deixada para ser encontrada."

        "Pedir que as duas parem de decidir sozinhas.":
            $ nereu_lead = "verdade"
            $ ariane_affinity += 1
            $ nerissa_affinity += 1
            $ ivo_honesty += 2
            ivo "Se o Coletor quer nos separar, correr em direções diferentes é fazer o trabalho dele."
            "Nerissa mediu Ivo por um instante. Ariane, contra toda expectativa, guardou a réplica pronta."
            nerissa "Certo. Juntos, então. Mas você segue minhas ordens quando a água subir."
            ariane "E as minhas quando ela der uma ordem ruim."

    "A cisterna estremeceu. Uma das ampolas se partiu no chão e uma voz desconhecida ocupou o ar por um segundo."
    moira_voice "A herdeira que recusa a coroa ainda pode afogar um reino."

    "Nerissa empalideceu. Não de medo: de reconhecimento."

    show nerissa embarrassed at portrait_emphasis_left
    nerissa "Há sete anos, meu pai fechou os portões de uma ilha para impedir uma doença de chegar a Nereu."
    nerissa "Duas mil pessoas ficaram do lado de fora. Ele chamou aquilo de decisão de Estado."
    nerissa "Eu era capitã de uma patrulha. Eu obedeci."

    ariane "Nerissa..."
    nerissa "Não preciso de piedade, Ariane. Preciso saber por que uma memória morta decidiu usar a minha culpa como chave."

    menu:
        "Como Ivo responde?"

        "Dizer que obedecer não apaga a responsabilidade.":
            $ nerissa_affinity += 1
            $ ivo_honesty += 1
            ivo "Não apaga. Mas também não te condena a repetir a escolha dele."
            nerissa "Você não torna nada mais fácil."
            ivo "Não estou tentando."

        "Dizer que ela não deve carregar a culpa sozinha.":
            $ nerissa_affinity += 2
            $ ivo_compassion += 1
            ivo "Um reino transformou uma capitã em escudo. Isso não te torna inocente, mas torna a culpa maior do que uma pessoa."
            "Nerissa respirou como quem tinha esquecido que era possível fazê-lo sem comando."

        "Perguntar o que ela fará quando tiver poder para escolher.":
            $ nerissa_affinity += 1
            $ ivo_courage += 1
            ivo "Se essa coroa vier até você, não me diga o que fez há sete anos. Diga o que vai fazer quando ninguém puder mandar em você."
            nerissa "Abrirei os portões antes de contá-los como perdas."

    show nerissa neutral at portrait_left
    "O alarme cessou. A linha de luz na mesa completou-se por um único segundo e revelou uma frase sob o símbolo de Asterion: 'A raiz lembra o nome do mar'."

    ariane "Mélia não é só uma curadora."
    nerissa "Não. E se a rota estiver certa, alguém já está a caminho dela."
    ivo "Então vamos antes."
    nerissa "Não. Vocês vão embarcar ao amanhecer. Eu vou determinar se posso acompanhá-los sem abandonar a cidade."
    ariane "Isso foi uma forma muito longa de dizer que quer ir."
    show nerissa embarrassed at portrait_left
    nerissa "Foi uma forma muito clara de dizer que ainda tenho deveres."

    scene bg nereu
    with dissolve
    play music "audio/music/nereu_blue_sails.wav" fadeout 0.8 fadein 1.0

    show melia neutral at portrait_enter_left
    show ivo neutral at portrait_bust_right

    "Quando o primeiro azul apareceu no horizonte, um pequeno barco atracou sem bandeira. Uma jovem desceu com uma caixa de mudas protegida contra o sal."
    "Ela olhou para Ivo como se reconhecesse a marca antes mesmo de ele tentar escondê-la."

    melia "Você é a pessoa que fez as raízes do Jardim pararem de dormir."
    ivo "Eu nem sabia que raízes dormiam."
    show melia embarrassed at portrait_emphasis_left
    melia "Dormem quando têm medo. Pessoas também."

    "Atrás dela, a caixa de mudas se abriu sozinha. Uma folha de cinco nervuras apontou para o mar, na direção de Asterion."

    $ heard_melia_name = True
    $ chapter_01_completed = True
    if "Mélia" not in unlocked_gallery:
        $ unlocked_gallery.append("Mélia")

    jump chapter_01_summary


label chapter_01_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 1{/size}\n\n{size=30}Nereu abriu seus arquivos. Asterion abriu uma porta.{/size}"

    if nereu_lead == "arquivo":
        "Ivo escolheu proteger memórias que não eram suas. Nerissa percebeu."
    elif nereu_lead == "comporta":
        "Ivo seguiu a pista até a comporta. Ariane percebeu."
    else:
        "Ivo recusou a pressa e impediu que o medo dividisse o grupo. As duas perceberam."

    "Vínculo com Nerissa: [bond_rank(nerissa_affinity)]."
    "Vínculo com Ariane: [bond_rank(ariane_affinity)]."
    "Mélia entrou na rota das herdeiras."
    "Continua no Capítulo 2 — O Jardim de Mélia."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 2 — O Jardim de Mélia":
            jump chapter_02_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_01_summary

        "Recomeçar o Capítulo 1":
            jump chapter_01_start

        "Voltar ao menu principal":
            return
