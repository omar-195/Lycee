from pickle import *

"""Lire un fichier binaire et afficher les données"""

with open("tableau.dat", "rb") as file:
    while True:
        try:
            print(load(file))
        except EOFError:
            break
