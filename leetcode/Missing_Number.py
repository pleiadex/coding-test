from typing import List
from math import log, ceil
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      res = 0

      # This does not look clean
      if len(nums) == 1:
        return nums[0] ^ 1

      for num in nums:
        res ^= num
      
      closestPowerOf2 = 2**ceil(log(len(nums) + 1 ,2))
      for num in range(len(nums) + 1, closestPowerOf2):
        res ^= num

      return res
