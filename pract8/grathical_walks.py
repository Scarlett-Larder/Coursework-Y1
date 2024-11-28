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

def take_a_walk(num_steps,distance):
    y1 = 0
    x1 = 0
    y2 = 0
    x2 =0
    me = Point(200,200)
    while me.y > (distance/2):
        print("meow")
        direction = random.randint(1,4)
        #1 = North, 2 = East, 3 = South, 4 = West
        if direction == 1:
            y1 += 5
            print(me.y)
            me = Point(me.x, me.y+5)
            line = Line(me, Point(me.x, me.y))
            line.draw(win)
        elif direction == 2:
            line = Line(me, Point(me.x+5, me.y))
            line.draw(win)
        elif direction == 3:
            line = Line(me, Point(me.x, me.y-5))
            line.draw(win)
        else:
            line = Line(me, Point(me.x-5, me.y))
            line.draw(win)
    print("finished!")

def take_walks(num_walks, distance):
    for walk in range(num_walks):
        take_a_walk(num_walks, distance)
    else:
        pass

def get_inputs():
    distance = int(input("How far away should it be? (>200) "))
    print(distance/2)
    num_walks = int(input("How many random walks to take? "))
    return num_walks, distance

def main():    
    num_walks, distance = get_inputs()
    grathic(distance)
    take_walks(num_walks, distance)

main()
