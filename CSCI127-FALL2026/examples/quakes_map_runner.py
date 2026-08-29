# Turtle Quakes Demo — browser-runnable (Python 3) version of quakes_map.py
# Plots one week of USGS earthquakes (allWeek2017Jan17.csv) by lat/long;
# redder = larger magnitude. Runs self-contained in the in-browser runner.
#Mapping USGS earthquake data from CSV file.
import turtle

screen = turtle.Screen()
# Canvas size MUST match world_map.jpg (1000x500) so the background lines up:
screen.setup(1000, 500)
#Longitude is the x-axis (-180..180), latitude the y-axis (-90..90):
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world_map.jpg")     # equirectangular world map behind the points
screen.tracer(0, 0)               # turn off animation so ~1,300 points plot fast

teddy = turtle.Turtle()
teddy.penup()
teddy.speed(0)
teddy.shape('triangle')

f = open("allWeek2017Jan17.csv", 'r')
f.readline()                      # skip the header row
lines = f.readlines()

for lineOfData in lines:
    columns = lineOfData.split(',')
    lat = float(columns[1])
    lon = float(columns[2])
    mag = float(columns[4])
    location = columns[13]
    print("mag:", mag, "\tlong:", lon, "\tlat:", lat, "\t", location)
    teddy.goto(lon, lat)
    #Scale the red intensity by magnitude (0.0-1.0; bigger quake = redder):
    shade = min(1.0, mag / 6.0)
    teddy.color(shade, 0, 0)
    teddy.stamp()

screen.update()                   # draw everything at once
