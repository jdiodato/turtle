#=================================================================================================
# Joseph A. Diodato
# Turtle Mail Envelope
# 
# This program includes the following additional features:
# - The user can specify their envelope size.
# - The user can select their envelope color from a menu of options (implemented with if/elif logic).
# - The user can select one of two stamp designs (a sun or music note design).
#==================================================================================================

import turtle

# Defining a method to collect recipient information.

def recipient_info(length, width):
    name = (input("Name: "))
    adr = (input("Street Address: "))
    city = (input("City: "))
    state = (input("State: "))
    zipCode = (input("Zip Code: "))
    turtle.pendown()
    turtle.write(name, font = ("Times New Roman", 12, "normal"))
    turtle.penup()
    turtle.left(180)
    turtle.forward(15)
    turtle.write(adr, font = ("Times New Roman", 12, "normal"))
    turtle.forward(15)
    turtle.write(city + ", " + state + ", " + zipCode,
    font = ("Times New Roman", 12, "normal"))

# Defining a method to collect the return address.

def return_info(length, width):
    turtle.left(90)
    turtle.forward(length / 2)
    name = (input("Name: "))
    adr = (input("Street Address: "))
    city = (input("City: "))
    state = (input("State: "))
    zipCode = (input("Zip Code: "))
    turtle.write(name, font = ("Times New Roman", 8, "normal"))
    turtle.left(180)
    turtle.forward(15)
    turtle.write(adr, font = ("Times New Roman", 8, "normal"))
    turtle.forward(15)
    turtle.write(city + ", " + state + ", " + zipCode,
    font = ("Times New Roman", 8, "normal"))

# Defining a function to draw the sun stamp.

def sun_stamp():
    turtle.begin_fill()
    turtle.fillcolor("cyan")

# Drawing the stamp outline.
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.hideturtle()


def main():

    #turtle.speed("slowest")

    # Prompting the user for their envelope dimensions and color; Draws the envelope.

    print("This program will help you to complete the back side of your envelope so that it can be mailed")
    print("Let's get started.\n")
    print("If you are not satisfied with your envelope, please enter an exclamation point (!) in any of the prompts.")
    print("This will allow you to start from the beginning to make any changes.")

    length = float(input("Enter the length of your envelope: "))
    width = float(input("Enter the width of your envelope: "))
    print("The dimensions of your envelope are {0} by {1}\n".format(length,width))
    print("Which color would you like your envelope to be?\n")

    print("1: Light Coral")
    print("2: Orange")
    print("3: Yellow")
    print("4: Lime")
    print("5: Aquamarine")
    print("6: Orchid")
    print("7: Mint Cream\n")

    envelope_color = int(input("Please enter a number from the list below to indicate your preference.\n"))

    if envelope_color == 1:
        turtle.color("light coral")
        turtle.fillcolor("light coral")
    elif envelope_color == 2:
        turtle.color("orange")
    elif envelope_color == 3:
        turtle.color("yellow")
    elif envelope_color == 4:
        turtle.color("lime")
    elif envelope_color == 5:
        turtle.color("aquamarine")
    elif envelope_color == 6:
        turtle.color("orchid")
    elif envelope_color == 7:
        turtle.color("spring green")
    else:
        print("You've entered an incorrect option.")
        print("The Envelope Wizard will now exit.")
        print("Have a great day!")
        exit()

    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.end_fill()

    print("Please follow the below prompts to provide the recipient's address.\n")
    recipient_info(length, width)

    # Moving the turtle back to the origin so that we can compute the location for the return address.
    turtle.setposition(0,0)
    turtle.left(180)
    turtle.forward(width - 25)
    turtle.right(90)
    turtle.forward(25)

    print("Please follow the below prompts to provide the return address.\n")
    return_info(length, width) #turtle facing down after this

    # Moving the turtle to the upper right corner to draw the stamp.
    turtle.forward(35)
    turtle.left(90)
    turtle.forward(length - 90)
    turtle.left(90) # turtle now facing north, ready to draw the stamp.

    print("Below is a menu of the stamps that are currently available.")
    print("1: Sun Stamp")
    print("2: Music Note Stamp")
    stamp_selection = input("Please enter the number that corresonds with your stamp selection: ")

    if stamp_selection == "1":
        sun_stamp()
    elif stamp_selection == "2":
        music_note_stamp()
    else:
        print("Sorry, you've entered an incorrect option.")
        print("The Envelope Wizard will now exit. Please try agian!")

    exit()

    print("Oops! Our clerk accidently put your stamp on the envelope sideways.")
    print("Sorry about that -- he's still in training!")
    print("Either way, your envelope is ready to be mailed.")
    print("Have a great day!")

 
main()

input()