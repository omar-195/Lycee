def saisir():
    n = int(input("Donner le nombre des eleves: "))
    if not n in range(2, 51):
        return saisir()
    else:
        return n


def remplir(T, n):
    for i in range(n):
        T[n]["Nom"] = input(f"Donner le nom du eleve N°{i}: ")
        T[n]["Moy"] = int(input(f"Donner le Moyenne du eleve N°{i}: "))


def supprimer(T, n):
    pos = int(input("Supprimer le nom du eleve N°{i}: "))
    for i in range(pos, n-1):
        T[i] = T[i+1]
    n = n - 1


def insertion(T, n):
    pos = int(input("Supprimer le nom du eleve N°: "))
    for i in range(n, pos+2):
        T[i] = T[i-1]
    T[pos]["Nom"] = input(f"Donner le nom du eleve N°{i}: ")
    T[pos]["Moy"] = int(input(f"Donner le Moyenne du eleve N°{i}: "))
    n += 1


T = [dict()]*51
n = saisir()
remplir(T, n)
insertion(T, n)
