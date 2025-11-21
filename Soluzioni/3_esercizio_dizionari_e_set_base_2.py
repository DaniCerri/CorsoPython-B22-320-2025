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
# 1.1 Facciamo un ciclo all'interno delle comande
# 1.2 Per ogni comanda, aggiorniamo il contatore che tiene conto di quanti piatti del suo tipo ci
#     sono da fare
# {
#    "Carbonara": 3,
#    "Amatriciana": 2,
#    "Cacio e Pepe": 1,
#    "Gricia": 1
#  }
# 1.3 Stampiamo il resoconto

# 2. Prepariamo la lista della spesa
# 2.1 Capiamo qual è l'elenco completo di tutti gli ingredienti
# 2.2 Capiamo quali ingredienti "unici" dobbiamo comprare
# 2.3 Stampiamo la lista degli ingredienti unici (lista della spesa)