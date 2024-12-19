#Question 1
def say_name():
    print("Bazinga")
    
say_name()

#Question 2
def say_hello_2():
    print("hello");
    print("world");
    
# say_hello_2()

#Question 3
def dollars_to_pounds():
    dollar = float(input("Please input your number of dollars:"))
    dollar_convert = dollar * 1.35
    print(dollar_convert)

#Question 4
def sum_and_diffrence():
    num_1 = float(input("Please enter your first number:"))
    num_2 = float(input("Please enter your second number:"))
    sum = num_1 + num_2
    dif = num_1 - num_2
    print("Your sum is", sum, "Your diffrence is", dif)

#Question 5
def change_counter():
    one_pence = float(input("How many 1s do you have: "))
    two_pence = float(input("How many 2s do you have: "))
    five_pence = float(input("How many 5s do you have: "))
    two_pence = two_pence * 2
    five_pence = five_pence * 5
    sum = (one_pence + two_pence + five_pence) / 100
    print("Your total amount is: ",sum)

#Question 6
def ten_hellos():
    for i in range(10):
            print("HELLO")
#ten_hellos()
#Queston 7
def zoom_zoom():
    zoom_level = int(input("zoom amount: "))
    for i in range(zoom_level):
        print("zoom", i+1)
#zoom_zoom()

#Question 8
def count_to():
    count = int(input("Please enter your amount"))
    for i in range(count):
        print(i)
# count_to()

#question 9
def count_from_to():
    count_1 = int(input("Please enter your first amount"))
    count_2 = int(input("Please enter your second amount"))
    for i in range(count_1, count_2 + 1):
        print(i)
#count_from_to()

#question 10
def weight_table():
    ounce_ten_kilo = 352.74
    for i in range(1, 10):
        ounce_amount = ounce_ten_kilo * i
        kilo_amount = i * 10
        print("Kilo:",kilo_amount, "Ounce: ",ounce_amount)
weight_table()

#question 11
def future_value():
    initial = int(input("How much is the inital amount: "))
    years = int(input("How many years: "))
    total = initial
    intrest = (initial / 100) * 3.5
    for i in range(years):
        total = intrest + total
    print(total)
#future_value()