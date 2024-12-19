from graphix import Point, Circle, Rectangle, Window, Polygon

TILE = 100
SCREEN = 500
RADIUS = 50
BOX_SIZE = 50


def draw_circle(win, centre, radius, colour, outline):
    cir = Circle(centre, radius)
    cir.fill_colour = colour
    cir.outline_colour = outline
    cir.draw(win)


def draw_rectangle(win, tlp, brp, colour, outline):
    rect = Rectangle(tlp, brp)
    rect.fill_colour = colour
    rect.outline_colour = outline
    rect.draw(win)


def draw_triangle(win, p1, p2, p3, colour):
    tri = Polygon([p1, p2, p3])
    tri.fill_colour = colour
    tri.outline_colour = colour
    tri.draw(win)


def pat2():
    for Y in range(0, SCREEN, TILE):
        for X in range(0, SCREEN, TILE):
            if (X // TILE + Y // TILE) % 2 == 0:
                # Draw square
                p1 = Point(X, Y)
                p2 = Point(X + TILE, Y + TILE)
                draw_rectangle(win, p1, p2, "red", "black")
            else:
                # Draw circle
                center = Point(X + RADIUS, Y + RADIUS)
                draw_circle(win, center, RADIUS, "red", "black")
                # Draw white triangle
            if Y // TILE % 2 == 0:  # First row, left side
                draw_triangle(
                    win,
                    Point(X, Y),
                    Point(X, Y + TILE),
                    Point(X + RADIUS, Y + RADIUS),
                    "white",
                )
            else:  # Second row, right side
                draw_triangle(
                    win,
                    Point(X + TILE, Y),
                    Point(X + TILE, Y + TILE),
                    Point(X + RADIUS, Y + RADIUS),
                    "white",
                )
    win.get_mouse()
    win.close()


def stair_pattern():
    win = Window("Stair Pattern", SCREEN, SCREEN)
    for i in range(10):
        x = i * (SCREEN // 10)
        y = SCREEN - (i + 1) * (SCREEN // 10)
        p1 = Point(x, y)
        p2 = Point(x + BOX_SIZE, y + BOX_SIZE)
        draw_rectangle(win, p1, p2, "red", "black")
        win.get_mouse()
        win.close()


def plain_patch(win, tl, br, colour):
    rect = Rectangle(tl, br)
    rect.fill_colour = colour
    rect.draw(win)


def get_inputs():
    win_sizes = [5, 7, 9]
    colour_list = []
    size = 0
    while size not in win_sizes:
        size = int(input(f"Window size (Avalible Sizes {win_sizes} ): "))
    for i in range(3):
        color = input(f"colour {i+1}:")
        colour_list.append(color)
    return colour_list, size


def main():
    colour_list, size = get_inputs()
    main_patch(colour_list, size)


def main_patch(colour_list, size):
    window_size = size * 100
    win = Window("Patch", window_size, window_size)
    f_patch_flag = True
    for Y in range(0, window_size, 100):
        # If true, do the F patch
        f_patch_flag = not f_patch_flag
        for X in range(0, window_size, 100):
            tl = Point(X, Y)
            br = Point(X + 100, Y + 100)
            if X + Y == window_size - 100:
                # To define the current colour for section.
                current_colour = colour_list[0]
                # Check the f_patch_flag, IF true plain patch, ELSE true print f_patch
                plain_patch(win, tl, br, current_colour)
            elif X + Y < window_size - 100:
                current_colour = colour_list[1]
                # Check if the P patch should be used.
                # To do this, check if Y < 100 or X < 100
                plain_patch(win, tl, br, current_colour)
            else:
                current_colour = colour_list[2]
                # Check the f_patch_flag, IF true plain patch, ELSE true print f_patch
                plain_patch(win, tl, br, current_colour)


# 1- Try to do the F patch using the comments as a guide. You'll have to remake the patch code when
#    calling it!
# 2- Try to do the P patch using the comments again. Same as before you'll have to remake the patch code.
