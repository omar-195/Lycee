from numpy import*
from random import*
def saisir():
    n=int(input("entrer la taille"))
    while not( 20<=n<=100):
        n=int(input("entrer la taille"))
    return(n)

def remplir(n):
    
    for i in range(n):
        t[i]=randint(10,99)
    return t

def affiche(t,n):
    
    for i in range(n):
        print(t[i],end='  ')


#module determine pos max
def posMax(t,n):
    pmax=0
    for i in range(1,n):
        if(t[i]>t[pmax]):
            pmax=i
    return pmax
#module determine pos min
def posMin(t,n):
    pmin=0
    for i in range(1,n):
        if(t[i]<t[pmin]):
            pmin=i
    return pmin
#Tri par création d un nouveau tableau
def tricreation(t,n,v):
    for i in range(n):
        v[i]=t[posMin(t,n)]
        t[posMin(t,n)]=t[posMax(t,n)]

#___________PROGRAMME PRINCIPAL___________
n=saisir()
t=array([int()]*n)
v=array([int()]*n)
t=remplir(n)
print('tableau non trié')
affiche(t,n)
tricreation(t,n,v)
print('\ntableau trié')
affiche(v,n)