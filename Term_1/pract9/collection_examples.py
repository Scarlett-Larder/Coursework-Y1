from graphix import Window, Circle, Point, Polygon


# Examples of Lists:
def display_months():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in months:
        print(month)


def display_temperature_of_week():
    temperatures = [14.5, 8.0, -2.5, 15.0, 12.5, 9.0, -1.0]
    for temp in temperatures:
        print(f"It's {temp} degrees today")
        if temp < 0:
            print("Brrrrr, that's freezing!")


def process_numbers():
    numbers = [11, 28, 32, 34, 45, 67, 70, 89, 90, 99]
    for i in range(len(numbers)):
        if i % 2 == 0:  # Only process numbers at even indexes
            square = numbers[i] ** 2
            print(f"The square of {numbers[i]} is {square}")


def read_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        num = int(input("Enter a prime number less than 20: "))
        if num in primes:
            break
    print(f"{num} is a prime number less than 20")


def change_colours():
    win = Window()
    circles = []
    for x in range(50, 200, 100):
        for y in range(50, 200, 100):
            circle = Circle(Point(x, y), 50)
            circle.fill_colour = "red"
            circle.draw(win)
            circles.append(circle)  # Add the circle to the list

    for circle in circles:  # For each circle in the list
        win.get_mouse()  # Wait for a mouse click
        circle.fill_colour = "green"  # Change the colour of the circle


# Example of Tuples:
def display_menu():
    menu = [("Chicken Tikka Masala", 900, 8.95),
            ("Lamb Rogan Josh", 700, 7.95),
            ("Vegetable Biryani", 600, 6.95),
            ("Portion of poppadoms", 100, 0.75)]
    for item in menu:
        name, calories, price = item
        print(f"{name:20} {calories:5} calories, £{price:4.2f}")


# Example of Sets:
def filter_fruits():
    fruits = {"apple", "banana", "kiwi", "pear", "orange"}
    favourite_fruits = set()  # Create an empty set
    for fruit in fruits:
        if fruit != "kiwi" and fruit != "pear":
            favourite_fruits.add(fruit)
    print(favourite_fruits)


# Example of Dictionaries:
def iterate_students():
    students = {
        3419903: "Lou",
        7470773: "Nannie",
        5285384: "Hester"
    }
    for up_num in students:
        name = students[up_num]
        print(f"UP{up_num} is {name}")
