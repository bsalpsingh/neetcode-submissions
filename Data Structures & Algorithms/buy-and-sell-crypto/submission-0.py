class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp=prices[0]
        profit=0

        for i in range(len(prices)):
            if i == 0:
                continue  
            if prices[i-1] < cp:
                cp = prices[i-1]
            if prices[i] - cp > profit:
                  
                profit=prices[i]-cp 
        return profit 