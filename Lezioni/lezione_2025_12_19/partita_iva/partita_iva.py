import json

from fattura import Fattura

class PartitaIva:
    def __init__(self, coeff_reddito: float, coeff_inps: float, coeff_irpef: float):
        self.coeff_reddito = coeff_reddito
        self.coeff_inps = coeff_inps
        self.coeff_irpef = coeff_irpef

        self.lista_fatture = []

    def carica_da_file(self, nome_file: str):# -> bool:
        """
        Dato il nome del file cerca di caricare all'interno della lista_fatture le fatture presenti aggiungendole
        a quelle già caricate
        :param nome_file: nome del file .json
        :return: True se il caricamento va a buon fine, False altrimenti
        """
        # TODO: Gestire tutti i possibili errori (file inesistente o tutte le fatture già importate)
        with open(nome_file) as file_in:
            dati_raw = json.load(file_in)

        nuove_fatture = [Fattura.from_dict(fattura_raw) for fattura_raw in dati_raw]
        self.lista_fatture += nuove_fatture
        # return True

    def fatturato_totale(self):  # TODO: implementare metodo __add__ nella classe Fattura
        totale = 0
        for fattura in self.lista_fatture:
            totale += fattura.importo
        return totale

        # return sum(self.lista_fatture)

    def calcolo_inps(self):
        totale = self.fatturato_totale()
        pagamento_inps = totale * self.coeff_reddito * self.coeff_inps
        return pagamento_inps

    def calcolo_irpef(self):
        totale = self.fatturato_totale()
        pagamento_irpef = totale * self.coeff_reddito * self.coeff_irpef
        return pagamento_irpef

    def calcolo_netto(self):
        totale = self.fatturato_totale()
        inps = self.calcolo_inps()
        irpef = self.calcolo_irpef()

        return totale - (inps + irpef)

    def conta_fatture_per_mese(self) -> dict:
        """
        Conta per ogni mese il numero di fatture emesse
        :return: {"Jan": 2, "Feb": 3, ..., "Dec": 3}
        """
        conteggio_fatture = {
            "Jan": 0, "Feb": 0, "Mar": 0,
            "Apr": 0, "May": 0, "Jun": 0,
            "Jul": 0, "Aug": 0, "Sep": 0,
            "Oct": 0, "Nov": 0, "Dec": 0,
        }

        # Per ogni fattura nel nostro elenco, andiamo a ottenere il valore del conteggio del suo mese
        # e lo incrementiamo di 1
        for fattura in self.lista_fatture:
            mese_fattura = fattura.data.strftime("%b") # Otteniamo il mese della fattura
            # conteggio_fatture[mese_fattura] += 1
            conteggio = conteggio_fatture.get(mese_fattura, 0)
            conteggio_fatture[mese_fattura] = conteggio + 1

        return conteggio_fatture

    # TODO: fare lo stesso ma con i giorni della settimana