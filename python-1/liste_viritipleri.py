
liste=["kashkar","korla","urumqi","Q","M","A",1,2]
print(liste[0])

# append --> bu fonkisyonu listeye eleman eklemek için kullanırız.
liste.append("aksu")
liste.append("N")

# insert --> bu fonkisyonu kullanarak istediğimiz index'e eleman ekleyebiliriz.
liste.insert(8,5.4)

# pop --> listeden eleman silmek için kullanılır.
liste.pop(6)

# remove --> listeden şu elemanı sil.
liste.remove("korla")

# clear --> listenin tüm eleman larını sil
#liste.clear()
print(liste)

# index --> listedeki A elemanı'nın hangi indexte olduğunu öğrenmek için kullanılır.
a=[1,1,2,"B","B",2,2,"B",3,"A",4,"B",5]
b=a.index("A")
print(b)

# count --> listede B elemanından kaçtane var?
print(a.count("B"))
print(a.count(2))

g=[1,2,7,5,3,4,0,6]
h=["phyton","java","c","a"]

# sort --> küçükten büyüğe ve elfabetik sırala anlamına gelir.
g.sort()
print(g)
h.sort()
print(h)

# reverse --> listeyi ters yönüne siraler.
g.reverse()
print(g)

print("Uzunluk hesaplama...")
a=input("lutfen bir ifade giriniz: ")
b=len(a)
print(a,"ifadesi'nin uzunlugu","{}".format(b))