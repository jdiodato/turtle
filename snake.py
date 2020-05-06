'''
A simple snake game using Python's Turtle module 
Created by Joseph Diodato (@jdiodato) 
'''

import turtle, random, time 

# Setting up the screen
scn = turtle.Screen()
scn.bgcolor("green")
scn.setup(600, 600)
scn.title("Snake!")

head = turtle.Turtle()
head.shape("square")

# seg = turtle.Turtle()
# seg.shape("square")
# seg.color("dark gray")
# seg.forward(40)

'''
A function to randomly generate fruit on the screen. 
'''
def fruit():
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
scn.exitonclick()
