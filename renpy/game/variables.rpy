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
default unlocked_gallery = ["Ariane", "Nerissa"]

init python:
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
        global nerissa_question, prologue_completed, chapter_01_completed, chapter_02_completed, chapter_03_completed, chapter_04_completed, chapter_05_completed, chapter_06_completed, chapter_07_completed, chapter_08_completed, chapter_09_completed, chapter_10_completed, chapter_11_completed, chapter_12_completed, chapter_13_completed, chapter_14_completed
        global nereu_lead, trusted_nerissa_with_coin, protected_ariane_in_nereu
        global heard_melia_name, asterion_choice, lyria_choice, akris_choice, nix_choice
        global trusted_lyra_song, protected_mikon, trusted_thalia_with_map, saved_akris_scouts
        global trusted_cassia_vision, kept_future_secret, first_arc_completed, assembly_choice, arc_2_priority, trusted_polemon_again
        global nereu_decision, trusted_nerissa_command, asterion_response, trusted_melia_seed, lyria_response, trusted_lyra_leadership
        global akris_siege_choice, trusted_thalia_council, mirror_choice, trusted_cassia_truth, abyss_choice, saved_herdades_at_abyss, oryx_choice, faced_future_ivo

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
