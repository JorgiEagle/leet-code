def searchInsert(nums: list[int], target: int) -> int:
        # binary search
        search_length = len(nums)
        midpoint = (search_length+1) // 2
        while search_length > 1:
            if target == nums[midpoint-1]:
                return midpoint-1
            elif target < nums[midpoint-1]:
                search_length = midpoint
                midpoint //= 2
            else:
                search_length = len(nums) - midpoint
                midpoint = (midpoint // 2) + midpoint
        if midpoint < len(nums):
            if nums[midpoint] == target:
                return midpoint
            else:
                 return midpoint-1
        return midpoint


print(searchInsert([1,3,5,6], 7))