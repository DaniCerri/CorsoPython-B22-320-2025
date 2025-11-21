dizionario_spese = {
    "Gen": 32,
    "Feb": 45,
    "Mar": 69,
    "Apr": 41,
    "Mag": 30,
    "Giu": 45,
    "Lug": 74,
    "Ago": 46,
    "Set": 36,
    "Ott": 98,
    "Nov": 46,
    "Dic": 51,
}

# Otteniamo le chiavi del dizionario
print(f"Chiavi del dizionario: {dizionario_spese.keys()}")

# Otteniamo i valori del dizionario
print(f"Valori del dizionario: {dizionario_spese.values()}")

# Otteniamo le coppie chiave-valore del dizionario
print(f"Coppie chiave-valore del dizionario: {dizionario_spese.items()}")

print(f"Media delle chiavi del dizionario: {sum(dizionario_spese.values()) / len(dizionario_spese.values()):.2f}")
print(f"Spesa massima: {max(dizionario_spese.values())}")
print(f"Spesa minima: {min(dizionario_spese.values())}")
