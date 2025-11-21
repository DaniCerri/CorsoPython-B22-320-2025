lista_spese = [
    122.1, 145.2, 172.9,
     92.3, 123.2,  75.2,
    132.1, 123.2,  89.5,
     56.3, 152.2, 164.8,
]

# Aggiungere un elemento
lista_spese.append(162.7)
print(f"Lista: {lista_spese}")

# Rimuovere un elemento - con indice
lista_spese.pop(5)  # Rimuove l'elemento ad indice 5 -> Se non mettiamo niente, rimuove l'ultimo elemento
print(f"Lista: {lista_spese}")

# Rimuovere un elemento - con valore
lista_spese.remove(122.1)  # Rimuove il primo elemento con valore 122.1
print(f"Lista: {lista_spese}")

# lista_2 = [9, 2, 2, 9, 4, 5]
# lista_2.remove(9) # -> [2, 2, 9, 4, 5]

# Ordiniamo la lista
# 1 -> Creando una versione ordinata della lista
lista_ordinata = sorted(lista_spese)
# La lista originale rimane disordinata
print(f"Lista ordinata: {lista_ordinata} \nLista spese: {lista_spese}")

# 2 -> "Inplace"
lista_spese.sort()
# Da ora in poi, la lista è ordinata
print(f"Lista spese: {lista_spese}")

# Inserire un elemento a un dato indice
lista_spese.insert(5, 'Prova')
print(f"{lista_spese}")

# Contare quante volte un elemento compare in una lista
count = lista_spese.count(123.2)
print(f"123.2 compare {count} volte")



