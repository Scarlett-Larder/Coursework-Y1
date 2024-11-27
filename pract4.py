from graphix import Window, Point, Circle, Line, Rectangle, Polygon, Text, Entry
import os

#Group work testing
def draw_chain_of_circles():
    win = Window("Chain of Circles", 400, 600)
    radius = 20
    click = win.get_mouse()
    for i in range(10):   
        centre = Point(click.x, click.y + i * radius)  
        circle = Circle(centre, radius)
        circle.draw(win)
        circle.outline_colour = "blue"
#draw_chain_of_circles()
        

def personal_greeting():
    name = input("Please enter your name: ")
    print(f"Hello, {name} nice to meet you!")
#personal_greeting()
    
def formal_name():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    first_fname = fname[:1]
    print(f"{first_fname}. {lname}")

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    ounces = round(ounces, 2)
    print("The weight in ounces is", ounces)
    
def generate_email():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    dob = input("Year of birth: ")
    fname = fname[:1]
    lname = lname[:4]
    dob = dob[2:]
    footer = "@myport.ac.uk"
    print(f"Email: {lname}.{fname}.{dob}{footer}")
    
def graphic_letters():
    text = input("What text would you like?")
    win = Window("letters", 400,400)
    for i in text:
        point = win.get_mouse()
        text_p = Text(Point(point.x, point.y), i)
        text_p.draw(win)
    win.get_mouse()
    win.close()

def sing_a_song():
    holder = ""
    text = input("What text would you like?")
    lines = int(input("lines: "))
    words = int(input("words per line: "))
    for i in range(words):
            holder = holder + text + " "
    for i in range(lines):
        print(f"{holder} \n")

def exchange_tables():
    for i in range(0,20+1):
            print(f"Pound:{i} {'%.2f' % (i*1.17):>15}")
            
def make_initialism():
    text = input("Phase: ")
    text = text.split()
    total = ""
    for i in text:
        i = i[:1]
        total = total + i
    total = total.upper()
    print(total)

def write_in_caps():
    input_file = open("quotation.txt", "r")
    contents = input_file.read()
    contents = contents.upper()
    print(contents)

def total_spending():
    input_file = open("spending.txt", "r")
    contents = input_file.read()
    contents = contents.split()
    total = 0
    for i in contents:
        i = float(i)
        total = total + i
    print(total)
    
    

