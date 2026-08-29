# Source: index.html week 1 — "Hexagon example"
#Draws a hexagon, using the turtle module

#Import the turtle commands to use below:
import turtle

#Create a turtle, named: thomasH
thomasH = turtle.Turtle()

#Repeat 6 times:
for i in range(6):
  thomasH.forward(100)  #Move thomasH forward 100 steps
  thomasH.left(60)      #Turn thomasH 60 degrees to the left
