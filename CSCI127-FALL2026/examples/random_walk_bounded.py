# Source: lab_10 — bounded random walk (stops when turtle leaves the -50..50 box)
# Original (retiring 2026-08-31): https://trinket.io/python/6738c47304
import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

while (-50 < trey.xcor() < 50) and (-50 < trey.ycor() < 50):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)
