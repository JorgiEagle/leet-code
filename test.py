def solution(skills):
    winning_arr, winnging_index = divide(skills)
    winning_arr[winnging_index] -= 1
    return winning_arr


def divide(arr):
    if len(arr) == 1:
        return [1], 0
    else:
        left, l_winner = divide(arr[:len(arr)//2])
        right, r_winner = divide(arr[len(arr)//2:])
        winning_index = 0
        if arr[l_winner] > arr[(len(arr)//2)+r_winner]:
            left[l_winner] += 1
            winning_index = l_winner
        else:
            right[r_winner] += 1
            winning_index = (len(arr)//2) + r_winner
        return left+right, winning_index

print(solution([4, 2, 7, 3, 1, 8, 6, 5]))