def saisir_rec():
    n = int(input("Donner un entier positif: "))
    return n if n in range(2, 11) else saisir_rec()


print(saisir_rec())
