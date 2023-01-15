from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      maxValue = len(nums)
      return maxValue * (maxValue + 1) // 2 - sum(nums)