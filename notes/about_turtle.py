import turtle

myturtle = turtle.Turtle()

# create a canvas instance ( without goto it started form (0,0) )

# go to a certain coordinate
myturtle.penup()      # without plotting the trace
myturtle.goto(50, 75)

myturtle.pendown()    # start drawing 
myturtle.forward(100) # Turtle(RawTurtle) -> RawTurtle(TPen,TNavigator) -> forward is a method from TNavigator
                      # Move 100 pixels
myturtle.left(90)     # turn left with 90 degree
myturtle.forward(200) 
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200) 

turtle.done()         # keep the window open