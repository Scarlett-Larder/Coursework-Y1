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
    distance = distance / 2
    distance = int(distance)
    distance2 = Point(distance,distance)
    status = distance_between_points(me, distance2)
    print(f"starter status: {status}")

    while status-200 < distance:
        direction = random.randint(1,4)
        status = distance_between_points(me, distance2)
        print(status-200)
        print(distance)
        #1 = North, 2 = East, 3 = South, 4 = West
        if direction == 1:
            y1 += 5
            me = Point(me.x, me.y+5)
            line = Line(me, Point(me.x, me.y+5))
            line.draw(win)
        elif direction == 2:
            me = Point(me.x+5, me.y)
            line = Line(me, Point(me.x+5, me.y))
            line.draw(win)
        elif direction == 3:
            me = Point(me.x, me.y-5)
            line = Line(me, Point(me.x, me.y-5))
            line.draw(win)
        else:
            me = Point(me.x-5, me.y)
            line = Line(me, Point(me.x-5, me.y))
            line.draw(win)
    print(me)
    print("finished!")
    win.get_mouse()

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
