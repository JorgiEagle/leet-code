from math import log10, floor

def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        no_digits = floor(log10(x))+1
        # even no digits
        if no_digits % 2 == 0:
            return x%11 == 0
        # odd
        else:
            for digit_no in range(1, (no_digits//2)+1):
                right_digit_no = no_digits - digit_no + 1

                left_digit = (x%(10**digit_no)) // (10**(digit_no-1))
                right_digit = (x%(10**right_digit_no))//(10**(right_digit_no-1))
                if left_digit != right_digit:
                    return False
            return True
        

isPalindrome(121)
isPalindrome(15651)