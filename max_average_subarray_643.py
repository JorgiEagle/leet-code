def findMaxAverage(nums, k: int) -> float:
    current_max = sum(nums[:k])
    current_total = current_max
    for index in range(k, len(nums)):
        current_total += nums[index]
        current_total -= nums[index-k]
        current_max = max(current_max, current_total)
    return current_max/k

findMaxAverage([1,12,-5,-6,50,3], 4)