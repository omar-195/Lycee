def remplir(ft, rep):
    if rep != "NON":
        ch = input("Donner une phrase : ")
        ft.write(ch+"\n")
        rep = input("Ajouter une autre phrase OUI/NON : ")
        remplir(ft, rep)


def remplir_tab():
    #

def remplacer():
    T = remplir_tab()
    # for i in range(0, len(


ft = open("intiale.txt", "w")
remplir(ft, "OUI")
