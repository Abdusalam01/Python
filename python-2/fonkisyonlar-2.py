def kokbul(a,b,c):
    delta=(b*b-4*a*c)
    if (delta<0):
        print("Real kok bulunamadi...!")
        return
    elif (delta==0):
        x1=-b/2*a
        return(x1)
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/2*a
    return(x1,x2)
a=int (input("a:"))
b=int (input("b:"))
c=int (input("c:"))
sonuc=kokbul(a,b,c)
print("fonkisyonun kokleri: ",sonuc)