label prologue_start:
    $ reset_prologue_state()

    scene bg kallipolis
    with fade
    play music "audio/music/kallipolis_harbor.wav" fadein 1.5

    centered "{size=58}PRÓLOGO{/size}\n{size=34}A Marca das Moiras{/size}"

    "A última lembrança de Ivo era o convés se partindo sob seus pés."
    "Depois vieram o frio, uma voz chamando seu nome de dentro do mar e a certeza impossível de que alguma coisa havia escolhido mantê-lo vivo."

    "Quando despertou, estava deitado entre redes molhadas no cais de Kallípolis."
    "A cidade subia em pedra branca sobre o porto, bela demais para alguém sem dinheiro, documentos ou explicação."

    show ivo neutral at portrait_center
    ivo "Sem navio. Sem bolsa. E com uma cicatriz nova."

    "No pulso esquerdo, linhas finas formavam um símbolo que lembrava três fios entrelaçados."

    menu:
        "O que mais preocupa Ivo?":

        "Descobrir por que o mar o devolveu.":
            $ ivo_courage += 1
            $ ivo_honesty += 1
            $ prologue_priority = "verdade"
            thoughts "Sobreviver sem entender parecia apenas uma forma mais lenta de se perder."

        "Encontrar comida e um teto antes do anoitecer.":
            $ ivo_compassion += 1
            $ ivo_honesty += 1
            $ prologue_priority = "sobrevivencia"
            thoughts "Mistérios não aqueciam o corpo nem enchiam o estômago."

        "Fingir que tudo fazia parte de um plano.":
            $ ivo_humor += 2
            $ prologue_priority = "humor"
            thoughts "Se o mundo insistia em ser absurdo, ele podia ao menos escolher a piada."

    hide ivo

    "Uma mulher descarregando cestos indicou uma pensão perto das escadarias."
    "— Lysandra não confia em estranhos — avisou. — Mas confia menos ainda em cadáveres no cais."

    scene bg pensao
    with dissolve

    "A Pensão dos Degraus cheirava a pão, azeite e madeira aquecida pelo sol."
    "Atrás do balcão, Lysandra observou as roupas encharcadas de Ivo e, depois, a marca em seu pulso."

    lysandra "Você não é o primeiro homem que o mar cospe aqui."
    lysandra "É apenas o primeiro que ele devolve marcado."

    ivo "Sabe o que significa?"

    lysandra "Se soubesse, não diria a um desconhecido."

    "Ela colocou uma tigela de caldo diante dele, mas não soltou a colher."

    lysandra "Nome, origem e motivo para eu não chamar a guarda."

    menu:
        "Como Ivo conquista a confiança de Lysandra?":

        "Contar tudo que consegue lembrar.":
            $ ivo_honesty += 2
            $ lysandra_trust += 2
            ivo "Meu nome é Ivo. Meu navio afundou. Acordei no cais e não sei quem desenhou isto em mim."
            lysandra "Uma verdade incompleta ainda é melhor que uma mentira completa."

        "Dizer apenas que procura trabalho.":
            $ ivo_courage += 1
            $ lysandra_trust += 1
            ivo "Não tenho respostas. Tenho duas mãos e preciso trabalhar."
            lysandra "Kallípolis tem trabalho suficiente para matar homens mais preparados."

        "Usar humor para desarmar a situação.":
            $ ivo_humor += 2
            $ lysandra_trust += 1
            ivo "Se chamar a guarda, peça que tragam pão. Quero ser preso de estômago cheio."
            lysandra "Você usa piadas como outros usam armadura."
            lysandra "Armaduras também afundam."

    "Lysandra soltou a colher."

    lysandra "Pólemon compra serviços discretos na Ágora."
    lysandra "Se ele oferecer uma caixa selada, recuse."

    ivo "Isso foi estranhamente específico."

    lysandra "Porque ninguém segue conselhos vagos."

    if lysandra_trust >= 2:
        lysandra "E Ivo... se a marca aquecer, não deixe ninguém perceber."
        $ knows_mark_is_dangerous = True
    else:
        lysandra "Volte antes de escurecer. Ou não volte. Só não traga problemas para minha porta."

    scene bg agora
    with dissolve
    play music "audio/music/agora_of_columns.wav" fadeout 0.8 fadein 1.2

    "A Ágora das Colunas era um labirinto de tecidos azuis, bronze polido e vozes negociando futuros."
    "Pólemon aguardava junto a uma caixa pequena demais para justificar os dois guardas que fingiam não observá-la."

    polemon "Lysandra ainda envia náufragos para fazer o trabalho que seus filhos recusariam?"

    ivo "Ela mandou recusar uma caixa selada."

    polemon "Então já discutimos a parte mais cansativa."

    "Pólemon empurrou a caixa pela mesa. No lacre, o mesmo desenho da marca de Ivo se repetia em bronze."

    polemon "Leve-a até o cais velho. Sete moedas agora, sete na entrega."
    polemon "Não abra. Não entregue à guarda. E, acima de tudo, não escute se ela chamar seu nome."

    menu:
        "O que Ivo exige antes de aceitar?":

        "A verdade sobre a caixa.":
            $ ivo_honesty += 1
            $ polemon_respect += 2
            ivo "Diga o que estou carregando ou encontre outro desesperado."
            polemon "Uma relíquia retirada de ruínas que oficialmente não existem."
            polemon "Homens ricos pagam para possuir o passado. Homens sábios pagam para mantê-lo enterrado."

        "Pagamento dobrado pelo risco.":
            $ ivo_courage += 1
            $ ivo_humor += 1
            $ polemon_respect += 1
            ivo "Quatorze moedas não compram silêncio, mas compram uma tentativa."
            polemon "Sobreviva e discutiremos matemática."

        "Recusar o serviço.":
            $ ivo_honesty += 1
            ivo "Não vou carregar algo que sabe meu nome."
            "Ivo se afastou."
            "A marca queimou. De dentro da caixa, uma voz sussurrou uma palavra que ele ouvira durante o naufrágio."
            voice "Ivo."
            menu:
                "Voltar porque precisa entender.":
                    $ ivo_courage += 1
                    $ accepted_for_answers = True
                    ivo "Mudei de ideia. Mas agora faço perguntas."
                    polemon "Agora você faz parte da resposta."

                "Voltar apenas para impedir que outro a leve.":
                    $ ivo_compassion += 2
                    $ accepted_to_protect = True
                    ivo "Se isso é perigoso, não vou deixar nas mãos de alguém que não ouviu o aviso."
                    polemon "Uma intenção nobre. As relíquias adoram esse tipo."

    scene bg kallipolis
    with dissolve
    play music "audio/music/kallipolis_harbor.wav" fadeout 0.8 fadein 1.0

    "No cais velho, o movimento da cidade parecia distante."
    "Cada passo fazia o símbolo da caixa responder à marca em seu pulso."

    if knows_mark_is_dangerous:
        thoughts "Lysandra tinha razão. A marca não estava apenas quente. Estava reconhecendo alguma coisa."

    voice "Abra."

    "A voz não vinha da caixa."
    "Vinha da lembrança do mar."

    menu:
        "Diante do lacre, Ivo decide:":

        "Abrir a caixa por vontade própria.":
            $ opened_crate_willingly = True
            $ ivo_courage += 2
            "Ivo rompeu o lacre antes que o medo pudesse decidir por ele."
            "Uma moeda azul ergueu-se do interior e pairou sobre sua palma."

        "Resistir e cumprir o acordo.":
            $ resisted_crate = True
            $ ivo_honesty += 2
            "Ivo fechou os dedos e se afastou."
            "O bronze se partiu sozinho."
            "A moeda atravessou a madeira como luz através da água e pousou em sua mão."

        "Procurar ajuda antes de tocar na relíquia.":
            $ sought_help = True
            $ ivo_compassion += 1
            $ ivo_honesty += 1
            "Ivo chamou pelo vigia do cais."
            "Antes que a voz saísse por completo, uma lâmina lançada do alto cortou o lacre."
            "A moeda azul saltou da caixa diretamente para sua palma."

    "A dor veio primeiro."
    "Três linhas luminosas correram pelo pulso de Ivo e se fecharam ao redor da moeda."

    "Kallípolis desapareceu."

    "Ele viu uma cidade afundada sob um céu sem sol."
    "Viu seis mulheres diante de um trono vazio."
    "E viu fios dourados partindo de seu próprio peito até os pulsos de cada uma delas."

    voice "Encontre as herdeiras."
    voice "Antes que Atlântida as encontre."

    "A visão terminou com o som de uma lâmina sendo recolhida."

    show ariane neutral at portrait_enter_right
    ariane "Você demorou mais do que eu esperava."

    ivo "Foi você quem abriu a caixa?"

    ariane "Eu impedi que a guarda chegasse primeiro."
    ariane "A caixa abriu porque reconheceu você."

    if opened_crate_willingly:
        ariane "E porque você não hesitou."
    elif resisted_crate:
        ariane "Mesmo quando tentou recusar."
    else:
        ariane "Mesmo quando tentou dividir a decisão com outra pessoa."

    ivo "Quem é você?"

    ariane "Ariane. Mensageira quando preciso ser respeitável."
    ariane "Ladra quando preciso ser honesta."

    "Ela olhou para a marca, e o sarcasmo desapareceu de seu rosto."

    ariane "Você carrega o Selo das Moiras. Isso deveria ser impossível."
    ariane "O último homem marcado desapareceu vinte anos atrás."

    menu:
        "O que Ivo quer de Ariane?":

        "A verdade, mesmo que seja perigosa.":
            $ ariane_affinity += 2
            $ ivo_honesty += 1
            $ asked_ariane_for_truth = True
            ivo "Não quero proteção. Quero saber o que aconteceu comigo."
            ariane "Então comece aceitando que algumas respostas vão tentar usar você."

        "Ajuda para impedir que outros sejam feridos.":
            $ ariane_affinity += 2
            $ ivo_compassion += 1
            $ asked_ariane_for_help = True
            ivo "Se a guarda procura isso, alguém mais pode se machucar."
            ariane "Você acabou de sobreviver ao mar e já está preocupado com desconhecidos."
            ariane "Isso é admirável ou muito inconveniente."

        "Uma explicação que não comece com profecias.":
            $ ariane_affinity += 1
            $ ivo_humor += 2
            ivo "Tente explicar sem usar destino, sangue antigo ou 'você foi escolhido'."
            show ariane embarrassed at portrait_right
            ariane "Vou tentar limitar a tragédia a duas dessas opções."

    show ariane neutral at portrait_right

    collector "Afaste-se dele, Ariane."

    "O Coletor surgiu na entrada do cais com dois homens armados."
    "Seu uniforme não trazia o símbolo da cidade, apenas um círculo negro atravessado por seis riscos."

    collector "Entregue a moeda e a garota."
    collector "O estrangeiro ainda pode sair daqui sem nome em uma lista."

    ariane "Ele já estava em uma lista antes de chegar."

    menu:
        "Como Ivo reage ao ultimato?":

        "Confiar no plano de Ariane.":
            $ trusted_ariane = True
            $ ariane_affinity += 2
            ariane "Quando eu disser agora, pule para o barco abaixo."
            ivo "Existe um barco abaixo?"
            ariane "Essa dúvida é sua última chance de voltar atrás."
            "Ariane cortou uma amarra. Uma vela despencou entre eles e os homens do Coletor."
            "Ivo saltou quando ela gritou e encontrou o convés um instante antes da água."

        "Assumir a culpa para proteger Ariane.":
            $ protected_ariane = True
            $ ariane_affinity += 2
            $ ivo_courage += 2
            ivo "A moeda me escolheu. Ela só tentou impedir que vocês a roubassem."
            ariane "Você não sabe nem quem eu sou."
            ivo "Então considere um investimento em respostas."
            "O Coletor voltou a arma para Ivo."
            "Ariane usou o segundo roubado para derrubar ânforas, agarrar sua mão e arrastá-lo por uma passagem lateral."

        "Usar Pólemon como distração.":
            $ blamed_polemon = True
            $ ivo_humor += 1
            $ ivo_courage += 1
            ivo "Chegou tarde. Pólemon já vendeu a relíquia para alguém no mercado."
            collector "Pólemon não tocaria em algo que canta."
            ivo "Então você o conhece melhor do que deveria."
            "O olhar do Coletor vacilou."
            ariane "Blefe perigoso."
            ivo "Funcionou?"
            ariane "Pergunte enquanto corre."
            $ ariane_affinity += 1

    hide ariane

    "A passagem terminava em uma porta de ferro sob o cais."
    "Ariane abriu três fechaduras sem diminuir o passo."

    ariane "A moeda veio da Cisterna Esquecida."
    ariane "Se existe uma resposta, está lá embaixo."
    ariane "Se existe uma armadilha, também."

    scene bg cisterna
    with fade
    play music "audio/music/cistern_forgotten_echoes.wav" fadeout 1.0 fadein 1.5

    "A Cisterna Esquecida não parecia construída."
    "Parecia lembrada."

    "Colunas surgiam da água escura. Símbolos azuis pulsavam nas paredes como veias."
    "Diante de uma porta de bronze, três fragmentos luminosos flutuavam sobre pedestais."

    show ariane neutral at portrait_right

    ariane "Ecos de Atlântida."
    ariane "Memórias arrancadas de pessoas que morreram sem conseguir esquecê-las."

    ivo "E precisamos tocar neles."

    ariane "Precisamos é uma palavra otimista."

    "O primeiro Eco mostrou o naufrágio por outro ângulo."
    "Nas profundezas, uma figura segurava Ivo enquanto o navio desaparecia acima."

    voice "O portador voltou."

    menu:
        "Ivo mantém contato com a lembrança?":

        "Ouvir até o fim.":
            $ listened_to_echoes += 1
            $ ivo_courage += 1
            "A figura abriu os olhos."
            "Eram os olhos de Ivo, muitos anos mais velhos."
            voice "Não confie no trono vazio."

        "Romper o contato antes que a visão o reconheça.":
            $ ivo_honesty += 1
            $ refused_first_echo = True
            "Ivo soltou o fragmento."
            "A visão continuou por um segundo dentro de sua própria sombra."

    "O segundo Eco revelou seis mãos sobre uma mesa de pedra."
    "Cada pulso carregava um símbolo diferente."
    "Uma delas usava a mesma fita vermelha amarrada no braço de Ariane."

    voice "Seis juramentos. Seis herdeiras. Nenhuma rainha."

    menu:
        "O que Ivo conta a Ariane?":

        "Tudo, inclusive que ela é uma das seis.":
            $ listened_to_echoes += 1
            $ told_ariane_everything = True
            $ ariane_affinity += 2
            $ ivo_honesty += 1
            ivo "Uma das mãos era sua. A fita, a cicatriz no dedo... você é uma das seis."
            ariane "Não."
            ivo "Você reconheceu a mesa."
            ariane "Reconheci uma história usada para condenar minha família."
            ivo "Então me conte antes que outra pessoa conte por você."

        "Dizer apenas que existem seis herdeiras.":
            $ hid_heirs_from_ariane = True
            $ ivo_courage += 1
            ivo "Falou de seis herdeiras e de um trono vazio."
            ariane "Você omitiu alguma coisa."
            ivo "Ainda estou decidindo se era memória ou isca."
            $ ariane_affinity -= 1

    "O terceiro Eco mostrou a porta aberta."
    "Do outro lado, Kallípolis estava submersa."
    "Ariane permanecia diante da água, sozinha, enquanto uma voz ordenava que ela escolhesse quem salvar."

    show ariane embarrassed at portrait_right
    ariane "O que você viu?"

    menu:
        "Como Ivo responde?":

        "Contar a visão e prometer que ela não estará sozinha.":
            $ promised_ariane = True
            $ ariane_affinity += 2
            $ ivo_compassion += 2
            ivo "Vi você diante desta porta, escolhendo sozinha quem viveria."
            ivo "Não sei impedir uma profecia. Mas sei dividir uma escolha."
            ariane "Promessas feitas a pessoas que você acabou de conhecer são perigosas."
            ivo "Então não trate como promessa. Trate como plano."

        "Contar apenas o perigo imediato.":
            $ warned_ariane = True
            $ ariane_affinity += 1
            $ ivo_honesty += 1
            ivo "A porta mostrou Kallípolis sob a água. Não devemos abri-la sem saber como fechar."
            ariane "Cautela. Finalmente algo sensato em você."

        "Esconder a visão para não assustá-la.":
            $ hid_third_echo = True
            $ ivo_compassion += 1
            ivo "Vi a cidade. Nada que ajude agora."
            ariane "Você mente olhando para a direita."
            $ ariane_affinity -= 1

    show ariane neutral at portrait_right

    "Os três Ecos se encaixaram nos círculos da porta."
    "O bronze não se abriu."
    "Em vez disso, a Marca das Moiras projetou um mapa sobre a água."

    "Uma rota ligava Kallípolis a Nereu."
    "No centro do mapa havia o mesmo símbolo negro usado pelo Coletor."

    voice "A herdeira das marés guarda a primeira chave."
    voice "O portador deve encontrá-la antes dos Coletores."

    ariane "Nereu."
    ariane "Se o Conselho de lá souber que a Marca voltou, fechará os portos e prenderá qualquer pessoa ligada a você."

    ivo "Incluindo você."

    ariane "Principalmente eu."

    if told_ariane_everything:
        ariane "Você me contou o que viu mesmo quando isso podia me afastar."
        ariane "Vou levá-lo até Nereu."
    elif trusted_ariane or protected_ariane:
        ariane "Você confiou em mim quando tinha poucos motivos."
        ariane "Vou retribuir levando você até Nereu."
    elif ariane_affinity >= 3:
        ariane "Ainda não decidi se você é corajoso ou apenas desorientado."
        ariane "Descobrirei no caminho para Nereu."
    else:
        ariane "Não confio em você."
        ariane "Mas confio menos ainda em quem enviou o Coletor."
        ariane "Por enquanto, isso basta."

    hide ariane

    "Eles deixaram a Cisterna antes do amanhecer."
    "Pólemon providenciou um barco sem fazer perguntas — talvez porque Ivo já tivesse respondido demais."

    if blamed_polemon:
        "Antes de soltarem as amarras, Pólemon entregou a Ivo uma bolsa vazia."
        polemon "Para guardar o pagamento que você não receberá depois de usar meu nome como isca."
        ivo "Então estamos quites?"
        polemon "Nem de longe."

    scene bg nereu
    with fade
    play music "audio/music/nereu_blue_sails.wav" fadeout 1.0 fadein 1.5

    centered "{size=52}NEREU{/size}\n{size=30}A cidade das velas azuis{/size}"

    "Nereu surgiu do mar como se Atlântida tivesse se recusado a afundar por completo."
    "Canais atravessavam avenidas de mármore. Velas azuis escondiam arqueiros nas muralhas."
    "No porto, soldados revistavam passageiros antes mesmo que os barcos tocassem o cais."

    ariane "Não mostre a marca."
    ariane "E, se alguém perguntar, você é meu assistente."

    ivo "Assistente de quê?"

    ariane "Ainda estou escolhendo uma profissão respeitável."

    "Uma mulher de uniforme azul aguardava no fim da passarela."
    "Ela não olhou para Ariane."
    "Olhou diretamente para o pulso coberto de Ivo."

    show nerissa neutral at portrait_enter_left

    nerissa "Capitã Nerissa Vael, guarda das marés de Nereu."
    nerissa "O Conselho recebeu notícias de um naufrágio, uma relíquia roubada e um estrangeiro que sobreviveu ao impossível."

    ariane "As notícias viajam rápido."

    nerissa "Mentiras viajam rápido."
    nerissa "Verdades chegam antes."

    nerissa "Diga-me, Ivo: por que a cidade deveria permitir sua entrada?"

    menu:
        "A primeira resposta a Nerissa:":

        "Porque o mesmo inimigo está procurando nós dois.":
            $ nerissa_question = "inimigo"
            $ nerissa_affinity += 2
            $ ivo_honesty += 1
            ivo "O Coletor carregava um símbolo ligado a Nereu. Se ele procura a Marca, seu problema já chegou antes de mim."
            nerissa "Você negocia informação como alguém que aprendeu rápido."

        "Porque preciso encontrar a herdeira das marés.":
            $ nerissa_question = "herdeira"
            $ nerissa_affinity += 1
            $ ivo_courage += 1
            ivo "Uma memória me enviou até a herdeira das marés."
            nerissa "Então começamos com blasfêmia pública."
            nerissa "É uma entrada memorável."

        "Porque não sei em quem confiar — e prefiro admitir isso.":
            $ nerissa_question = "incerteza"
            $ nerissa_affinity += 2
            $ ivo_honesty += 2
            ivo "Não sei quem me marcou, quem enviou o Coletor ou por que seu Conselho sabia que eu viria."
            ivo "Mas fingir certeza agora seria entregar vantagem a todos eles."
            nerissa "Uma resposta rara em Nereu."

    show nerissa neutral at portrait_left

    if promised_ariane:
        nerissa "E você, Ariane? Já está fazendo promessas a náufragos?"
        ariane "Só as que pretendo cobrar."
    elif hid_heirs_from_ariane or hid_third_echo:
        nerissa "Há algo que vocês não contaram um ao outro."
        nerissa "Excelente. A cidade aprecia relações construídas sobre fundações instáveis."
    else:
        nerissa "Vocês chegaram juntos. Isso não significa que sairão daqui do mesmo lado."

    nerissa "Podem entrar."
    nerissa "Mas não confundam permissão com liberdade."

    "Quando Nerissa se virou, a moeda sob a roupa de Ivo respondeu à presença dela."
    "Por um instante, um segundo símbolo brilhou sob a luva da capitã."

    thoughts "A herdeira das marés não estava escondida em Nereu."
    thoughts "Ela havia acabado de permitir sua entrada."

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

    centered "{size=56}FIM DO PRÓLOGO{/size}\n\n{size=32}Duas herdeiras cruzaram o caminho da Marca.{/size}"

    "Perfil de Ivo: [trait]."
    "Vínculo com Ariane: [main_bond]."
    "Primeira impressão de Nerissa: [second_bond]."

    if told_ariane_everything and promised_ariane:
        "Ivo e Ariane chegaram a Nereu ligados por uma verdade compartilhada e uma promessa que nenhum dos dois considera pequena."
    elif trusted_ariane or protected_ariane:
        "Ariane ainda guarda segredos, mas agora reconhece Ivo como alguém capaz de caminhar ao seu lado."
    elif ariane_affinity >= 3:
        "A curiosidade venceu a desconfiança. Ariane decidiu permanecer por perto."
    else:
        "Ariane o acompanha por necessidade. Uma única mentira poderá separá-los."

    if nerissa_affinity >= 2:
        "Nerissa percebeu que Ivo pode ser útil — ou perigoso demais para perder de vista."
    else:
        "Nerissa permitiu sua entrada, mas colocou olhos do Conselho em cada passo do estrangeiro."

    if opened_crate_willingly:
        "Ivo escolheu tocar o desconhecido antes que o desconhecido escolhesse por ele."
    elif resisted_crate:
        "Ivo tentou honrar sua palavra, mesmo quando a relíquia recusou sua decisão."
    else:
        "Ivo procurou dividir o peso da escolha, mas a Marca o encontrou assim mesmo."

    "Continua no Capítulo 1 — As Velas Azuis de Nereu."

    jump prologue_summary_menu


label prologue_summary_menu:
    menu:
        "O que deseja fazer?":

        "Ver os vínculos":
            call screen relationships(close_action=Return())
            jump prologue_summary_menu

        "Recomeçar o prólogo":
            jump prologue_start

        "Voltar ao menu principal":
            return
