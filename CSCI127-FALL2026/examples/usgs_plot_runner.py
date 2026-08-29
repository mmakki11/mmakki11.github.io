# Plotting USGS data — browser-runnable version of usgs_plot.py (lab_09)
# Marks two cities (LA and Tokyo) on an equirectangular world map.
# Include turtles and set up screen:
import turtle
screen = turtle.Screen()
# Canvas size MUST match world_map.jpg (1000x500) so the background lines up:
screen.setup(1000, 500)
# Set coordinates so x = longitude (-180..180) and y = latitude (-90..90):
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world_map.jpg")

# Create a turtle, set its shape/color, and lift the pen:
thea = turtle.Turtle()
thea.shape('turtle')
thea.color('purple')
thea.penup()

# Plot LA:
thea.goto(-118, 34)
thea.stamp()

# Plot Tokyo:
thea.goto(140, 35)
thea.stamp()

# Return to the origin when done:
thea.home()
