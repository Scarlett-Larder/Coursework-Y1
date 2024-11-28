import random
import math
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry

def distance_between_points(p1, p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return(distance)

def take_a_walk(num_steps):
    y1 = 0
    x1 = 0
    y2 = 0
    x2 =0
    for step in range(num_steps):
        direction = random.randint(1,4)
        #1 = North, 2 = East, 3 = South, 4 = West
        if direction == 1:
            y1 += 1
        elif direction == 2:
            x1 += 1
        elif direction == 3:
            y2 += 1
        else:
            x2 += 1
        x = x1 - x2
        y = y1 - y2
    return x, y

def print_expected_distance(average_steps):
    print("The expected number of steps away from the", end=" ")
    print(f"start point is {average_steps:0.2f}")

def take_walks(num_walks, num_steps):
    total_steps = 0
    for walk in range(num_walks):
        x,y = take_a_walk(num_walks)
        print(f"{walk} x{x} y{y}")
        ahh = distance_between_points(Point(0,0),Point(x,y))
    return ahh

def get_inputs():
    num_walks = int(input("How many random walks to take? "))
    num_steps = int(input("How many steps for each walk? "))
    return num_walks, num_steps

def main():
    num_walks, num_steps = get_inputs()
    average_steps = take_walks(num_walks, num_steps)
    print_expected_distance(average_steps)

main()
