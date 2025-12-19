class Prodotto:
    def __init__(self, nome: str, prezzo: float, sono_allergico=False):
        self.nome = nome
        self.prezzo = prezzo
        self.sono_allergico = sono_allergico

    def __str__(self):
        nota = "* Attenzione all'allergia" if self.sono_allergico else ""
        # if self.sono_allergico:
        #     nota = "Attenzione all'allergia"
        # else:
        #     nota = ""
        return f"{self.nome}: {self.prezzo} € {nota}"