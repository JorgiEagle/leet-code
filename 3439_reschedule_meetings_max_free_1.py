class queue:
    def __init__(self, size, elements=None):
        self.size = size
        self.elements = [0] * size
        self.cost = 0
        self._index = 0
        if elements is not None:
            for index, element in enumerate(elements):
                self.elements[index] = element
            self._index = len(elements) % size
            self.cost = sum(self.elements)

    def push(self, element):
        self.cost -= self.elements[self._index]
        self.cost += element
        self.elements[self._index] = element
        self._index = (self._index + 1) % self.size
        

def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    # obtain list of gaps between events
    gaps = queue(k+1)
    gaps.push(startTime[0])
    best_gap = gaps.cost
    for i in range(1, len(startTime)):
        gaps.push(startTime[i] - endTime[i-1])
        best_gap = max(best_gap, gaps.cost)
    gaps.push(eventTime-endTime[-1])
    best_gap = max(best_gap, gaps.cost)
    # find maximal continuous subset of gaps of length k
    return best_gap