def addToArrayForm(num: list[int], k: int) -> list[int]:
    index = len(num)-1
    while k > 0 and index > 0:
        num[index] += k%10
        push_index = index
        while push_index > 0 and num[push_index] > 9:
            num[push_index-1] += num[push_index] // 10
            num[push_index] %= 10
            push_index -= 1
        k //= 10
        index -= 1
    index = 0
    to_add = []
    num[index] += k%10
    if num[index] > 9:
        to_add = [num[index] // 10]
        num[index] %= 10
    k //= 10
    
    while k > 0:
        to_add = [k%10] + to_add
        k //= 10
    return to_add + num

addToArrayForm([6], 809)