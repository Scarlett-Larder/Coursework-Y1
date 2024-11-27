from math import pi, sqrt, pow

#Question 1
def speed_calculator():
    int1 = int(input("How many km?  "))
    int2 = int(input("How many hours? "))
    kmh = int1 / int2
    print("Your km/h:",kmh)
#speed_calculator()

#Question 2
def circumference_of_circle():
    radius = int(input("What is the radius of the circle? "))
    circumference = 2 * pi * radius
    print(circumference)
#circumference_of_circle()

#Question 3
def area_of_circle():
    radius = int(input("What is the radius of the circle? "))
    area = pi * radius ** 2
    print(area)
#area_of_circle()

#Question 4 - IDK
def cost_of_pizza():   
    dia = int(input("What is the dia of the circle in cm? "))
    radius = dia / 2
    area = pi * radius ** 2
    print(area)
    cost  = area / 3.5
    print(cost)
cost_of_pizza()
    
#Question 5
def slope_of_line():
    x_1 = int(input("Point x_1: "))
    y_1 = int(input("Point y_1: "))
    x_2 = int(input("Point x_2: "))
    y_2 = int(input("Point y_2: "))
    m = (x_1 - x_2) / (y_1 - y_2)
    print(m)
#slope_of_line()

#Question 6
def distance_between_points():
    x_1 = int(input("Point x_1: "))
    y_1 = int(input("Point y_1: "))
    x_2 = int(input("Point x_2: "))
    y_2 = int(input("Point y_2: "))
    distance = sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    print(distance)
#distance_between_points()

#Question 7
def travel_statistics():
    adverage = int(input("Adverage speed: "))
    duration = int(input("Duration (in hours): "))
    distance = adverage * duration
    fuel_use = distance / 5
    print("The overall distance is: ", distance)
#travel_statistics()

#Question 8
def sum_of_squares():
    n = int(input("Heyo"))
    total = 0
    for counter in range(1, n+1):
        total += pow(counter, 2)
    print(total)
#sum_of_squares()

#Question 9
def adverage_of_numbers():
    ding = int(input("how many"))
    total = 0
    counter = 0
    for i in range(ding):
        num = int(input(""))
        total = total + num
        counter = counter + 1
    total = total / counter
    print(total)
#adverage_of_numbers()
    
#Question 10
def fibonacci():
    ding = int(input("how many"))
    num1 = 0
    num2 = 1
    newnum = num2
    for i in range(ding):
        num1, num2 = num2, newnum
        newnum = num1 + num2
        print(newnum)
fibonacci()
        

        