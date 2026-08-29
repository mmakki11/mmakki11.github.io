# Source: index.html week 10 ("Random Walk") and lab_10 ("Random Walk")
# Original (retiring 2026-08-31): https://trinket.io/python/ab6cddc880
import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)
