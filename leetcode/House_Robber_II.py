from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

      if len(nums) == 1:
        return nums[0]

      rob1, rob2 = 0, 0
      maxProfit = 0

      for n in nums[1:]:
        money = max(rob1 + n, rob2)
        maxProfit = max(money, maxProfit)
        rob1, rob2 = rob2, money
      
      rob1, rob2 = 0, 0
      for n in nums[:-1]:
        money = max(rob1 + n, rob2)
        maxProfit = max(money, maxProfit)
        rob1, rob2 = rob2, money
      
      return maxProfit