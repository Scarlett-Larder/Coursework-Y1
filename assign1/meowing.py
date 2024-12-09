from graphix import Window, Point, Circle, Rectangle


def draw_circle(win, centre, radius, colour, outline_colour="red"):
    circle = Rectangle(centre, radius)
    circle.fill_colour = colour
    circle.outline_colour = outline_colour
    circle.outline_width = 1
    circle.draw(win)
    return circle


def draw_patch(win, tl_x, tl_y, colour="red"):
    patch_objects = []
    for i in range(tl_x, tl_x + 100, 20):
        for j in range(tl_y, tl_y + 100, 20):
            circle = draw_circle(win, Point(i + 10, j + 10), Point(i + 20, j + 20), colour)
            patch_objects.append(circle)
    return patch_objects


def delete_patch_group(patch_objects):
    for obj in patch_objects:
        obj.undraw()


def main():
    win = Window()

    grid_objects = {}

    for x in range(0, 400, 100):
        for y in range(0, 400, 100):
            patch = draw_patch(win, x, y)
            grid_objects[(x, y)] = patch

    while True:
        click = win.get_mouse()
        patch_x, patch_y = click.x // 100 * 100, click.y // 100 * 100

        delete_patch_group(grid_objects[(patch_x, patch_y)])
        grid_objects.pop((patch_x, patch_y))

main()