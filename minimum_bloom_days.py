from itertools import groupby
from math import inf
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        elif len(bloomDay) == m*k:
            return max(bloomDay)
        else:
            current_best = inf
            values = list(sorted(set(bloomDay)))
            l, r = 0, len(values)-1
            
            while l <= r:
                mid = (l+r)//2
                day = values[mid]
                dayBloom = map(lambda x: x<=day, bloomDay)
                all_groups = groupby(dayBloom)
                all_valid_groups = [len(list(g)) for x, g in all_groups if x]
                running_total = sum(group//k for group in all_valid_groups)
                if running_total < m:
                    l = mid + 1
                else:
                    current_best = min(day, current_best)
                    r = mid - 1

            return current_best
        

solution = Solution()

print(solution.minDays([1,10,3,10,2], 3, 1))
print(solution.minDays([1,10,3,10,2], 3, 2))
print(solution.minDays([7,7,7,7,12,7,7], 2, 3))