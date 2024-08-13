from heapq import heapify, heappop, heappushpop
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(nums) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if val > self.heap[0]:
            heappushpop(self.heap, val)
        return self.heap[0]

KthLargest(3,[4,5,8,2])