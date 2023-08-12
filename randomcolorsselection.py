#shows how to use turtle graphics to create a random walk
#shows how to create random colors using tuples
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

directions = [0, 90, 170, 270]
tim.pensize(15)
tim.speed("fastest")
 
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

