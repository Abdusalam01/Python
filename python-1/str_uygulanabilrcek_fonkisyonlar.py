""" string ifadelerine uygulanıla bilecek fonkisyonlar"""

# İNDEX LEME

a="merhaba"
print (a[0])
print (a[2])
print (a[0:2])
print (a[4:7])
print (a[0:7])
print (a[::-1])



# upper    küçük harf ile yazilan bir string'i Büyük harflere çevirir...
print("phyton".upper())

# lower    Büyük harf ile yazılan bir string'i Küçük çevirerek ekrena yazar...
print("PHYTON".lower())
# isupper --> yazı büyük harfmi?   print("A".isupper()) true(doğru)
# islower --> yazı küçük harfmi?   print("A".islower()) false(yanlış)

# join  --> 
print ("@".join(["salam008","gmail.com"])) # >>> salam008@gmail.com,  @'i alır salam008 ile gmail.com ortasına yazar.

# replace --> yerini deiştir.
b="selam?"
print(b.replace("?","..."))  # ? işareti yerine ... yazar.

# split
c="hello world 111"
print(c.split(" "))

# isnumeric --> ifade sayılar'danmı oluşuyor? fonkisyonu
d="123"
print(d.isnumeric())

# strip --> str başindaki ve sonundaki ifadeleri silmek için kullanılır.
e=";;;;;;merhaba dunya"
print(e.strip(";"))

# count --> .count("A")        ifade'de A 'yı  say
i="Abudureyimu Abudusalamu"
print(i.count("u"))

# find --> .find("k")    ilk k'nın kaçıncı indexte olduğunu bulur
f="c programlama dili"
print(f.find("m"))

# startswith --> şununlamı başlıyor
s="gelecek sene"
print(s.startswith("ge"))

# endswith --> şununlamı bitiyor
g="gelecek yazilimda"
print(g.endswith("da"))


