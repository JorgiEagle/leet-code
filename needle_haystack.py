import re

def strStr(haystack: str, needle: str) -> int:
        return re.search(needle, haystack).start()

print(strStr("leetcode","leeto"))