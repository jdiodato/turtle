#=============================================#

# Joseph Diodato

# CSCI-A597 Project 1: Flags

# 1/22/2019

# Italian flag colors:

# green: 008c45

# white: #f4f5f0

# red: #cd212a

# Flag proportion: 2:3

#=============================================#




ITL_flag_colors = ['#008c45', '#f4f5f0', '#cd212a']



from turtle import *



speed('fastest')



for i in range(0,3):

fillcolor(ITL_flag_colors[i])

begin_fill()



forward(120)

left(90)

forward(250)

left(90)

forward(120)

left(90)

forward(250)

left(90)

forward(120)



end_fill()



penup()

left(180)

forward(180)

left(90)

forward(80)

hideturtle()



write("The Flag of Italy", move = False, align = "center",

font = ("Times New Roman", 26, "normal"))

penup()



input()
