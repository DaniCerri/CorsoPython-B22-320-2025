"""
Hai appena chiuso il mese per un grosso cliente ("MegaCorp") a cui stai sviluppando un portale interno.
Il contratto prevede tariffe orarie differenziate in base alla tecnologia usata: lo sviluppo Frontend (React)
viene pagato 50€/h, il Backend (Python) 60€/h, mentre le ore dedicate all'AI (Modelli/RAG) valgono 100€/h.
C'è però una complicazione (il "twist"): se il cliente ha richiesto un intervento con flag "urgente",
quella specifica sessione di lavoro subisce una maggiorazione del 30% sulla tariffa base.
Il tuo obiettivo è processare il registro delle ore grezzo e calcolare quanto devi fatturare per
ogni singola voce, senza impazzire con calcolatrice e fogli Excel se le tariffe dovessero
cambiare mese prossimo.
"""


def ottieni_tariffa_base(tipo):
    """
    Restituisce la tariffa oraria base per il tipo di lavoro specificato.

    Args:
        tipo: Il tipo di lavoro (React, Python, AI_RAG, DevOps, ecc.)

    Returns:
        La tariffa oraria in euro
    """
    tariffe = {
        "React": 50,
        "Python": 60,
        "AI_RAG": 100,
        "DevOps": 50  # Tariffa default per tipi non previsti
    }

    return tariffe.get(tipo, 50)  # Default 50€ se tipo non riconosciuto


def calcola_costo_voce(ore, tipo, urgente):
    """
    Calcola il costo di una singola voce di timesheet.

    Args:
        ore: Numero di ore lavorate
        tipo: Tipo di lavoro
        urgente: Boolean che indica se il lavoro era urgente

    Returns:
        Il costo totale per questa voce
    """
    tariffa_base = ottieni_tariffa_base(tipo)

    if urgente:
        tariffa_effettiva = tariffa_base * 1.30  # Maggiorazione 30%
    else:
        tariffa_effettiva = tariffa_base

    costo = ore * tariffa_effettiva
    return costo


def genera_report_fatturazione(timesheet):
    """
    Processa il timesheet completo e genera un report di fatturazione.

    Args:
        timesheet: Lista di voci di lavoro

    Returns:
        Lista di stringhe con il report
    """
    linee = []
    linee.append("=" * 80)
    linee.append("REPORT FATTURAZIONE MEGACORP")
    linee.append("=" * 80)

    totale_generale = 0

    for voce in timesheet:
        costo = calcola_costo_voce(voce["ore"], voce["tipo"], voce["urgente"])
        totale_generale += costo

        urgente_flag = " [URGENTE +30%]" if voce["urgente"] else ""
        tariffa_base = ottieni_tariffa_base(voce["tipo"])
        tariffa_effettiva = tariffa_base * 1.30 if voce["urgente"] else tariffa_base

        linee.append(f"\n{voce['id']} - {voce['data']}")
        linee.append(f"  Descrizione: {voce['descrizione']}")
        linee.append(f"  Tipo: {voce['tipo']}{urgente_flag}")
        linee.append(f"  Ore: {voce['ore']}h × {tariffa_effettiva:.2f}€/h = {costo:.2f}€")

    linee.append("\n" + "=" * 80)
    linee.append(f"TOTALE DA FATTURARE: {totale_generale:.2f}€")
    linee.append("=" * 80)

    return linee


if __name__ == "__main__":
    timesheet = [
        {
            "id": "LOG-001",
            "data": "2025-11-01",
            "tipo": "React",
            "ore": 4.5,
            "descrizione": "Setup iniziale struttura progetto frontend",
            "urgente": False
        },
        {
            "id": "LOG-002",
            "data": "2025-11-02",
            "tipo": "Python",
            "ore": 3.0,
            "descrizione": "Creazione API endpoint login e auth",
            "urgente": False
        },
        {
            "id": "LOG-003",
            "data": "2025-11-03",
            "tipo": "AI_RAG",
            "ore": 5.0,
            "descrizione": "Studio fattibilità integrazione LLM locale",
            "urgente": False
        },
        {
            "id": "LOG-004",
            "data": "2025-11-05",
            "tipo": "React",
            "ore": 2.0,
            "descrizione": "Hotfix bug menu mobile che non si apriva",
            "urgente": True  # <-- Attenzione: Urgente (+30%)
        },
        {
            "id": "LOG-005",
            "data": "2025-11-07",
            "tipo": "Python",
            "ore": 6.5,
            "descrizione": "Sviluppo logica business processamento dati",
            "urgente": False
        },
        {
            "id": "LOG-006",
            "data": "2025-11-08",
            "tipo": "AI_RAG",
            "ore": 2.0,
            "descrizione": "Debug risposte allucinate del modello su query specifiche",
            "urgente": True  # <-- Attenzione: Urgente e tariffa alta
        },
        {
            "id": "LOG-007",
            "data": "2025-11-10",
            "tipo": "DevOps",
            # <-- Attenzione: Tipo non previsto nel contratto standard? (Decidi tu come gestirlo, es: default 50€)
            "ore": 1.5,
            "descrizione": "Configurazione Docker e CI/CD pipeline",
            "urgente": False
        },
        {
            "id": "LOG-008",
            "data": "2025-11-12",
            "tipo": "React",
            "ore": 4.0,
            "descrizione": "Implementazione dashboard grafici con Recharts",
            "urgente": False
        },
        {
            "id": "LOG-009",
            "data": "2025-11-15",
            "tipo": "Python",
            "ore": 1.0,
            "descrizione": "Fix critico su crash server in produzione",
            "urgente": True
        },
        {
            "id": "LOG-010",
            "data": "2025-11-18",
            "tipo": "AI_RAG",
            "ore": 3.5,
            "descrizione": "Ottimizzazione embedding vettoriali",
            "urgente": False
        }
    ]

    report = genera_report_fatturazione(timesheet)
    for linea in report:
        print(linea)
