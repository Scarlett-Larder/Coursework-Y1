from random import random

def walk_pavement(length, pavement):
    current_square = length/2
    current_square = int(current_square)
    while 0 <= current_square < length:
        pavement[current_square] += 1
        if random() < 0.5:
            current_square -= 1
        else:
            current_square += 1

    print("|Square| Step |")
    for square, value in pavement.items():
        print(f"{value:>4}{square+1:>8}")

def make_pavement(length):
    pavement = {}
    for i in range(length):
        pavement[i] = 0
    return pavement

def main():
    length = int(input("How long should the pavement be: "))
    pavement = make_pavement(length)
    walk_pavement(length, pavement)

main()