def geometri(sekil):
    if (len(sekil) == 3):
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a + b) > c and (a + c) > b and (b + c) > a:
            if (a == b) and (a == c) and (b ==c):
                print("Eskenar ucgen")
            elif (a == b) and (a == c):
                print("Ikiz kenar ucgen")
            else:
                print("Cesit kenar ucgen")

        else:
            print("Ucgen belirtmiyor")

    elif (len(sekil) == 4):
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if (a == b) and (a == c) and (a == d):
            print("Kara")
        elif (a == c) and (b == d):
            print("Dik dortgen")
        else:
            print("Normal dortgen")

    else:
        print("herhanngi bir sekil degil...")

while (True):
    eleman_sayisi =int(input ("eleman sayisini giriniz: "))
    if(eleman_sayisi == 3):
        a = int (input("a: "))
        b = int (input("b: "))
        c = int (input("c: "))
        geometri([a,b,c])
    elif(eleman_sayisi == 4):
        a = int (input("a: "))
        b = int (input("b: "))
        c = int (input("c: "))
        d = int (input("d: "))
        geometri([a,b,c,d])

    else:
        print("lutfen tekrar Deneyiniz")
        break
