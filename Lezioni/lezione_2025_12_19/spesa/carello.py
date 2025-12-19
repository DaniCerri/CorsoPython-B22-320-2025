from prodotto import Prodotto


class Carrello:
    def __init__(self, budget: float):
        self.budget = budget
        self.prodotti = []
        self.totale = 0

    def aggiungi(self, prodotto: Prodotto):
        # Controllare se il prodotto può essere aggiunto senza sforare il budget.
        # In tal caso aggiungerlo, altrimenti restituire un False.

        # Prima di controllare se possiamo aggiungerlo per budget, controlliamo di non essere allergici
        if prodotto.sono_allergico:
            return False

        if self.totale + prodotto.prezzo > self.budget:
            return False

        self.prodotti.append(prodotto)
        self.totale += prodotto.prezzo
        return True

    def __str__(self):
        output = "Elenco prodotti: \n"
        for prodotto in self.prodotti:
            output += f" * {str(prodotto)} \n"

        output += f"Totale: {self.totale:.2f} €"
        return output