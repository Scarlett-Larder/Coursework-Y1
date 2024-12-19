import random
import math
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry

win = Window()

def distance_between_points(p1, p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return(distance)

def grathic(radius):
    circle = Circle(Point(200,200), radius)
    circle.draw(win)

def take_a_walk(num_steps,distance,colour):
    me = Point(200,200)
    dif = distance_between_points(Point(200,200), me)
    while dif < distance:
        dif = distance_between_points(Point(200,200), me)
        direction = random.randint(1,4)
        #1 = North, 2 = East, 3 = South, 4 = West
        if direction == 1:
            me = Point(me.x, me.y+5)
            line = Line(me, Point(me.x, me.y+5))
            line.outline_colour = colour
            line.draw(win)
        elif direction == 2:
            me = Point(me.x+5, me.y)
            line = Line(me, Point(me.x+5, me.y))
            line.outline_colour = colour
            line.draw(win)
        elif direction == 3:
            me = Point(me.x, me.y-5)
            line = Line(me, Point(me.x, me.y-5))
            line.outline_colour = colour
            line.draw(win)
        else:
            me = Point(me.x-5, me.y)
            line = Line(me, Point(me.x-5, me.y))
            line.outline_colour = colour
            line.draw(win)
    print("finished!")

def take_walks(num_walks, distance):
    colours = ["red", "blue", "green", "black"]
    for walk in range(num_walks):
        color = colours[walk % len(colours)]
        take_a_walk(num_walks, distance, color)
    else:
        pass

def get_inputs():
    distance = int(input("How far away should it be? (>200) "))
    num_walks = int(input("How many random walks to take? "))
    return num_walks, distance

def main():    
    num_walks, distance = get_inputs()
    grathic(distance)
    take_walks(num_walks, distance)

main()
