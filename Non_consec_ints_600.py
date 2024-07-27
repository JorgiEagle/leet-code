def findIntegers(n: int) -> int:
    max_len = 0
    while (n >> max_len) > 0:
        max_len += 1
    
    total = fib(max_len-1) + 2

    base_number = 1 << max_len-1
    if base_number == n:
        return total
    number_to_push = 1
    bin_length = 1
    while bin_length <= max_len-2:
        for x in range(max_len-bin_length-1):
            new_num = base_number + (number_to_push << x)
            if new_num <= n:
                total += 1
        number_to_push = (number_to_push << 2)+1
        bin_length += 2
    return total



def fib(n):
    first, second = 0, 1
    total = 1
    for x in range(n-1):
        result = first + second
        total += result
        first = second
        second = result
    return total


print(findIntegers(100))