import random
import os

l1 = [" ", " ", " "]
l2 = [" ", " ", " "]
l3 = [" ", " ", " "]


def render(l1, l2, l3):
    os.system('cls')
    print("")
    a1=l1[0]
    a2=l1[1]
    a3=l1[2]
    b1=l2[0]
    b2=l2[1]
    b3=l2[2]
    c1=l3[0]
    c2=l3[1]
    c3=l3[2]
    print("      | 1  | 2  | 3  |")
    print("   ---|----|----|----|")
    print("    A | ",a1,"| ",a2,"| ",a3,"|")
    print("   ---|----|----|----|")
    print("    B | ",b1,"| ",b2,"| ",b3,"|")
    print("   ---|----|----|----|")
    print("    C | ",c1,"| ",c2,"| ",c3,"|")
    print("   ---|----|----|----|")
    print("")

def Getcase(l1,l2,l3,signe,joueur):
    print(joueur)
    print("")
    case=str(input("entre ton choix: "))

                                                        # LIGNE 1 #
    if case == "a1" or "a2" or "a3":
        ligne2=l2
        ligne3=l3
                                                        # CASE 1 #
        if case == "a1":
            if l1[0] == " ":
                del l1[0]
                l1.insert(0, signe)
                                                        # CASE 2 #
        elif case == "a2":
            if l1[1] == " ":
                del l1[1]
                l1.insert(1, signe)
                                                        # CASE 3 #
        elif case == "a3":
            if l1[2] == " ":
                del l1[2]
                l1.insert(2, signe)
        ligne1=l1

                                                        # LIGNE 2 #            
    if case == "b1" or "b2" or "b3":
        ligne1=l1
        ligne3=l3
                                                        # CASE 1 #
        if case == "b1":
            if l2[0] == " ":
                del l2[0]
                l2.insert(0, signe)
                                                        # CASE 2 #
        elif case == "b2":
            if l2[1] == " ":
                del l2[1]
                l2.insert(1, signe)
                                                        # CASE 3 #
        elif case == "b3":
            if l2[2] == " ":
                del l2[2]
                l2.insert(2, signe)
        ligne2=l2

                                                        # LIGNE 3 #            
    if case == "c1" or "c2" or "c3":
        ligne1=l1
        ligne2=l2
                                                        # CASE 1 #
        if case == "c1":
            if l3[0] == " ":
                del l3[0]
                l3.insert(0, signe)
                                                        # CASE 2 #
        elif case == "c2":
            if l3[1] == " ":
                del l3[1]
                l3.insert(1, signe)
                                                        # CASE 3 #
        elif case == "c3":
            if l3[2] == " ":
                del l3[2]
                l3.insert(2, signe)
        ligne3=l3

    data = [ligne1, ligne2, ligne3]
    return data

def check(l1,l2,l3):
    result=0
    full=0
    deck=l1+l2+l3
    if " " in deck:
        full=0
    else:
        full=1
    if l1[0] + l1[1] + l1[2] == "X"+"X"+"X":
        result=1
    if l1[0] + l1[1] + l1[2] == "O"+"O"+"O":
        result=1
    if l2[0] + l2[1] + l2[2] == "X"+"X"+"X":
        result=1
    if l2[0] + l2[1] + l2[2] == "O"+"O"+"O":
        result=1
    if l3[0] + l3[1] + l3[2] == "X"+"X"+"X":
        result=1
    if l3[0] + l3[1] + l3[2] == "O"+"O"+"O":
        result=1
    if l1[0] + l2[0] + l3[0] == "X"+"X"+"X":
        result=1
    if l1[0] + l2[0] + l3[0] == "O"+"O"+"O":
        result=1
    if l1[1] + l2[1] + l3[1] == "X"+"X"+"X":
        result=1
    if l1[1] + l2[1] + l3[1] == "O"+"O"+"O":
        result=1
    if l1[2] + l2[2] + l3[2] == "X"+"X"+"X":
        result=1
    if l1[2] + l2[2] + l3[2] == "O"+"O"+"O":
        result=1
    if l1[0] + l2[1] + l3[2] == "X"+"X"+"X":
        result=1
    if l1[0] + l2[1] + l3[2] == "O"+"O"+"O":
        result=1
    if l1[2] + l2[1] + l3[0] == "X"+"X"+"X":
        result=1
    if l1[2] + l2[1] + l3[0] == "O"+"O"+"O":
        result=1
    if full == 1:
        result=2
    return result




play=0
while True :
    finish=0
    player1=str(input("Premier joueur : "))
    player2=str(input("Deuxième joueur : "))
    symbole=["O","X"]
    print(player1, "commence")
    render(l1,l2,l3)
    while finish == 0 and play != 9:
        if finish == 0:
            data=Getcase(l1,l2,l3,symbole[1],player1)
            render(data[0],data[1],data[2])
            finish=check(data[0],data[1],data[2])
            if finish == 1 :
                print (player1, "est le grand GAGNANT !!!")
        if finish == 0 :
            data=Getcase(l1,l2,l3,symbole[0],player2)
            render(data[0],data[1],data[2])
            finish=check(data[0],data[1],data[2])
            if finish == 1 :
                print (player2, "est le grand GAGNANT !!!")
        if finish == 2:
            print("PERDUE, plus de place disponible")
            break
    break
    
