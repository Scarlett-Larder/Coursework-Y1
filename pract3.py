from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    arms = Line(Point(300, 180), Point(100,180))
    arms.draw(win)
    legs_r = Line(Point(250, 280), Point(200,240))
    legs_r.draw(win)
    legs_l = Line(Point(150, 280), Point(200,240))
    legs_l.draw(win)
#draw_stick_figure()

def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()

def draw_circle():
    win = Window()
    message = Text(Point(200, 50), "Please look at the console")
    message.draw(win)
    radius = int(input("What's your radius: "))
    message.text = "This is your circle:"
    circle = Circle(Point(200, 200), radius)
    circle.draw(win)
    win.get_mouse()
    win.close()
#draw_circle()

def draw_archery_target():
    win = Window()
    circle_outer = Circle(Point(200, 200), 200)
    circle_mid = Circle(Point(200, 200), 150)
    circle_inner = Circle(Point(200, 200), 100)
    circle_outer.fill_colour = "blue"
    circle_mid.fill_colour = "red"
    circle_inner.fill_colour = "yellow"
    circle_outer.draw(win)
    circle_mid.draw(win)
    circle_inner.draw(win)
#draw_archery_target()

def draw_rectangle():
    win = Window()
    height = int(input("Height: "))
    width = int(input("Width: "))
    topleft_h = height / 2 + 200
    topleft_w = width / 2 + 200
    botright_h = 200 - height / 2
    botright_w = 200 - width / 2
    rectangle = Rectangle(Point(int(topleft_h), int(topleft_w)), Point(int(botright_h), int(botright_w)))
    rectangle.draw(win)
    win.get_mouse()
    win.close()
#draw_rectangle()
    
def blue_circle():
    win = Window()
    point = win.get_mouse()
    circle_point = Circle(Point(point.x, point.y), 100)
    circle_point.draw(win)
    win.get_mouse()
    win.close()
#blue_circle() 
    
def ten_lines():
    win = Window()
    for i in range(10):
        message = Text(Point(200, 50), "click on first point")
        message.draw(win)
        p1 = win.get_mouse()
        message.text = "click on second point"
        p2 = win.get_mouse()
        line = Line(p1, p2)
        line.draw(win)
        message.text = f"Click anywhere to continue ({i+1})"
        win.get_mouse()
        message.text = ""
    message.text = "Drawing finished!"  
    win.get_mouse()
    win.close()
#ten_lines()
  
def ten_strings():
    win = Window()
    string = input("Please enter your string: ")
    message = Text(Point(200, 50), "Click anywhere on screen")
    message.draw(win)
    for i in range (10):
        p1 = win.get_mouse()
        comp = Text(Point(p1.x, p1.y), string)
        comp.draw(win)
        print(f"Click anywhere to continue ({i+1})")
        message.text = ""
    message.text = "Drawing finished!"  
    win.get_mouse()
    win.close()
#ten_strings()

def ten_coloured_rectangles():
    win = Window()
    for i in range(3):
        colour = input("Colour: ")
        message = Text(Point(200, 50), "First Point")
        message.draw(win)
        p1 = win.get_mouse()
        message.text = "Second Point"
        p2 = win.get_mouse()
        rectangle = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y))
        rectangle.fill_colour = colour
        rectangle.draw(win)
        message.text = ""
    win.get_mouse()
    win.close()
#ten_coloured_rectangles()
    
