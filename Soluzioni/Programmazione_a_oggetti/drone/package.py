"""
Classe Package per il sistema di ottimizzazione flotta droni
"""


class Package:
    """Rappresenta un pacco da spedire"""

    def __init__(self, pkg_id, content, weight, value):
        """
        Inizializza un pacco.

        Args:
            pkg_id: ID univoco del pacco
            content: Descrizione contenuto
            weight: Peso in kg
            value: Valore in euro
        """
        self.id = pkg_id
        self.content = content
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.id} [{self.content}] - {self.weight}kg (€{self.value})"

    def __repr__(self):
        return self.__str__()
