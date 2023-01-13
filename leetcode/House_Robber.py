from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
      money = [0]
      money.append(nums[0])
      if len(nums) == 1:
        return money[-1]

      money.append(max(nums[0], nums[1]))
      if len(nums) == 2:
        return money[-1]
      
      for i in range(2, len(nums)):
        money.append(max(money[-2] + nums[i], money[-1]))

      return money[-1]