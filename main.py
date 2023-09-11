import pandas as pd
import random
import itertools


def starting_random_numbers(n, lo, hi):
    if n > (hi - lo + 1):
        raise ValueError("Cannot generate unique numbers. Range too small.")
    random_numbers = random.sample(range(lo, hi + 1), n)
    return random_numbers


def unique_combinations(random_numbers, x, a, b):
    valid_combinations = []
    for combination in itertools.combinations(random_numbers, x):
        if a <= combination[-1] <= b:
            valid_combinations.append(combination)
    return valid_combinations


def engine(n, lo, hi, x, a, b):

    random_numbers = starting_random_numbers(n, lo, hi)
    combinations = unique_combinations(random_numbers, x, a, b)
    df = pd.DataFrame(combinations)
    df = df.sort_values(by=[0, 1, 2, 3, 4, 5], ascending=[True, True, True, True, True, True])
    df.to_csv('output.csv', index=False)


n = 30
lo = 1
hi = 39
x = 6
a = 1
b = 14

engine(n, lo, hi, x, a, b)