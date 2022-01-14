def __init__(self):
    self.small,self.big=[],[]
    
def addNum(self, num: int) -> None:
    heapq.heappush(self.small,-num)
    if len(self.big) and -self.small[0]>self.big[0]:
        current=heapq.heappop(self.small)
        heapq.heappush(self.big,-current)
    if len(self.small)>len(self.big)+1:
        current=heapq.heappop(self.small)
        heapq.heappush(self.big,-current)
    if len(self.big)>len(self.small)+1:
        current=heapq.heappop(self.big)
        heapq.heappush(self.small,-current)

def findMedian(self) -> float:
    if len(self.small)>len(self.big):
        return -self.small[0]
    elif len(self.small)<len(self.big):
        return self.big[0]
    else:
        return 0.5*(-self.small[0]+self.big[0])