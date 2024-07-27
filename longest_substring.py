def lengthOfLongestSubstring(s: str) -> int:
    letters = {}
    front = 0
    back = 0
    longest = 0
    while front < len(s):
        if s[front] in letters:
            back = letters[s[front]] if letters[s[front]] > back else back
        letters[s[front]] = front
        longest = max(front - back, longest)
        front += 1
    return longest


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abba"))