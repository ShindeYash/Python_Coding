# Write a program to take the turtle to its destination - north, south, east or west based on the destination it wants to reach. Refer the output screens provided for each destination.


destination = input("Please enter the destination (north, south, east or west) : ").lower()
while destination not in ['north', 'south', 'east', 'west']:
    print("please enter valid destination.")
    destination = input("Please enter the destination (north, south, east or west) : ").lower()
print(destination)

import turtle
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color("blue")          # alex has a color

'''
alex.backward(50)            # alex moves 50 positions backward
alex.forward(50)             # alex moves 50 positions forward
alex.right(60)               # alex turns 60 degrees right
alex.left(60)                # alex turns 60 degrees left
alex.write("Hello")          # alex says "Hello"
'''

#Write the logic to take the turtle to its destination
#Refer the statements given above to draw the pattern
#Provide different values and test your program
if destination == 'north':
    alex.right(-90)
    alex.forward(250)
elif destination == 'east':
    alex.right(0)
    alex.forward(250)
elif destination == 'south':
    alex.right(90)
    alex.forward(250)
else:
    alex.right(0)
    alex.backward(250)

              




