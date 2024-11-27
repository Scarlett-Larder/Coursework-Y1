#Question 1
def say_name():
    print("Bazinga")
    
say_name()

#Question 2
def say_hello_2():
    print("hello");
    print("world");
    
say_hello_2()

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

#Queston 7
def zoom_zoom():
    zoom_level = int(input("zoom amount: "))
    zoom_level = zoom_level + 1
    for i in range(zoom_level):
        print("zoom", i)
zoom_zoom()