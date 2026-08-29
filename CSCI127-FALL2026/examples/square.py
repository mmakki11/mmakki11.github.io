# Source: lab_01 — "Draws a square"
# Original (retiring 2026-08-31): https://trinket.io/python/22709f8349
#Draws a square, using the turtle module

#Import the turtle commands to use below:
import turtle

#Create a turtle, named: thomasH
thomasH = turtle.Turtle()

#Repeat 4 times:
for i in range(4):
  thomasH.forward(100)  #Move thomasH forward 100 steps
  thomasH.left(90)      #Turn thomasH 90 degrees to the left
