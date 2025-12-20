"""
Hai sviluppato un sistema RAG (Retrieval-Augmented Generation) che usa diversi modelli LLM
a seconda della domanda dell'utente (routing dinamico).
Il cliente vuole un report dettagliato. Non gli basta sapere "quanto ho speso",
vuole sapere il costo esatto calcolato sui token, distinguendo tra Input
(il prompt + i documenti recuperati) e Output (la risposta generata).

Le sfide sono:

1. Ogni modello ha un costo diverso per Input e Output (di solito per milione di
   token, ma per semplicità useremo prezzi per 1.000 token).

2. Devi identificare le chiamate "lente": se la latency_ms supera una
   certa soglia (es. 2000ms), quella chiamata va segnalata come "Performance Warning".

3. Se lo status non è "success", il costo è 0 (l'API non ha addebitato nulla).
"""


def calcola_costo_chiamata(tokens_input, tokens_output, model, pricing_table):
    """
    Calcola il costo di una singola chiamata API basata sui token.

    Args:
        tokens_input: Numero di token in input
        tokens_output: Numero di token in output
        model: Nome del modello
        pricing_table: Dizionario con i prezzi per modello

    Returns:
        Dizionario con costo_input, costo_output e costo_totale
    """
    # Se il modello non è nel listino, costo = 0
    if model not in pricing_table:
        return {
            "costo_input": 0.0,
            "costo_output": 0.0,
            "costo_totale": 0.0,
            "warning": "Modello non in listino"
        }

    prezzi = pricing_table[model]

    # I prezzi sono per 1.000 token
    costo_input = (tokens_input / 1000) * prezzi["input_price"]
    costo_output = (tokens_output / 1000) * prezzi["output_price"]
    costo_totale = costo_input + costo_output

    return {
        "costo_input": costo_input,
        "costo_output": costo_output,
        "costo_totale": costo_totale
    }


def verifica_performance(latency_ms, soglia=2000):
    """
    Verifica se la chiamata è considerata lenta.

    Args:
        latency_ms: Latenza in millisecondi
        soglia: Soglia oltre la quale la chiamata è considerata lenta

    Returns:
        True se la chiamata è lenta, False altrimenti
    """
    return latency_ms > soglia


def analizza_log_api(api_logs, pricing_table, soglia_latency=2000):
    """
    Analizza tutti i log delle chiamate API e genera un report completo.

    Args:
        api_logs: Lista di log delle chiamate API
        pricing_table: Tabella dei prezzi
        soglia_latency: Soglia di latenza per warning (default 2000ms)

    Returns:
        Lista di stringhe con il report
    """
    linee = []
    linee.append("=" * 80)
    linee.append("REPORT ANALISI COSTI API - SISTEMA RAG")
    linee.append("=" * 80)

    costo_totale_generale = 0.0
    chiamate_lente = []
    chiamate_fallite = []
    modelli_sconosciuti = []

    for log in api_logs:
        linee.append(f"\n{log['request_id']} - {log['timestamp']}")
        linee.append(f"  Modello: {log['model']}")
        linee.append(f"  Status: {log['status']}")
        linee.append(f"  Latenza: {log['latency_ms']}ms")

        # Se la chiamata non è riuscita, costo = 0
        if log["status"] != "success":
            linee.append(f"  ⚠️  Chiamata fallita - Costo: $0.00")
            chiamate_fallite.append(log["request_id"])
            continue

        # Calcola il costo
        costi = calcola_costo_chiamata(
            log["tokens"]["input"],
            log["tokens"]["output"],
            log["model"],
            pricing_table
        )

        # Gestione modello sconosciuto
        if "warning" in costi:
            linee.append(f"  ⚠️  {costi['warning']} - Costo: $0.00")
            modelli_sconosciuti.append(log["request_id"])
            continue

        # Mostra dettagli costi
        linee.append(f"  Token Input: {log['tokens']['input']} → ${costi['costo_input']:.6f}")
        linee.append(f"  Token Output: {log['tokens']['output']} → ${costi['costo_output']:.6f}")
        linee.append(f"  Costo Totale: ${costi['costo_totale']:.6f}")

        costo_totale_generale += costi["costo_totale"]

        # Verifica performance
        if verifica_performance(log["latency_ms"], soglia_latency):
            linee.append(f"  ⚠️  PERFORMANCE WARNING: Latenza {log['latency_ms']}ms (soglia: {soglia_latency}ms)")
            chiamate_lente.append({
                "request_id": log["request_id"],
                "latency": log["latency_ms"],
                "model": log["model"]
            })

    # Report finale
    linee.append("\n" + "=" * 80)
    linee.append("RIEPILOGO")
    linee.append("=" * 80)
    linee.append(f"Costo totale: ${costo_totale_generale:.6f}")
    linee.append(f"Chiamate totali: {len(api_logs)}")
    linee.append(f"Chiamate riuscite: {len([l for l in api_logs if l['status'] == 'success'])}")
    linee.append(f"Chiamate fallite: {len(chiamate_fallite)}")
    linee.append(f"Modelli sconosciuti: {len(modelli_sconosciuti)}")

    if chiamate_lente:
        linee.append(f"\n⚠️  PERFORMANCE WARNINGS: {len(chiamate_lente)} chiamate lente")
        for chiamata in chiamate_lente:
            linee.append(f"  - {chiamata['request_id']} ({chiamata['model']}): {chiamata['latency']}ms")

    if chiamate_fallite:
        linee.append(f"\n❌ CHIAMATE FALLITE:")
        for rid in chiamate_fallite:
            linee.append(f"  - {rid}")

    if modelli_sconosciuti:
        linee.append(f"\n❓ MODELLI NON IN LISTINO:")
        for rid in modelli_sconosciuti:
            linee.append(f"  - {rid}")

    return linee


if __name__ == "__main__":
    # Prezzi in dollari per 1.000 token
    pricing_table = {
        "gpt-4o": {
            "input_price": 0.0050,
            "output_price": 0.0150
        },
        "gpt-3.5-turbo": {
            "input_price": 0.0005,
            "output_price": 0.0015
        },
        "claude-3-opus": {  # Modello costoso
            "input_price": 0.0150,
            "output_price": 0.0750
        }
    }

    api_logs = [
        {
            "request_id": "req_abc123",
            "timestamp": "2025-11-28T10:00:05",
            "model": "gpt-4o",
            "status": "success",
            "tokens": {"input": 450, "output": 120},
            "latency_ms": 1200
        },
        {
            "request_id": "req_def456",
            "timestamp": "2025-11-28T10:05:10",
            "model": "gpt-3.5-turbo",
            "status": "success",
            "tokens": {"input": 1500, "output": 50},  # Molto context, poca risposta
            "latency_ms": 450
        },
        {
            "request_id": "req_ghi789",
            "timestamp": "2025-11-28T10:15:00",
            "model": "gpt-4o",
            "status": "error",  # Chiamata fallita
            "tokens": {"input": 0, "output": 0},
            "latency_ms": 5000  # Timeout
        },
        {
            "request_id": "req_jkl012",
            "timestamp": "2025-11-28T10:20:30",
            "model": "claude-3-opus",
            "status": "success",
            "tokens": {"input": 2000, "output": 800},  # Chiamata pesante e costosa
            "latency_ms": 8500  # Molto lento -> Warning
        },
        {
            "request_id": "req_mno345",
            "timestamp": "2025-11-28T10:25:12",
            "model": "gpt-3.5-turbo",
            "status": "success",
            "tokens": {"input": 120, "output": 60},
            "latency_ms": 300
        },
        {
            "request_id": "req_pqr678",
            "timestamp": "2025-11-28T10:30:00",
            "model": "gpt-4o",
            "status": "success",
            "tokens": {"input": 3000, "output": 150},  # RAG pesante
            "latency_ms": 2100  # Appena sopra soglia 2000ms -> Warning?
        },
        {
            "request_id": "req_stu901",
            "timestamp": "2025-11-28T10:35:45",
            "model": "unknown-model",  # Caso limite: modello non in listino
            "status": "success",
            "tokens": {"input": 100, "output": 100},
            "latency_ms": 500
        },
        {
            "request_id": "req_vwx234",
            "timestamp": "2025-11-28T10:40:20",
            "model": "claude-3-opus",
            "status": "success",
            "tokens": {"input": 500, "output": 2500},  # Generazione lunga
            "latency_ms": 6200
        },
        {
            "request_id": "req_yz1234",
            "timestamp": "2025-11-28T10:45:00",
            "model": "gpt-3.5-turbo",
            "status": "rate_limit_exceeded",  # Errore
            "tokens": {"input": 0, "output": 0},
            "latency_ms": 100
        },
        {
            "request_id": "req_567890",
            "timestamp": "2025-11-28T10:50:55",
            "model": "gpt-4o",
            "status": "success",
            "tokens": {"input": 800, "output": 800},
            "latency_ms": 1500
        }
    ]

    report = analizza_log_api(api_logs, pricing_table)
    for linea in report:
        print(linea)
