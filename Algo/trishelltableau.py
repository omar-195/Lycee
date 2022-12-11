from random import*
from numpy import*



def saisie():
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
        
        
        p=p//3
        

#programme principale
n=saisie()
t=array([int()]*n)
remplir(n)
print('avant tri')
affiche(t,n)
tri_shell(t,n)
print("\n")
print('après tri')
affiche(t,n)
