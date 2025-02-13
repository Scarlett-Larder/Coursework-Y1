
from graphix import Point

class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"

def test_point():
    p = Point(100, 50)


#Question 1, 2, 3

class Square:

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.x + side, p1.y + side)
        self.outline_colour = "black"
        self.fill_colour = "white"

    def get_perimeter(self):
        return self.side * 4
    
    def get_area(self):
        return self.side * self.side

    def get_center(self):
        start_point = self.p1
        center_x = start_point.x + self.side / 2
        center_y = start_point.y + self.side / 2
        return MyPoint(center_x, center_y)

    def __str__(self):
        return f"Square({self.p1}, {self.p2})"


def test_square():
    p = MyPoint(100, 50)
    square = Square(p, 50)

    print(f"Square's Outline colour: {square.outline_colour}")
    print(f"Square's Fill colour: {square.fill_colour}")

    square.fill_colour = "red"
    print(f"Chaning square's fill colour to {square.fill_colour}")

    print(f"Square's Outline colour: {square.outline_colour}")
    print(f"Square's Fill colour: {square.fill_colour}")

    print()

    print("Area: ", square.get_area())
    print("Perimeter:", square.get_perimeter())

    print()

    print(square.get_center())

# Question 4
class MyCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.fill_outline = "black"
        self.fill_colour = "white"
    
    def move(self, dx, dy):
        self.center = Point(self.center.x + dx, self.center.y + dy)
        
    def __str__(self):
        return f"MyCircle({self.center.x}),({self.center.y})"
    
def test_circle():
    circle = MyCircle(Point(100,200), 50)
    print(circle)
    circle.move(50,50)
    print(circle)


#Question 5
class BankAccount:

    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.account_name}: {self.balance}"

def test_bankaccount():
    tester = BankAccount("Scarlett")
    tester.deposit(50)
    print(tester)
    tester.withdraw(20)
    print(tester)

#Question 6
class HotelRoom:

    def __init__(self, room_num):
        self.room_num = room_num
        self.guest_name = ""
    
    def check_in(self, guest_name):
        self.guest_name = guest_name
    
    def check_out(self):
        self.guest_name = ""
    
    def is_occupied(self):
        if not self.guest_name:
            return False
        else:
            return True
    
    def __str__(self):
        if not self.guest_name:
            return f"Room number {self.room_num} is vacant"
        else:
            return f"Room number {self.room_num} is occupied by {self.guest_name}"

def test_hotel_room():
    hotel = HotelRoom(101)
    hotel.check_in("Winton")
    print(hotel)
    hotel.check_out()
    print(hotel)

#Question 7
class GradeBook:

    def __init__(self):
        self.grades = {}
    
    def add_grade(self, module_name, grade):
        self.grades[module_name] = grade

    def remove_grade(self, module_name):
        del self.grades[module_name]
    
    def adverage_grade(self):
        counter = 0
        total = 0
        for module, grades in self.grades.items():
            counter += 1
            total += grades
        return f"Adverage: {total / counter}"

    def get_grade(self, module_name):
        if module_name in self.grades:
            print(self.grades[module_name])
        else:
            print("Module not found!")
    
def test_gradebook():
    grade = GradeBook()
    grade.add_grade("Prog", 50)
    grade.get_grade("Prog")
    grade.add_grade("Wowza", 100)
    wow = grade.adverage_grade()
    print(wow)