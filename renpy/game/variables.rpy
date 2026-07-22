default ariane_affinity = 0
default nerissa_affinity = 0
default melia_affinity = 0
default lyra_affinity = 0
default thalia_affinity = 0
default cassia_affinity = 0

default ivo_courage = 0
default ivo_honesty = 0
default ivo_humor = 0
default ivo_compassion = 0

default prologue_priority = ""
default lysandra_trust = 0
default polemon_respect = 0
default knows_mark_is_dangerous = False
default accepted_for_answers = False
default accepted_to_protect = False

default opened_crate_willingly = False
default resisted_crate = False
default sought_help = False

default asked_ariane_for_truth = False
default asked_ariane_for_help = False
default trusted_ariane = False
default protected_ariane = False
default blamed_polemon = False

default listened_to_echoes = 0
default refused_first_echo = False
default told_ariane_everything = False
default hid_heirs_from_ariane = False
default promised_ariane = False
default warned_ariane = False
default hid_third_echo = False

default nerissa_question = ""
default prologue_completed = False
default chapter_01_completed = False
default chapter_02_completed = False
default chapter_03_completed = False
default chapter_04_completed = False
default chapter_05_completed = False
default chapter_06_completed = False
default chapter_07_completed = False
default chapter_08_completed = False
default chapter_09_completed = False
default chapter_10_completed = False
default chapter_11_completed = False
default chapter_12_completed = False
default chapter_13_completed = False
default chapter_14_completed = False
default chapter_15_completed = False
default nereu_lead = ""
default asterion_choice = ""
default lyria_choice = ""
default akris_choice = ""
default nix_choice = ""
default trusted_nerissa_with_coin = False
default protected_ariane_in_nereu = False
default heard_melia_name = False
default trusted_lyra_song = False
default protected_mikon = False
default trusted_thalia_with_map = False
default saved_akris_scouts = False
default trusted_cassia_vision = False
default kept_future_secret = False
default first_arc_completed = False
default assembly_choice = ""
default arc_2_priority = ""
default trusted_polemon_again = False
default nereu_decision = ""
default trusted_nerissa_command = False
default asterion_response = ""
default trusted_melia_seed = False
default lyria_response = ""
default trusted_lyra_leadership = False
default akris_siege_choice = ""
default trusted_thalia_council = False
default mirror_choice = ""
default trusted_cassia_truth = False
default abyss_choice = ""
default saved_herdades_at_abyss = False
default oryx_choice = ""
default faced_future_ivo = False
default ending_route = ""
default ending_choice_complete = False
default ivo_integrity = 0
default broken_oath = False
default ariane_crisis = ""
default nerissa_crisis = ""
default melia_crisis = ""
default lyra_crisis = ""
default thalia_crisis = ""
default cassia_crisis = ""
default unlocked_gallery = ["Ariane", "Nerissa"]
default unlocked_cgs = []
default combat_focus = 0
default combat_focus_limit = 3
default combat_enemy = 0
default combat_companion = ""
default combat_result = ""
default combat_style = "base"
default combat_phase = ""
default combat_action_labels = []
default combat_action_texts = []

init python:
    def combat_profile_for(style):
        profiles = {
            "naval": {
                "labels": ["Ler as correntes — abrir uma rota sem expor os civis.", "Desafinar o sino — atingir o encanto na fonte.", "Segurar o convés — cobrir Nerissa enquanto ela manobra."],
                "texts": ["Ivo segue a corrente menor e transforma pânico em passagem. A cidade vê uma saída que não exige sacrificar ninguém.", "A Marca encontra a vibração falsa no bronze. O golpe é preciso, mas cobra foco demais.", "Ivo toma a posição exposta e Nerissa ganha segundos para guiar o barco para fora da linha de fogo."],
            },
            "roots": {
                "labels": ["Acalmar a seiva — separar memória de sentença.", "Cortar o nó de bronze — atacar o sino na raiz.", "Proteger as mudas — dar tempo para Mélia replantar."],
                "texts": ["Ivo nomeia as lembranças em vez de expulsá-las. A seiva perde a necessidade de apertar quem sofre.", "A Marca encontra o bronze escondido dentro da raiz. O corte é eficaz, mas deixa o pulso de Ivo em brasa.", "Ivo segura as raízes que avançam enquanto Mélia transforma perigo em novas mudas."],
            },
            "song": {
                "labels": ["Ouvir o contraponto — encontrar as vozes apagadas.", "Quebrar o compasso — atingir o ritmo dos sinos.", "Abrir espaço para Lyra — proteger uma nota sem dono."],
                "texts": ["Ivo escuta as pausas entre os sinos; nelas, as vozes da praça voltam a existir.", "A Marca quebra o ritmo imposto ao templo. Funciona, mas quase deixa Ivo sem fôlego.", "Ivo sustenta o silêncio necessário para que Lyra escolha a própria nota, sem comando nem permissão."],
            },
            "fortress": {
                "labels": ["Redistribuir a linha — dar uma função a cada vigia.", "Abrir a brecha — desmontar o padrão dos arautos.", "Ficar no portão — proteger Thalia e os refugiados."],
                "texts": ["Ivo transforma soldados e civis em uma linha que protege sem fechar a cidade.", "A Marca localiza a falha na formação de bronze. O esforço deixa o campo aberto por um instante.", "Ivo fica entre a névoa e o portão; Thalia pode escolher uma rota sem abandonar quem chegou tarde."],
            },
            "stars": {
                "labels": ["Fixar o presente — separar previsão de destino.", "Rasgar a repetição — atingir o gesto da máscara.", "Cobrir Cássia — guardar tempo para ela recalcular."],
                "texts": ["Ivo recusa a imagem mais fácil do futuro. A previsão se torna apenas uma possibilidade entre muitas.", "A Marca corta o padrão que a máscara repete. É rápido e perigoso, como enfrentar a própria sombra.", "Ivo impede que o fragmento alcance Cássia enquanto ela encontra a única linha de futuro que não exige uma vítima."],
            },
            "final": {
                "labels": ["Unir os fios — reafirmar que ninguém carrega o juramento sozinho.", "Expor a mentira — atacar a regra que exige uma vítima.", "Guardar uma cadeira — proteger o elo mais abalado do grupo."],
                "texts": ["Ivo chama cada herdeira pelo que ela escolheu ser. Os fios se unem sem se amarrar uns aos outros.", "A Marca alcança a regra escondida na cadeira: eficiência não é justiça. O impacto cobra um preço.", "Ivo recusa deixar o elo mais frágil virar custo do grupo. A cadeira perde uma peça que achava garantida."],
            },
            "base": {
                "labels": ["Ancorar o grupo — reduzir a pressão sem ferir ninguém.", "Ler a abertura — atacar o mecanismo por trás da ameaça.", "Proteger a companheira — trocar vantagem por segurança."],
                "texts": ["Ivo recusa o ritmo que o inimigo impõe. A linha de defesa se fecha como promessa de que ninguém será deixado para trás.", "A Marca encontra o ponto onde o medo foi transformado em ordem. O golpe funciona, mas cobra concentração demais.", "Ivo escolhe a posição mais difícil e abre espaço para a companheira respirar. A formação não perde ninguém."],
            },
        }
        return profiles.get(style, profiles["base"])

    def bond_rank(points):
        if points >= 7:
            return "Laço profundo"
        if points >= 5:
            return "Confiança"
        if points >= 3:
            return "Interesse"
        if points >= 1:
            return "Primeira impressão"
        if points < 0:
            return "Desconfiança"
        return "Desconhecida"

    def dominant_trait():
        values = {
            "Coragem": ivo_courage,
            "Honestidade": ivo_honesty,
            "Humor": ivo_humor,
            "Compaixão": ivo_compassion,
        }

        highest = max(values.values())
        leaders = [name for name, score in values.items() if score == highest]

        if highest <= 0:
            return "Indefinido"
        if len(leaders) == 1:
            return leaders[0]
        if len(leaders) == 2:
            return "{} e {}".format(leaders[0], leaders[1])
        return ", ".join(leaders[:-1]) + " e " + leaders[-1]

    def integrity_rank(value):
        if value <= -2:
            return "Promessas quebradas"
        if value == -1:
            return "Confiança abalada"
        return "Palavra preservada"

    def legacy_score():
        positive = [
            told_ariane_everything, trusted_nerissa_with_coin, trusted_lyra_song,
            protected_mikon, saved_akris_scouts, trusted_thalia_with_map,
            trusted_cassia_vision, trusted_cassia_truth, trusted_polemon_again,
            trusted_nerissa_command, trusted_melia_seed, trusted_lyra_leadership,
            trusted_thalia_council, saved_herdades_at_abyss, faced_future_ivo,
        ]
        negative = [hid_heirs_from_ariane, hid_third_echo, blamed_polemon, kept_future_secret]
        return sum(1 for flag in positive if flag) - sum(1 for flag in negative if flag)

    def legacy_rank(score):
        if score >= 8:
            return "Aliança conquistada"
        if score <= 2:
            return "Aliança frágil"
        return "Aliança em construção"

    def crisis_break_count():
        crises = [ariane_crisis, nerissa_crisis, melia_crisis, lyra_crisis, thalia_crisis, cassia_crisis]
        return sum(1 for crisis in crises if crisis == "broken")

    def reset_prologue_state():
        global ariane_affinity, nerissa_affinity
        global ivo_courage, ivo_honesty, ivo_humor, ivo_compassion
        global prologue_priority, lysandra_trust, polemon_respect
        global knows_mark_is_dangerous, accepted_for_answers, accepted_to_protect
        global opened_crate_willingly, resisted_crate, sought_help
        global asked_ariane_for_truth, asked_ariane_for_help
        global trusted_ariane, protected_ariane, blamed_polemon
        global listened_to_echoes, refused_first_echo
        global told_ariane_everything, hid_heirs_from_ariane
        global promised_ariane, warned_ariane, hid_third_echo
        global nerissa_question, prologue_completed, chapter_01_completed, chapter_02_completed, chapter_03_completed, chapter_04_completed, chapter_05_completed, chapter_06_completed, chapter_07_completed, chapter_08_completed, chapter_09_completed, chapter_10_completed, chapter_11_completed, chapter_12_completed, chapter_13_completed, chapter_14_completed, chapter_15_completed
        global nereu_lead, trusted_nerissa_with_coin, protected_ariane_in_nereu
        global heard_melia_name, asterion_choice, lyria_choice, akris_choice, nix_choice
        global trusted_lyra_song, protected_mikon, trusted_thalia_with_map, saved_akris_scouts
        global trusted_cassia_vision, kept_future_secret, first_arc_completed, assembly_choice, arc_2_priority, trusted_polemon_again
        global nereu_decision, trusted_nerissa_command, asterion_response, trusted_melia_seed, lyria_response, trusted_lyra_leadership
        global akris_siege_choice, trusted_thalia_council, mirror_choice, trusted_cassia_truth, abyss_choice, saved_herdades_at_abyss, oryx_choice, faced_future_ivo
        global ending_route, ending_choice_complete, ivo_integrity, broken_oath, unlocked_cgs
        global ariane_crisis, nerissa_crisis, melia_crisis, lyra_crisis, thalia_crisis, cassia_crisis

        ariane_affinity = 0
        nerissa_affinity = 0

        ivo_courage = 0
        ivo_honesty = 0
        ivo_humor = 0
        ivo_compassion = 0

        prologue_priority = ""
        lysandra_trust = 0
        polemon_respect = 0
        knows_mark_is_dangerous = False
        accepted_for_answers = False
        accepted_to_protect = False

        opened_crate_willingly = False
        resisted_crate = False
        sought_help = False

        asked_ariane_for_truth = False
        asked_ariane_for_help = False
        trusted_ariane = False
        protected_ariane = False
        blamed_polemon = False

        listened_to_echoes = 0
        refused_first_echo = False
        told_ariane_everything = False
        hid_heirs_from_ariane = False
        promised_ariane = False
        warned_ariane = False
        hid_third_echo = False

        nerissa_question = ""
        prologue_completed = False
        chapter_01_completed = False
        chapter_02_completed = False
        chapter_03_completed = False
        chapter_04_completed = False
        chapter_05_completed = False
        chapter_06_completed = False
        chapter_07_completed = False
        chapter_08_completed = False
        chapter_09_completed = False
        chapter_10_completed = False
        chapter_11_completed = False
        chapter_12_completed = False
        chapter_13_completed = False
        chapter_14_completed = False
        chapter_15_completed = False
        nereu_lead = ""
        asterion_choice = ""
        lyria_choice = ""
        akris_choice = ""
        nix_choice = ""
        trusted_nerissa_with_coin = False
        protected_ariane_in_nereu = False
        heard_melia_name = False
        trusted_lyra_song = False
        protected_mikon = False
        trusted_thalia_with_map = False
        saved_akris_scouts = False
        trusted_cassia_vision = False
        kept_future_secret = False
        first_arc_completed = False
        assembly_choice = ""
        arc_2_priority = ""
        trusted_polemon_again = False
        nereu_decision = ""
        trusted_nerissa_command = False
        asterion_response = ""
        trusted_melia_seed = False
        lyria_response = ""
        trusted_lyra_leadership = False
        akris_siege_choice = ""
        trusted_thalia_council = False
        mirror_choice = ""
        trusted_cassia_truth = False
        abyss_choice = ""
        saved_herdades_at_abyss = False
        oryx_choice = ""
        faced_future_ivo = False
        ending_route = ""
        ending_choice_complete = False
        ivo_integrity = 0
        broken_oath = False
        ariane_crisis = ""
        nerissa_crisis = ""
        melia_crisis = ""
        lyra_crisis = ""
        thalia_crisis = ""
        cassia_crisis = ""
        unlocked_cgs = []
