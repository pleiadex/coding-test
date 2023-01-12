from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}
        
        for i, num in enumerate(nums):
            if num in hmap:
                return [hmap[num], i]
            else:
                hmap[target - num] = i
        return []
