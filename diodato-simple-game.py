#============================================================================================================================================================
# Joseph Diodato
# A simple Turtle game
# This program includes the following additional features/mechanics:
# - Draw cookie at the turtle's location when the user presses "c".
# - Instead of simply stopping when the turtle hits a boundary, this program turns the turtle around 180 degrees so that the player can continue.
#   This makes for a smoother user experience. 
#============================================================================================================================================================

import turtle 

t = turtle.Turtle(shape = "turtle")
MOVE_DISTANCE = 10

# Functions that move the turtle in one of four directions
def up():
    t.setheading(90)
    if t.ycor() == 230:
        t.setheading(270)
    t.forward(MOVE_DISTANCE)

def down():
    t.setheading(270)
    if t.ycor() == -230:
        t.setheading(90)
    t.forward(MOVE_DISTANCE)

def left(): 
    t.setheading(180)
    if t.xcor() == -280:
        t.setheading(0)
    t.forward(MOVE_DISTANCE)

def right(): 
    t.setheading(0)
    if t.xcor() == 280:
        t.setheading(180)
    t.forward(MOVE_DISTANCE)

# A function to draw a cookie
def cookie():
    t.speed(0)
    heading = t.heading()
    pos = t.position()
    t.setheading(90)
    t.dot(45, "khaki")
    t.dot(9, "brown")
    t.forward(10)
    t.dot(6, "brown")
    t.right(90)
    t.forward(10)
    t.dot(9,"brown")
    t.right(90)
    t.forward(24)
    t.dot(5, "brown")

    # Returning the turtle back to its original position when the cookie function was called.
    t.setheading(heading)
    t.setposition(pos)
    t.speed(6)

def main():
    t.penup()

    # Drawing the orange canvas.
    turtle.bgcolor("orange")
    turtle.penup()
    turtle.setposition(-300, 250)
    turtle.pendown()
    
    # Drawing the garden
    turtle.fillcolor("lime")
    turtle.begin_fill()
    turtle.pensize(3)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.hideturtle()
    turtle.end_fill()

    # Allowing the turtle to respond to user input
    turtle.listen()
    turtle.onkey(up, "Up")
    turtle.onkey(down, "Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")

    # Additional feature
    turtle.onkey(cookie, "c")

    input()

main()

