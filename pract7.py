import math
import time
import random
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry
from pract6 import calculate_grade
from pract5 import draw_brown_eye, distance_between_points

def hello_while():
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1


def countdown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


def mystery_loop():
    i = 1
    # Be careful! This loop will run forever!
    while i < 1000:
        print(i)
        i = i * 2


def add_up_numbers1():
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = int(input("Enter a number: "))
        total = total + number
        more_numbers = input("Any more numbers? (y/n) ")
    print("The total is", total)


def add_up_numbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def add_up_numbers3():
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "":
        number = int(n_str)
        total += number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)


def add_up_numbers4():
    total = 0
    while True:
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break  # Exit the loop if the input is not a number
        number = int(n_str)
        total += number
    print("The total is", total)


# Note: msg == "" needs to appear twice
def get_string1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def get_string2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def can_apply_for_job(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False


def can_vote1():
    age = int(input("How old are you? "))
    while age <= 18:
        print("Wait until you are 18!")
        age = int(input("How old are you? "))


def can_vote2():
    while True:
        age = int(input("How old are you? "))
        if age > 18:
            break
        print("Wait until you are 18!")


#  For question 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        time.sleep(1)
        amber.fill_colour = "yellow"
        time.sleep(1)
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(1)
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        time.sleep(1)
        red.fill_colour = "red"
        amber.fill_colour = "black"
        


# For question 6
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

# Solutions to the programming exercises:

#Question 1
def name_checker():
    name_check = False
    while name_check == False:
        name = input("Please enter a name")
        name_check = name.isalpha()
    print("wow correct")

#Question 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        time.sleep(1)
        amber.fill_colour = "yellow"
        time.sleep(1)
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(1)
        amber.fill_colour = "yellow"
        green.fill_colour = "black"
        time.sleep(1)
        red.fill_colour = "red"
        amber.fill_colour = "black"

#Question 3 - DO WITHOUT AN IF
def grade_coursework2():
    mark = ""
    while mark != "X":
        mark = int(input("Please enter your mark: "))
        grade = calculate_grade(mark)
        print(grade)

#Question 4
def order_price():
    total = 0
    while True:
        price = int(input("Price of item: "))
        qty = int(input("How many: "))
        total += total + price * qty
        finish = input("Type 1 to finish. Press enter to continue.")
        if finish == '1':
            break
    print(f"Your total is: {total}")

#Question 5
def clickable_eye():
    win = Window()
    draw_brown_eye(win, Point(200,200))
    text = Text(Point(200, 360),"Please click anywhere on the eye")
    text.draw(win)
    while True:
        click = win.get_mouse()
        distance = distance_between_points(Point(200,200), click)
        print(distance)
        if 60 < distance < 120:
            print("sclera")
        elif 30 < distance < 60:
            print("iris")
        elif distance < 30:
            print("pupil")
        else:
            break
clickable_eye()
# Question 6
# def fahrenheit_to_celsius():
#     fahrenheit = int(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print(f"{celsius:0.2f}")

# def celsius_to_fahrenheit():
#     celsius = int(input("Enter temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{fahrenheit:0.2f}")

def temperature_converter():
    while True:
        choice = input("Fahrenheit to celsius: 1 Celsius_to_fahrenheit: 2 ")
        if choice == '1':
            fahrenheit_to_celsius()
        if choice == '2':
            celsius_to_fahrenheit()
        else:
            continue
        leave = input("Press enter to continue. Type 1 to exit: ")
        if leave == "1":
            break
                
#Question 7 
def table_tennis_scorer():
    player_1 = 0
    player_2 = 0
    win = Window()
    line = Line(Point(200,0), Point(200, 400))
    line.draw(win)
    while player_1 < 11 and player_2 < 11:
        click = win.get_mouse()
        if click.x < 200:
            player_1 += 1
            print(player_1)
        elif click.x > 200:
            player_2 += 1
            print(player_2)
        else:
            print("Invalid input?")
    win.get_mouse()

#Question 8
def guess_the_number():
    num = random.randint(1,100)
    print(num)
    for i in range(7):
        guess = int(input("Guess: "))
        if guess < num:
            print("Too Low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"You Got it! Total guesses: {i}")
            return    
    print(f"You failed! The number was {num}")

                
    
def grade_coursework2():
    grade = ""
    while grade != "X":
        mark = int(input("Please enter your mark: "))
        grade = calculate_grade(mark)
    print(grade)