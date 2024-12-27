import random
import turtle as t
tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

angles = [0, 90, 180, 270]

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

tim.pensize(15)
tim.speed("fastest")

def draw_shape():
    tim.forward(30)
    tim.setheading(random.choice(angles))

for shape_side_n in range(200):
    tim.color(random.choice(colours))
    draw_shape()
