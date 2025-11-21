"""
Lo Chef ti ha lanciato il foglio con gli ordini del pranzo (comande)
e ti ha chiesto di preparare immediatamente la linea per la cucina;
il tuo script deve analizzare gli ordini per stampare un resoconto che dica ai
cuochi esattamente quanti piatti preparare per ogni tipo (es. "3 Carbonara"),
e contemporaneamente deve consultare il ricettario per generare una "Lista della Spesa"
contenente l'elenco di tutti gli ingredienti grezzi necessari per coprire il servizio,
assicurandosi che nella lista ogni ingrediente compaia una volta sola
(non importa se il Pecorino serve per 3 ricette diverse,
nella lista deve apparire solo come "Pecorino").
"""

ricettario = {
    "Carbonara": ["Guanciale", "Uova", "Pecorino", "Pepe"],
    "Amatriciana": ["Guanciale", "Pomodoro", "Pecorino", "Peperoncino"],
    "Cacio e Pepe": ["Pecorino", "Pepe"],
    "Gricia": ["Guanciale", "Pecorino", "Pepe"]
}

comande = [
    "Carbonara",
    "Amatriciana",
    "Carbonara",
    "Cacio e Pepe",
    "Carbonara",
    "Gricia",
    "Amatriciana"
]

# 1. Prepariamo il resoconto delle ricette da preparare
# 1.0 Definiamo un dizionario vuoto in cui metteremo le coppie "piatto: numero da preparare"
diz_resoconto = {}
# 1.1 Facciamo un ciclo all'interno delle comande
for comanda in comande:
    # 1.2 Per ogni comanda, aggiorniamo il contatore che tiene conto di quanti piatti del suo tipo ci
    #     sono da fare

    # Cerchiamo di ottenere il numero di volte che il piatto attuale è già comparso facendo il for.
    # Per fare questo usiamo il metodo dei dizionari ".get()" che, se trova la chiave richiesta all'interno del
    # dizionario, restituisce il valore associato, altrimenti un valore di default.
    # Nel nostro caso, il valore di default è 0, perchè se la chiave non è presente nel dizionario, non abbiamo ancora
    # visto quel piatto.
    conteggio_piatto = diz_resoconto.get(comanda, 0)

    # Siccome abbiamo trovato una nuova richiesta per il piatto attuale, incrementiamo di 1 il contatore
    conteggio_piatto += 1  # -> conteggio_piatto = conteggio_piatto + 1

    # Aggiorniamo il nostro dizionario del resoconto, per tenere traccia di quante volte effettive il piatto è
    # comparso all'interno della lista
    diz_resoconto[comanda] = conteggio_piatto  # Se la chiave c'era già, va a sovrascrivere il valore che c'era assegnato
    # [Che quindi risulterà incrementato di uno]
    # Altrimenti crea una nuova coppia "comanda": conteggio_piatto -> "comanda": 1

# Al termine del for, il nostro diz_resoconto avrà questa forma:
# {
#    "Carbonara": 3,
#    "Amatriciana": 2,
#    "Cacio e Pepe": 1,
#    "Gricia": 1
# }


# 1.3 Stampiamo il resoconto
print("Resoconto dei piatti da preparare: ")
for nome_piatto, n_da_preparare in diz_resoconto.items():
    print(f" * {nome_piatto}: {n_da_preparare}")


# 2. Prepariamo la lista della spesa
# 2.1 Capiamo qual è l'elenco completo di tutti gli ingredienti
# 2.2 Capiamo quali ingredienti "unici" dobbiamo comprare
# 2.3 Stampiamo la lista degli ingredienti unici (lista della spesa)