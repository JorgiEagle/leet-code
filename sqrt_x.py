from random import randint

def mySqrt(x: int) -> int:
    if x in [0, 1]:
        return x
    current_guess = x/2
    counter = 1
    next_guess = 0.5 * (current_guess + (x/current_guess))
    while next_guess//1 != current_guess//1:
        counter += 1
        current_guess = next_guess
        next_guess = 0.5 * (current_guess + (x/current_guess))
    return int(current_guess), counter

def mySqrt_b(x: int) -> int:
    left = 0
    right = x
    counter = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid < x:
            left = mid + 1
        elif mid * mid > x:
            right = mid -1
        else:
            return mid, counter
        counter += 1
        
    return right, counter

z = 100
y = randint(10**z, 10**(z+1))
print(mySqrt(y))

print(mySqrt_b(y))
