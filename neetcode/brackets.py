def isValid(s: str) -> bool:
    open_brackets = set("({[")
    closing_brackets = ")}]"
    stack_of_open_brackets = []
    for char in s:
        if char in open_brackets:
            stack_of_open_brackets.append(char)
        else:
            if stack_of_open_brackets:
                most_recent_open_bracket = stack_of_open_brackets.pop()
                if most_recent_open_bracket != char:
                    return False
            else:
                return False
    if len(stack_of_open_brackets) > 0:
        return False
    return True


print(isValid("[]"))
print(isValid("([{}])"))
