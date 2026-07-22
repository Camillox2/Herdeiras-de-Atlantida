label chapter_09_start:
    if not chapter_08_completed:
        jump chapter_08_start

    scene bg asterion
    with fade
    play music "audio/music/agora_of_columns.wav" fadeout 1.0 fadein 1.2

    if "As Raízes" not in unlocked_cgs:
        $ unlocked_cgs.append("As Raízes")

    scene cg asterion_roots
    with dissolve

    centered "{size=52}CAPÍTULO 9{/size}\n{size=30}As Raízes que Lembram{/size}"

    call late_consequence_ch09

    "Asterion não estava em silêncio. As raízes sob os terraços falavam pela pedra, fazendo portas se abrirem sozinhas e oliveiras deixarem cair frutos salgados. Quem dormia perto dos jardins acordava lembrando da pior coisa que já tinha perdido."

    show melia neutral at portrait_left
    show ivo wary at portrait_bust_right

    melia "O Coletor não trouxe um exército. Ele ensinou as raízes a guardar medo como se fosse água."
    ivo "E dá para desaprender?"
    melia "Tudo que vive pode aprender outra coisa. A questão é quanto vamos machucar tentando ensinar."
    "No canteiro central, uma criança abraçava a raiz de uma oliveira e chorava por uma mãe que ainda estava viva. Mélia se ajoelhou, mas não puxou a menina. Esperou até que ela escolhesse soltar."

    show ariane neutral at portrait_center
    ariane "Os sinos de Nereu tinham um mapa. Um deles apontava para cá."
    melia "Eu encontrei o outro. Plantado no coração da estufa. Se eu cortar a raiz errada, o jardim inteiro vira cinza."

    menu:
        "O que Ivo prioriza com Mélia?"

        "Criar um lugar seguro para as pessoas descansarem antes de enfrentar as raízes.":
            $ asterion_response = "abrigo"
            $ melia_affinity += 2
            $ ivo_compassion += 2
            ivo "Uma cidade assustada não precisa de mais ordens. Precisa de alguém dizendo onde pode respirar."
            "Mélia transformou a estufa menor em abrigo. As flores azuis foram cobertas, chá foi servido e os sonhos deixaram de ter plateia."

        "Seguir a raiz até o sino, mesmo correndo risco.":
            $ asterion_response = "raiz"
            $ ivo_courage += 2
            ivo "Se a fonte continuar falando, cada pessoa vai escutar uma versão do medo. Vamos até ela."
            "A raiz se abriu diante de Ivo como uma escada de madeira viva. Lá embaixo, o bronze do sino vibrava dentro de uma esfera de seiva escura."

        "Pedir a Mélia que explique o que está sentindo antes de decidir.":
            $ asterion_response = "escuta"
            $ melia_affinity += 2
            $ ivo_honesty += 1
            ivo "Você conhece este jardim melhor do que ninguém. O que ele está pedindo?"
            "Mélia tocou a casca da oliveira. Os olhos dela se encheram de lágrimas que não caíram."
            melia "Ele não quer destruir a cidade. Está tentando esconder as pessoas da dor, e não sabe que isso também machuca."

    "No fundo da estufa, Ivo encontrou a fonte: uma raiz enorme enroscada em torno de um sino. Cada vibração extraía uma lembrança das pessoas acima e a misturava à seiva."
    show melia embarrassed at portrait_emphasis_left
    melia "Eu poderia queimar tudo. Seria rápido. Mas queimaria a memória das sementes, dos jardineiros, do que esta cidade cultivou antes de mim."
    ivo "Então não vamos chamar rapidez de solução."

    menu:
        "Mélia pede uma decisão. Ivo responde:"

        "Corte o sino, não a raiz.":
            $ trusted_melia_seed = True
            $ melia_affinity += 2
            $ ivo_honesty += 1
            ivo "O inimigo é o mecanismo. Não a coisa viva que ele aprendeu a usar."
            "Mélia usou uma lâmina fina para separar o bronze da seiva. O sino rachou sem que uma única folha morresse."

        "Divida a raiz em novas mudas antes que ela exploda.":
            $ trusted_melia_seed = True
            $ melia_affinity += 1
            $ ivo_compassion += 1
            ivo "Se ela guarda memórias, talvez possa guardar muitas sem esmagar ninguém."
            "Mélia distribuiu a seiva em seis vasos. Cada muda recebeu apenas uma lembrança: pequena, humana, capaz de ser cuidada."

        "Use a Marca para puxar o medo para fora da cidade.":
            $ ivo_courage += 2
            ivo "Se a raiz precisa de uma âncora, usa a minha. Mas não deixa ela escolher por você."
            "A dor atravessou o pulso de Ivo, fria e antiga. Mélia segurou sua mão e conduziu a memória para a terra, até que ela virasse apenas chuva sob as pedras."

    "Quando o sino se calou, o jardim não voltou a ser perfeito. Algumas árvores continuaram tortas; algumas pessoas ainda precisariam falar sobre o que haviam sonhado. Mas a cidade parou de confundir lembrança com sentença."
    "Mélia guardou uma das mudas num vaso de barro. Dentro dela, uma luz azul pulsava devagar."
    melia "Isto não é uma arma. É uma testemunha. Pode nos avisar quando outro sino estiver perto."
    ariane "Então agora temos um jardim espionando para nós."
    melia "Você consegue dizer qualquer coisa de um jeito que parece ameaça."
    ariane "É um talento."

    "A muda apontou suas folhas para oeste. Lá, além das montanhas, o vento carregava uma nota de Lyra interrompida no meio."
    ivo "Lýria."
    melia "O Coletor aprendeu que não consegue nos separar usando só medo. Agora ele vai tentar silenciar quem faz as pessoas ouvirem."

    $ chapter_09_completed = True
    jump chapter_09_summary


label chapter_09_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    centered "{size=54}FIM DO CAPÍTULO 9{/size}\n\n{size=30}Asterion se lembrou sem se afogar nas lembranças.{/size}"

    "Vínculo com Mélia: [bond_rank(melia_affinity)]."
    "A próxima rota leva a Lýria, onde a música de Lyra foi interrompida."

    menu:
        "O que deseja fazer?"

        "Continuar para o Capítulo 10 — A Voz que Não se Curva":
            jump chapter_10_start

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump chapter_09_summary

        "Recomeçar o Capítulo 9":
            jump chapter_09_start

        "Voltar ao menu principal":
            return
