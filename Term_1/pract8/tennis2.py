# Lecture 8 - an example of top-down design
from random import random


def get_inputs():
    point_win_probability = float(input("Probability of winning each point: "))
    number_of_games = int(input("Games to simulate: "))
    return point_win_probability, number_of_games

def simulate_sets(point_win_probability, number_of_sets):
    set_win = 0
    set_loss = 0
    for sets in range(number_of_sets):
        sets_wins = 0
        sets_loss = 0
        while True:
            game_result = simulate_games(point_win_probability)
            if game_result:
                sets_wins = sets_wins + 1
            else:
                sets_loss = sets_loss + 1
            print(f"Set: {sets} Game Result: win,{sets_wins} loss,{sets_loss}")
            if sets_wins >= 6 or sets_loss >= 6 or sets_wins <= sets_loss-2 or sets_loss <= sets_loss-2:
                break
            else:
                continue
        if sets_wins > sets_loss:
            set_win = set_win + 1
        else:
            set_loss = set_loss + 1
    return set_win, set_loss

def simulate_games(point_win_probability):
    points_player, points_opponent = simulate_game(point_win_probability)
    if points_player > points_opponent:
        win = True
    else: 
        win = False
    return win

def simulate_game(point_win_probability):
    points_player, points_opponent = 0, 0
    while not game_over(points_player, points_opponent):
        if random() < point_win_probability:
            points_player = points_player + 1
        else:
            points_opponent = points_opponent + 1
    return points_player, points_opponent


def game_over(points_player, points_opponent):
    return (points_player >= 4 or points_opponent >= 4) and \
        abs(points_player - points_opponent) >= 2


def print_summary(set_win, set_loss, number_of_games):
    proportion = set_win / number_of_games
    print(f"Wins: {set_win} Loss: {set_loss}, proportion: {proportion:.2f}")


def main():
    point_win_probability, number_of_games = get_inputs()
    set_win, set_loss = simulate_sets(point_win_probability, number_of_games)
    print_summary(set_win, set_loss, number_of_games)


main()