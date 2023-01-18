"""
defkullanici = "abdusalam"
defparola = "1234"
while (1<7):
    kullnici=input("kullanici adi:")
    parola=input("parola:")
    if (kullnici!=defkullanici) or (parola != defparola):
        print("yanlis giris!")
    else:
        print("Hosgeldiniz")
        break 
"""
listeler = [2,3,4]
for i in range(1,10):
    if (i in listeler):
        continue
    print(i)
