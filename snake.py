'''
A simple snake game using Python's Turtle module 
Created by Joseph Diodato (diodato.org) 
'''

import turtle, random, time 

# Setting up the screen
scn = turtle.Screen()
scn.bgcolor("green")
scn.setup(600, 600)
scn.title("Snake!")

wall = turtle.Turtle()
wall.speed(0)
wall.pensize(3)
wall.penup()
wall.setpos(-285,290)
wall.pendown()

for i in range(4):
    wall.forward(570)
    wall.right(90)

wall.hideturtle()

head = turtle.Turtle()
head.shape("square")
head.speed(1)
head.penup()

# seg = turtle.Turtle()
# seg.shape("square")
# seg.color("dark gray")
# seg.forward(40)

def up():
    head.setheading(90)

def down():
    head.setheading(270)

def left():
    head.setheading(180)

def right():
    head.setheading(0)

'''
A function to randomly generate fruit on the screen. 
'''
def fruit():
    pass 

'''
A function to increase snake length when fruit is eaten
'''

def fruitEaten():
    pass 


'''
Game over functionality
'''

def gameOver():
    pass 

'''
Game over condition for hitting wall collision.
'''
def GO_wall():
    pass
    # If snake head hits any wall:
        # Game Over 

'''
Game over condition for colliding with self. 
'''
def GO_self():
    pass
    # If snake head coords = any segment coords:
        # Game over 

# Placeholder to exit the program for now. 

scn.listen()
scn.onkeypress(up, "w")
scn.onkeypress(down, "s")
scn.onkeypress(left, "a")
scn.onkeypress(right, "d")


def movement():
    head.forward(20)
    time.sleep(0.05)
    movement()


movement()




scn.exitonclick()
