# Biblioteca "Civica Aldrovandi"

Costruiamo il backend per una biblioteca che gestisce il catalogo, i tag
descrittivi e i prestiti dei lettori.

## Entità

- **Tag**: nome, giorni_extra (int, giorni in più di prestito), riservato (bool), didattico (bool)
- **Libro**: titolo, isbn, anno, descrizione, durata_base (giorni), disponibile (bool)
- **Lettore**: nome, telefono, email, tessera
- **Prestito**: data_ora, stato (`prenotato` | `ritirato` | `restituito` | `in_ritardo`),
  lettore, note
- **VocePrestito**: prestito, libro, quantità (copie), tag_extra (lista)

## Relazioni

- Un **libro** ha molti **tag** "di base" (molti-a-molti)
- Un **prestito** appartiene a un solo **lettore** (uno-a-molti)
- Un **prestito** contiene molte **voci** (uno-a-molti)
- Una **voce prestito** può avere tag **extra** rispetto a quelli base
  del libro (molti-a-molti)

## Requisiti

- Stack: **FastAPI + SQLAlchemy + Pydantic**, DB **MySQL** con `pymysql`
  (database `db_biblioteca`)
- Variabili di connessione in `.env` (no credenziali hardcoded)
- Struttura modulare: `routers/`, `schemas/`, `crud/`, `models/`,
  `database.py`, `dependencies.py`, `main.py`
- **CRUD completo** per Libri, Tag, Lettori
- `GET /libri/` ritorna anche un campo `durata_totale` calcolato come
  `durata_base + somma(giorni_extra dei tag base)`
- `GET /libri/?didattici=true` filtra solo libri 100% didattici
- `GET /libri/?senza_riservati=true` filtra libri senza tag riservati
- Ricerca libri per titolo (parziale, case-insensitive)
- Endpoint per creare un prestito completo in **una sola POST** (lettore
  esistente + lista voci con tag extra)
- `PATCH /prestiti/{id}/stato` per avanzare lo stato del prestito
- `GET /prestiti/oggi` lista prestiti con `data_ora` di oggi, ordinati per ora
- `GET /lettori/{id}/storico` ritorna prestiti passati e **totale giorni di prestito**
- Validazione Pydantic: telefono non vuoto, quantità ≥ 1, stato fra valori ammessi
- Script `init_db.py` che popola il DB con: 8 libri classici, 15 tag,
  3 lettori, 5 prestiti di esempio

## Extra (opzionali)

- Endpoint `GET /statistiche/` con: libro più prestato del mese, prestiti giornalieri,
  tag extra più richiesto
- Bonus di 7 giorni in più se il prestito contiene più di 5 libri
  (campo `durata_bonus` nella response)
- Soft delete sui libri (campo `disponibile=false` invece di DELETE fisico)
- Test con `pytest` su almeno gli endpoint di creazione prestito