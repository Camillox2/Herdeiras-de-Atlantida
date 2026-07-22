label chapter_04_start:
    if not chapter_03_completed:
        jump chapter_03_start

    scene bg akris_fortress
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 4{/size}\n{size=30}A Muralha que Escolhe{/size}"

    "Akris apareceu depois de dois dias de subida como uma cidade que decidira transformar medo em pedra. Seus muros recortavam a montanha; as bandeiras vermelhas não celebravam vitória, apenas avisavam que alguém ainda estava de guarda."
    "Perto da ponte quebrada, três batedores encostavam um rapaz ferido contra um bloco de mármore. Acima deles, uma mulher de cabelo vermelho apontava uma espada para a única passagem segura."

    show thalia defensive at portrait_left
    show ivo wary at portrait_bust_right

    thalia "Mais um passo e eu derrubo a ponte."
    ivo "Você fala isso para todos que chegam ou só para os que trazem problemas?"
    thalia "Ainda estou decidindo em qual categoria você entra."
    "O vento puxou a capa dela para trás e revelou uma máscara de bronze presa ao cinto. Não era um troféu. Pelos riscos fundos na superfície, alguém a tinha usado muitas vezes para esconder o rosto."

    show lyra neutral at portrait_center
    lyra "Thalia de Akris. O símbolo da espada e da coroa estava no templo."
    thalia "Então vocês foram seguindo símbolos até uma fortaleza em guerra. Vocês são corajosos ou péssimos em planejamento."

    "Um estrondo veio de dentro da cidadela. A ponte tremeu; o rapaz ferido caiu de joelhos. Thalia virou os olhos para o portão por tempo demais, e Ivo percebeu que ela não estava protegendo a fortaleza dos visitantes. Estava protegendo alguma coisa dentro dela."

    menu:
        "Diante da ponte, Ivo decide:"

        "Ajudar os batedores feridos antes de pedir passagem.":
            $ saved_akris_scouts = True
            $ thalia_affinity += 2
            $ ivo_compassion += 2
            ivo "Se a ponte cair, eles morrem primeiro. Me diga como estabilizar a corda."
            "Thalia não baixou a espada, mas indicou o nó certo. Ivo e Lyra puxaram juntos até o rapaz alcançar terreno firme."
            thalia "Você não conhece nenhum deles."
            ivo "Eu conheço o bastante para saber que ninguém merece ser usado como teste."

        "Perguntar o que existe dentro da fortaleza.":
            $ akris_choice = "verdade"
            $ ivo_honesty += 2
            ivo "Não vim tomar Akris. Vim entender por que suas muralhas estão gritando."
            "Por um instante, a dureza do rosto de Thalia se partiu. Ela olhou para a pedra sob as botas como se esperasse que ela respondesse."
            thalia "Porque elas aprenderam os nomes de quem morreu defendendo-as. E agora querem que eu escolha mais nomes."

        "Aceitar o desafio e atravessar sem ameaçá-la.":
            $ akris_choice = "coragem"
            $ ivo_courage += 2
            ivo "Se você precisa de uma razão para não derrubar a ponte, eu vou dar uma: ainda não decidimos se somos inimigos."
            thalia "Essa é uma resposta melhor do que a maioria dos generais me deu."
            "Ela fez um gesto curto. Uma tábua escondida deslizou sobre a fenda, estreita demais para imprudência, larga o bastante para confiança."

    hide lyra
    show thalia neutral at portrait_left
    "Dentro da muralha, Akris não tinha soldados marchando. Tinha famílias carregando água, ferreiros reforçando janelas e crianças dormindo sob escudos antigos. A guerra não estava do lado de fora; ela se instalara nos corredores, entre pessoas que ainda precisavam umas das outras."
    "Thalia conduziu o grupo até uma sala de mapas. Cada estrada marcada em carvão tinha um risco vermelho atravessando-a."

    thalia "O Conselho de Akris quer abrir a passagem norte. Dizem que isso traz provisões."
    ivo "E você acha que traz o quê?"
    thalia "O Coletor. Ele não ataca cidades. Ele compra pessoas desesperadas para abrirem portas por ele."
    "Ariane surgiu da escada lateral, com uma fita de Nereu presa ao pulso."
    show ariane neutral at portrait_center
    ariane "Uma das minhas informantes viu um navio sem bandeira na enseada. Pólemon também está por perto."
    thalia "Ótimo. Então a minha pior semana conseguiu companhia."

    "Thalia abriu uma gaveta e retirou um pequeno mapa de cobre. O mesmo desenho de três fios cruzava uma torre no extremo norte."
    thalia "Meu pai guardava isto como segredo militar. Depois que ele morreu, descobri que era uma rota para o Observatório de Nix."
    lyra "Cássia procura respostas em observatórios. Se ela está lá, não será coincidência."

    menu:
        "O que Ivo pede a Thalia?"

        "Que confie o mapa ao grupo.":
            $ trusted_thalia_with_map = True
            $ thalia_affinity += 2
            $ ivo_honesty += 1
            ivo "Se você quer impedir o Coletor, não pode carregar cada segredo sozinha."
            "Thalia fechou os dedos sobre o mapa. Depois o deixou na palma de Ivo, como quem entrega uma arma sem saber se ela será usada contra si."
            thalia "Não confunda confiança com perdão. Ainda não decidi se vocês merecem os dois."

        "Que diga quem ela perdeu na primeira guerra.":
            $ akris_choice = "memoria"
            $ thalia_affinity += 1
            $ ivo_compassion += 1
            ivo "Você fala das mortes como se fosse responsável por cada uma. Quem foi a primeira?"
            "A pergunta não feriu Thalia porque era cruel. Feriu porque ninguém a fazia havia tempo demais."
            thalia "Meu irmão. Eu deixei o portão aberto para salvar refugiados. Ele ficou na retaguarda para fechá-lo."
            ivo "Salvar pessoas não torna a perda menor. Mas também não transforma você na pessoa que a causou."

        "Que use a fortaleza para proteger os moradores, não o Conselho.":
            $ ivo_courage += 1
            $ thalia_affinity += 1
            ivo "Uma muralha serve a quem se abriga atrás dela. Não a quem manda do alto dela."
            thalia "Você fala como alguém que nunca comandou uma retirada."
            ivo "Não. Falo como alguém que sabe que ordens podem virar desculpas."

    "Antes que Thalia respondesse, os sinos internos tocaram três vezes. Um batedor entrou correndo com sangue no ombro e uma flecha de ponta azul."
    oren "Capitã! A passagem norte foi aberta. Não pelos rebeldes — pelo Conselho."
    thalia "Quantos guardas?"
    oren "Bastante para fingir que foi acidente. Poucos para aguentar um cerco."

    show thalia defensive at portrait_emphasis_left
    thalia "Eles querem que eu ataque. Se eu atacar, as famílias ficam sem defesa. Se eu não atacar, chamam de traição."
    "A máscara de bronze bateu contra o quadril dela quando Thalia se moveu. Pela primeira vez, Ivo entendeu: ela a carregava para lembrar que uma comandante podia sobreviver a uma decisão e ainda não reconhecer a própria face depois."

    menu:
        "Como Ivo ajuda Thalia a escolher?"

        "Ir com ela fechar a passagem, enquanto Ariane protege a cidade.":
            $ thalia_affinity += 2
            $ ariane_affinity += 1
            $ ivo_courage += 1
            ivo "Você não vai para a passagem sozinha. Ariane, fica com as famílias."
            ariane "Eu preferia a parte da ponte explodindo, mas aceito a promoção."
            "Na passagem norte, Ivo segurou a corrente enquanto Thalia travava o portão. Ela não precisou matar ninguém; bastou fazer os mercenários verem que não havia vitória ali."

        "Usar o mapa para descobrir quem abriu o portão.":
            $ akris_choice = "estrategia"
            $ ivo_honesty += 1
            $ thalia_affinity += 1
            ivo "Se eles queriam uma batalha, não vamos entregar uma. Mostre-me os túneis."
            "O mapa revelava uma galeria antiga sob o Conselho. O grupo encontrou a alavanca da passagem e, ao lado dela, o selo de cera de Hieron — não do ancião, mas de alguém que falsificava as marcas das cidades para colocá-las umas contra as outras."

        "Pedir a Lyra que faça os guardas ouvirem a verdade que escondem.":
            $ lyra_affinity += 1
            $ thalia_affinity += 1
            ivo "Não para expor ninguém. Só para quebrar a mentira que está mantendo todos no lugar."
            "Lyra cantou uma única nota. Os guardas ouviram, cada um, a promessa que haviam feito ao entrar na muralha: proteger pessoas. Um por um, baixaram as lanças."

    scene bg akris_fortress
    with dissolve
    show thalia neutral at portrait_left
    show ivo neutral at portrait_bust_right

    "Ao amanhecer, a passagem norte estava fechada e Akris continuava de pé. Não porque alguém vencera uma guerra, mas porque uma pessoa se recusara a transformar medo em sentença."
    thalia "Meu irmão me pediu para não virar uma muralha. Eu achei que ele queria que eu fosse mais fraca."
    ivo "Talvez ele quisesse que você deixasse alguém entrar."
    "Thalia riu uma vez, sem humor, e então tirou a máscara de bronze do cinto. Não a largou; apenas deixou de escondê-la atrás do corpo."

    show thalia embarrassed at portrait_emphasis_left
    thalia "Você fala demais para alguém que chegou aqui há dez minutos."
    ivo "Foram quase três dias."
    thalia "Continua sendo demais."

    "O mapa de cobre se abriu sozinho sobre a mesa. A torre de Nix brilhava, e um novo traço surgiu ao lado dela: uma constelação partida em duas."
    moira_voice "A observadora vê aquilo que os outros escolhem esquecer."
    lyra "Cássia."
    thalia "Então vamos buscá-la antes que alguém transforme a visão dela numa arma."

    $ chapter_04_completed = True
    if "Thalia" not in unlocked_gallery:
        $ unlocked_gallery.append("Thalia")
    jump chapter_04_summary


label chapter_04_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 4{/size}\n\n{size=30}Uma muralha não precisa ser uma prisão.{/size}"

    "Vínculo com Thalia: [bond_rank(thalia_affinity)]."
    "A próxima rota aponta para Cássia e o Observatório de Nix."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 5 — O Céu que Não Promete":
            jump chapter_05_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_04_summary

        "Recomeçar o Capítulo 4":
            jump chapter_04_start

        "Voltar ao menu principal":
            return
