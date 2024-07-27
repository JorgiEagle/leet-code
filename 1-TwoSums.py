# https://leetcode.com/problems/two-sum/

def twoSum(nums: list[int], target: int) -> list[int]:
    hash_nums = [None] * (max(nums)+1)
    for index, element in enumerate(nums):
        if hash_nums[target-element]:
            return [index, hash_nums[target-element]]
        hash_nums[element] = index


if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))