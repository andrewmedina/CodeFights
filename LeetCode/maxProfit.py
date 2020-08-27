class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        maxprof, low = 0, prices[0]
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            maxprof = max(maxprof, prices[i] - low)
        return maxprof