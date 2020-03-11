#================================================#
# Joseph A. Diodato
# A connect the dots program implemented in Turtle
# NOTE This program includes an additional feature that allows the user
# to select their line color.
#================================================#

import turtle

# Creating the needed variables in the global scope  
screen = turtle.Screen()
t = turtle.Turtle()
clickCoords = [] 


def handle_click(xclick,yclick):
    '''Moves the turtle after each clicks; adds new clicks to the list of coordinates'''
    if clickCoords == []:
        t.setpos(xclick,yclick)
        clickCoords.append(t.pos())
    else:
        print("ELSE")

    


def main():
    ''' The main function draws the first dot and calls other functions'''
    screen.bgpic('/home/joe/Desktop/plane.png')
    t.penup()
    t.hideturtle()
    screen.onscreenclick(handle_click)

    input()

main()