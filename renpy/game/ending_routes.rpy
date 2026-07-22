# Epílogos da primeira temporada. As rotas românticas exigem vínculo alto;
# nenhuma delas é tratada como prêmio automático pelo fim da aventura.

label ending_single_menu:
    scene bg title
    with fade

    "Uma escolha não apaga os demais laços. Ela apenas diz qual deles Ivo quer cuidar de outro modo."

    menu:
        "Com quem Ivo quer construir um futuro?"

        "Ariane — uma chama escolhida com calma." if ariane_affinity >= 7:
            $ ending_route = "Ariane"
            jump ending_ariane

        "Nerissa — uma maré que não precisa mandar." if nerissa_affinity >= 7:
            $ ending_route = "Nerissa"
            jump ending_nerissa

        "Mélia — uma raiz que aprende a pedir." if melia_affinity >= 7:
            $ ending_route = "Mélia"
            jump ending_melia

        "Lyra — uma canção que não exige silêncio." if lyra_affinity >= 7:
            $ ending_route = "Lyra"
            jump ending_lyra

        "Thalia — uma porta aberta sem máscara." if thalia_affinity >= 7:
            $ ending_route = "Thalia"
            jump ending_thalia

        "Cássia — um amanhã que não precisa ser calculado." if cassia_affinity >= 7:
            $ ending_route = "Cássia"
            jump ending_cassia

        "Voltar":
            jump ending_selector


label ending_ariane:
    scene bg kallipolis
    with dissolve

    if "Ariane — Varanda" not in unlocked_cgs:
        $ unlocked_cgs.append("Ariane — Varanda")

    scene cg ariane_balcony
    with dissolve

    "Um ano depois, a praça de Kallípolis tinha crianças correndo ao redor da fonte e uma nova placa na porta da antiga pensão: CASA DAS CHEGADAS."

    ariane "Não é uma homenagem a você. Antes que a sua cabeça faça isso virar uma lenda."
    ivo "Eu estava só pensando que você mandou gravar as letras bem grandes."
    ariane "Para pessoas perdidas lerem de longe. Você sabe como são as pessoas perdidas."
    "Ela tenta disfarçar o sorriso; falha com a mesma elegância com que falhara em disfarçar o medo na primeira noite."
    ivo "Ariane, eu não quero que você seja a razão de eu ficar. Quero que seja alguém que eu escolho todos os dias."
    ariane "Então escolha direito. E me deixe escolher também."
    "Eles seguem pela praça, sem profecia e sem testemunhas. Apenas com a promessa menos grandiosa — e mais difícil — que os dois poderiam fazer: voltar um para o outro amanhã."
    jump ending_credits


label ending_nerissa:
    scene bg nereu
    with dissolve
    show nerissa embarrassed at portrait_left
    show ivo neutral at portrait_bust_right

    "Nereu amanhecia com o cheiro de sal e de pão recém-assado. Nerissa tinha trocado o antigo gabinete de comando por uma sala com janelas abertas para o cais."

    nerissa "O conselho ainda espera que eu dê ordens mais depressa."
    ivo "E você?"
    nerissa "Eu espero ouvir antes de falar. Às vezes é insuportavelmente lento."
    ivo "Posso sentar aqui enquanto você pratica?"
    "Nerissa olha o mar. A mão dela encontra a de Ivo sobre a mesa, sem puxá-lo, sem decidir por ele."
    nerissa "Só se você me disser quando eu estiver confundindo cuidado com controle."
    ivo "Só se você me disser quando eu estiver confundindo medo com prudência."
    "A primeira embarcação da manhã parte. Nenhum dos dois a comanda. Ainda assim, os dois ficam."
    jump ending_credits


label ending_melia:
    scene bg asterion
    with dissolve
    show melia embarrassed at portrait_left
    show ivo neutral at portrait_bust_right

    "Em Asterion, a primeira horta plantada depois do cerco ocupava o lugar onde antes havia uma trincheira. Mélia se ajoelha na terra com as mãos sujas de verde."

    melia "Esta semente só abre depois da primeira chuva. Não adianta mandar."
    ivo "Parece que ela aprendeu com você."
    melia "Ou eu com ela."
    "Ela ergue os olhos, vulnerável sem pedir desculpas por isso."
    melia "Eu passei tempo demais achando que precisar de alguém era o mesmo que usar alguém. Com você... eu quero aprender a diferença."
    ivo "A diferença é que eu posso dizer sim. E também posso dizer não."
    melia "Então fica porque quer. Hoje basta."
    "Quando a chuva chega, os dois correm para cobrir as mudas e riem da inutilidade do gesto. Algumas coisas precisam molhar para crescer."
    jump ending_credits


label ending_lyra:
    scene bg lyria_temple
    with dissolve
    show lyra embarrassed at portrait_left
    show ivo neutral at portrait_bust_right

    "O templo de Lýria não guardava mais silêncio obrigatório. Em suas escadarias, crianças desafinavam coros inteiros com uma liberdade quase sagrada."

    lyra "Eles erram o refrão de propósito. Dizem que é para ver se eu presto atenção."
    ivo "E você presta?"
    lyra "Em tudo. Talvez esse seja o problema."
    "Lyra abre um pequeno caderno. Nele, a primeira canção que compôs sem consultar nenhuma memória do passado."
    lyra "Não fala sobre destino. Fala sobre duas pessoas que aprendem a não interromper uma à outra."
    ivo "Posso ouvir?"
    lyra "Pode. Mas não precisa entender tudo."
    "A melodia vem baixa, imperfeita e viva. No fim, Ivo não aplaude de imediato; apenas segura a mão dela, para que a música tenha onde pousar."
    jump ending_credits


label ending_thalia:
    scene bg akris_fortress
    with dissolve
    show thalia embarrassed at portrait_left
    show ivo neutral at portrait_bust_right

    "Em Akris, o portão que antes fechava ao cair da noite agora permanecia aberto durante as horas do mercado. Thalia ainda inspecionava as dobradiças toda manhã."

    thalia "Portões abertos exigem guardas melhores. Não gente menos cuidadosa."
    ivo "Você está explicando ou se defendendo?"
    thalia "Os dois. E não gosto que você perceba."
    "Ela tira a máscara de combate e a pendura num gancho, com uma solenidade que não consegue esconder o nervosismo."
    thalia "Sem ela, eu não sei muito bem o que fazer com a cara."
    ivo "Pode começar deixando que eu veja."
    "Thalia respira fundo, depois ri — curto, surpresa, verdadeiro."
    thalia "Não me faça prometer que vou ficar fácil."
    ivo "Não. Só que vai ficar honesta."
    "Eles atravessam o portão lado a lado, não como uma vitória, mas como uma passagem escolhida."
    jump ending_credits


label ending_cassia:
    scene bg nix_observatory
    with dissolve

    if "Cássia — Estrelas" not in unlocked_cgs:
        $ unlocked_cgs.append("Cássia — Estrelas")

    scene cg cassia_stars
    with dissolve

    "Na torre de Nix, Cássia tinha transformado a antiga sala de previsões em uma oficina para mapas incompletos. Havia estrelas nas paredes e espaços em branco deliberados entre elas."

    cassia "Descobri que as lacunas são mais honestas do que os números."
    ivo "Vindo de você, isso é quase uma revolução."
    cassia "É uma revolução pequena. As que sobrevivem costumam ser."
    "Ela fecha um livro que, antes, teria lido até encontrar uma resposta confortável."
    cassia "Não sei o que acontecerá conosco daqui a dez anos."
    ivo "Nem eu."
    cassia "E ainda assim você está aqui."
    ivo "Porque hoje eu quero estar."
    "Cássia guarda o livro e oferece a mão. Pela primeira vez, ela não chama aquilo de previsão. Chama de encontro."
    jump ending_credits


label ending_collective:
    scene bg sunken_hall
    with dissolve
    show ariane neutral at portrait_left
    show nerissa neutral at portrait_right
    show ivo neutral at portrait_bust_center

    "O salão não tinha voltado a ser uma corte. Tinha virado uma casa de decisões — com portas, horários e a possibilidade real de dizer não."
    "Ariane, Nerissa, Mélia, Lyra, Thalia e Cássia não chegavam ali por terem sido conquistadas. Chegavam porque cada uma tinha escolhido, repetidas vezes, confiar."
    ariane "Uma relação não resolve as diferenças entre nós."
    nerissa "Nem dá a ninguém o direito de falar por outra pessoa."
    ivo "Então só existe se todo mundo puder mudar de ideia."
    "As seis trocam olhares. Não há juramento mágico, nem posse escondida sob palavras bonitas. Há conversas difíceis, ciúmes que precisam ser nomeados, e uma vontade coletiva de aprender."
    "O vínculo entre eles não é um prêmio pelo fim da jornada. É uma nova jornada, escolhida devagar."
    jump ending_credits


label ending_alliance:
    scene bg kallipolis
    with dissolve
    show ivo neutral at portrait_bust_center

    "Ivo permaneceu em Kallípolis, mas não escolheu transformar nenhum dos vínculos em romance."
    "Ariane abriu a Casa das Chegadas; Nerissa renovou os pactos marítimos; Mélia plantou jardins em cidades feridas; Lyra ensinou canções novas; Thalia manteve os portões abertos; Cássia desenhou mapas que admitiam o desconhecido."
    "Eles continuaram próximos, não por falta de coragem para amar, mas por respeito ao momento em que cada um estava."
    ivo "Nem toda história precisa terminar com alguém pertencendo a alguém."
    "Dessa vez, o mar não discordou."
    jump ending_credits


label ending_credits:
    scene bg title
    with fade
    stop music fadeout 2.0

    centered "{size=58}FIM DA PRIMEIRA TEMPORADA{/size}\n\n{size=30}Rota escolhida: [ending_route].\n\nAs escolhas permanecem. O mar também.{/size}"

    $ ending_choice_complete = True
    return
