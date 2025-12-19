import random

# Definiamo il seed di random
random.seed(42)  # Facciamo questa cosa per rendere riproducibili i nostri test e non avere ad ogni esecuzione
# dei valori diversi

class ContoCorrente:  # Dichiariamo una nuova classe chiamata "ContoCorrente"
    # Per prima cosa definiamo il metodo costruttore
    def __init__(self, importo_iniziale: float, titolare: str):  # <- Unica metodologia per definire il costruttore
        """
        Inizializza un oggetto "ContoCorrente" con un importo iniziale e il nome completo del titolare
        :param importo_iniziale: Importo di deposito iniziale in €
        :param titolare: Nome e Cognome del titolare, es: "Daniele Cerrina"
        """
        self.importo = importo_iniziale  # Creiamo un attributo "importo" della nostra classe e ci assegniamo il valore
        # Passato dall'esterno dell'importo iniziale
        self.titolare = titolare  # Creiamo un attributo "titolare" della nostra classe e ci assegniamo il valore
        # Passato dall'esterno del nome del titolare
        self.iban = self.calcola_IBAN()  # Possiamo anche creare degli attributi da zero, senza input esterni

    def deposito(self, importo_da_depositare: float):
        """
        Prende un importo in € e lo aggiunge al saldo del conto corrente
        :param importo_da_depositare: Importo in €
        """
        self.importo += importo_da_depositare  # Aggiungiamo all'attributo "importo" della nostra classe i soldi dell'
        # importo da depositare

    def prelievo(self, importo_da_prelevare: float) -> bool:
        """
        Dato un importo da prelevare, se possibile, lo toglie dal saldo del conto
        :param importo_da_prelevare: Importo in €
        :return: True se riuscito, False altrimenti
        """
        if importo_da_prelevare > self.importo:  # Controlliamo che si possa il prelievo
            return False  # Se non si può fare, interrompiamo la funzione restituendo False

        # Se non abbiamo interrotto la funzione, vuol dire che il prelievo si può fare, quindi scaliamo i soldi dal saldo
        # del conto
        self.importo -= importo_da_prelevare
        return True

    def calcola_IBAN(self):
        iban = "IT"
        numero = random.randint(1_000_000_000_000_000_000_000_000, 1_999_999_999_999_999_999_999_999)
        return f"{iban}{numero}"

    def __str__(self):
        ## NON mettiamo mai print all'interno di questo metodo
        output = "*" * 50 + "\n"
        output+= f"Titolare: {self.titolare}\n"
        output+= f"Importo: {self.importo} €\n"
        output+= f"IBAN: {self.iban}\n"
        output += "*" * 50
        return output

    def __add__(self, other):
        # Questo metodo gestisce la somma quando il conto corrente è a sinistra: conto + altro
        if isinstance(other, ContoCorrente):
            # Se other è un conto corrente, sommiamo i due importi
            return self.importo + other.importo
        else:
            # Altrimenti sommiamo l'importo attuale + il numero int / float
            return self.importo + other

    def __radd__(self, other):
        # Questo metodo gestisce la somma quando il conto corrente è a destra: altro + conto
        # È necessario per far funzionare sum() su una lista di ContoCorrente
        # sum() inizia con 0, quindi fa: 0 + conto1 + conto2 + ...
        return self.__add__(other)

if __name__ == "__main__":
    # Rapido test della classe
    # 1. Dobbiamo istanziare un oggetto della nostra classe
    conto_personale = ContoCorrente(100, "Daniele Cerrina")
    print(conto_personale)
    # 2. Ora possiamo provare a fare un deposito
    conto_personale.deposito(340.23)
    print(conto_personale)
    # 3. Proviamo ad eseguire un prelievo
    if conto_personale.prelievo(120):
        print("Il prelievo è andato a buon fine")
    else:
        print("Non hai abbastanza soldi nel conto")
    print(conto_personale)
    conto2 = ContoCorrente(674, "Giulia Bianchi")
    print(f"Importo totale: {conto_personale + conto2}")
    print(sum((conto_personale, conto2)))
