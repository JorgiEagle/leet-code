def search(self, nums: List[int], target: int) -> int:
        l_index, r_index = 0, len(nums)-1
        while l_index <= r_index:
            mid = (l_index + r_index)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l_index = mid
            else:
                r_index = mid

        if nums[mid] == target:
            return mid
        else:
            return -1 