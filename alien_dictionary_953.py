def isAlienSorted(words: list[str], order: str) -> bool:
    key = {item: index for index, item in enumerate(order)}
    word_conv = [[key[char] for char in x] for x in words]
    for index in range(1, len(words)):
        for w_index in range(min(len(words[index]), len(words[index-1]))):
            if word_conv[index][w_index] > word_conv[index-1][w_index]:
                break
            elif word_conv[index][w_index] < word_conv[index-1][w_index]:
                return False
    return True

isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")