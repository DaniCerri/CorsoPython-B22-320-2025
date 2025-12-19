class Prodotto:
    def __init__(self, nome: str, prezzo: float, sono_allergico=False):
        self.nome = nome
        self.prezzo = prezzo
        self.sono_allergico = sono_allergico

    @classmethod
    def from_dict(cls, dati_json):
        return cls(
            nome=dati_json['nome'],
            prezzo=dati_json['prezzo'],
            sono_allergico=dati_json['sono_allergico']
        )

    def __str__(self):
        nota = "* Attenzione all'allergia" if self.sono_allergico else ""
        # if self.sono_allergico:
        #     nota = "Attenzione all'allergia"
        # else:
        #     nota = ""
        return f"{self.nome}: {self.prezzo} € {nota}"