from time import time

def climbStairs(n: int) -> int:
    n += 1
    # Binet formula
    return int(((((1 + 5**0.5)/2)**n) - ((1 - 5**0.5)/2))/(5**0.5))


def climbStairs_2(n: int) -> int:
    sub_1, sub_2 = 1, 1
    for x in range(n-1):
        temp = sub_1
        sub_1 = sub_1 + sub_2
        sub_2 = temp
    return sub_1
x = 1000000

start_time = time()
climbStairs(x)
end_time = time()

print(end_time - start_time)