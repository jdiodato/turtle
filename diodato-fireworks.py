#========================================================================================#
# Joseph A. Diodato
# Creating a simple fireworks display in Turtle. 
# NOTE: This program also generates a random color (using RGB values) for each explosion
#========================================================================================#

import turtle, random 

def trail():
    # Drawing the trail for each display.
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(3) # Setting the turtle speed to normal before drawing a new trail. 
    t.setheading(90)
    t.setpos(0,-330)
    t.pendown()
    heading = random.randrange(20,160)
    t.setheading(heading)
    trailLength = random.randrange(50,400)
    t.width(2)
    t.forward(trailLength)
    t.clear()

    # Drawing the star. 

    # Implementing the extra credit mechanic where each star is drawn in a random color.
    turtle.colormode(255)
    r = random.randrange(0,256,10)
    g = random.randrange(0,256,10)
    b = random.randrange(0,256,10)
    t.color(r,g,b)
    t.speed(0) # Using the fastest turtle speed to draw a the explosions.
    t.penup()
    starDistance = random.randrange(20,100)
    t.forward(starDistance)
    t.pendown()
    starCenter = t.position()
    starDiameter = random.randrange(40, 200)
    numPoints = random.randrange(8,25)
    degreesToTurn = 360 / numPoints
    
    for i in range(numPoints):
        t.forward(starDiameter / 2)
        t.setpos(starCenter)
        t.right(degreesToTurn)
    t.hideturtle()
    
def main():
    for i in range(0,10):
        trail()
    #input() Used when program executed in VS Code
main()
