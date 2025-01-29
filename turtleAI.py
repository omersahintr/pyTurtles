import turtle

# Function that draws nested geometric shapes
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

# Create a Turtle window
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Çizim hızı ayarı (0 en hızlı)

# Set starting position and angles
t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)

# Drawing nested shapes
draw_nested_shapes(t, 200, 10, 60)

# Turtle shutdown
turtle.done()
