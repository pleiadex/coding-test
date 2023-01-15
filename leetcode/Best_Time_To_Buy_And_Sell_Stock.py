from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGain = 0
        l, r = 0, 0

        while r < len(prices):
          if prices[l] <= prices[r]:
            maxGain = max(maxGain, prices[r] - prices[l])
            r += 1
          else:
            l = r
            r = l + 1

        return maxGain
