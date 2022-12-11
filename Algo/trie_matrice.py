from random import randint
from xml.etree.ElementTree import QName


def saisir():
    x = int(input("Entrez un nombre entier positif: "))
    while x < 0:
        x = int(input("Entrez un nombre entier positif: "))
    return x


def remplir(n):
    M = [[int()]*10]*10
    for i in range(n):
        for j in range(n):
            M[i][j] = randint(0, 99)
    return M


def trier_ligne(M, n, lig, order):
    change = True
    while change:
        change = False
        for j in range(n-1):
            if order == 0:
                if M[lig][j] > M[lig][j+1]:
                    M[lig][j], M[lig][j] = M[lig][j+1], M[lig][j]
                    change = True
            else:
                if M[lig][j] < M[lig][j+1]:
                    M[lig][j], M[lig][j+1] = M[lig][j+1], M[lig][j]
                    change = True


def trier_matrice(n, M):
    for _ in range(n):
        trier_ligne(M, n, _, _ % 2)


n = saisir()

M = remplir(n)
for i in range(n):
    print(M[i])
print("----------------------------------------------------------------")
trier_matrice(n, M)
for i in range(n):
    print(M[i])
