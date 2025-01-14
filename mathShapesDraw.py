import turtle

kose = 0
koseSay = int(input("Köşe Sayısını giriniz: "))
kenarUzunluk = int(input("Köşe Sayısını giriniz: "))

yazi_tahtasi = turtle.Screen()
yazi_tahtasi.bgcolor("yellow") #Sayfa arkaplan rengi
yazi_tahtasi.title("Yazı Tahtası") #Sayfa Başlığı

turtle_ins = turtle.Turtle() #turtle çalıştır

while(True):
    if kose!=koseSay:
        turtle_ins.forward(kenarUzunluk) #100px ileri git
        turtle_ins.left(180-(((koseSay-2)*180)/koseSay)) #sola X derece aci yap
        kose+=1
    else:
        break

turtle.done() #turtle kapat