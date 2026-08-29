# Source: lab_03 — "Color by red-green-blue (RGB)"
# Original (retiring 2026-08-31): https://trinket.io/python/11f1644654
# Note: uses 0-255 RGB values, so requires turtle.colormode(255) in standard
#       CPython. (Trinket defaulted to 255-mode.)
#Color by red-green-blue (RGB):

import turtle

mysteryCol = turtle.Turtle()

#What color am I?
mysteryCol.color(0,0,0)
mysteryCol.forward(50)
mysteryCol.left(90)

#What color am I?
mysteryCol.color(255,0,0)
mysteryCol.forward(60)
mysteryCol.left(90)

#What color am I?
mysteryCol.color(0,0,255)
mysteryCol.forward(70)
mysteryCol.left(90)

#What color am I?
mysteryCol.color(255,0,255)
mysteryCol.forward(80)
mysteryCol.left(90)

#What color am I?
mysteryCol.color(100,100,100)
mysteryCol.forward(90)
mysteryCol.left(90)


mysteryCol.color(255,255,0)
mysteryCol.forward(100)
mysteryCol.left(90)
