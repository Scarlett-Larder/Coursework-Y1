import random

#Question 1
def main():
    num_filps = get_inputs()
    heads,tails = simulate_flips(num_filps)
    display_results(heads,tails,num_filps)


def get_inputs():
    num_filps = int(input("Please enter your inputs: "))
    return num_filps


def simulate_flips(num_filps):
    heads = 0
    tails = 0
    for _ in range(num_filps):
        result = random.randint(1,2)
        if result == 1:
            heads += 1
        else:
            tails += 1
    return heads, tails


def display_results(heads,tails, num_flips):
    print(f"Heads: 0.{num_flips - heads} Tails: 0.{num_flips - tails}")


main()