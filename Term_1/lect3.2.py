from graphix import Window, Text, Point, Circle

def hello_graphix():
    win = Window("Wowza", 600, 100)
    
    input_text = input("YO: ")
    point = Point(200,25)
    text = "wowza"+input_text
    
    message = Text(point, text)
    message.draw(win)
    
    for i in range(10):
        message.move(i,0)
        win.get_mouse()

    
    win.close()
    
hello_graphix()