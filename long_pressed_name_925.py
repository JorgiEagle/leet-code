def isLongPressedName(name: str, typed: str) -> bool:
    typed_index = 0
    for char in name:
        while typed[typed_index] != char:
            typed_index += 1
        typed_index += 1
            
    return True

print(isLongPressedName("leelee", "lleeelee"))