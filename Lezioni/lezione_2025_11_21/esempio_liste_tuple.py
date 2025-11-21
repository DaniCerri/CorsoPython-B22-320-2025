lista_spese = [
    122.1, 145.2, 172.9,
     92.3, 123.2,  75.2,
    132.1, 123.2,  89.5,
     56.3, 152.2, 164.8,
]

print(f"Lunghezza lista: {len(lista_spese)}")
print(f"Somma della lista: {sum(lista_spese)}")
print(f"Media della lista: {(sum(lista_spese) / len(lista_spese)):.3f}")
print(f"Massimo della lista: {max(lista_spese)}")
print(f"Minimo della lista: {min(lista_spese)}")

# Prendiamo le spese da febbraio a giugno compresi
print(f"Spese da Febbraio a Giungo [compresi]: {lista_spese[1:6]}")

# Prendiamo le spese da gennaio a marzo compresi
print(f"Spese da Gennaio a Marzo [compresi]: {lista_spese[:3]}")

# Prendiamo le spese da settembre a dicembre compresi
print(f"Spese da Settembre a Dicembre [compresi]: {lista_spese[8:]}")

# Prendiamo le spese da giugno a dicembre, in ordine inverso
print(f"Spese da Giugno a Dicembre [compresi]: {lista_spese[5:][::-1]}")  # [::-1] inverte la lista
# TODO: provare a prende le spese da giugno a dicembre, con una sola indicizzazione -> [p:f:-1]

# Prendiamo le spese da gennaio a dicembre, solo dei mesi con posto pari (0 -> pari)
print(f"Spese dei mesi pari: {lista_spese[::2]}")

# Prendiamo le spese da gennaio a dicembre, solo dei mesi con posto dispari (0 -> pari)
print(f"Spese dei mesi dispari: {lista_spese[1::2]}")

# Prendiamo l'ultimo elemento
print(f"Ultimo elemento lista: {lista_spese[-1]}")

lista_spese[9] = "ottobre"
print(lista_spese)

tupla_mesi = (
    'Gen', 'Feb', 'Mar',
    'Apr', 'Mag', 'Giu',
    'Lug', 'Ago', 'Set',
    'Ott', 'Nov', 'Dic'
)

print(f"Lunghezza della tupla: {len(tupla_mesi)}")
print(f"Max della tupla: {max(tupla_mesi)}")
print(f"Min della tupla: {min(tupla_mesi)}")
print(f"Indicizzazioni della tupla: {tupla_mesi[:5]}, {tupla_mesi[6:]}, {tupla_mesi[7:9][::-1]}")