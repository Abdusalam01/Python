"""
    döngü değişkeni başlatma ve 
    while (mantık cumlesi);
    (girinti) yapılacak işlemler
    artım işlemleri
"""
defkullanici="abdusalam"
defparola="1234"
while (1<8):
    kullanici=input("kullanici adi: ")
    parola= input("parola:")
    if ((kullanici == defkullanici) and (parola == defparola)):
        print("Hosgeldiniz",kullanici)
        break
    elif ((kullanici != defkullanici) and (parola == defparola)):
        print("kullanici adinizi yanlis girdiniz")
    elif ((kullanici == defkullanici) and (parola != defparola)):
        print("sifrenizi mi unuttunuz")
        print("sifreyi degistirmek istermisiniz?(E/H)")
        cevap=input()
        if (cevap=="E"):
            
            yeniparola=input("yeni parola:")
            print("lutfen bekeyin")
            defparola=yeniparola
            print("sifre basariyla degistirildi")
    
    else : 
        print("tekrar deneyin")
        
     
