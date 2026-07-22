label chapter_13_start:
    if not chapter_12_completed:
        jump chapter_12_start

    scene bg sunken_hall
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    centered "{size=52}CAPÍTULO 13{/size}\n{size=30}O Abismo de Tálassa{/size}"

    if cassia_crisis == "":
        call crisis_cassia
    call late_consequence_ch13

    "Desta vez, o Salão Afundado não aguardava vazio. A água além dos arcos subia em espirais lentas, levando pequenos sinos de bronze como peixes sem vida. Todos tocavam sem produzir som."
    "As seis cadeiras continuavam vazias. No centro, porém, uma sétima cadeira havia surgido — feita de máscara derretida e raízes negras."

    show cassia vision at portrait_left
    show ivo wary at portrait_bust_center
    show ariane neutral at portrait_right

    cassia "A máscara está tentando fabricar um lugar para você antes de conseguir fabricar uma decisão."
    ivo "Então não sentamos."
    ariane "Parece óbvio. Isso geralmente significa que vai dar errado de um jeito criativo."

    "No alto das ruínas, Nerissa chamou atenção para uma galeria inundada. Dentro dela, seis pessoas estavam presas em bolhas de água: comerciantes, pescadores e dois dos aprendizes de Lýria. O Coletor não os escolhera por importância. Escolhera porque cada um vinha de uma cidade diferente."
    show nerissa neutral at portrait_left
    nerissa "Ele quer que a gente escolha quais cidades têm prioridade."
    thalia "Então ele não entendeu nada."

    collector "Eu entendo perfeitamente. Vocês só preferem adiar o momento em que alguém paga a conta."
    "A voz saiu da cadeira central. A máscara não tinha rosto, mas seis silhuetas apareceram nela: versões de Ivo usando coroas diferentes, todas cansadas demais para discordar."

    menu:
        "Diante dos reféns, Ivo escolhe o primeiro movimento:"

        "Mandar o grupo resgatar todos, dividindo as seis tarefas.":
            $ abyss_choice = "todos"
            $ saved_herdades_at_abyss = True
            $ ivo_compassion += 2
            $ ariane_affinity += 1
            $ nerissa_affinity += 1
            $ melia_affinity += 1
            $ lyra_affinity += 1
            $ thalia_affinity += 1
            $ cassia_affinity += 1
            ivo "Cada cidade importa. Ninguém espera uma ordem para ser salvo."
            "Ariane cortou as cordas de luz, Nerissa guiou as correntes, Mélia acalmou as raízes escuras, Lyra cantou para as bolhas, Thalia segurou os arcos e Cássia encontrou o ponto em que o tempo da água desacelerava."

        "Atacar a cadeira antes que ela transforme os reféns em escolha.":
            $ abyss_choice = "cadeira"
            $ ivo_courage += 2
            ivo "Se a máquina continua falando, cada resgate vira chantagem. Eu paro a máquina."
            "Ivo avançou. A Marca ardeu, mas Cássia e Ariane seguraram seus braços antes que a cadeira pudesse se fechar em torno dele. O golpe abriu uma fissura, e as bolhas começaram a cair."

        "Pedir que Cássia revele a rota menos destrutiva.":
            $ abyss_choice = "rota"
            $ trusted_cassia_truth = True
            $ cassia_affinity += 2
            $ ivo_honesty += 1
            ivo "Você não precisa decidir por nós. Só mostra onde a máscara está mentindo."
            "Cássia girou o astrolábio. A visão mostrou que uma das bolhas era falsa — um espelho criado para fazer o grupo perder tempo enquanto a cadeira tomava a Marca."

    "Quando os últimos reféns tocaram chão seco, a cadeira central rachou. Em vez de desabar, ela projetou uma memória: o primeiro portador da Marca, ajoelhado diante de uma cidade inundada, recusando-se a escolher."
    "Ao redor dele, seis herdeiras da antiga Atlântida tinham dividido a Marca em fragmentos, para que nenhuma pessoa voltasse a carregar a decisão sozinha."
    moira_voice "O juramento não falhou. Foi interrompido."
    cassia "O Coletor não quer substituir o juramento. Quer convencer a todos que ele já falhou."

    "A máscara tentou envolver Ivo. Por um segundo, ele viu uma solução fácil: sentar, ordenar, salvar cinco cidades e aceitar a sexta como estatística. A ideia era terrível porque funcionava rápido."
    show ivo wary at portrait_bust_center
    ivo "É isso que você oferece? Um mundo com menos mortes e mais culpa?"
    collector "Um mundo previsível."
    ivo "Então você nunca entendeu pessoas."

    menu:
        "A máscara oferece a cadeira. Ivo responde:"

        "Recusar e entregar a Marca ao círculo das seis.":
            $ saved_herdades_at_abyss = True
            $ ivo_compassion += 1
            ivo "A Marca não é minha para comandar. É nossa para vigiar."
            "As seis herdeiras tocaram a luz no pulso de Ivo. Pela primeira vez, a Marca se dividiu sem ferir, formando sete fios que se mantinham separados e juntos."

        "Quebrar a cadeira, mesmo sem saber o custo.":
            $ ivo_courage += 2
            ivo "Não preciso de trono para decidir que isto acaba."
            "Thalia deu o primeiro golpe. Ivo deu o segundo. A cadeira se partiu, e o abismo respondeu com um rugido que parecia raiva e alívio ao mesmo tempo."

        "Perguntar à máscara quem a está usando agora.":
            $ ivo_honesty += 2
            ivo "Você continua falando como ideia. Quem lucra quando esta máscara vence?"
            "Por um instante, a superfície refletiu uma figura humana no topo de uma torre distante: alguém sem máscara, segurando uma das partes do juramento. A imagem se apagou antes que Cássia reconhecesse o rosto."

    "A máscara perdeu a cadeira, mas não desapareceu. Um fragmento escuro escapou pela corrente e atravessou o arco exterior, rumo à superfície."
    nerissa "Ele fugiu."
    cassia "Não. Ele recuou com uma informação: agora sabe que não consegue nos fazer escolher sozinhos."
    ariane "Então vai tentar separar a gente de um jeito mais inteligente."
    lyra "Ou vai tentar nos fazer querer isso."

    "No chão, onde a sétima cadeira existira, restou uma bússola de bronze apontando para uma torre sem nome acima do mar. A torre do reflexo da Ilha do Espelho."
    cassia "A Torre de Oryx. Não deveria existir."
    ivo "Parece que temos um endereço."
    thalia "E, pela primeira vez, ele parece ter um."

    $ chapter_13_completed = True
    jump chapter_13_summary


label chapter_13_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 13{/size}\n\n{size=30}A máscara perdeu a cadeira. O inimigo ganhou um rosto a encontrar.{/size}"

    "O grupo salvou os reféns e recusou a escolha falsa do Coletor."
    "A próxima rota aponta para a Torre de Oryx, onde o dono do fragmento espera."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 14 — O Homem que Voltou Tarde Demais":
            jump chapter_14_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_13_summary

        "Recomeçar o Capítulo 13":
            jump chapter_13_start

        "Voltar ao menu principal":
            return
