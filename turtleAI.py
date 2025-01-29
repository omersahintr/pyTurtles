import turtle

# İç içe geçen geometrik şekiller çizen fonksiyon
def draw_nested_shapes(t, size, depth, angle):
    if depth == 0:
        return
    else:
        t.forward(size)
        t.left(angle)
        draw_nested_shapes(t, size * 0.8, depth - 1, angle)
        t.right(2 * angle)
        draw_nested_shapes(t, size * 0.8, depth - 1, angle)
        t.left(angle)
        t.backward(size)

# Turtle penceresi oluşturma
screen = turtle.Screen()
screen.bgcolor("white")

# Turtle nesnesi oluşturma
t = turtle.Turtle()
t.speed(0)  # Çizim hızı ayarı (0 en hızlı)

# Başlangıç konumu ve açıları ayarlama
t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)

# İç içe geçen şekilleri çizme
draw_nested_shapes(t, 200, 10, 60)

# Turtle'ı kapatma
turtle.done()
