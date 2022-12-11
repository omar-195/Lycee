class livre:
    ref = str()
    nom = str()
    prix = float()


def saisir():
    """Saisie d'un nombre entier"""
    n = int(input("Saisir un nombre entier : "))
    while n not in range(2, 51):
        n = int(input("Saisir un nombre entier : "))
    mt = float(input("Entrer le montant total : "))
    while mt < 0:
        mt = float(input("Entrer le montant total : "))
    return n, mt


def Valide(ch):
    """Valide le nom du livre"""
    i = 0
    while i < len(ch) and (ch[i] == " " or ch[i].isalpha() or ch[i].isdigit()):
        i += 1
    return len(ch) <= i


def remplir(T, n):
    """Remplir 3 table"""
    for i in range(n):
        T[i].ref = input(f"Saisir la reference N° {i+1}: ")
        while len(T[i].ref) != 8 and T[i].ref.isdigit() == False:
            T[i].ref = input(f"Saisir la reference N° {i+1}: ")
        #
        T[i].nom = input(f"Saisir la nom du livre N° {i+1}: ")
        while not Valide(T[i].nom):
            T[i].nom = input(f"Saisir la nom du livre N° {i+1}: ")

        T[i].prix = float(input(f"Saisir le prix du livre N° {i+1}: "))
        while T[i].prix < 0:
            T[i].prix = float(input(f"Saisir le prix du livre N° {i+1}: "))


def trier_1(T, n):
    """Trier les table"""
    change = True
    while change and n != 1:
        change = False
        for i in range(n-1):
            if T[i].prix < T[i+1].prix:
                change = True
                T[i], T[i+1] = T[i], T[i+1]
        n -= 1


def recherche_pos_max(T, d, f):
    m = d
    for i in range(d+1, f):
        if T[m].prix < T[i].prix:
            m = i
    return m


def trier_selection(T, n):
    for i in range(n-2):
        pos = recherche_pos_max(T, i+1, n)
        if T[i].prix < T[pos].prix:
            T[i], T[pos] = T[pos], T[i]


def Afficher(T, n, mt):
    """Afficher les table"""
    print("Reference\tNom\tPrix\tPrix_total\trestant")
    i = 0
    pt = 0
    while i < n and mt - T[i+1].prix >= 0 and mt != 0:
        pt = pt + T[i].prix
        print(
            f"{T[i].ref}\t{T[i].nom}\t{T[i].prix}\t{pt}\t{mt-pt}")
        i += 1

# Autre method pour trier un tableau


# Programme principal
n, mt = saisir()
T = [livre()] * 50
remplir(T, n)
trier_1(T, n)
Afficher(T, n, mt)
