def saisir():
    n = int(input("Donner le taille du tableau: "))
    while n < 3:
        n = int(input("Donner le taille du tableau: "))
    return n


def remplirTableauRec(t, i, n):
    if i < n:
        t[i] = int(input(f"Entrez le {i+1}° entier: "))
        remplirTableauRec(t, i+1, n)
    # return t


n = saisir()
t = [int()]*15
remplirTableauRec(t, 0, n)
for i in range(n):
    print(t[i], end=' | ')
