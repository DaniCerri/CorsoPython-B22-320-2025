# Scriviamo un semplice programma che saluti 3 persone
persona1 = "Daniele"
persona2 = "Ilaria"
persona3 = "Marco"

print(f"Ciao {persona1}, {persona2} e {persona3}")

# Facciamo un semplice separatore di sezioni
titolo = "Calcolo mcm"
separatore = f"{'-' * 50} {titolo} {'-' * 50}"
print(separatore)

# Esempi di informazioni che possiamo ottenere sulle stringhe
titolo = "Ricerca del minimo"
lunghezza = len(titolo)  # Attraverso len() troviamo la lunghezza di una stringa
print(f"La lunghezza della parola '{titolo}' è: {lunghezza}")

# Vogliamo stampare le lettere che compongono la stringa dalla seconda all'ultima
print(titolo[1:])

# Vogliamo stampare le lettere che compongono la stringa dalla prima alla quarta [esclusa]
print(titolo[:3])

# Vogliamo stampare le lettere che compongono la stringa dalla terza alla penultima [inclusa]
print(titolo[2:-1])

# ciaocomestai -> [1:4]: iao