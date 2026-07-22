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
        global nerissa_question, prologue_completed

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
