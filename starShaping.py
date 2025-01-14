### STAR SHAPING ###
import turtle

kose = 0
koseSay = 5
kenarPx = int(input("Kenar Uzunluğu Giriniz: "))

yazi_tahtasi = turtle.Screen()
yazi_tahtasi.bgcolor("yellow") #Sayfa arkaplan rengi
yazi_tahtasi.title("Yazı Tahtası") #Sayfa Başlığı

turtle_ins = turtle.Turtle() #turtle çalıştır

for i in range(koseSay):
    turtle_ins.forward(kenarPx)
    turtle_ins.left(144)

turtle.done() #turtle kapat