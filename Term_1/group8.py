def mystery3():
    number = input("Enter a number: ")
    x = 0
    for y in number:
        x = x + int(y)
    print(x)

def mystery4(n):
    for i in range(n):
        for j in range(i, n):
            print("#", end="")
        print()

def mystery5(n):
    string = ""
    while n > 0:
        string = str(n % 2) + string
        n = n // 2
    print(string)
