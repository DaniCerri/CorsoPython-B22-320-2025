"""
Dato un elenco di fatture, andiamo a calcolare imposte, guadagni, etc.
"""
import datetime # Importiamo la libreria di funzioni per gestire le date

FATTURATO_TOTALE = 1
FATTURATO_INCASSATO = 2
FATTURATO_DA_INCASSARE = 3

def calcola_fatturato_totale(elenco_fatture: list[dict], tipologia: int) -> float:
    """
    Calcola il totale del fatturato di un elenco di dizionari "fattura"
    :param tipologia: Tipologia di calcolo del fatturato -> da costanti
    :param elenco_fatture: Lista di dizionari "fattura"
    :return: fatturato totale, float
    """
    tot = 0  # inizializziamo il totale a 0
    for fattura in elenco_fatture:
        totale_selezionato = tipologia == FATTURATO_TOTALE
        solo_incassate = tipologia == FATTURATO_INCASSATO and fattura['pagata']
        solo_da_incassare = tipologia == FATTURATO_DA_INCASSARE and not fattura['pagata']
        da_aggiungere = totale_selezionato or solo_incassate or solo_da_incassare

        if da_aggiungere:
            tot += fattura.get("importo", 0)  # Proviamo a prendere l'importo, altrimenti mettiamo uno 0

    return tot  # Restituiamo il totale

def calcola_fatturato_medio(elenco_fatture: list[dict]) -> float:
    """
    Calcola l'importo medio delle fatture
    :param elenco_fatture: Lista di dizionari "fattura"
    :return: valore medio dell'importo delle fatture, float
    """
    media = calcola_fatturato_totale(elenco_fatture) / len(elenco_fatture)
    return media

def converti_data(data: str):
    """
    Converte la stringa di una data in una data "oggetto" di Python
    :param data: data sotto forma di stringa
    :return: Data convertita
    """
    data_convertita = datetime.datetime.strptime(data, "%Y-%m-%d")  # %Y-%m-%d -> aaaa-mm-gg
    return data_convertita

def converti_date(elenco_fatture: list[dict]) -> list[dict]:
    for i, fattura in enumerate(elenco_fatture):
        # Sovrascriviamo la data della fattura che era in formato stringa con quella in formato "data"
        fattura['data'] = converti_data(fattura['data'])
        fattura['scadenza'] = converti_data(fattura['scadenza'])

        # Sovrascriviamo la fattura che aveva la data stringa con quella con la data "data"
        elenco_fatture[i] = fattura

    return elenco_fatture

def calcola_delta_tempo_fatture(elenco_fatture: list[dict]) -> int:
    """
    Calcola il numero di giorni tra la prima e l'ultima fattura
    :param elenco_fatture: Elenco di dizionari "fattura"
    :return: Numero di giorni tra la prima e l'ultima, int
    """
    lista_date = []
    for fattura in elenco_fatture:
        lista_date.append(fattura['data'])

    prima_data = min(lista_date)
    ultima_data = max(lista_date)

    return (ultima_data - prima_data).days  # Calcoliamo "implicitamente" i giorni di differenza tra le date

def calcolo_delta_giorni_scadenza(elenco_fatture: list[dict]) -> list[dict]:
    """
    Data ogni fattura calcola il numero di giorni (intero) che mancano da oggi alla scadenza
    :param elenco_fatture: Lista di dizionari "fattura"
    :return: Lista orginale in cui ogni fattura ha la nuova chiave "giorni-a-scadenza" e valore numero di giorni
    """
    oggi = datetime.datetime.now()  # Otteniamo la data di oggi
    for i, fattura in enumerate(elenco_fatture):
        delta_giorni = fattura['scadenza'] - oggi
        fattura['giorni-a-scadenza'] = delta_giorni.days
        elenco_fatture[i] = fattura

        # elenco_fatture[i]['giorni-a-scadenza'] = fattura['scadenza'] - oggi
    return elenco_fatture

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
            "pagata": False # <-- Da incassare
        },
        {
            "numero": "2025-007",
            "importo": 1500.00,
            "data": "2025-11-30",
            "scadenza": "2025-12-30",
            "cliente": "E-Commerce Srl",
            "descrizione": "Integrazione sistema raccomandazione AI",
            "pagata": False # <-- Appena emessa
        },
        {
            "numero": "2025-008",
            "importo": 75.00,
            "data": "2025-12-01",
            "scadenza": "2025-12-01",
            "cliente": "Mario Rossi",
            "descrizione": "Consulenza rapida configurazione Docker",
            "pagata": True # Pagamento immediato
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
    lista_fatture = converti_date(lista_fatture)
    print(f"Giorni dalla prima all'ultima fattura: {calcola_delta_tempo_fatture(lista_fatture)}")
    lista_fatture = calcolo_delta_giorni_scadenza(lista_fatture)
    print(lista_fatture)
