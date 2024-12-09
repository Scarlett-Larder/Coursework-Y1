from graphix import Window, Rectangle, Circle, Point


# Function to draw a rectangle with specified parameters
def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.outline_colour = "black"
    rect.draw(win)


# Function to draw a circle with specified parameters
def draw_circle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.fill_colour = colour
    circle.draw(win)


def tile_1(win, tl,colour):
    TILE = 100
    SMALL_TILE = 20
    SMALL_RADIUS = 10

    X = tl.x
    Y = tl.y

    for y in range(Y, TILE + Y, SMALL_TILE):
        for x in range(X, TILE + X, SMALL_TILE):
            # Draw rectangle
            p1 = Point(x, y)
            p2 = Point(x + SMALL_TILE, y + SMALL_TILE)
            draw_rectangle(win, p1, p2, colour)
            # Draw circle
            center = Point(x + SMALL_RADIUS, y + SMALL_RADIUS)
            draw_circle(win, center, SMALL_RADIUS, "white")


def tile_2(win, tl,colour):
    TILE = 100
    SMALL_TILE = 20
    SMALL_RADIUS = 10

    X = tl.x
    Y = tl.y

    flag = True
    for y in range(Y, TILE + Y, SMALL_TILE):
        for x in range(X, TILE + X, SMALL_TILE):
            if (flag == True):
                # Draw rectangle
                p1 = Point(x, y)
                p2 = Point(x + SMALL_TILE, y + SMALL_TILE)
                draw_rectangle(win, p1, p2, colour)
            else:
                # Draw circle
                center = Point(x + SMALL_RADIUS, y + SMALL_RADIUS)
                draw_circle(win, center, SMALL_RADIUS, "white")
            flag = not flag


def placement_logic():
    pass


def program():
    SCREEN = 500
    TILE = 100
    first_colour = "blue"
    second_colour = "orange"
    third_colour = "red"


    win = Window("Grid Patterns", SCREEN, SCREEN)

    for x in range(0,500,100):
        p1 = Point(x, 100)
        p2 = Point(p1.x + TILE, p1.y + TILE)
        draw_rectangle(win, p1, p2, first_colour)

    for x in range(0,500,100):
        p1 = Point(x, 300)
        p2 = Point(p1.x + TILE, p1.y + TILE)
        if x == 100:
            draw_rectangle(win, p1, p2, second_colour)
        elif x == 200 or x == 300:
            draw_rectangle(win, p1, p2, third_colour)
        else:
            draw_rectangle(win, p1, p2, first_colour)

    for x in range(0,500,100):
        p1 = Point(x, 0)
        tile_2(win, p1, first_colour)
        p1 = Point(x, 400)
        tile_2(win, p1, first_colour)


    win.get_mouse()
    win.close()


program()
