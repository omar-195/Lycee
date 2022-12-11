import sys
from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget


def saisir():
    n = int(input("Saisir un nombre entier: "))
    while n < 1000:
        n = int(input("Saisir un nombre entier: "))
    return n


def calc(x, ch):
    nbr = 0
    for i in range(len(ch)):
        if int(ch[i]) == x:
            nbr += 1
        # print(i, ch[i], x, nbr)
    return nbr


def verifRec(ch, i):
    if i < len(ch)-1 and int(ch[i]) == calc(i, ch):
        return verifRec(ch, i+1)
    else:
        return i == len(ch)-1


def mainFn():
    if window.nbr.text().isdigit() == False or len(window.nbr.text()) < 4:
        window.resTxt.setText(
            "Le nombre doit être un entier et supérieur à 1000")
    else:
        if verifRec(window.nbr.text(), 0):
            window.resTxt.setText(
                f"Le nombre {window.nbr.text()} est autodescriptif")
        else:
            window.resTxt.setText(
                f"Le nombre {window.nbr.text()}  n'est pas autodescriptif")


app = QApplication([])
window = loadUi("app1_Qt.ui")
window.btn.clicked.connect(mainFn)
window.show()
app.exec()
