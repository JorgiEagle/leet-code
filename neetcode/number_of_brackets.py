def solution(s: str) -> tuple[int, int]:
    """
    Accepts a string of brackets: ( and ), returns a tuple (x,y) where x is how many '(' must be added to the start of the string
    and y how many ")" must be added to the end to make it a valid and closed string of brackets
    """
    open_to_add = 0
    open_seen = 0
    for char in s:
        if char == ')':
            if open_seen == 0:
                open_to_add += 1
            else:
                open_seen -= 1
        elif char == '(':
            open_seen += 1
    return open_to_add, open_seen


print(solution("((()()))))))"))
print(solution(")))))(((()"))
print(solution(") () ) )("))
print(solution(""))