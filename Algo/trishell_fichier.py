from random import*
from numpy import*
import pickle as pk


def saisie():
    n=int(input("entrer la taille"))
    while not( 20<=n<=100):
        n=int(input("entrer la taille"))
    return(n)

def remplir(n):
    f=open("nombre.dat","wb")
    for i in range(n):
        e=randint(10,99)
        pk.dump(e,f)
    f.close()

def transfert (t,n):
    f=open("nombre.dat","rb")
    for i in range(n):
        t[i]=pk.load(f)
        
        
    f.close()


def affiche(t,n):
    ft=open("etape.txt","a")
    for i in range(n):
        ft.write(str(t[i]) + "|")
    
    ft.write("\n")
    ft.close()


def tri_shell(t,n):
    p=1
    while ((p*3)+1 <n):
        p=p*3+1
        
    while(p>=1):
        for i in range (p,n):
            aux=t[i]
            j=i
            while(j>p-1) and (t[j-p] > aux)  :
                t[j]=t[j-p]
                j=j-p
            t[j]=aux
        
        affiche(t,n)
        p=p//3
        

#programme principale
n=saisie()
t=array([int()]*n)
remplir(n)
transfert(t,n)
ft=open("etape.txt","w")
ft.close()
tri_shell(t,n)