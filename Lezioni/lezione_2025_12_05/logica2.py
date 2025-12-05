import matplotlib.pyplot as plt

"""
Dato un numero n positivo, restituire una lista con i primi n numeri di fibonacci
"""
def lista_fibonacci(n: int) -> list[int]:
    # 0 1 1 2 3 5 8 13 21 ...
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci = [0, 1]

    for i in range(2, n):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

    return fibonacci

"""
Dato un numero n positivo, restituire l'enne-simo numero di fibonacci (partendo da 0, 1)
"""
def calc_fibonacci(n: int) -> int:
    # fib[i] = fib[i-2] + fib[i-1]
    if n == 1:
        return 0
    if n == 2:
        return 1

    finestra = [0, 1, 1]
    for i in range(2, n):
        finestra[2] = finestra[0] + finestra[1]
        finestra[0] = finestra[1]
        finestra[1] = finestra[2]

    return finestra[2]

"""
Scriviamo un while per ottenere la sequenza di Collatz di n
"""
def sequenza_collatz(n: int) -> list[int]:
    sequenza = []
    while n != 1:  # Finché n rimane diverso da 1
        if n % 2 == 0:
            n //= 2  # <- n = n // 2
        else:
            n = n * 3 + 1  # n *= 3, n += 1

        sequenza.append(n)
    return sequenza

def plot_sequenza(lista: list[int]) -> None:
    plt.plot(lista)
    plt.show()

if __name__ == "__main__":
    print(lista_fibonacci(20))
    print(calc_fibonacci(20))
    plot_sequenza(sequenza_collatz(15))
