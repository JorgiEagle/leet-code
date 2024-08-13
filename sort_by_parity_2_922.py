

def sortArrayByParityII(nums: list[int]) -> list[int]:
    even, odd = 0, 1
    while even < len(nums) and odd < len(nums):
        while even < len(nums) and not nums[even] % 2:
            even += 2
        while odd < len(nums) and nums[odd] % 2:
            odd += 2
        if even >= len(nums) or odd  >= len(nums):
            break
        temp = nums[even]
        nums[even] = nums[odd]
        nums[odd] = temp
    return nums

sortArrayByParityII([4,2,5,7])