def cryptage(mot=str(),cle=int()):
    mot=mot.upper()
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    crypt=""
    for i in mot:
        j=alphabet.index(i)
        crypt=crypt+(alphabet[j+cle])
    print(crypt)

# cryptage(mot='SALUT',cle=3)


def decryptage(mot=str(),cle=int()):
    mot=mot.upper()
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    crypt=""
    for i in mot:
        j=alphabet.index(i)
        crypt=crypt+(alphabet[j-cle])
    print(crypt)

decryptage(mot='',cle=3)