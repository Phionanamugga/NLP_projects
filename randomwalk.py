#shows how to use turtle graphics to create a random walk
import turtle as t
import random

tim = t.Turtle()

colors = ['CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue',
          'LightSeaGreen','wheat','SlateGray','SeaGreen',
          'medium aquamarine']
directions = [0, 90, 170, 270]
tim.pensize(15)
tim.speed("fastest")
 
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
