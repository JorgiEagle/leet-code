def longestCommonPrefix(strs: list[str]) -> str:
    longest_prefix = min(strs, key=len)
    for entry in strs:
        for index, letter in enumerate(longest_prefix):
            if entry[index] != letter:
                longest_prefix = longest_prefix[:index]
                break
        if not longest_prefix:
            return ""
    return longest_prefix

