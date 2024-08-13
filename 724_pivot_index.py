def pivotIndex(nums: list[int]) -> int:
    left_sum = 0
    right_sum = sum(nums)
    for index, num in enumerate(nums):
        right_sum -= num
        if left_sum == right_sum:
            return index
        left_sum += num
        
        
    return -1

pivotIndex([1,7,3,6,5,6])