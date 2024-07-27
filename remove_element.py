def removeElement(nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = len(nums) - nums.count(val)
        r_index = len(nums)-1
        val_index = 0
        while val_index < r_index:
            while val_index < len(nums) and nums[val_index] != val:
                val_index += 1
            while r_index >= 0 and nums[r_index] == val:
                r_index -= 1
            if val_index >= len(nums) or r_index < 0:
                break
            nums[val_index] = nums[r_index]
            r_index -= 1
        return k

print(removeElement([3, 3], 2))