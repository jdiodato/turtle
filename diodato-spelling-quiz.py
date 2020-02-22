#====================================#
# Joseph Diodato
# A simple spelling quiz with turtle.
#
# ==========Words====================#
# bagpipe, bagpepe, bogpipe
# museic, museek, music
# Scatland, Scotland, Scotloch
# chanter, chante, chanti 
# moosician, musiciaan, musician
# =======Extra features=======#
# - 
# - 
# - 
# - 
# - 
#====================================#

import turtle 

def main():

    # d1 and d2 turtles draw the lines for the program. 
    d1 = turtle.Turtle()
    d2 = turtle.Turtle()
    d1.penup()
    d1.setpos(150,300)
    d1.pendown()
    d1.right(90)
    d1.width(2)
    d1.forward(600)
    d1.hideturtle()
    d2.penup()
    d2.setpos(-150,300)
    d2.pendown()
    d2.right(90)
    d2.width(2)
    d2.forward(600)
    d2.hideturtle()


    # Creating three turtles and placing them where words for the program will be printed.
    # The answer turtle will print CORRECT or INCORRECT after receiving user input.
    lWord = turtle.Turtle()
    lWord.penup()
    lWord.setpos(-275, 0)
    lWord.pendown()
    cWord = turtle.Turtle()
    rWord = turtle.Turtle()
    rWord.penup()
    rWord.setpos(275, 0)
    rWord.pendown()
    answer = turtle.Turtle()
    answer.penup()
    answer.left(90)
    answer.backward(130)
    answer.pendown()

    # Left word pos:
    # Center word pos:
    # Right word pos:

    words = (
        ('bagpipe', 'bagpepe', 'bogpipe'),
        ('museic', 'museek', 'music'),
        ('Scatland', 'Scotland', 'Scotloch'),
        ('chanter', 'chante', 'chanti' ),
        ('moosician', 'musiciaan', 'musician')
        )

    input()

main()


    
 





