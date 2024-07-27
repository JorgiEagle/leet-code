nums = [2, 1 ,3 ,4, 2]
print((len(nums)-nums[::-1].index(2)-1) - nums.index(2))