label prologue_start:
    scene bg kallipolis
    with fade
    play music "audio/music/kallipolis_harbor.wav" fadein 1.5

    centered "{size=58}PRÓLOGO{/size}\n{size=34}A Marca das Moiras{/size}"

    "O mar devolveu Ivo a Kallípolis sem cerimônia."
    "Quando abriu os olhos, o sal ardia em seus lábios, sua bolsa estava quase vazia e a cidade branca subia diante dele como uma promessa feita a outra pessoa."
    "Navios rangiam contra o cais. Gaivotas disputavam restos de peixe. No alto, bandeiras azuis tremulavam entre colunas gastas pelo vento."

    show ivo neutral at portrait_center
    ivo "Sem dinheiro. Sem destino. Pelo menos o mar teve a educação de me deixar perto de uma cidade."

    menu:
        "Qual foi o primeiro pensamento de Ivo?":

        "Preciso descobrir por que sobrevivi.":
            $ ivo_courage += 1
            $ ivo_honesty += 1
            thoughts "O medo ainda estava ali, mas agora tinha uma pergunta para enfrentar."

        "Preciso encontrar comida antes de respostas.":
            $ ivo_honesty += 1
            $ ivo_compassion += 1
            thoughts "Mistérios eram importantes. Pão, naquele instante, era mais."

        "Ótimo. Mais uma cidade pronta para se arrepender de me conhecer.":
            $ ivo_humor += 2
            thoughts "A piada não melhorou sua situação. Melhorou um pouco sua respiração."

    hide ivo
    "Uma placa pintada com uma escada e uma ânfora apontava para a Pensão dos Degraus."

    scene bg pensao
    with dissolve

    "O cheiro de pão, azeite e madeira antiga afastou parte do frio."
    "Atrás do balcão, uma mulher observava Ivo com a paciência de quem já vira dezenas de náufragos jurarem que estavam apenas de passagem."

    lysandra "Você dormiu no cais. Isso explica o cheiro e a expressão."
    lysandra "Kallípolis não é gentil com quem chega sem nome, moedas ou amigos."
    lysandra "Vai continuar fingindo que sabe aonde vai?"

    menu:
        "Como Ivo responde?":

        "Dizer a verdade: estou perdido.":
            $ ivo_honesty += 2
            $ ivo_compassion += 1
            lysandra "Bom. A verdade não compra cama, mas evita que você durma em lugar pior."

        "Fingir que só procura trabalho.":
            $ ivo_courage += 1
            lysandra "Todo mundo procura trabalho. Pouca gente admite que procura uma chance."

        "Fazer uma piada e mudar de assunto.":
            $ ivo_humor += 2
            lysandra "Humor é uma casa sem janela. Um dia você vai precisar sair dela."

    lysandra "Pólemon contrata carregadores na Ágora. Procure as colunas com tecidos azuis."
    lysandra "E não aceite nada que ele chame de simples."

    scene bg agora
    with dissolve
    play music "audio/music/agora_of_columns.wav" fadeout 0.8 fadein 1.2

    "A Ágora das Colunas parecia vender tudo: azeite, mapas, promessas, informações e silêncios."
    "Pólemon esperava junto a uma caixa selada com bronze, sorrindo como alguém que já havia calculado o preço da necessidade de Ivo."

    polemon "Você tem cara de quem perdeu tudo antes do almoço."
    polemon "Leve esta caixa ao cais e eu pago sete moedas. Não abra."

    menu:
        "O que Ivo faz?":

        "Aceitar sem fazer perguntas.":
            $ ivo_courage += 1
            polemon "Bom senso é raro. Leve a caixa até a marca no cais."

        "Perguntar o que há dentro.":
            $ ivo_honesty += 1
            $ ivo_courage += 1
            polemon "Dentro? Problema. E problema paga melhor que pão."

        "Recusar e ir embora.":
            $ ivo_honesty += 1
            polemon "Claro. Você é livre para passar fome por princípios."
            "Ivo deu dois passos."
            "A marca antiga em seu pulso queimou pela primeira vez."
            thoughts "A caixa estava chamando por ele — ou algo dentro dela estava."
            menu:
                "Voltar e aceitar o trabalho":
                    $ ivo_courage += 1
                    polemon "Sabia que sua consciência teria bom senso."
                "Exigir o dobro":
                    $ ivo_humor += 1
                    $ ivo_courage += 1
                    polemon "Sete agora. O resto se você sobreviver à curiosidade."

    scene bg kallipolis
    with dissolve
    play music "audio/music/kallipolis_harbor.wav" fadeout 0.8 fadein 1.0

    "No cais, a caixa pareceu ficar mais pesada."
    "O símbolo em seu lacre repetia as linhas da cicatriz no pulso de Ivo."

    menu:
        "A caixa deveria permanecer fechada.":

        "Abrir a caixa por vontade própria.":
            $ opened_crate_willingly = True
            $ ivo_courage += 2
            "Ivo rompeu o selo."
            "Dentro havia uma moeda azul, fria como água profunda."
            "Quando seus dedos tocaram o metal, a Marca das Moiras despertou."

        "Tentar cumprir o acordo.":
            $ ivo_honesty += 2
            "Ivo afastou a mão."
            "A madeira estalou sozinha."
            "Uma fissura azul percorreu o selo, e a moeda saltou para sua palma como se tivesse esperado anos por aquele contato."
            "A Marca das Moiras despertou."

        "Procurar alguém antes de decidir.":
            $ ivo_compassion += 1
            $ ivo_honesty += 1
            "Antes que pudesse chamar um guarda, uma sombra atravessou os telhados."
            "Uma pequena lâmina atingiu o selo. A caixa se abriu, revelando a moeda azul."
            "A Marca das Moiras despertou."

    "Por um instante, o cais desapareceu."
    "Ivo viu uma cidade submersa, seis silhuetas diante de um trono vazio e fios dourados ligando destinos que ainda não haviam se encontrado."

    show ariane neutral at portrait_enter_right
    ariane "Você está olhando para o telhado errado."
    ariane "Ou isso é coragem demais, ou falta de prática."

    ivo "Foi você quem abriu a caixa?"

    ariane "Você tocou a moeda. Essa foi a escolha que importou."
    ariane "Podia vendê-la e desaparecer. Por que ainda está aqui?"

    menu:
        "Responder a Ariane":

        "Porque não quero ser a pessoa que foge.":
            $ ariane_affinity += 2
            $ ivo_courage += 1
            ariane "Então tente não morrer antes de provar isso."

        "Porque preciso entender a Marca.":
            $ ariane_affinity += 1
            $ ivo_honesty += 1
            ariane "Uma resposta honesta. Quase suspeita, vindo de você."

        "Porque você claramente sentiria minha falta.":
            $ ivo_humor += 2
            $ ariane_affinity += 1
            show ariane embarrassed at portrait_right
            ariane "Não abuse da sorte, estrangeiro."

    show ariane neutral at portrait_right
    ariane "Meu nome é Ariane. E o homem vindo pela ponte não negocia."

    collector "Entregue a moeda. Cidadãos sem registro não carregam relíquias."

    "O Coletor avançou com dois guardas. Ariane já procurava uma rota entre cordas, barcos e caixas."

    menu:
        "Como escapar do Coletor?":

        "Confiar no plano de Ariane.":
            $ trusted_ariane = True
            $ ariane_affinity += 2
            ariane "Quando eu disser agora, pule."
            ivo "Pular para onde?"
            ariane "Esse é o tipo de pergunta que estraga um plano."
            "Ariane cortou uma amarra. Uma vela despencou entre eles e os guardas."
            "Ivo saltou para o barco inferior no instante em que ela gritou."

        "Distrair os guardas para proteger Ariane.":
            $ protected_ariane = True
            $ ariane_affinity += 2
            $ ivo_courage += 2
            ivo "A moeda está comigo. Ela não tem nada a ver com isso."
            ariane "Ivo..."
            "O Coletor voltou toda a atenção para ele."
            "Ariane aproveitou o segundo roubado, derrubou uma pilha de ânforas e puxou Ivo pela mão."

        "Blefar dizendo que a moeda foi entregue a Pólemon.":
            $ ivo_humor += 1
            $ ivo_courage += 1
            ivo "Chegou tarde. Pólemon já levou a relíquia."
            collector "Pólemon não tocaria em algo que canta."
            ariane "Foi um blefe ruim."
            ivo "Mas você ganhou tempo."
            $ ariane_affinity += 1
            "Ariane sorriu contra a vontade antes de abrir uma passagem entre as redes."

    hide ariane
    "Eles escaparam por uma porta de ferro escondida sob o cais."
    "Os degraus desciam para um lugar que Kallípolis havia decidido esquecer."

    scene bg cisterna
    with fade
    play music "audio/music/cistern_forgotten_echoes.wav" fadeout 1.0 fadein 1.5

    "A Cisterna Esquecida respirava água e memória."
    "Três luzes azuis pulsavam entre colunas partidas. Ao fundo, uma porta de bronze aguardava com três círculos vazios."

    show ariane neutral at portrait_right
    ariane "Esses são Ecos de Atlântida."
    ariane "Não são objetos. São lembranças que perderam seus donos."
    ariane "Se ouvir alguma voz, não prometa nada."

    "O primeiro Eco mostrou Ivo ainda criança diante de um mar negro."
    voice "Você sempre soube que voltaria."

    menu:
        "Como reagir ao primeiro Eco?":

        "Ouvir até o fim.":
            $ listened_to_echoes += 1
            $ ivo_courage += 1
            "A lembrança deixou uma palavra em sua mente: herdeiras."

        "Romper o contato.":
            $ ivo_honesty += 1
            "Ivo soltou o fragmento antes que a visão criasse raízes."

    "O segundo Eco revelou seis mãos sobre uma mesa de pedra, cada uma marcada por um símbolo diferente."
    voice "Nenhuma delas herdará Atlântida sozinha."

    menu:
        "Contar a Ariane exatamente o que viu.":
            $ listened_to_echoes += 1
            $ ariane_affinity += 1
            $ ivo_honesty += 1
            ariane "Seis herdeiras... Então os registros estavam incompletos."

        "Esconder a parte sobre as seis mulheres.":
            $ ivo_courage += 1
            thoughts "Ainda não sabia se a visão era profecia, ameaça ou armadilha."

    "O terceiro Eco não mostrou ruínas."
    "Mostrou Ariane diante da porta de bronze, sozinha, enquanto a cidade desabava atrás dela."

    menu:
        "O que Ivo faz?":

        "Segurar a mão de Ariane.":
            $ ariane_affinity += 2
            $ ivo_compassion += 2
            show ariane embarrassed at portrait_right
            ivo "Desta vez você não vai atravessar sozinha."
            ariane "Você não sabe o que existe do outro lado."
            ivo "Você também não."

        "Avisá-la sobre a visão.":
            $ ariane_affinity += 1
            $ ivo_honesty += 2
            ivo "O Eco mostrou você aqui. Sozinha."
            ariane "E você pretende impedir uma memória de se repetir?"
            ivo "Pretendo dar a ela uma escolha diferente."

        "Guardar a visão por enquanto.":
            $ ivo_courage += 1
            thoughts "Algumas verdades precisavam de um momento em que não parecessem ameaças."

    show ariane neutral at portrait_right
    "Os três Ecos ocuparam os círculos da porta."
    "O bronze se abriu sem ruído, revelando água suspensa no ar como um espelho vertical."

    voice "Aquele que carrega a Marca encontrará as seis."
    voice "Quando o último juramento for quebrado, escolherá entre restaurar Atlântida ou libertar suas herdeiras."

    ariane "Isso não é poder, Ivo."
    ariane "É responsabilidade."

    menu:
        "A escolha que encerra o prólogo":

        "Prometer seguir ao lado de Ariane.":
            $ promised_ariane = True
            $ ariane_affinity += 2
            $ ivo_compassion += 1
            show ariane embarrassed at portrait_right
            ivo "Então não carregue essa responsabilidade sozinha."
            ariane "Promessas feitas em ruínas costumam cobrar juros."
            ivo "Pode cobrar."

        "Pedir tempo para entender a Marca.":
            $ ivo_honesty += 2
            ivo "Não vou prometer algo que ainda não entendo."
            ariane "Ótimo."
            ariane "Eu desconfiaria mais se você prometesse."

        "Dizer que encontrará as seis, custe o que custar.":
            $ ivo_courage += 2
            ivo "Se existem seis pessoas presas a isso, vou encontrá-las."
            ariane "Só não transforme destino em desculpa para decidir por elas."

    hide ariane
    "Atrás do espelho, uma rota marítima surgiu gravada na pedra."
    "O primeiro destino era Nereu."

    scene bg nereu
    with fade
    play music "audio/music/nereu_blue_sails.wav" fadeout 1.0 fadein 1.5

    centered "{size=52}NEREU{/size}\n{size=30}A cidade das velas azuis{/size}"

    "A travessia terminou entre muralhas brancas, canais luminosos e navios de velas azuis."
    "Kallípolis cheirava a sobrevivência."
    "Nereu cheirava a poder bem administrado — o que talvez fosse mais perigoso."

    show nerissa neutral at portrait_enter_left
    nerissa "Então você é o estrangeiro que fez Kallípolis lembrar do que enterrou."
    nerissa "Em Nereu, memórias são catalogadas, armadas e lançadas ao mar."
    nerissa "Se veio por respostas, aprenda a reconhecer uma pergunta perigosa."

    menu:
        "A primeira resposta a Nerissa":

        "Perguntar diretamente sobre Atlântida.":
            $ nerissa_question = "Atlantida"
            $ nerissa_affinity += 1
            $ ivo_courage += 1
            nerissa "Direto. Isso pode ser coragem ou uma vida muito curta."

        "Dizer que procura Ariane.":
            $ nerissa_question = "Ariane"
            $ nerissa_affinity += 1
            $ ivo_honesty += 1
            show nerissa embarrassed at portrait_left
            nerissa "Interessante. Ela costuma ser a pessoa que desaparece, não a procurada."

        "Admitir que ainda não sabe o que procura.":
            $ nerissa_question = "Incerteza"
            $ nerissa_affinity += 2
            $ ivo_honesty += 2
            nerissa "A resposta mais perigosa costuma ser a verdadeira."

    show nerissa neutral at portrait_left
    nerissa "Entre na cidade, Ivo."
    nerissa "Nereu já sabia seu nome antes de você chegar."

    hide nerissa
    $ prologue_completed = True

    jump prologue_summary


label prologue_summary:
    scene bg title
    with fade
    stop music fadeout 1.5

    $ main_bond = bond_rank(ariane_affinity)
    $ second_bond = bond_rank(nerissa_affinity)
    $ trait = dominant_trait()

    centered "{size=56}FIM DO PRÓLOGO{/size}\n\n{size=32}A Marca das Moiras despertou.{/size}"

    "Perfil de Ivo: [trait]."
    "Vínculo com Ariane: [main_bond]."
    "Primeira impressão de Nerissa: [second_bond]."

    if promised_ariane:
        "Ariane guardará a promessa feita diante da porta de bronze."
    elif ariane_affinity >= 4:
        "Ariane ainda não chama isso de confiança, mas já não trata Ivo como um estranho."
    else:
        "Ariane permanece cautelosa. O destino os uniu antes que a confiança pudesse fazê-lo."

    if nerissa_affinity >= 2:
        "A sinceridade de Ivo despertou a curiosidade de Nerissa."
    else:
        "Nerissa observará cada passo do estrangeiro em sua cidade."

    "Continua no Capítulo 1 — As Velas Azuis de Nereu."

    menu:
        "O que deseja fazer?":

        "Ver os vínculos":
            call screen relationships(close_action=Return())

        "Voltar ao menu principal":
            return

        "Recomeçar o prólogo":
            jump restart_prologue

    return


label restart_prologue:
    $ ariane_affinity = 0
    $ nerissa_affinity = 0
    $ ivo_courage = 0
    $ ivo_honesty = 0
    $ ivo_humor = 0
    $ ivo_compassion = 0
    $ opened_crate_willingly = False
    $ trusted_ariane = False
    $ protected_ariane = False
    $ listened_to_echoes = 0
    $ promised_ariane = False
    $ nerissa_question = ""
    $ prologue_completed = False
    jump prologue_start
