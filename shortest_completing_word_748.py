from collections import Counter

def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    l_counter = Counter(licensePlate.lower())
    valid_words = []
    for word in words:
        c_word = Counter(word)
        for letter in l_counter:
            if l_counter[letter] > c_word[letter]:
                break
        else:
            valid_words.append(word)
    return min(valid_words, key=len)

shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"])