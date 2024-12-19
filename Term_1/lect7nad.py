import math
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry

# Constants
SCREEN = 500
TILE = 100
RADIUS = 50

# Function to draw a rectangle with specified parameters
def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)

# Function to draw a circle with specified parameters
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.draw(win)
    
def draw_tiled_blue_rectangles():
    win = Window("Blue Tiled Rec", SCREEN, SCREEN)
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            tl = Point(X,Y)
            br = Point(X + TILE, Y + TILE)
            draw_rectangle(win, tl, br, "blue")
    win.get_mouse()

def draw_blue_rec_and_circles():
    win = Window("Circle", SCREEN, SCREEN)
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            tl = Point(X,Y)
            br = Point(X + TILE, Y + TILE)
            draw_rectangle(win, tl, br, "blue")
            #New code
            center = Point(X + RADIUS, Y + RADIUS)
            draw_circle(win,center,RADIUS, "red")
            
def two():
    win = Window("Circle", SCREEN, SCREEN)
    flag = True
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            if (flag == True):
                tl = Point(X,Y)
                br = Point(X + TILE, Y + TILE)
                draw_rectangle(win, tl, br, "blue")
            else:
                #New code
                center = Point(X + RADIUS, Y + RADIUS)
                draw_circle(win,center,RADIUS, "red")
            flag = not flag
        win.get_mouse()

