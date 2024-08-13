def search(nums: list[int], target: int) -> int:
    l_index, r_index = 0, len(nums)-1
    while l_index <= r_index:
        mid = (l_index + r_index)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l_index = mid+1
        else:
            r_index = mid-2

    if nums[mid] == target:
        return mid
    else:
        return -1 
    
search([-1,0,3,5,9,12], 2)