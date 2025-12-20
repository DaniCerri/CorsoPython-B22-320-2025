"""
Scrivere una funzione ricorsiva che dato n calcoli n!
"""


def fattoriale(n):
    """
    Calcola il fattoriale di n in modo ricorsivo.

    Il fattoriale di n (n!) è il prodotto di tutti i numeri interi positivi
    minori o uguali a n.
    Per esempio: 5! = 5 × 4 × 3 × 2 × 1 = 120

    Args:
        n: Numero intero non negativo

    Returns:
        Il fattoriale di n
    """
    # Caso base: 0! = 1 e 1! = 1
    if n == 0 or n == 1:
        return 1
    # Caso ricorsivo: n! = n × (n-1)!
    else:
        return n * fattoriale(n - 1)


if __name__ == "__main__":
    # Test della funzione
    print("Calcolo dei fattoriali:")
    for i in range(11):
        print(f"{i}! = {fattoriale(i)}")

    # Test con alcuni valori specifici
    print(f"\nTest aggiuntivi:")
    print(f"5! = {fattoriale(5)}")   # Dovrebbe essere 120
    print(f"10! = {fattoriale(10)}") # Dovrebbe essere 3628800
