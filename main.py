from turtle import Turtle,Screen,colormode
import random
timmy=Turtle()
colormode(255)
timmy.shape("square")

colors=["forest green","deep sky blue","gold","orange","orange","pale violet red","turquoise",
        "green yellow","green yellow"]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

directions=[0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))




















screen=Screen()
screen.exitonclick()