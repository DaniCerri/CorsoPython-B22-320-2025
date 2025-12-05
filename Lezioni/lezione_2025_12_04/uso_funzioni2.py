"""
Scriviamo un report del nostro elenco di fatture
"""

import funzioni2  # Importiamo nel file corrente il codice del file "funzioni2.py"

def genera_report(elenco_fatture: list[dict]) -> str:
    output = []  # Definiamo una lista in cui metteremo le varie righe dell'output
    # Per prima cosa dobbiamo assicurarci che le date siano del formato corretto
    elenco_fatture = funzioni2.converti_date(elenco_fatture)

    # Poi calcoliamo i giorni che mancano alla scadenza
    elenco_fatture = funzioni2.calcolo_delta_giorni_scadenza(elenco_fatture)

    numero_fatture = len(elenco_fatture)
    # Calcoliamo la distribuzione delle fatture
    da_aspettare, non_pagate, pagate = funzioni2.distribuzione_scadenze(elenco_fatture)

    output.append(f"Di {numero_fatture} fatture, abbiamo: ")
    output.append(f" * Fatture per cui aspettare: {da_aspettare}/{numero_fatture}")
    output.append(f" * Fatture scadute: {non_pagate}/{numero_fatture}")
    output.append(f" * Fatture pagate: {pagate}/{numero_fatture}")

    fatturato_totale = funzioni2.calcola_fatturato_totale(elenco_fatture, funzioni2.FATTURATO_TOTALE)
    output.append(f"Fatturato totale: {fatturato_totale:.2f} €")

    return "\n".join(riga for riga in output)

if __name__ == "__main__":
    lista_fatture = [
        {
            "numero": "2025-001",
            "importo": 1200.00,
            "data": "2025-11-28",
            "scadenza": "2025-12-28",
            "cliente": "Pallino S.r.l.",
            "descrizione": "Consulenza per installazione del server privato",
            "pagata": True
        },
        {
            "numero": "2025-002",
            "importo": 2500.00,
            "data": "2025-10-15",
            "scadenza": "2025-11-15",
            "cliente": "TechInnovations SpA",
            "descrizione": "Sviluppo MVP agente AI per customer care",
            "pagata": True
        },
        {
            "numero": "2025-003",
            "importo": 850.00,
            "data": "2025-10-20",
            "scadenza": "2025-11-20",
            "cliente": "Studio Legale Associato",
            "descrizione": "Restyling frontend sito web vetrina in React",
            "pagata": True
        },
        {
            "numero": "2025-004",
            "importo": 60.00,
            "data": "2025-11-02",
            "scadenza": "2025-11-02",
            "cliente": "Edicola del Corso",
            "descrizione": "Risoluzione bug script automazione invio email",
            "pagata": True
        },
        {
            "numero": "2025-005",
            "importo": 3200.00,
            "data": "2025-11-10",
            "scadenza": "2025-12-10",
            "cliente": "GreenEnergy Corp",
            "descrizione": "Sviluppo Dashboard React e Backend API Python",
            "pagata": False  # <-- Da incassare
        },
        {
            "numero": "2025-006",
            "importo": 450.00,
            "data": "2025-11-12",
            "scadenza": "2025-12-12",
            "cliente": "Startup X",
            "descrizione": "Ottimizzazione performance query database",
            "pagata": False  # <-- Da incassare
        },
        {
            "numero": "2025-007",
            "importo": 1500.00,
            "data": "2025-11-30",
            "scadenza": "2025-12-30",
            "cliente": "E-Commerce Srl",
            "descrizione": "Integrazione sistema raccomandazione AI",
            "pagata": False  # <-- Appena emessa
        },
        {
            "numero": "2025-008",
            "importo": 75.00,
            "data": "2025-12-01",
            "scadenza": "2025-12-01",
            "cliente": "Mario Rossi",
            "descrizione": "Consulenza rapida configurazione Docker",
            "pagata": True  # Pagamento immediato
        },
        {
            "numero": "2025-009",
            "importo": 1800.00,
            "data": "2025-12-05",
            "scadenza": "2026-01-05",
            "cliente": "Logistica Veloce",
            "descrizione": "Sviluppo interfaccia React Native e microservizi",
            "pagata": False
        },
        {
            "numero": "2025-010",
            "importo": 500.00,
            "data": "2025-12-10",
            "scadenza": "2026-01-10",
            "cliente": "Agenzia Web Alpha",
            "descrizione": "Formazione team interno su React Hooks",
            "pagata": False
        }
    ]
    report = genera_report(lista_fatture)
    print(report)