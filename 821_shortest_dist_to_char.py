def shortestToChar(s: str, c: str):
        all_c = [s.index(c)]
        try:
            while True:
                all_c.append(s[all_c[-1]+1:].index(c)+all_c[-1]+1)
        except ValueError:
            pass
        char_index = 0
        results = []
        for index in range(len(s)):
            if char_index < len(all_c):
                if index == all_c[char_index]:
                    results.append(0)
                    char_index += 1
                else:
                    results.append(min(abs(index-all_c[char_index]), abs(index-all_c[char_index-1])))
            else:
                 results.extend(range(1, len(s)-index+1))
                 break
        return results

shortestToChar("abaa", "b")