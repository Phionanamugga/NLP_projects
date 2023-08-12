#shows how to use turtle graphics to create a random walk
import turtle as t
import random

tim = t.Turtle()
directions = [0, 90, 170, 270]
 
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choices(directions))
    