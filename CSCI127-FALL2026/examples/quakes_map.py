# Source: index.html week 13 — "Turtle Quakes Demo"
# REQUIRES ASSETS: mapNASA.jpg (800x404 background) and allWeek2017Jan17.csv
#   (the original trinket also bundled alternate data files:
#    4.5week / 2.5week / 4.5month / 2.5month 2017Jan17.csv)
# WARNING: This is Python 2 code (note the `print "..."` statement below).
#   For Python 3 / a browser runner, change it to: print("mag:", mag, ...)
#Mapping USGS earthquake data from CSV file.
import turtle

screen = turtle.Screen()

# this assures that the size of the screen will match the map image:
screen.setup(800, 404)
#Set coordinates for latitude and longitude:
screen.setworldcoordinates(-180,-90,180,90)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("mapNASA.jpg")

teddy = turtle.Turtle()
teddy.penup()
teddy.shape('triangle')

f = open("allWeek2017Jan17.csv",'r')
f.readline()
lines = f.readlines()

for lineOfData in lines:
  #Split each line into pieces:
  columns = lineOfData.split(',')
  lat = float(columns[1])
  lon = float(columns[2])
  #Now also getting the magnitude:
  mag = float(columns[4])
  location = columns[13]
  print "mag:", mag,"\t", "long:", lon,"\tlat:", lat,"\t", location
  teddy.goto(lon,lat)
  #Scale the color by magnitude:
  teddy.color(40*mag,0,0)
  teddy.stamp()
