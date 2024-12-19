from random import random

def take_a_walk(num_steps):
    steps_forward_of_start = 0
    for step in range(num_steps):
        if random() < 0.5:
            steps_forward_of_start = steps_forward_of_start - 1
        else:
            steps_forward_of_start = steps_forward_of_start + 1
    return abs(steps_forward_of_start)

def print_expected_distance(average_steps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", average_steps)

def take_walks(num_walks, num_steps):
    total_steps = 0
    for walk in range(num_walks):
        steps_away = take_a_walk(num_steps)
        total_steps = total_steps + steps_away
    return total_steps / num_walks

def get_inputs():
    num_walks = int(input("How many random walks to take? "))
    num_steps = int(input("How many steps for each walk? "))
    return num_walks, num_steps

def main():
    num_walks, num_steps = get_inputs()
    average_steps = take_walks(num_walks, num_steps)
    print_expected_distance(average_steps)

main()

