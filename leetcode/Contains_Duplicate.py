from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        
        for n in nums:
          if n in hmap:
            return True
          else:
            hmap[n] = True
        return False