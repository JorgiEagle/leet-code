from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        straddle = len(nums1 + nums2) % 2
        median_index = len(nums1 + nums2) // 2
        i = j = 0
        while i+j <= median_index:
            if i == len(nums1):
                return nums2[median_index - (i+j)]
            elif j == len(nums2):
                return nums1[median_index - (i+j)]
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
        if not straddle:
            return (nums1[i] + nums2[j])/2
        else:
            return min(nums1[i], nums2[j])
        

print(findMedianSortedArrays([1, 3], [2]))

print(findMedianSortedArrays([1, 2], [3, 4]))

print(findMedianSortedArrays([1, 3, 6, 7, 12, 45], [2, 7]))
print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 3], [2]))