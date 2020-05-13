'''
A simple snake game using Python's Turtle module 
Created by Joseph Diodato (diodato.org) 
'''

import turtle, random, time 

# Setting up the screen
scn = turtle.Screen()
scn.bgcolor("green")
scn.setup(600, 600)
scn.title("Snake! by @joe_diodato")

head = turtle.Turtle()
head.shape("square")
head.speed(1)
head.penup() 

global direction
direction = ""

# seg = turtle.Turtle()
# seg.shape("square")
# seg.color("dark gray")
# seg.forward(40)

def up():
    direction = "north"
    y = head.ycor()
    head.sety(y + 1000)

def down():
    direction = "south"
    y = head.ycor()
    head.sety(y - 1000)

def left():
    direction = "west"
    x = head.xcor()
    head.setx(x - 1000)

def right():
    direction = "east"
    x = head.xcor()
    head.setx(x + 1000)

'''
A function to randomly generate fruit on the screen. 
'''
def fruit():
    pass 

'''
A function to increase snake length when fruit is eaten
'''

def fruit_eaten():
    pass 


'''
Game over functionality
'''

def game():
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


#def movement():
    
    #head.forward(20)
    #time.sleep(0.05)
    #movement()


#movement()




scn.exitonclick()
