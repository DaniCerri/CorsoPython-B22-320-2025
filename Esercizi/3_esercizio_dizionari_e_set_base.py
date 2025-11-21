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

# 1. Creiamo un elenco di persone "uniche" che partecipano all'evento
# 1.1. Creiamo un set vuoto dove tenere i partecipanti unici
set_partecipanti = set()  # Non usiamo '{}' per fare un set vuoto, perchè per python questo sarebbe un dizionario vuoto
lista_partecipanti = []   # Creiamo una lista vuota in cui mettiamo i partecipanti

# 1.2. Facciamo un ciclo attraverso le registrazioni
for registrazione in registrazioni:
    # 1.3. Se non abbiamo già salvato la persona, ce la salviamo
    if registrazione['email'] not in set_partecipanti:  # Ci chiediamo se la mail NON è all'interno del set con le mail viste finora
        set_partecipanti.add(registrazione['email'])  # Salviamo la mail nel set, per i prossimi controlli
        lista_partecipanti.append(registrazione)  # Salviamo tutti i dati del nuovo partecipante

# 1.4 Stampiamo le partecipazioni ottenute
for indice, partecipazione in enumerate(lista_partecipanti):
    print(f"Partecipante {indice + 1}: ")
    print(f" * Nome: {partecipazione['nome']}")
    print(f" * Azienda: {partecipazione['azienda']}")
    print(f" * Email: {partecipazione['email']}")

# 2. Creiamo l'elenco di aziende con il numero di partecipanti
# 2.1 Creiamo un dizionario vuoto in cui salveremo le coppie "azienda: n_partecipanti_dell_azienda"
diz_affluenza_aziende = {}  # Creiamo un dizionario vuoto in cui salveremo i conteggi delle persone per ogni azienda

# 2.2 Per ogni persona unica, aggiorniamo il contatore associata alla sua azienda nel dizionario
for partecipazione in lista_partecipanti:
    # Se abbiamo già visto l'azienda, prendiamo il dizionario alla chiave nome_azienda e incrementiamo il conteggio di 1
    # Se non abbiamo mai visto l'azienda (all'interno di questo for), creiamo la coppia nome_azienda: 1
    nome_azienda = partecipazione['azienda']  # Mettiamo il nome dell'azienda in una variabile

    # Cerchiamo di ottenere il numero di persone che abbiamo visto finora che lavorano per l'azienda della persona attuale.
    # Se troviamo questa azienda nel dizionario, otteniamo il numero, altrimenti, vuol dire che non avevamo ancora trovato
    # nessuna persona che lavora per questa azienda, quindi il contatore vale 0
    contatore_azienda = diz_affluenza_aziende.get(nome_azienda, 0)

    # Siccome abbiamo trovato ora una persona in più che lavora per questa azienda, incrementiamo il contatore di 1
    contatore_azienda += 1  # -> contatore_azienda = contatore_azienda + 1

    # Aggiorniamo il valore all'interno del dizionario
    diz_affluenza_aziende[nome_azienda] = contatore_azienda

# 2.3 Stampiamo il resoconto con le aziende partecipanti
for azienda, n_persone in diz_affluenza_aziende.items():
    # TODO: Gestire il print se la persona è una sola
    print(f"Per l'azienda {azienda} verranno {n_persone} persone")



