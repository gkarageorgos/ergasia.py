import random
import numpy as np


def game_termination_check(arr):
    if np.all(arr == arr[0]):
        return True
    if arr[1] == 2:
        return arr[0] + arr[2] == 4
    return False


def check_row(array, r):
    row = array[r]
    return game_termination_check(row)


def check_column(array, col):
    column = array[:, col]
    return game_termination_check(column)


def check_diagonal(array):
    diagonal = np.diagonal(array)
    return game_termination_check(diagonal)


def check_secondary_diagonal(array):
    secondary_diagonal = np.diagonal(np.fliplr(array))
    return game_termination_check(secondary_diagonal)


def game():
    square = np.zeros((3, 3), dtype=np.int32)
    caps = [1, 2, 3]*9       # 1.μικρό 2.μεσαίο 3.μεγάλο
    random.shuffle(caps)

    steps = 0
    while True:
        steps += 1
        x = random.randrange(3)
        y = random.randrange(3)
        cap = caps.pop()
        if cap > square[x][y]:
            square[x][y] = cap
            if check_row(square, x):
                return steps
            if check_column(square, y):
                return steps
            if x - y == 0:
                if check_diagonal(square):
                    return steps
            if x + y == 2:
                if check_secondary_diagonal(square):
                    return steps
        else:
            caps.append(cap)
            random.shuffle(caps)


steps_per_game = [game() for _ in range(100)]
print("The average number of the demanded steps for the termination of the game %.2f" % (sum(steps_per_game) / 100))
