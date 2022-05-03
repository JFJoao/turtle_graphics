import turtle
from turtle import Turtle, Screen
import random

totylson = Turtle()
turtle.colormode(255)
totylson.shape("turtle")
totylson.color("yellow")



# for move in range (4):
#     totylson.forward(100)
#     totylson.left(90)

# range = int(input("Qual a distancia original ?"))
# while 2 > 1:
#     totylson.forward((range))
#     totylson.left(90)
#     range += 4

# alcance = 20
# while 2 > 1:
#     for _ in range (0, 400, 1):
#         paleta = ("yellow", "red", "black", "pink", "blue", "white")
#         cor = paleta[randint(0,5)]
#         if _ % 2 != 0:
#             totylson.pencolor(cor)
#             totylson.forward(alcance)
#             alcance += 8
#             totylson.left(90)
#
#         elif _ % 2 == 0:
#             totylson.pencolor(cor)
#             totylson.forward(alcance)
#             alcance += 8
#             totylson.left(90)

def draw_shape(num_sides):
    """Draw selected times until size requested"""
    angle = 360 / num_sides
    for _ in range (num_sides):
        totylson.forward(100)
        totylson.left(angle)

# for shape_side in range (3,11):
#     draw_shape(shape_side)

# directions = [0, 90, 180, 270]
# totylson.pensize(15)
# totylson.speed()
#
# for _ in range(250):
#     totylson.forward(30)
#     totylson.setheading(random.choice(directions))

def random_color():
    """Teste"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color

# directions = [0, 90, 180, 270]
# totylson.pensize(15)
# totylson.speed()
#
# for _ in range(250):
#     totylson.color(random_color())
#     totylson.forward(30)
#     totylson.setheading(random.choice(directions))

totylson.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)):
        totylson.color(random_color())
        totylson.circle(100)
        totylson.setheading(totylson.heading()+ size_of_gap)

draw_spirograph(int(input(("Size of gap wanted: "))))


screen = Screen()
screen.exitonclick()
