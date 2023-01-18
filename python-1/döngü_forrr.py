faktoryel=1
while (1<8):
    sayi = int(input("lutfen negatif olmayan bir sayi giriniz:"))
    if (sayi<=0):
        print("lutfen negatif olmayan bir sayi giriniz.")
    else:
        for i in range(1,sayi+1):
            faktoryel *= i
        print("Faktoryel",faktoryel)
        break