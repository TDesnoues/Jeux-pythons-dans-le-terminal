import random

invités = ["Mme Leblanc","Colonel Moutarde","Professeur Violet","Mlle Rose","Révérend Olive","Mme Pervenche"]
armes = ["la clé anglaise","le chandelier","la matraque","le revolver","le poignard","la corde"]
pièces = ["la salle de billard","le salon","la salle de bal","la salle à manger","le hall","la cuisine","le bureau","la véranda","la bibliothèque"]

def GetDeck():
    dead = invités[random.randint(0, len(invités)-1)]
    invités.remove(dead)
    killer = invités[random.randint(0, len(invités)-1)]
    killertool = armes[random.randint(0, len(armes)-1)]
    killerlocation = pièces[random.randint(0, len(pièces)-1)]
    deck = [dead, killer, killertool, killerlocation]
    return deck

deck = GetDeck()
print("Bonjour Inspecteur, j'ai une très mauvaise nouvelle !")
print(deck[0], "n'est plus des nôtres !")
print("Dans ses derniers mots, la victime m'as confié que c'étais ########## qui souhaitais se venger.")
print("A vous de retrouver le tueur !")
print()

while True:
    print(invités)
    print("")
    killer = int(input("Entre l'ID de celui que tu pense être le tueur (1, 2, 3, 4, 5)"))-1
    print("")
    print("----------------------------------------------------------------------")
    print("Donc, pour toi,", invités[killer], "aurais tué", deck[0], "? Mais où ?")
    print("----------------------------------------------------------------------")
    print("")
    print(pièces)
    print("")
    killerlocation = int(input("Entre l'ID de la pièce que tu pense être celle du crime (1, 2, 3, 4, 5, 6, 7, 8, 9) :"))-1
    print("")
    print("-------------------------------------------------------------------------------")
    print("Hmmm, dans", pièces[killerlocation], " tu pense ? Soit, mais avec quelle arme ?")
    print("-------------------------------------------------------------------------------")
    print("")
    print(armes)
    print("")
    killertool = int(input("Entre l'ID de l'arme que tu pense être celle du crime (1, 2, 3, 4, 5, 6) :"))-1
    print("")
    print("-------------------------------------------------------------------------------------------------------------")
    print("Doonc, tu pense que", invités[killer], "aurais tué", deck[0], "dans", pièces[killerlocation], "avec", armes[killertool], "? Après tout, c'est toi l'inspecteur.")
    print("alors, ...")
    score=0
    if invités[killer] == deck[1] :
        score = score + 1
    if pièces[killerlocation] == deck[3] :
        score = score + 1
    if armes[killertool] == deck[2] :
        score = score + 1
    print("tu as", score, "bons choix")
    if score == 3 :
        print("---------------------------------------BRAVO---------------------------------------")
        print("c'étais bien", invités[killer], "qui as tué", deck[0], "dans", pièces[killerlocation], "avec", armes[killertool], "!")
        break
    print("-------------------------------------------------------------------------------------------------------------")
    print("")
