def saisir():
    n = int(input("Entrez un nombre entier positif: "))
    while n < 0:
        n = int(input("Entrez un nombre entier positif: "))
    return n


def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n * factorielle(n - 1)


n = saisir()
print(factorielle(n))
