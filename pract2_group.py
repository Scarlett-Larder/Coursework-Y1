def adverage_calc():
    int1 = int(input("First number"))
    int2 = int(input("Sec Number"))
    adverage = (int1 + int2) / 2
    print(adverage)
#adverage_calc()

def future_value():
    initial = int(input("How much is the inital amount: "))
    years = int(input("How many years: "))
    total = initial
    intrest = (initial / 100) * 3.5
    for i in range(years):
        total = intrest + total
    print(total)
future_value()