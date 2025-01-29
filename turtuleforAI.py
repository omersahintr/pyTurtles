import turtle
import random

# Ekran ve Turtle nesnesi oluşturma
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  # En hızlı çizim hızı

# Renk listesi (rastgele renk seçimi için)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# İç içe geçen renkli daireleri çizen fonksiyon
def draw_nested_circles(turtle, size, depth):
    if depth == 0:
        return
    else:
        # Rastgele bir renk seç
        color = random.choice(colors)
        turtle.color(color)

        # Daireyi çiz
        turtle.circle(size)

        # Yeni dairenin merkezine git
        turtle.up()
        turtle.forward(size * 0.6)  # İç içe geçme oranı ayarı
        turtle.left(90)
        turtle.down()

        # Daha küçük bir daire çizmek için recursive çağrı yap
        draw_nested_circles(turtle, size * 0.75, depth - 1)

        # Geri dön ve başka bir daire çizmek için hazırlık yap
        turtle.up()
        turtle.right(90)
        turtle.backward(size * 0.6)
        turtle.down()

# Başlangıç konumu ve açı ayarı
t.up()
t.goto(0, -200)
t.down()

# İlk dairenin çizimini başlat
draw_nested_circles(t, 250, 10)

# Turtle'ı kapat
turtle.done()
