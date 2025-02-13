from Term_2.graphix import Window, Point, Rectangle, Polygon
import random

def main():
    door_colour, lights_on, num_houses = get_inputs()
    draw_street(door_colour, lights_on, num_houses)


def get_inputs():
    door_colour = input("Enter door colour: ")
    lights_on = float(input("The probability of the lights being on (0 to 1): "))
    num_houses = int(input("Enter the number of houses on the street: "))
    return door_colour, lights_on, num_houses


def draw_house(door_colour, lights_on, win, offset):
    roof_points = [Point(0 + offset, 60), Point(100 + offset, 0), Point(200 + offset, 60)]
    roof = Polygon(roof_points)
    roof.fill_colour = "pink"
    roof.outline_colour = "pink"
    roof.draw(win)

    # Draw wall and door
    draw_rectangle(win, Point(2 + offset, 60), Point(198 + offset, 198), "brown")
    draw_rectangle(win, Point(30 + offset, 110), Point(80 + offset, 198), door_colour)

    # Draw window
    window_colour = "yellow" if lights_on else "black"
    draw_rectangle(win, Point(110 + offset, 110), Point(170 + offset, 170), window_colour)


def draw_street(door_colour, lights_on, num_houses):
    win_width = 200 * num_houses
    win = Window("Street", win_width, 200)
    offset = 0
    for _ in range(num_houses):
        ran = random.random()
        lights_on = random.random() <= ran
        draw_house(door_colour, lights_on, win, offset)
        offset += 200
    win.get_mouse()


def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.fill_colour = colour
    rectangle.outline_colour = colour
    rectangle.draw(win)


main()