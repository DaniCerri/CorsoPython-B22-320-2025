set_ingredienti = {
    "Sale", "Pepe", "Uova",
    "Zucchero", "Latte", "Mele",
    "Cannella"
}  # Set con gli ingredienti in dispensa

set_torta_di_mele = {
    "Uova", "Zucchero", "Latte", "Mele", "Vaniglia"
}  # Ingredienti necessari per la torta di mele

# Capiamo se ci sono degli ingredienti che non abbiamo per fare la torta di mele
ingredienti_mancanti = set_torta_di_mele - set_ingredienti
print(f"Ingredienti mancanti per la torta di mele: {ingredienti_mancanti}")

set_crema_pasticcera = {
    "Limone", "Uova", "Zucchero", "Farina"
}

# Vogliamo sapere quali sono tutti gli ingredienti necessari per fare entrambe le ricette
ingredienti_per_entrambe = set_torta_di_mele | set_crema_pasticcera # -> | unisce i due insiemi
print(f"Ingredienti per fare tutte e due le ricette: {ingredienti_per_entrambe}")

# Vogliamo sapere quali ingredienti le due ricette hanno in comune
ingredienti_comuni = set_torta_di_mele & set_crema_pasticcera  # -> & fa l'intersezione degli insiemi
print(f"Ingredienti comuni: {ingredienti_comuni}")

# Metodi per i set
# Per aggiungere un elemento alla dispensa
set_ingredienti.add("Farina")

# Per rimuovere un elemento dalla dispensa
# set_ingredienti.discard("Mele")
# print(f"Ingredienti dopo aver tolto le mele [discard]: {set_ingredienti}")
set_ingredienti.remove("Mele")  # Dà errore se non trova le mele
print(f"Ingredienti dopo aver tolto le mele [remove]: {set_ingredienti}")
set_ingredienti.discard("Mele")  # Non dà errore se non trova le mele
print(f"Ingredienti dopo aver tolto le mele [discard]: {set_ingredienti}")