# Pizzeria "Da Mario"

Costruiamo il backend per una pizzeria che gestisce il menù, gli
ingredienti e gli ordini di asporto.

## Entità

- **Ingrediente**: nome, prezzo_extra, allergene (bool), vegetariano (bool)
- **Pizza**: nome, prezzo_base, descrizione, disponibile (bool)
- **Cliente**: nome, telefono, indirizzo
- **Ordine**: data_ora, stato (`ricevuto` | `in_preparazione` | `pronto` | `consegnato`),
  cliente, note
- **VocePizzaOrdine**: ordine, pizza, quantità, ingredienti_extra (lista)

## Relazioni

- Una **pizza** ha molti **ingredienti** "di base" (molti-a-molti)
- Un **ordine** appartiene a un solo **cliente** (uno-a-molti)
- Un **ordine** contiene molte **voci** (uno-a-molti)
- Una **voce ordine** può avere ingredienti **extra** rispetto a quelli base
  della pizza (molti-a-molti)

## Requisiti

- Stack: **FastAPI + SQLAlchemy + Pydantic**, DB **MySQL** con `pymysql`
  (database `db_pizzeria`)
- Variabili di connessione in `.env` (no credenziali hardcoded)
- Struttura modulare: `routers/`, `schemas/`, `crud/`, `models/`,
  `database.py`, `dependencies.py`, `main.py`
- **CRUD completo** per Pizze, Ingredienti, Clienti
- `GET /pizze/` ritorna anche un campo `prezzo_totale` calcolato come
  `prezzo_base + somma(prezzo_extra ingredienti base)`
- `GET /pizze/?vegetariane=true` filtra solo pizze 100% vegetariane
- `GET /pizze/?senza_allergeni=true` filtra pizze senza ingredienti allergenici
- Ricerca pizze per nome (parziale, case-insensitive)
- Endpoint per creare un ordine completo in **una sola POST** (cliente
  esistente + lista voci con ingredienti extra)
- `PATCH /ordini/{id}/stato` per avanzare lo stato dell'ordine
- `GET /ordini/oggi` lista ordini con `data_ora` di oggi, ordinati per ora
- `GET /clienti/{id}/storico` ritorna ordini passati e **totale speso**
- Validazione Pydantic: telefono non vuoto, quantità ≥ 1, stato fra valori ammessi
- Script `init_db.py` che popola il DB con: 8 pizze classiche, 15 ingredienti,
  3 clienti, 5 ordini di esempio

## Extra (opzionali)

- Endpoint `GET /statistiche/` con: pizza più ordinata del mese, incasso giornaliero,
  ingrediente extra più richiesto
- Sconto del 10% se l'ordine supera i 30€ (campo `totale_scontato` nella response)
- Soft delete sulle pizze (campo `disponibile=false` invece di DELETE fisico)
- Test con `pytest` su almeno gli endpoint di creazione ordine
