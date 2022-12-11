def saisir():
    x = float(input("Entrez un nombre entier positif: "))
    while x < 0:
        x = float(input("Entrez un nombre entier positif: "))
    y = int(input("Entrez la puissance positif: "))
    while y < 0:
        y = int(input("Entrez la puissance positif: "))
    return x, y


def puiss(x, y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        return x * puiss(x, y - 1)


x, y = saisir()
print(puiss(x, y))
