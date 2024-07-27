from collections import deque
def countBinarySubstrings(s: str) -> int:
    substrings = 0
    count = deque([], 2)
    current_char = s[0]
    current_count = 0
    for x in s:
        if x == current_char:
            current_count += 1
        else:
            count.append(current_count)
            if len(count) > 1:
                substrings += min(count)
            current_count = 1
            current_char = x
    count.append(current_count)
    if len(count) < 2:
        return 0
    return substrings + min(count)


print(countBinarySubstrings("0"))
        