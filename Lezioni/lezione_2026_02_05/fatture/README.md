# API Gestione Fatture

API REST per la gestione semplificata delle fatture di una partita IVA.

## 🏗️ Struttura del Progetto

```
fatture/
├── main.py                    # Entry point dell'applicazione
├── dependencies.py            # Dipendenze FastAPI (get_db, ecc.)
├── database.py                # Configurazione database
├── init_db.py                 # Script di popolamento database
├── requirements.txt           # Dipendenze Python
│
├── routers/                   # Endpoint API organizati per risorsa
│   ├── tags.py
│   ├── clients.py
│   └── invoices.py
│
├── schemas/                   # Schemi Pydantic per validazione
│   ├── tags.py
│   ├── clients.py
│   └── invoices.py
│
├── crud/                      # Operazioni CRUD sul database
│   ├── tags.py
│   ├── clients.py
│   └── invoices.py
│
└── models/                    # Modelli SQLAlchemy
    ├── tag.py
    ├── client.py
    ├── invoice.py
    ├── invoice_item.py
    ├── invoice_status.py
    └── invoice_tag_association.py
```

## 🚀 Setup

### 1. Installare le dipendenze

```bash
pip install -r requirements.txt
```

### 2. Configurare il database

Modificare `database.py` con le credenziali del tuo database MySQL:

```python
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/fatture"
```

### 3. Popolare il database (opzionale)

```bash
python init_db.py
```

Questo script:
- Crea le tabelle nel database
- Popola il database con dati di esempio (10 fatture, 4 clienti, 6 tag)

### 4. Avviare il server

```bash
uvicorn main:app --reload
```

L'API sarà disponibile su: `http://localhost:8000`

## 📖 Documentazione API

### Documentazione interattiva

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoint principali

#### Tags
- `POST /tags/` - Crea un nuovo tag
- `GET /tags/` - Lista tutti i tag

#### Clients
- `POST /clients/` - Crea un nuovo cliente
- `GET /clients/` - Lista clienti (con paginazione: `?skip=0&limit=100`)
- `GET /clients/{client_id}` - Dettagli di un cliente

#### Invoices
- `POST /invoices/` - Crea una nuova fattura
- `GET /invoices/` - Lista fatture (con paginazione: `?skip=0&limit=100`)
- `GET /invoices/{invoice_id}` - Dettagli di una fattura
- `POST /invoices/{invoice_id}/items/` - Aggiungi una voce alla fattura

## 🗂️ Struttura Dati

### Client (Cliente)
```json
{
  "name": "NextGen StartUp SRL",
  "vat_number": "12345678901",
  "email": "amm@nextgen.it"
}
```

### Invoice (Fattura)
```json
{
  "number": "1/2024",
  "date": "2024-01-15",
  "status": "paid",
  "client_id": 1,
  "tag_ids": [1, 2, 3]
}
```

### InvoiceItem (Voce di Fattura)
```json
{
  "description": "Sviluppo API Backend",
  "quantity": 20,
  "unit_price": 60.0
}
```

### Tag
```json
{
  "name": "Urgente",
  "color": "#DC3545"
}
```

## 💡 Features

- ✅ **CRUD completo** per clienti, fatture e tag
- ✅ **Paginazione** su endpoint di lista
- ✅ **Relazioni complesse**:
  - Cliente → Fatture (1-a-molti)
  - Fattura → Items (1-a-molti)
  - Fattura ↔ Tag (molti-a-molti)
- ✅ **Calcolo automatico** del totale fattura
- ✅ **Validazione** con Pydantic
- ✅ **Documentazione** automatica con Swagger/ReDoc
- ✅ **Architettura modulare** production-ready

## 🛠️ Tecnologie

- **FastAPI** - Framework web moderno
- **SQLAlchemy** - ORM per database
- **Pydantic** - Validazione dati
- **MySQL** - Database relazionale
- **PyMySQL** - Driver MySQL per Python
- **Uvicorn** - Server ASGI

## 📝 Note

- I file `models.py`, `schemas.py` e `crud.py` nella root sono stati sostituiti da package modulari
- La struttura modulare facilita la manutenzione e scalabilità
- Ogni risorsa ha il proprio modulo in `models/`, `schemas/`, `crud/` e `routers/`
