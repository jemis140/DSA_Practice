class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min = float('inf')
        maxProfit = 0
        
        for i in prices:
            if i < min:
                min = i
            elif i -min > maxProfit:
                maxProfit = i - min
        return maxProfit