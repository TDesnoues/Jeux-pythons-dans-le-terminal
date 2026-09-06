import random

rep = 0
min = 0
max = 500
secret = random.randint(min, max)

while True :
    rep = int(input("guess : "))
    if rep == 0 :
        print("VRAIMENT..... Tu galère ? Tient Chomeur :", secret)
        break
    if rep > secret :
        if rep < max :
            max = rep
        print("[",min,",",max,"]")
    elif rep < secret :
        if rep > min :
            min = rep
        print("[",min,",",max,"]")
    elif rep == secret :
        print("YES !!!, c'était bien", rep)
        break
