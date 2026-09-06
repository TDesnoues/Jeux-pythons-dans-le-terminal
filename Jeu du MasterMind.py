import random

colors=["rouge","vert","bleu","orange","noir","blanc","rose","violet"]
block=[]
guessblock=[]
nbrcolor=int(input("Combien de couleurs à deviner ?"))
good=0
maybe=0
for i in range(nbrcolor):
    block.append(colors[random.randint(0, len(colors)-1)])
while good != nbrcolor:
    print(block)
    print(colors)
    print("")
    for i in range(nbrcolor):
        print("couleur", i+1, "?")
        color=str(input(""))
        if color == "exit":
            good=nbrcolor
            break
        guessblock.append(color)
    for i in range(nbrcolor):
        if guessblock[i] == block[i]:
            good=good+1
        elif guessblock[i] in block:
            maybe=maybe+1
    print(maybe, "couleurs mal placées")
    print(good, "couleurs bien placées")
    maybe=0
    good=0
    guessblock=[]
    if good == nbrcolor:
        break
print("YEAH !!!")
