import math
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


# Remember to update the line above if you are using other Graphix objects

def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)

#Question 1
def fast_food_order_price():
    meow = int(input("Pricing : "))
    if meow >= 20:
        print(f"Your price is {meow+2.50}")
    else:
        print(f"Your price is {meow}")

#Question 2
def what_to_do_today():
    temp = int(input("Temp: "))
    if temp > 25:
        print("A swim in the sea should be recomended")
    elif 10 <= temp <= 25:
        print("Shopping in Gunwharf Quays is a good idea")
    else:
        print("It’s best to watch a film at home")
        
#Question 3
def display_square_roots(start, end):
    for i in range(start,end):
        print(f"The square root of {i} is: {math.sqrt(i):0.3f}")
    
#Question 4
def calculate_grade(mark):
    grade = ""
    if mark > 20:
        grade = "X"
    elif mark >= 16:
        grade = "A"
    elif 12 >= mark <= 15:
        grade = "B"
    elif 8 >= mark <= 11:
        grade = "C"
    else:
        grade = "F"
    return grade

#Question 5
def peas_in_a_pod():
    num = int(input("num: "))
    x = num * 100
    win = Window("Peas in a Pod", x, 100)
    total = 0
    for i in range(num):
        meow = (i * 100) + 50
        meow = int(meow)
        center = Point(meow,50)
        circle = Circle(center, 50)
        circle.fill_colour = "green"
        circle.draw(win)

#Question 6
def ticket_price():
    price = 10
    km = int(input("How many KM: "))
    price = km * 0.15 + price
    age = int(input("Age: "))
    if 15 >= age <= 60:
        price = price * 0.4
    print(f"{price:0.2f}")
    
#Question 7
def numbered_square(n):
    for add in range(n):
        total = ""
        for length in range(n):
            length = str(length+n-add)
            total += length + " "
        print(total)

#Question 8 func
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)

def draw_eye(win, center, radius, colour_input):
    radius = 120
    colour = "white"
    draw_circle(win, center, radius, colour)
    radius = 60
    draw_circle(win, center, radius, colour_input)
    radius = 30
    colour = "black"
    draw_circle(win, center, radius, colour)
    
#Question 8 code
def draw_coloured_eye():
    colour_input = input("Colour: ")
    if colour_input == "blue" or colour_input == "gray" or colour_input \
    == "green" or colour_input == "brown":
        center_x = int(input("X: "))
        center_y = int(input("Y: "))
        win = Window()
        draw_eye(win, Point(center_x,center_y), 50, colour_input)
    else:
        print("nope")

#Question 9
def draw_patch_window():
    win = Window("Patch Design",500,500)
    SCREEN = 500
    TILE = 100
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            tl = Point(X,Y)
            br = Point(X + TILE, Y + TILE)
            draw_rectangle(win, tl, br, "lime")
            message = Text(Point(int(X+50),int(Y+50)), "Brat")
            message.draw(win)

#Question 10
def draw_patch(win, x, y, colour):
    SCREEN = 500
    TILE = 100
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            tl = Point(X,Y)
            br = Point(X + TILE, Y + TILE)
            draw_rectangle(win, tl, br, colour)
            message = Text(Point(int(X+50),int(Y+50)), "Brat")
            message.draw(win)
            
def draw_patchwork():
    draw_patch(Window("meow",300,200), 0,0,"blue")
    
#Question 11
def draw_coloured_eye_11():
        center_x = int(input("X: "))
        center_y = int(input("Y: "))
        win = Window()
        draw_eye(win, Point(center_x,center_y), 50, colour_input)
        print("nope")
        
#Question 12

def eyes():
    win = Window("wowza",500,500)
    radius = 30
    colour = ["blue","gray","green","brown"]
    for _ in range(10):
        for item in colour:
            center = win.get_mouse()
            draw_coloured_eyed(win,center,radius,item)

def draw_coloured_eyed(win, center, radius, colour_pick):
    colour = "white"
    radius_1 = radius
    draw_circle(win, center, radius_1, colour)
    radius_2 = radius * 0.66
    radius_2 = int(radius_2)
    radius_2 = int(radius_2)
    draw_circle(win, center, radius_2, colour_pick)
    radius_3 = radius * 0.33
    radius_3 = int(radius_3)
    colour = "black"
    draw_circle(win, center, radius_3, colour)
        

