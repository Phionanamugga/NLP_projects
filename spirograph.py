#shows how to use turtle graphics to create a random walk
#shows how to create random colors using tuples
#shows how to create a spiral graph
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


tim.speed("fastest")
 
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

#shows how to draw a spirograph by shifting the circle 5 degrees each time
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


