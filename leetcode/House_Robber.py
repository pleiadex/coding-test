from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

      # A smart way to eliminate any branches by edge cases
      rob1, rob2 = 0, 0

      for n in nums:
        money = max(rob1 + n, rob2)
        rob1, rob2 = rob2, money
      
      return rob2