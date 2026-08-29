# Source: index.html week 3 — "Color Challenges"
import turtle
teddy = turtle.Turtle()

names = ["violet", "purple", "indigo", "lavender"]
for c in names:
  teddy.color(c)
  teddy.left(60)
  teddy.forward(40)
  teddy.dot(10)

teddy.penup()
teddy.forward(100)
teddy.pendown()

hexNames = ["#FF00FF", "#990099", "#550055", "#111111"]
for c in hexNames:
  teddy.color(c)
  teddy.left(60)
  teddy.forward(40)
  teddy.dot(10)
