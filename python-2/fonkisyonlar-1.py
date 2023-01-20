# *** fonkisyonlarimi tanımlamak için DEF anahtar kelimesini kullaniyoruz.

def factoriel(numara):
    factoriel=1
    for i in range(1,numara+1):
        factoriel*=i
    print("factoriel:",factoriel)
    
sayi=int(input("Sayi giriniz: "))

factoriel(sayi) # --> sayi değişkenine girilen sayinin factorielini hesaplar.
factoriel(5)    # --> 5'n factorielini hesaplar.
#factoriel(4) factoriel(7) ... gibi bibrden fazla kez fonkisyonumuzu çağıra biliriz.