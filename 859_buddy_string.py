from collections import Counter

def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    if s == goal:
        s_count = Counter(s)
        return any([x >= 2 for x in s_count.values()])
    index = 0
    second = 0
    while index < len(s):
        if s[index] != goal[index]:
            if second:
                second -= 1
                s = s[:second] + s[index] + s[second+1:index] + s[second] + s[index+1:]
                return s == goal
            else:
                second = index + 1
        index += 1
    return False


print(buddyStrings("ab", "ab"))

print(buddyStrings("ab", "ba"))

print(buddyStrings("aa", "aa"))

print(buddyStrings("baa", "aaa"))
