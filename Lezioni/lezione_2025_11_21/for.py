# Ripetiamo un blocco di codice 5 volte
for i in range(5):
    print(f"Il contatore 'i' vale {i}")

# Creiamo una lista
lista_mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu']

# Stampiamo un elenco numerato degli elementi della lista
for i in range(len(lista_mesi)): # Il range va da 0 alla lunghezza della lista (-1)
    print(f"{i + 1}. {lista_mesi[i]}")

lista_costi = [
    [12, 23, 10],  # Questo è un elemento della lista_costi
    [45, 12,  7],
    [34, 75,  3],
]

# Per ogni lista di costi calcoliamo la media:
for lista_mensile in lista_costi:  # Per ogni elemento della lista_costi
    print(f"Media: {sum(lista_mensile) / len(lista_mensile):.2f}")   # Calcoliamo la sua media

for indice, lista_mensile in enumerate(lista_costi):
    # Calcoliamo la sua media
    print(f"Media elemento alla posizione {indice + 1}: {sum(lista_mensile) / len(lista_mensile):.2f}")
print(f"\n{'-' * 100}")
# -----------------------------------------------------------------------------------------------------------
# Definiamo un dizionario di spese
diz_spese = {
    "Gen": [23, 54, 23, 6],
    "Feb": [56, 12, 23],
    "Mar": [10, 54, 45, 45],
    "Apr": [69],
    "Mag": [78, 54, 12, 6, 7, 9],
    "Giu": [10, 120, 3, 45],
}

# Stampiamo l'elenco dei mesi che fanno parte del nostro dizionario
for mese in diz_spese.keys():
    print(f"* {mese}")

# Stampiamo l'elenco delle spese che fanno parte del nostro dizionario
for spese in diz_spese.values():
    print(f"* {spese}")

# Calcoliamo per ogni mese la spesa totale e la spesa media
for mese, spese in diz_spese.items():
    tot = sum(spese)  # Calcoliamo la spesa totale
    media = tot / len(spese)  # Calcoliamo la spesa media
    spesa_min = min(spese)  # Troviamo la spesa minima
    spesa_max = max(spese)  # Troviamo la spesa massima
    print(f"Spese di {mese}: ")
    print(f" * Spesa minima: {spesa_min:.2f}")
    print(f" * Spesa massima: {spesa_max:.2f}")
    print(f" * Media: {media:.2f}")
    print(f" * Totale: {tot:.2f}")














