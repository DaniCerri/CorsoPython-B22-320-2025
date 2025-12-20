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


def processa_transazioni(transazioni):
    """
    Processa le transazioni per aggregare dati per cliente.

    Returns:
        Tupla (totale_speso_per_cliente, categorie_per_cliente, contatore_categorie)
    """
    totale_speso_per_cliente = {}
    categorie_per_cliente = {}
    contatore_categorie = {}

    for transazione in transazioni:
        cliente = transazione["cliente"]
        totale = transazione["totale"]
        categorie = transazione["categorie"]

        # Aggregare il totale speso per cliente
        if cliente in totale_speso_per_cliente:
            totale_speso_per_cliente[cliente] += totale
        else:
            totale_speso_per_cliente[cliente] = totale

        # Aggregare le categorie per cliente usando set per unicità
        if cliente in categorie_per_cliente:
            categorie_per_cliente[cliente].update(categorie)
        else:
            categorie_per_cliente[cliente] = set(categorie)

        # Contare le occorrenze delle categorie
        for categoria in categorie:
            if categoria in contatore_categorie:
                contatore_categorie[categoria] += 1
            else:
                contatore_categorie[categoria] = 1

    return totale_speso_per_cliente, categorie_per_cliente, contatore_categorie


def identifica_top_spender(totale_speso_per_cliente, categorie_per_cliente, soglia=1000):
    """
    Identifica i clienti che hanno speso più della soglia.

    Returns:
        Dizionario {cliente: set_categorie}
    """
    top_spender = {}
    for cliente, totale in totale_speso_per_cliente.items():
        if totale > soglia:
            top_spender[cliente] = categorie_per_cliente[cliente]
    return top_spender


def identifica_tech_purists(categorie_per_cliente):
    """
    Identifica clienti con Tech ma senza Books.

    Returns:
        Lista di clienti tech purists
    """
    tech_purists = []
    for cliente, categorie in categorie_per_cliente.items():
        if "Tech" in categorie and "Books" not in categorie:
            tech_purists.append(cliente)
    return tech_purists


def trova_categoria_piu_popolare(contatore_categorie):
    """
    Trova la categoria con più occorrenze.

    Returns:
        Tupla (categoria, count)
    """
    categoria = max(contatore_categorie, key=contatore_categorie.get)
    return categoria, contatore_categorie[categoria]


def genera_report(transazioni, totale_speso_per_cliente, categorie_per_cliente,
                  top_spender, tech_purists, contatore_categorie):
    """
    Genera il report completo come lista di stringhe.

    Returns:
        Lista di stringhe da stampare
    """
    linee = []

    # Top Spender
    linee.append("=== TOP SPENDER (oltre 1000€) ===")
    for cliente, categorie in top_spender.items():
        totale = totale_speso_per_cliente[cliente]
        linee.append(f"{cliente}: {totale:.2f}€ - Categorie: {categorie}")

    # Tech Purists
    linee.append("\n=== TECH PURISTS (Tech ma no Books) ===")
    for cliente in tech_purists:
        linee.append(f"{cliente}: {categorie_per_cliente[cliente]}")

    # Categoria più popolare
    categoria_popolare, count = trova_categoria_piu_popolare(contatore_categorie)
    linee.append("\n=== CATEGORIA PIÙ POPOLARE ===")
    linee.append(f"Categoria: {categoria_popolare} - Occorrenze: {count}")

    # Report completo
    linee.append("\n=== REPORT COMPLETO ===")
    linee.append(f"Top Spender trovati: {len(top_spender)}")
    linee.append(f"Tech Purists trovati: {len(tech_purists)}")
    linee.append("\nDistribuzione categorie:")
    for categoria, count in sorted(contatore_categorie.items(), key=lambda x: x[1], reverse=True):
        linee.append(f"  {categoria}: {count} occorrenze")

    return linee


if __name__ == "__main__":
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

    # Processa le transazioni
    totale_speso_per_cliente, categorie_per_cliente, contatore_categorie = processa_transazioni(transazioni)

    # Identifica top spender e tech purists
    top_spender = identifica_top_spender(totale_speso_per_cliente, categorie_per_cliente)
    tech_purists = identifica_tech_purists(categorie_per_cliente)

    # Genera e stampa il report
    report = genera_report(transazioni, totale_speso_per_cliente, categorie_per_cliente,
                          top_spender, tech_purists, contatore_categorie)

    for linea in report:
        print(linea)
