import random

liste=["banane","lion","avion","voiture","camion","maison","collège","cours","arc-en-ciel","ciel"]
lettres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
motsecret=str(liste[random.randint(0, len(liste)-1)])
affichage=[]
toguess=0
good=0
bad=0
for lettre in motsecret:
    if lettre in lettres:
        affichage.append("_")
        toguess=toguess+1
    else :
        affichage.append(lettre)
while good != toguess:
    txt="".join(affichage)
    print(txt)
    guess=str(input("Quelle lettre ?"))
    if guess in motsecret and guess not in txt:
        indices = [i for i, lettre in enumerate(motsecret) if lettre == guess]
    else :
        indices=[]
        bad=bad+1
    for i in range(len(indices)):
        indexx=indices[i]
        good=good+1
        del affichage[indexx]
        affichage.insert(indexx, guess)     
    indices=[]
print("Bravo, c'était bien :", motsecret, "et tu as trouvé avec", good+bad, "essais.")

