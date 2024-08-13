def solution(row1, row2):
    # Implement your solution here
    balance_1 = 0
    balance_2 = 0
    replace = 0

    for index in range(len(row1)):
        if row1[index] == '?':
            if row2[index] == row1[index]:
                continue
            replace += 1
            if row2[index] == 'W':
                balance_2 += 1
                balance_1 -= 1
            else:
                balance_2 -= 1
                balance_1 += 1
        else:
            if row2[index] == '?':
                    replace += 1
                
        if row1[index] == 'W':
            if row2[index] == 'W':
                return -1
            balance_1 += 1
            balance_2 -= 1

        if row1[index] == 'R':
            if row2[index] == 'R':
                return -1
            balance_1 -= 1
            balance_2 += 1

solution('W?WR?', 'R??W?')