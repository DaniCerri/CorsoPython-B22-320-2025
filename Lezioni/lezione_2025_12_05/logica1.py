"""
Scrivere una funzione che data una lista di numeri restituisce una lista di stringhe di questo tipo:
 * Se il numero nella lista di input è multiplo di 3 -> al suo posto ci mette "AAAA"
 * Se il numero nella lista di input è multiplo di 5 -> al suo posto ci mette "BBBB"
 * Se il numero nella lista di input è multiplo di 15 -> al suo posto ci mette "AABB"
 * Altrimenti mette la stringa del numero della lista di input
"""
def sost_multipli(lista: list[int]) -> list[str]:
    output = []
    for elemento in lista:
        if elemento % 15 == 0:
            output.append("AABB")
        elif elemento % 5 == 0:
            output.append("BBBB")
        elif elemento % 3 == 0:
            output.append("AAAA")
        else:
            output.append(str(elemento))
    return output

"""
Scrivere una funzione che data una lista di n numeri capisca quale numero da 0 a n manca al range
es: [3, 0, 1] -> 2
es: [1, 2, 5, 6, 3, 0] -> 4  
"""
def trova_mancante(lista: list[int]) -> int:
    # Otteniamo la lunghezza della lista -> che è l'estremo del range di riferimento
    lunghezza = len(lista)
    somma_desiderata = lunghezza * (lunghezza + 1) // 2
    somma_attuale = sum(lista)

    return somma_desiderata - somma_attuale

"""
Scrivere una funzione che dato un numero >= 0 calcoli la somma dei dispari fino a quel numero (compreso)
"""
def somma_dispari(num: int) -> int:
    if num % 2 == 1:
        num += 1
    return (num // 2) ** 2

"""
Scrivere una funzione che dato un numero >= 0 calcoli la somma dei pari fino a quel numero (compreso)
"""
def somma_pari(num: int) -> int:
    ...

if __name__ == "__main__":
    # Test delle funzioni
    lista_1 = [12, 4, 17, 25, 45, 10, 23, 9, 18]
    print(sost_multipli(lista_1))
    # <- ["AAAA", "4", "17", "BBBB", "AABB", "BBBB", "23", "AAAA", "AAAA"]

    print(f"Mancante nel range: {trova_mancante([3, 0, 1, 5, 2, 7, 4])}")
    massimo = 6
    print(f"Somma numeri dispari fino a {massimo}: {somma_dispari(massimo)}")
    # print(f"Somma numeri pari fino a {massimo}: {somma_pari(massimo)}")
