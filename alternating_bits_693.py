def hasAlternatingBits(n: int) -> bool:
    last = n%2
    while n > 0:
        n = n >> 1
        if last == n%2:
            return False
        else:
            last = n%2
    return True

print(hasAlternatingBits(5))
print(hasAlternatingBits(7))
print(hasAlternatingBits(11))