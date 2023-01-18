""" 
    a && b <==> a and b
    a || b <==> a or b
    not a --> a digiri doğru olsada başına not geldiği için yanlış oalcaktır
"""

# Kullanıcı ismi ve prola kontrol programi

defkullanici="yazilimci"
defparola="1234"

kullanici=input("kullanici adi:")
parola=input("parolaniz:")

if defkullanici==kullanici and defparola==parola:{
    print ("yazilim dunyasina hosgeldiniz...")
}
elif defkullanici != kullanici and defparola == parola:{
    print("kullanici adini yanlis girdiniz!!!")
}
elif defparola == kullanici or defparola != parola:{
    print("parolanizi mi unuttunuz?")
}
else:{
    print("tekrar deneyim")
}

