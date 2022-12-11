from json import load
from pickle import dump


def Lecteur():
    T = [int()]*100
    n = int(input("Donner le taille du tableau : "))
    while n < 0:
        n = int(input("Donner le taille du tableau : "))

    for i in range(n):
        T[i] = int(input(f"Donner le nombre N° {i+1}: "))
        dump(T[i], open("tableau.dat", "ab"))

    dump("------------------------------------", open("tableau.dat", "ab"))
    return T, n


def tri_inserstion(T, n):
    """trier un tableau en tri par insertion"""
    for i in range(n):
        print(T[i], end=" | ")
    print()
    for i in range(1, n):
        temp = T[i]
        j = i - 1
        while j >= 0 and T[j] > temp:
            T[j+1] = T[j]
            j = j-1
        T[j+1] = temp
    for i in range(n):
        dump(T[i], open("tableau.dat", "ab"))


def afficher():
    f = open("tableau.dat", "rb")
    fin_fichier = False
    while not fin_fichier:
        try:
            print(load(f))
        except:
            fin_fichier = True


T, n = Lecteur()
tri_inserstion(T, n)
afficher()
