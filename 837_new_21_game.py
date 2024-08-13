from math import ceil
from itertools import product

def new21Game(n: int, k: int, maxPts: int) -> float:
    min_draws = ceil(k / maxPts)
    max_draws = k
    # min value is k
    # max value, is k-1 + maxPts
    min_val = k
    max_val = k - 1 + maxPts
    total = 0
    valid = 0
    for cards in range(min_draws, k+1):
        all_values = [1 if k <= sum(x) <= n else 0 for x in product(range(1, maxPts+1), repeat=cards)]
        total += len(all_values)
        valid += sum(all_values)
    return valid/total

print(new21Game(10, 1, 10))
print(new21Game(6, 1, 10))
print(new21Game(21, 17, 10))