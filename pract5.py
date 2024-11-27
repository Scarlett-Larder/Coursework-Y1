import math
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount, years):
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2
def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    return 2 * math.pi * radius

def circle_info():
    radius = int(input("wowza: "))
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    print(f"Area: {area:0.2f} Circumference: {circumference:0.2f}")



# For exercise 3
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)

def draw_brown_eye_in_centre():
    window = Window()
    center = Point(200, 200)
    radius = 120
    colour = "white"
    draw_circle(window, center, radius, colour)
    radius = 60
    colour = "brown"
    draw_circle(window, center, radius, colour)
    radius = 30
    colour = "black"
    draw_circle(window, center, radius, colour)

# For exercise 5
def draw_brown_eye(win, center):
    radius = 120
    colour = "white"
    draw_circle(win, center, radius, colour)
    radius = 60
    colour = "brown"
    draw_circle(win, center, radius, colour)
    radius = 30
    colour = "black"
    draw_circle(win, center, radius, colour)
    
def draw_pair_of_brown_eyes():
    win = Window("meow", 600, 400)
    center = Point(300, 200)
    draw_brown_eye(win, center)
    print("test")
    center = Point(100, 200)
    draw_brown_eye(win, center)
    
    

def draw_block_of_starts(width, height):
    total = ""
    for i in range(width):
        total = total + "*"
    for i in range(height):
        print(total)

def draw_letter_e():
    draw_block_of_starts(9,2)
    draw_block_of_starts(2,2)
    draw_block_of_starts(5,2)
    draw_block_of_starts(2,2)
    draw_block_of_starts(9,2)



def distance_between_points(p1, p2):
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    return(distance)
    

def draw_blocks(a,b,c,d,e):
    result = a * " " + b * "*" + c * " " + d * "*"
    for i in range(e):
        print(result)

def draw_letter_a():
    draw_blocks(1,8,0,0,2)
    draw_blocks(0,2,6,2,2)
    draw_blocks(0,10,0,0,2)
    draw_blocks(0,2,6,2,3)
    
def draw_brown_eyed(win, center, radius):
    colour = "white"
    radius_1 = radius
    draw_circle(win, center, radius_1, colour)
    radius_2 = radius * 0.66
    radius_2 = int(radius_2)
    colour = "brown"
    radius_2 = int(radius_2)
    draw_circle(win, center, radius_2, colour)
    radius_3 = radius * 0.33
    radius_3 = int(radius_3)
    colour = "black"
    draw_circle(win, center, radius_3, colour)

def draw_four_pairs_of_brown_eyes():
    win = Window("wowza",800,800)
    for i in range(4):
        print(f"Pair: {i+1}")
        for i in range(2):
            print(f"Eye: {i+1}")
            p_center = win.get_mouse()
            p_out_circ = win.get_mouse()
            wowza = distance_between_points(p_center,p_out_circ)
            wowza = int(wowza)
            draw_brown_eyed(win,p_center,wowza) 
    win.close()

