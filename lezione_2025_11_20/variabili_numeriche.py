# Calcoliamo l'area di un triangolo date base e altezza
base = 12.1  # La base del nostro triangolo
altezza = 45.2  # L'altezza del nostro triangolo
area = base * altezza / 2  # Calcoliamo l'area

# per "stampare" il risultato usiamo la funzione "print" che ci fa vedere ciò che il nostro
# programma calcola nel terminale
print(area)

# Convertiamo un tempo in secondi in ore:minuti:secondi
tempo = 45698  # Tempo iniziale in secondi

ore = tempo // (60 * 60)  # Calcoliamo a quante ore (intere) corrispondono i secondi
secondi = tempo % (60 * 60)  # Calcoliamo quanti secondi rimangono "fuori" dalle ore intere

minuti = secondi // 60  # Calcoliamo a quanti minuti (interi) corrispondono i secondi rimanenti
secondi = tempo % 60  # Calcoliamo i secondi rimanenti

print(ore, minuti, secondi)  # Stampiamo il nostro risultato