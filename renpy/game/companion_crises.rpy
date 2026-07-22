# Crises de rota: cada herdeira recebe uma escolha que não pode ser resolvida
# apenas com afinidade. A decisão marca confiança, limites e o futuro da rota.

label crisis_ariane:
    scene bg kallipolis_storm
    with dissolve
    show ariane concerned at portrait_left
    show ivo wary at portrait_bust_right

    "Depois da assembleia, três famílias esperavam na porta da pensão. Um panfleto preso à parede chamava Ariane de herdeira da inundação e dizia que a Casa das Chegadas era uma lista disfarçada de quem deveria ser salvo primeiro."
    ariane "Eu posso rasgar todos. Amanhã aparecem outros."
    ivo "Quem escreveu isso quer que você escolha entre se explicar e virar a vilã."
    ariane "Então o que fazemos quando a verdade parece propaganda na boca errada?"

    menu:
        "Como Ivo responde à crise de Ariane?"

        "Abrir a pensão e contar publicamente o que sabem — inclusive o que não sabem.":
            $ ariane_crisis = "resolved"
            $ ariane_affinity += 2
            $ ivo_honesty += 1
            ivo "Não vou pedir que confiem em nós. Vou pedir que façam perguntas na nossa frente."
            "Ariane fica imóvel por um segundo. Depois abre a porta. A conversa dura até o amanhecer e não convence todos, mas ninguém sai sem ter sido ouvido."
            ariane "Obrigada por não transformar minha vida numa defesa sua."

        "Fechar a pensão por uma noite e protegê-la da multidão.":
            $ ariane_crisis = "strained"
            $ ariane_affinity += 1
            ivo "Você não precisa enfrentar gente armada de medo agora."
            "Ariane concorda, mas observa a porta trancada como se ela também tivesse sido deixada do lado de fora."
            ariane "Proteção é boa. Só não deixa ela virar a resposta para tudo."

        "Espalhar que o Conselho escreveu os panfletos para virar a cidade contra ele.":
            $ ariane_crisis = "broken"
            $ ariane_affinity -= 2
            $ ivo_integrity -= 1
            ivo "Se querem uma história, damos uma que machuque de volta."
            "Ariane não levanta a voz. Isso torna a decepção mais difícil de suportar."
            ariane "Eu não vou deixar que usem meu nome para fazer de outra família o próximo alvo."

    hide ariane
    hide ivo
    return


label crisis_nerissa:
    scene bg nereu
    with dissolve
    show nerissa neutral at portrait_left
    show ivo wary at portrait_bust_right

    "Um barco sem bandeira chega ao cais de Nereu trazendo dezesseis sobreviventes e uma menina febril. Os capitães querem rebocá-lo para longe: dizem que a embarcação pode carregar o mesmo símbolo que alimentou o bloqueio."
    nerissa "Se eu abrir o porto, assumo o risco por todos. Se eu recusar, escolho quem fica à deriva."
    ivo "O que sua tripulação espera?"
    nerissa "Que eu pareça certa antes de decidir."

    menu:
        "Que tipo de comando Ivo pede a Nerissa?"

        "Abrir uma quarentena visível, com médicos, testemunhas e escolha dos sobreviventes.":
            $ nerissa_crisis = "resolved"
            $ nerissa_affinity += 2
            $ ivo_compassion += 1
            ivo "Segurança não precisa ser uma porta fechada. Pode ser uma regra que todo mundo vê."
            "Nerissa dá ordens curtas, mas explica cada uma. Quando a menina é levada para a enfermaria, metade do cais aplaude e a outra metade enfim se cala para observar."
            nerissa "Hoje você me lembrou que comando não é esconder quem paga o preço."

        "Manter o barco fora até haver certeza absoluta.":
            $ nerissa_crisis = "strained"
            $ nerissa_affinity -= 1
            ivo "Se for uma armadilha, não podemos abrir a cidade inteira."
            "A decisão evita pânico imediato, mas o barco permanece pequeno demais no horizonte. Nerissa não discute; apenas não tira os olhos dele."
            nerissa "Certeza é uma palavra confortável para quem está em terra."

        "Mandar afundar o barco antes que o medo se espalhe.":
            $ nerissa_crisis = "broken"
            $ nerissa_affinity -= 3
            $ ivo_integrity -= 1
            ivo "Não podemos arriscar Nereu por dezesseis pessoas."
            "Nerissa entrega a ordem a outro oficial e se afasta antes que ele a cumpra. Quando volta, seus olhos não pedem desculpa nem perdão."
            nerissa "Não me peça para chamar isso de estratégia."

    hide nerissa
    hide ivo
    return


label crisis_melia:
    scene bg asterion
    with dissolve
    show melia neutral at portrait_left
    show ivo wary at portrait_bust_right

    "A raiz sob Asterion encontra uma cisterna antiga. Dentro dela, memórias de moradores mortos começaram a falar com as crianças da cidade. A prefeitura quer que Mélia queime a raiz inteira antes que mais gente a escute."
    melia "Se eu queimar tudo, silencio os mortos e a chance de curar a cidade. Se não queimar, alguém pode seguir uma voz que não sabe ser pai, mãe ou saudade."
    ivo "Você não precisa decidir sozinha."
    melia "Mas a mão que tocar a seiva vai ser a minha."

    menu:
        "O que Ivo pede a Mélia?"

        "Criar vigílias: famílias escolhem ouvir ou se despedir, com a cidade protegendo o limite.":
            $ melia_crisis = "resolved"
            $ melia_affinity += 2
            $ ivo_compassion += 1
            ivo "Não arrancamos a memória de ninguém. Damos a ela uma porta e alguém para fechar quando for demais."
            "Mélia organiza bancos, chá e lanternas ao redor da cisterna. Algumas pessoas ouvem uma única frase; outras escolhem não descer. Ambas saem inteiras."
            melia "Você entende que cuidado não é obrigar alguém a sarar do jeito certo."

        "Selar a cisterna até que exista uma cura segura.":
            $ melia_crisis = "strained"
            $ melia_affinity += 0
            ivo "Uma cidade em pânico não é laboratório."
            "Mélia sela a pedra com raízes pálidas. O som para, mas uma criança deixa uma flor diante da tampa e pergunta quando poderá ouvir a avó de novo."
            melia "Seguro não é o mesmo que justo. Não esquece disso."

        "Queimar a raiz e encerrar o problema de uma vez.":
            $ melia_crisis = "broken"
            $ melia_affinity -= 3
            $ ivo_integrity -= 1
            ivo "O risco não vale a pena. Acaba com isso."
            "O fogo de Mélia é verde e silencioso. Quando a última voz some, ela vira o rosto para que Ivo não veja as lágrimas."
            melia "Você me pediu para destruir uma possibilidade de despedida. Não chama isso de proteção."

    hide melia
    hide ivo
    return


label crisis_lyra:
    scene bg lyria_temple
    with dissolve
    show lyra worried at portrait_left
    show ivo wary at portrait_bust_right

    "Mikon é encontrado com uma placa de bronze roubada sob o casaco. O menino jura que não sabia ler o decreto gravado nela; queria apenas mostrar que podia carregar alguma coisa importante. A guarda quer puni-lo em praça pública para restaurar a ordem."
    lyra "Se eu falar por ele, dirão que a herdeira protege os seus. Se eu ficar calada, ele aprende a mesma lição que esta cidade tentou me ensinar."
    ivo "Qual é a lição?"
    lyra "Que a voz de uma criança só vale quando repete uma voz adulta."

    menu:
        "Como Ivo enfrenta a crise de Lyra e Mikon?"

        "Pedir que Mikon conte sua versão e aceitar uma reparação escolhida por ele.":
            $ lyra_crisis = "resolved"
            $ lyra_affinity += 2
            $ protected_mikon = True
            ivo "Ele fez algo errado. Isso não significa que precisa ser quebrado para aprender."
            "Mikon devolve a placa e passa uma semana ajudando a transcrever as canções proibidas. Na última noite, ele canta uma nota sozinha. Lyra responde com outra."
            lyra "Obrigada por não me deixar transformar medo em disciplina."

        "Assumir a culpa no lugar de Mikon para encerrar o caso.":
            $ lyra_crisis = "strained"
            $ lyra_affinity += 1
            ivo "Se precisam de um culpado, escolham alguém que aguenta."
            "A guarda aceita depressa demais. Mikon não é punido, mas baixa os olhos quando Ivo é levado para prestar depoimento."
            lyra "Ele precisava aprender a responder. Não a assistir você pagar."

        "Entregar Mikon à guarda para provar que ninguém está acima das regras.":
            $ lyra_crisis = "broken"
            $ lyra_affinity -= 3
            $ ivo_integrity -= 1
            ivo "Regra vale para todos."
            "Lyra fecha os olhos quando Mikon é levado. Ela não grita; a ausência da música na escadaria diz mais do que uma acusação."
            lyra "Você confundiu igualdade com abandono."

    hide lyra
    hide ivo
    return


label crisis_thalia:
    scene bg akris_fortress
    with dissolve
    show thalia defensive at portrait_left
    show ivo wary at portrait_bust_right

    "Dois soldados voltam de uma patrulha sem o terceiro. Dizem que ele desertou. A irmã do desaparecido chega ao portão com uma carta: ele teria ido procurar civis presos fora da rota oficial. O Conselho exige uma execução simbólica dos dois que retornaram por covardia."
    thalia "Se eu recusar, parecerá que minhas ordens são enfeite. Se eu aceitar, ensino a todos que voltar vivo é culpa."
    ivo "O que você acredita que aconteceu?"
    thalia "Que eu não sei. E é isso que o Conselho odeia."

    menu:
        "Que justiça Ivo propõe em Akris?"

        "Investigar com as famílias e os soldados; ninguém é condenado antes de a rota ser refeita.":
            $ thalia_crisis = "resolved"
            $ thalia_affinity += 2
            $ ivo_honesty += 1
            ivo "Justiça que precisa de pressa demais costuma estar escondendo medo."
            "Thalia abre o mapa no pátio e chama a irmã do desaparecido para apontar a última luz vista na encosta. Pela primeira vez, o Conselho precisa ouvir alguém sem patente."
            thalia "Você não tornou isso fácil. Tornou impossível fingir que era simples."

        "Suspender os dois soldados, mas evitar punição pública até haver prova.":
            $ thalia_crisis = "strained"
            $ thalia_affinity += 0
            ivo "A cidade precisa ver que ainda existe ordem."
            "Os soldados entregam as espadas sem protestar. A irmã do desaparecido não agradece nem acusa; apenas pergunta se alguém vai procurá-lo."
            thalia "Às vezes, meio caminho é só uma forma educada de deixar alguém esperando."

        "Executar os soldados para impedir novas deserções.":
            $ thalia_crisis = "broken"
            $ thalia_affinity -= 3
            $ ivo_integrity -= 1
            ivo "Exército sem medo de punição não segura muralha."
            "Thalia retira a insígnia de comandante e a coloca na mesa do Conselho. Ninguém consegue olhar para ela quando fala."
            thalia "Você pediu uma fortaleza. Não uma cidade."

    hide thalia
    hide ivo
    return


label crisis_cassia:
    scene bg nix_observatory
    with dissolve
    show cassia vision at portrait_left
    show ivo wary at portrait_bust_right

    "Cássia encontra uma previsão que mostra uma das seis cidades sendo sacrificada para impedir o retorno de Oryx. O nome da cidade não aparece; aparecem seis possibilidades, cada uma verdadeira em uma linha diferente do futuro."
    cassia "Se eu mostrar isso, cada cidade vai tentar descobrir se é a escolhida. Se eu esconder, faço exatamente o que jurei não fazer."
    ivo "Você quer que eu decida?"
    cassia "Quero que você me impeça de chamar medo de cálculo."

    menu:
        "O que Ivo pede a Cássia?"

        "Mostrar a previsão incompleta a todas as cidades e criar um pacto para impedir o sacrifício.":
            $ cassia_crisis = "resolved"
            $ cassia_affinity += 2
            $ trusted_cassia_truth = True
            ivo "A verdade não fica menos perigosa porque uma pessoa a guarda."
            "Cássia remove os números do quadro e deixa apenas as perguntas. Os emissários discutem por horas, mas saem com um pacto em vez de uma lista de suspeitos."
            cassia "Obrigada por não me pedir uma resposta limpa."

        "Guardar a previsão até que haja certeza sobre qual cidade será atingida.":
            $ cassia_crisis = "strained"
            $ cassia_affinity -= 1
            $ kept_future_secret = True
            ivo "Pânico não salva ninguém."
            "Cássia fecha o astrolábio. A sala fica mais quieta, mas o silêncio agora parece uma escolha com data de validade."
            cassia "Espero que você esteja certo. Eu nunca gosto de esperar isso."

        "Escolher preventivamente uma cidade para ser abandonada e salvar as outras cinco.":
            $ cassia_crisis = "broken"
            $ cassia_affinity -= 3
            $ ivo_integrity -= 1
            ivo "Uma perda pode evitar cinco."
            "Cássia não discute. Ela apenas apaga a previsão, uma estrela de cada vez, e deixa o astrolábio sobre a mesa entre os dois."
            cassia "Foi assim que Oryx começou. Com uma frase que parecia matemática."

    hide cassia
    hide ivo
    return
