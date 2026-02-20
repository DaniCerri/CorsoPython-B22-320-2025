import pytest

# 1. Facciamo la classe da testare
class DataProcessor:
    def __init__(self, db_connection):
        self.db = db_connection

    def process_data(self, user_id):
        data = self.db.get_data(user_id)
        if not data:
            raise ValueError("Nessun dato trovato per l'utente")

        return {
            "status": "success",
            "items": [item.upper() for item in data]
        }

# 2. Preparazione dell'ambiente per le fixtures
# 2.1 Andiamo a creare una "finta" istanza del database
class MockDatabase:
    def get_data(self, user_id):
        if user_id == 1:
            return ['item_a', 'item_b', 'item_c']
        return []

# 2.2 Facciamo le nostre fixtures <- rappresentano le condizioni iniziali per il nostro test
@pytest.fixture
def mock_db():
    """Fixture che fornisce un db fittizio"""
    db = MockDatabase()
    yield db   # Cediamo il controllo del DB al test, passando l'oggetto DB

    # Qua di solito mettiamo le fasi finali, es: chiusura connessioni, chiusura file, ...+

@pytest.fixture
def processor(mock_db):
    """La fixture che istanza il DataProcessor con il database fasullo ottenuto dalla fixture scritta prima"""
    return DataProcessor(db_connection=mock_db)

# 3. Definiamo le funzioni di test
def test_process_data_success(processor):
    """Testiamo il percorso funzionante"""
    # Utilizziamo le fixture per testare il nostro DataProcessor, quando lo user_id è 1. Ci aspettiamo un risultato di
    # 'success'
    result = processor.process_data(user_id=1)

    # Controlliamo il risultato, utilizzando gli assert nativi di python
    assert result['status'] == "success"
    assert len(result['items']) == 3
    assert result['items'][0] == "ITEM_A"

def test_process_data_not_found(processor):
    """Testiamo il DataProcessor quando non dovrebbe trovare nulla"""
    # Vogliamo controllare che venga sollevata la corretta eccezione
    with pytest.raises(ValueError, match="Nessun dato trovato per l'utente"):
        processor.process_data(user_id=99)