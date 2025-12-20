"""
Scrivere una funzione ricorsiva che dato n calcoli l'enne-simo numero di fibonacci (partendo da 0, 1)
"""


def fibonacci(n):
    """
    Calcola l'n-esimo numero della sequenza di Fibonacci in modo ricorsivo.

    La sequenza di Fibonacci è: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    dove ogni numero è la somma dei due precedenti.

    Args:
        n: L'indice del numero di Fibonacci da calcolare (n >= 0)

    Returns:
        L'n-esimo numero di Fibonacci
    """
    # Casi base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso ricorsivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Test della funzione
    print("Sequenza di Fibonacci (primi 15 numeri):")
    for i in range(15):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    # Test con alcuni valori specifici
    print(f"\nTest aggiuntivi:")
    print(f"fibonacci(10) = {fibonacci(10)}")  # Dovrebbe essere 55
    print(f"fibonacci(20) = {fibonacci(20)}")  # Dovrebbe essere 6765
