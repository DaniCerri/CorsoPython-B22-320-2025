"""
Il dipartimento marketing ti ha inviato i log delle vendite dell'ultima settimana
(la lista transazioni) e ha urgente bisogno di segmentare l'utenza per una nuova campagna
pubblicitaria mirata; il tuo script deve processare i dati per generare un report che identifichi
univocamente i "Top Spender" (clienti che hanno speso in totale più di 1000€ sommando tutti
i loro ordini) restituendo per ciascuno di essi l'insieme delle categorie merceologiche
uniche a cui si sono interessati, e contemporaneamente deve isolare un gruppo di "Tech Purists",
ovvero quei clienti che hanno acquistato almeno un prodotto della categoria "Tech" ma non hanno
mai comprato nulla dalla categoria "Books" in nessun ordine, calcolando infine quale categoria
merceologica è la più popolare in assoluto basandosi sul numero totale di volte che appare
nei carrelli di tutti i clienti indistintamente.
"""

transazioni = [
    {"id_ordine": 101, "cliente": "Marco_R", "prodotti": ["Laptop", "Mouse"], "categorie": ["Tech", "Tech"], "totale": 1200.00},
    {"id_ordine": 102, "cliente": "Giulia_S", "prodotti": ["Libro Python", "Caffè"], "categorie": ["Books", "Food"], "totale": 45.50},
    {"id_ordine": 103, "cliente": "Marco_R", "prodotti": ["Monitor", "Cavo HDMI"], "categorie": ["Tech", "Tech"], "totale": 300.00},
    {"id_ordine": 104, "cliente": "Luca_B", "prodotti": ["Tastiera", "Libro Java"], "categorie": ["Tech", "Books"], "totale": 150.00},
    {"id_ordine": 105, "cliente": "Sara_L", "prodotti": ["Smartphone"], "categorie": ["Tech"], "totale": 800.00},
    {"id_ordine": 106, "cliente": "Giulia_S", "prodotti": ["Webcam"], "categorie": ["Tech"], "totale": 60.00},
    {"id_ordine": 107, "cliente": "Luca_B", "prodotti": ["Cuffie"], "categorie": ["Tech"], "totale": 120.00},
    {"id_ordine": 108, "cliente": "Matteo_P", "prodotti": ["Tablet", "Custodia"], "categorie": ["Tech", "Accessories"], "totale": 450.00},
    {"id_ordine": 109, "cliente": "Sara_L", "prodotti": ["Smartwatch"], "categorie": ["Tech"], "totale": 250.00},
    {"id_ordine": 110, "cliente": "Elena_N", "prodotti": ["Romanzo", "Tè"], "categorie": ["Books", "Food"], "totale": 35.00},
    {"id_ordine": 111, "cliente": "Marco_R", "prodotti": ["Sedia Gaming"], "categorie": ["Furniture"], "totale": 200.00},
]