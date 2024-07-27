def validPalindrome(s: str, removed=True) -> bool:
    if len(s) < 2:
        return True
    for index in range(len(s)//2):
        if s[index] != s[len(s)-index-1]:
            if removed:
                return validPalindrome(s[index+1:len(s)-index], False) or validPalindrome(s[index:len(s)-index-1], False)
            else:
                return False
    return True

print(validPalindrome("abc"))