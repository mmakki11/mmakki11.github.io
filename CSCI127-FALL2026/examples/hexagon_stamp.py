# Source: index.html week 1 — "Fancier hexagon"
# Original (retiring 2026-08-31): https://trinket.io/python/a3bede6db8
#A program that demonstrates turtles stamping

import turtle

taylor = turtle.Turtle()
taylor.color("purple")
taylor.shape("turtle")

for i in range(6):
  taylor.forward(100)
  taylor.stamp()
  taylor.left(60)
