import time
from graphix import Window, Point, Rectangle, Text


# Used for the edit function
def draw_outline(win, point1, point2):
    rect = Rectangle(point1, point2)
    rect.outline_colour = "black"
    rect.outline_width = 5
    rect.draw(win)
    return rect


def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)
    return rect


def patch_plain(win, tl, br, colour):
    patch = []
    rect = Rectangle(tl, br)
    rect.fill_colour = colour
    rect.draw(win)
    patch.append(rect)
    return patch


# The H patch ()
def patch_2(win, tl, br, current_colour):
    patch = []
    colour_flip = True
    h_flip = True
    colour_store = current_colour
    flipped_colour = ""
    for Y in range(0, 100, 25):
        h_flip = not h_flip
        if Y >= 50:
            colour_flip = False
        for X in range(0, 100, 25):
            if colour_flip is False:
                current_colour = "white"
                flipped_colour = colour_store
            else:
                current_colour = colour_store
                flipped_colour = "white"
            rect_1 = draw_rectangle(win, Point(tl.x + X, tl.y + Y), br, current_colour)
            patch.append(rect_1)
            if h_flip:
                rect_2 = draw_rectangle(
                    win,
                    Point((tl.x + X) + 5, (tl.y + Y) + 25),
                    Point((tl.x + X) + 20, (tl.y + Y) + 15),
                    flipped_colour,
                )
                patch.append(rect_2)
                rect_3 = draw_rectangle(
                    win,
                    Point((tl.x + X) + 5, (tl.y + Y)),
                    Point((tl.x + X) + 20, (tl.y + Y) + 10),
                    flipped_colour,
                )
                patch.append(rect_3)
            else:
                rect_4 = draw_rectangle(
                    win,
                    Point((tl.x + X) + 15, (tl.y + Y) + 5),
                    Point((tl.x + X) + 25, (tl.y + Y) + 20),
                    flipped_colour,
                )
                patch.append(rect_4)
                rect_5 = draw_rectangle(
                    win,
                    Point((tl.x + X), (tl.y + Y) + 5),
                    Point((tl.x + X) + 10, (tl.y + Y) + 20),
                    flipped_colour,
                )
                patch.append(rect_5)
            colour_flip = not colour_flip
    return patch


def patch_1(win, tl, br, current_colour):
    patch = []
    for Y in range(0, 100, 20):
        for X in range(0, 100, 20):
            rect = Rectangle(Point(tl.x + X, tl.y + Y), br)
            rect.outline_colour = current_colour
            rect.draw(win)
            patch.append(rect)
            message = Text(Point(tl.x + (X + 10), tl.y + (Y + 10)), "Hi!")
            message.text_colour = current_colour
            message.draw(win)
            patch.append(message)
    return patch


# Primary patchwork function. Window, patchwork organization (colour, what patches to call etc) is done here.
def draw_patches(colours, size):
    patch_dict = {}
    window_size = size * 100
    counter = 0
    win = Window("Patchwork", window_size, window_size)
    for Y in range(0, window_size, 100):
        colour_count = True
        for X in range(0, window_size, 100):
            counter = counter + 1
            colour_count = not colour_count
            tl = Point(X, Y)
            br = Point(X + 100, Y + 100)
            if X > Y:
                current_colour = colours[1]
                if Y < 100 or X > window_size - 200:
                    patch = patch_1(win, tl, br, current_colour)
                else:
                    patch = patch_plain(win, tl, br, current_colour)
            else:
                if colour_count:
                    current_colour = colours[0]
                else:
                    current_colour = colours[2]
                if X < 100 or Y > window_size - 200:
                    patch = patch_plain(win, tl, br, current_colour)
                else:
                    patch = patch_2(win, tl, br, current_colour)
            patch_dict[(X, Y)] = patch
    return patch_dict, win


def delete_patch_group(patch_objects):
    for obj in patch_objects:
        obj.undraw()


# This function is used for editing the patchwork.
def edit_patchwork(colours, patch_dict, win):
    # A simple dictionary, used in the moving of patches. It keeps in what direction and how long it'll go.
    key_to_direction = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
    print(
        """
Your now in edit mode! Controls are as follows:
    - Select with your mouse what patch you'd like to edit
    - ESC | Deselect patch
    - X | Delete selected patch
    - 1,2,3 | Replace patch with a new H patch (1-Colour 1 etc)
    - 4,5,6 | Replace patch with a new Hi! patch (4-Colour 1 etc)
    - 7,8,9 | Replace patch with a new plain patch (8-Colour 1 etc)
    - Arrow keys | Move patch to the direction selected. Requires
    - the location to be empty!
          """
    )
    while True:
        click = win.get_mouse()
        patch_x, patch_y = click.x // 100 * 100, click.y // 100 * 100
        outline = draw_outline(
            win, Point(patch_x, patch_y), Point(patch_x + 100, patch_y + 100)
        )
        key = win.get_key()
        # Forces the outline to be undrawn, if any errors occur
        outline.undraw()
        # Deletes selected patch
        if key == "x":
            if (patch_x, patch_y) in patch_dict:
                delete_patch_group(patch_dict[(patch_x, patch_y)])
                patch_dict.pop((patch_x, patch_y))
                outline.undraw()
        # Deselects the patch
        elif key == "esc":
            click = None
            outline.undraw()
        # Replaces the selected patch with the H patch
        elif key == "1" or key == "2" or key == "3":
            if (patch_x, patch_y) in patch_dict:
                delete_patch_group(patch_dict[(patch_x, patch_y)])
                patch_dict.pop((patch_x, patch_y))
                outline.undraw()
                colour_select = int(key) - 1
                new_patch = patch_2(
                    win,
                    Point(patch_x, patch_y),
                    Point((patch_x + 100), (patch_y + 100)),
                    colours[colour_select],
                )
                patch_dict[(patch_x, patch_y)] = new_patch
        # Replaces the selected patch with the H patch
        elif key == "4" or key == "5" or key == "6":
            if (patch_x, patch_y) in patch_dict:
                delete_patch_group(patch_dict[(patch_x, patch_y)])
                patch_dict.pop((patch_x, patch_y))
                outline.undraw()
                colour_select = int(key) - 4
                new_patch = patch_1(
                    win,
                    Point(patch_x, patch_y),
                    Point((patch_x + 100), (patch_y + 100)),
                    colours[colour_select],
                )
                patch_dict[(patch_x, patch_y)] = new_patch
        # Replaces the selected patch with a plain patch
        elif key == "7" or key == "8" or key == "9":
            if (patch_x, patch_y) in patch_dict:
                delete_patch_group(patch_dict[(patch_x, patch_y)])
                patch_dict.pop((patch_x, patch_y))
                outline.undraw()
                colour_select = int(key) - 7
                new_patch = patch_plain(
                    win,
                    Point(patch_x, patch_y),
                    Point((patch_x + 100), (patch_y + 100)),
                    colours[colour_select],
                )
                patch_dict[(patch_x, patch_y)] = new_patch
        # Moves the patch in the direction selected, using the "key_to_direction" dictionary for the direction
        elif key == "Up" or key == "Left" or key == "Right" or key == "Down":
            move_cords = key_to_direction[key]
            move_x = move_cords[0]
            move_y = move_cords[1]
            # Checks if the patch in the direction selected exists
            if (patch_x + (move_x * 100), patch_y + (move_y * 100)) in patch_dict:
                print("Oops, its not empty there!")
            else:
                # For every object within the patch_dictionary, it'll be moved in the direction selected.
                for obj in patch_dict[(patch_x, patch_y)]:
                    # Within the range of 100, it'll move by 1, making the animation work with the sleep,
                    # and the placement correct with the "key_to_direction" dictionary
                    for _ in range(0, 100, 1):
                        obj.move(move_x, move_y)
                        time.sleep(0.00001)
                # Stores the patch objects, deletes the dictionary entry, then re-enters it with the new
                # location of the patch with all the objects with "store".
                store = patch_dict[(patch_x, patch_y)]
                del patch_dict[(patch_x, patch_y)]
                patch_dict[(patch_x + (move_x * 100), patch_y + (move_y * 100))] = store
            outline.undraw()


def get_inputs():
    # Size and colour options are defined here.
    size_allowed = [5, 7, 9]
    colours_allowed = ["red", "green", "blue", "magenta", "orange", "purple"]
    size = 0
    colours = []
    while size not in size_allowed:
        size = int(input(f"Please enter what size you'd like {size_allowed}: "))
    print("Please select a colour for your patch.")
    print(f"Colour options: {', '.join(colours_allowed)}")
    for i in range(3):
        colour = input(f"Colour {i + 1}: ")
        while colour in colours:
            print(
                "This colour is already in the list. Please choose a different colour."
            )
            colour = input(f"Colour {i + 1}: ")
        colours.append(colour)
    edit = input("If you'd like to edit the patch after, please enter 'Y': ")
    edit = edit.capitalize()
    if edit == "Y":
        edit = True
    else:
        edit = False
    return colours, size, edit


def main():
    colours, size, edit = get_inputs()
    patch_dict, win = draw_patches(colours, size)
    if edit:
        edit_patchwork(colours, patch_dict, win)

main()