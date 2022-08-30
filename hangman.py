
import random

def select(liste):
    n=len(liste)
    i=random.randint(0,n-1)
    return liste[i]

def recup_cara():
    c=input('entrer un caractère:\n')
    return c

def comparaison(mot,cara):
    for i in mot:
        if i==cara:
            return True
    return False

def partie():
    print('===============================')
    print('=          HANGMAN            =')
    print('===============================')
    liste=['papa','maman','devise','pays','haine']
    mot=select(liste)
    taille=len(mot)
    aff=('-'*taille)
    print(aff)
    pv=10

    
    while pv>0:
        cara=recup_cara()
        check=comparaison(mot,cara)
        if check== True:
            compteur=0
        
            for i in  mot:
                if i==cara:
                        taille=len(mot)
                        l=list(aff)
                        p=compteur
                        l[p]=str(cara)
                        aff="".join(l)
                compteur +=1  
            print (aff)
            if aff==mot:
                print('vous avez gagné\n')
                break
    
        if check== False:
            print("ce n'est pas le bon caractère\n")
            print(aff)
        pv=pv-1
    if pv==0:
        print('vous avez perdu')
partie()

