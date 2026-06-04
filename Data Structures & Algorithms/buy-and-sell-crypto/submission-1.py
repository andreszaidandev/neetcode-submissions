class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxProfit = 0
        while r != len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(prices[r]-prices[l], maxProfit)
            if prices[l] >= prices[r]:
                l = r
            r+=1
        return maxProfit