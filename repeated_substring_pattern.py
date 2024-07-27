def repeatedSubstringPattern(s: str) -> bool:
        if len(s) < 2:
            return True

        substring_lengths = [x for x in range(1, (len(s)//2)+1) if len(s)%x == 0]

        for sub_length in substring_lengths[::-1]:
            if all_equal(chunkstring(s, sub_length)):
                return True
        return False



def chunkstring(string, length):
    return (string[i:i + length] for i in range(0, len(string), length))

def all_equal(elements):
    first = next(elements)
    for element in elements:
        if first != element:
            return False
    return True


print(repeatedSubstringPattern("abab"))

