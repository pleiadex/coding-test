from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
      return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
      rob1, rob2 = 0, 0

      for n in nums:
        money = max(rob1 + n, rob2)
        rob1, rob2 = rob2, money
      
      return rob2