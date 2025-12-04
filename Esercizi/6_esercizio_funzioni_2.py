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