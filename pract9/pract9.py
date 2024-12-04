import math
from graphix import Window, Polygon


#Question 1
def display_date(day, month, year):
    month_names = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print(f"{day} {month_names[month-1]} {year}")

#Question 2
def words_length(list_of_words):
    for word in list_of_words:
        total_letters = 0
        for _ in word:
            total_letters += 1
        print(f"{word} {total_letters}")

#Question 3
def draw_hexagon():
    win = Window()
    points = []
    for i in range(6):
        click = win.get_mouse()
        points.append(click)
    print(points)
    triangle = Polygon(points)
    triangle.draw(win)
    win.get_mouse()

#Question 4
def test_marks():
    marks = []
    while True:
        mark = int(input("Please enter the mark (1-5). To exit enter a number above 5: "))
        marks.append(mark)
        if mark > 5:
            break
    for check in range(1,6):
        total = 0
        for mark in marks:
            if check == mark:
                total += 1
        print(f"{total} Students got: {check}")

#Question 5 - Do this later (:
def draw_barchart(values):
    for i in values:
        total = ""
        print(values[i])
        if values[i] > 0:
            total = total + "#"
        else:
            total = total + " "
        print(total)

#Question 6
def unique_models(values):
    topics = set()
    for i in values:
        topics.add(i)
    for top in topics:
        print(top)

#Question 8
def distance_between_tuples(p1, p2):
    distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return(distance)

#Question 9
def count_characters():
    characters = {}
    word = input("Please enter your string: ")
    for i in word:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    for character, total in characters.items():
        print(f"{total} occurrences of {character}")
