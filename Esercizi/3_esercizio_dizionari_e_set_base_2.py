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