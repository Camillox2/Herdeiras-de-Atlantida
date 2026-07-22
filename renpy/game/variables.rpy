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
        store.ariane_affinity = 0
        store.nerissa_affinity = 0

        store.ivo_courage = 0
        store.ivo_honesty = 0
        store.ivo_humor = 0
        store.ivo_compassion = 0

        store.prologue_priority = ""
        store.lysandra_trust = 0
        store.polemon_respect = 0
        store.knows_mark_is_dangerous = False
        store.accepted_for_answers = False
        store.accepted_to_protect = False

        store.opened_crate_willingly = False
        store.resisted_crate = False
        store.sought_help = False

        store.asked_ariane_for_truth = False
        store.asked_ariane_for_help = False
        store.trusted_ariane = False
        store.protected_ariane = False
        store.blamed_polemon = False

        store.listened_to_echoes = 0
        store.refused_first_echo = False
        store.told_ariane_everything = False
        store.hid_heirs_from_ariane = False
        store.promised_ariane = False
        store.warned_ariane = False
        store.hid_third_echo = False

        store.nerissa_question = ""
        store.prologue_completed = False
