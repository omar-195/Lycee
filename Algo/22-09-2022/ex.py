def saisir():
    """Saisie d'un nombre entier"""
    n = int(input("Saisir un nombre entier : "))
    while n not in range(5, 51):
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


def remplir(T1, T2, T3, n):
    """Remplir 3 table"""
    for i in range(n):
        T1[i] = input(f"Saisir la reference N° {i+1}: ")
        while len(T1[i]) != 8 and T1[i].isdigit() == False:
            T1[i] = input(f"Saisir la reference N° {i+1}: ")
        #
        T2[i] = input(f"Saisir la nom du livre N° {i+1}: ")
        while not Valide(T2[i]):
            T2[i] = input(f"Saisir la nom du livre N° {i+1}: ")

        T3[i] = float(input(f"Saisir le prix du livre N° {i+1}: "))
        while T3[i] < 0:
            T3[i] = float(input(f"Saisir le prix du livre N° {i+1}: "))


def trier_1(T1, T2, T3, n):
    """Trier les table"""
    change = True
    while change and n != 1:
        change = False
        for i in range(n-1):
            if T3[i] < T3[i+1]:
                change = True
                T1[i], T1[i+1] = T1[i+1], T1[i]
                T2[i], T2[i+1] = T2[i+1], T2[i]
                T3[i], T3[i+1] = T3[i+1], T3[i]
        n -= 1


def Afficher(T1, T2, T3, n, mt):
    """Afficher les table"""
    print("Reference\tNom\tPrix\tPrix_total\trestant")
    i = 0
    pt = 0
    while i < n and mt - T3[i+1] >= 0 and mt != 0:
        pt = pt + T3[i]
        print(
            f"{T1[i]}\t{T2[i]}\t{T3[i]}\t{pt}\t{mt-pt}")
        i += 1

# Autre method pour trier un tableau


def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def trierRapide(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        trierRapide(l, pi-1, nums)
        trierRapide(pi+1, r, nums)
    return nums


# Programme principal
n, mt = saisir()
T1, T2 = [str()] * 50, [str()] * 50
T3 = [int()] * 50
remplir(T1, T2, T3, n)
trier_1(T1, T2, T3, n)
Afficher(T1, T2, T3, n, mt)
