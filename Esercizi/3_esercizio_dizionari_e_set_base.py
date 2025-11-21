"""
La segreteria dell'evento ti ha passato l'export delle registrazioni web (lista registrazioni)
lamentandosi che il form ha permesso invii multipli creando dei duplicati;
il tuo compito è stampare a video la lista pulita dei partecipanti unici
(basandoti sulle loro email per distinguerli) per preparare i badge e, successivamente,
generare un piccolo report statistico che indichi quante persone partecipano per
ogni singola azienda, così da sapere chi sono i partner principali.
"""

registrazioni = [
    {"nome": "Alice", "azienda": "Google", "email": "alice@google.com"},
    {"nome": "Bob", "azienda": "Amazon", "email": "bob@amazon.com"},
    {"nome": "Alice", "azienda": "Google", "email": "alice@google.com"}, # Duplicato
    {"nome": "Charlie", "azienda": "Microsoft", "email": "charlie@ms.com"},
    {"nome": "David", "azienda": "Amazon", "email": "david@amazon.com"},
    {"nome": "Eve", "azienda": "Google", "email": "eve@google.com"},
    {"nome": "Bob", "azienda": "Amazon", "email": "bob@amazon.com"}, # Duplicato
    {"nome": "Frank", "azienda": "Facebook", "email": "frank@fb.com"}
]
