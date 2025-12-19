from datetime import datetime

class Fattura:
    def __init__(self, id_fattura: str, data: str, cliente: str, descrizione: str, importo: float):
        self.id_fattura = id_fattura
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.cliente = cliente
        self.descrizione = descrizione
        self.importo = importo

    @classmethod
    def from_dict(cls, dati_json):
        return cls(
            id_fattura=dati_json['id'],
            data=dati_json['data'],  # <- datetime.strptime(dati_json['data'], "%Y-%m-%d"),
            cliente=dati_json['cliente'],
            descrizione=dati_json['descrizione'],
            importo=dati_json['importo']
        )

    def __str__(self):
        output = f"ID: {self.id_fattura}, Data: {self.data}, Importo: {self.importo:.2f}"
        return output
