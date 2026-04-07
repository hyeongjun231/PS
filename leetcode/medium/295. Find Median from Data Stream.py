class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hi, num)
        heapq.heappush(self.lo, -heapq.heappop(self.hi))
        if len(self.hi) < len(self.lo):
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2
        return self.hi[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()