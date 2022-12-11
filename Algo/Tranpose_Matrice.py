from numpy import array
import random


def remplir(n):
    n = random.randint(5, 15)
    M = array(array([[int()]*n]*n))
    for i in range(n):
        for j in range(n):
            M[i, j] = random.randint(10, 99)
    return M


def Tranpose_Mat(n, M):
    for i in range(n):
        for j in range(i, n):
            M[i, j], M[j, i] = M[j, i], M[i, j]
    # return M


def affichier(n, M):
    for i in range(n):
        for j in range(n):
            print(M[i, j], end=" ")
        print()
    print("Done")


n = random.randint(3, 3)
M = remplir(n)
affichier(n, M)
Tranpose_Mat(n, M)
affichier(n, M)
