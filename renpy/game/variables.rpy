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

default opened_crate_willingly = False
default trusted_ariane = False
default protected_ariane = False
default listened_to_echoes = 0
default promised_ariane = False
default nerissa_question = ""

default prologue_completed = False
default unlocked_gallery = ["Ariane", "Nerissa"]

init python:
    def bond_rank(points):
        if points >= 6:
            return "Laço profundo"
        if points >= 4:
            return "Confiança"
        if points >= 2:
            return "Curiosidade"
        if points >= 1:
            return "Primeira impressão"
        return "Desconhecida"

    def dominant_trait():
        values = {
            "Coragem": ivo_courage,
            "Honestidade": ivo_honesty,
            "Humor": ivo_humor,
            "Compaixão": ivo_compassion,
        }
        return max(values, key=values.get)
