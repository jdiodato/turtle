import turtle, math

#==================================================================================================================#
# Joseph Diodato
# Final Project Milestone #2
# This project was designed to run in trinket.io with the default file names.

# TODO for next milestone
# - refactor button class to create two turtles for text below each object
# - Clean up code in general -- maybe putting the Button class and related methods into a custom module?
# - Top-left text: Make sure font stays consistent 
# - Neater way to incorporate the code for the house and car objects(?)
# - Get a head start on the flashing text color for button label text (see Chabane's milestone 2 example on Canvas)
# - More efficient way to implement button click actions? Make sure algo is scalable for more buttons. 
#==================================================================================================================#

# Boilerplate to set up the Turtle canvas and import the needed images from trinket.
scn = turtle.Screen()
scn.setup(600,500)
scn.addshape("shop.gif")
scn.addshape("home_g.gif")
scn.addshape("home_r.gif")
scn.addshape("coupe_g.gif")

# Setting up shop. 
shop = turtle.Turtle()
shop.setheading(90)
shop.shape("shop.gif")

global funds
funds = 0

global idleDrivers
idleDrivers = 1

global score
score = 0
buttonList = []

# Creating a Button class that inherits all properties of the Turtle class. 
class Button (turtle.Turtle):
  def __init__(self, color, redTxt, blkTxt):
    super(Button, self).__init__(self, color, redTxt, blkTxt)
    self.color = color
    self.redTxt = redTxt
    self.blkTxt = blkTxt
    self.size = 65 
    self.hasTimer = False # Determines if a button needs a timer.
    self.houseR = False # Draws an R house if True
    
    # Each button object is created with a darker color that will be the button's shadow.
    # Adding 40 to the G value creates a lighter tint of the button color that the user will interact with.
    self.lightColor = (self.color[0], self.color[1] + 40, self.color[2])
    
    buttonList.append(self)
    
    # Hiding the turtle initially to make things cleaner 
    self.penup()
    self.hideturtle()

# A method to handle setting up each button given a Button obj and the desired coordinates.
def buttonSetup(buttonObj, x_cord, y_cord):
  buttonObj.speed(0)
  buttonObj.setpos(x_cord, y_cord)
  buttonObj.rX = x_cord # Each button has an rX and rY attribute to calculate if 
  buttonObj.rY = y_cord # a mouse click is within the border of a button.
  
   # Draws an R house if needed.
  if buttonObj.houseR == True:
    houseR = turtle.Turtle()
    houseR.speed(0)
    houseR.penup()
    houseR.setheading(90)
    houseR.shape("home_r.gif")
    houseR.setpos(x_cord, y_cord)
  
  buttonObj.pencolor(buttonObj.color)
  buttonObj.dot(buttonObj.size)
  buttonObj.setpos(buttonObj.xcor(), buttonObj.ycor() + 3)
  buttonObj.pencolor(buttonObj.lightColor)
  buttonObj.dot(buttonObj.size)
  buttonObj.penup()
  buttonObj.setpos(buttonObj.xcor() - 30, buttonObj.ycor() - 50)
  buttonObj.fillcolor("red")
  buttonObj.write(buttonObj.redTxt)
  buttonObj.fillcolor("black")
  buttonObj.setpos(buttonObj.xcor(), buttonObj.ycor() - 15)
  buttonObj.write(buttonObj.blkTxt)
  
  # Draws a timer if needed. 
  if buttonObj.hasTimer == True:
    buttonObj.setpos(buttonObj.xcor() + 30, buttonObj.ycor() + 25)
    buttonObj.pencolor("black")
    buttonObj.pendown()
    buttonObj.circle(38)
    
 
# Creating three Turtle objects to display the global variable states.

def stateUpdate():
  global counter
  counter = 0
  if counter == 0:
    counter += 1
    
    global fundsT
    global idleDriversT
    global scoreT
    
    global funds
    global idleDrivers
    global score
    
    fundsT = turtle.Turtle()
    idleDriversT = turtle.Turtle()
    scoreT = turtle.Turtle()
    
    stateLabels = [fundsT, idleDriversT, scoreT]
    labelCoords = [160, 140, 120]
    labels = ["Funds: $0", "Idle Drivers: 1", "Score: 0"]
    
    for i in range(0,3):
        stateLabels[i].speed(0)
        stateLabels[i].penup()
        stateLabels[i].hideturtle()
        stateLabels[i].setpos(-280, labelCoords[i])
        stateLabels[i].write(labels[i], font=("Arial", 10, "bold"))
  else:
    fundsT.clear()
    fundsT.write("We rich!")
  
# A function to handle click events
def handle_click(x_click, y_click):
  global distanceList
  
  global fundsT
  global idleDriversT
  global scoreT
  
  global funds
  global idleDrivers
  global score
  
  
  
  distanceList = []
  index = 0 
  for b in buttonList:
    #print((b.rX, b.rY))
    distanceList.append(math.sqrt((b.rX - x_click)**2 + (b.rY - y_click)**2))
    
  for d in distanceList:
    if (d < 42):
      index = distanceList.index(d)
      
      if index == 2:
        if funds >= 20:
          funds -=20
          idleDrivers += 1
          fundsT.clear()
          fundsT.write("Funds $" + str(funds))
          
          idleDriversT.clear()
          idleDriversT.write("Idle Drivers: " + str(idleDrivers))
          
          
          
      if index == 3:
        funds += 10
        fundsT.clear()
        fundsT.write("Funds $" + str(funds))
        #print("Funds added!")
      
      
      
      #print(index)
      #print(distanceList.index(d))
      #print("Caller Added!")
  
  #Button Order: callBut, upDonateBut, driverBut, donateBut, houseRBut
  # Button size 65

# A function to update variable states
def update():
  pass 
  
# Setting up the initial variable state text.
stateUpdate()

# Creating each Button object needed for the program.
callBut = Button((173, 112, 24), "Add Caller: $20", "Callers: 0")
upDonateBut = Button((80, 2, 196), "Up Donation: $20", "Donation Level: 1")
driverBut = Button((49,160, 204), "Add Driver: $20", "Total Drivers: 1")

donateBut = Button((37, 156, 11), "Donation: $10", "Cooldown: 2 Seconds")
donateBut.hasTimer = True

houseRBut = Button((237, 163, 2), "Cost: $23", "Time Limit: 11 sec")
houseRBut.houseR = True 
houseRBut.hasTimer = True

buttonSetup(callBut, 0, -175)
buttonSetup(upDonateBut, 100, -175)
buttonSetup(driverBut, 200, -175)
buttonSetup(donateBut, -250, -175)
buttonSetup(houseRBut, 160, 120)

houseG = turtle.Turtle()
houseG.speed(0)
houseG.shape("home_g.gif")
houseG.setheading(90)
houseG.penup()
houseG.setpos(-50,95)

car = turtle.Turtle()
car.speed(0)
car.shape("coupe_g.gif")
car.penup()
car.setpos(-50,95)

# A space to print debug a few features. 
scn.onclick(handle_click)
