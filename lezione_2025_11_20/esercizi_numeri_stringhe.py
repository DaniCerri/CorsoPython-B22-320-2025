# Scriviamo uno script che calcoli il totale di una lista di oggetti che abbiamo comprato e ne stampi
# un resoconto
tavolo = 230  # Costo del tavolo
sedia = 45  # Costo della sedia
n_sedie = 4  # Numero di sedie acquistate
piatto_fondo = 3.4  # Costo di un piatto fondo
piatto_piano = 4.2  # Costo di un piatto piano
numero_persone_servizio = 6  # Numero di piatti piani e fondi

costo_sedie = sedia * n_sedie  # Calcoliamo il costo complessivo delle sedie
costo_piatti = (piatto_fondo + piatto_piano) * numero_persone_servizio  # Calcoliamo il costo complessivo dei piatti

costo_totale = tavolo + costo_sedie + costo_piatti  # Sommiamo tutti i costi parziali per ottenere il totale

# Stampiamo il resoconto
print("Riepilogo dei costi: ")  # Dopo il print, in python, il testo va a capo automaticamente
print(f" - Tavolo: {tavolo} €")
print(f" - Piatti: ({piatto_fondo} + {piatto_piano}) * {numero_persone_servizio}  -> {costo_piatti}€")
print(f" - Sedie: {sedia} * {n_sedie}  -> {costo_sedie}€")

print(f"Totale: {costo_totale} €")
print()  # Va a capo di una riga nel terminale

# Creiamo un sistema che date 3 dimensioni di un parallelepipedo restituisca:
# Area di base: base * profondita
# Volume totale: base * altezza * profondita
# Diagonale: (base ** 2 + altezza ** 2 + profondita ** 2) ** 1/2
# 6 ** 2 -> 36
# 6 ** 3 -> 216
# 16 ** (1/2) -> 4 <- Radice quadrata

base = 45
profondita = 12.1
altezza = 35

area_base = base * profondita  # Calcoliamo l'area di base
volume = base * altezza * profondita  # Calcoliamo il volume
diagonale = (base ** 2 + altezza ** 2 + profondita ** 2) ** 0.5  # Calcoliamo la diagonale

# Una volta calcolate le informazioni richieste, fare un print dettagliato
print(f"Informazioni calcolate sul parallelepipedo di dimensioni {base} * {altezza} * {profondita}: ")
print(f" - Area di base: {area_base}")
print(f" - Volume: {volume}")
print(f" - Digonale: {diagonale}")

