from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l_index = 0
    r_index = 0
    l_last = True
    index = 0
    odd = (len(nums1) + len(nums2)) % 2
    mid = (len(nums1) + len(nums2)) // 2
    while l_index < len(nums1) and r_index < len(nums2) and index < mid:
        if nums1[l_index] < nums2[r_index]:
            l_index += 1
            l_last = True
        else:
            r_index += 1
            l_last = False
        index += 1
    if index == mid:

        if odd:
            if l_index == len(nums1):
                return nums2[r_index]
            elif r_index == len(nums2):
                return nums1[l_index]
            if not l_last:
                return nums1[l_index]
            else:
                return nums2[r_index]
        else:
            return (nums1[l_index] + nums2[r_index]) /2
    if l_index == len(nums1):
        r_index += mid-index
        if odd:
            return nums2[r_index]
        else:
            return (nums2[r_index]+nums2[r_index+1])/2
    else:
        l_index += mid-index
        if odd:
            return nums1[l_index]
        else:
            return (nums1[l_index]+nums1[l_index])/2

print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))