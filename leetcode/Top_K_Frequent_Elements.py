from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      hmap = defaultdict(int)

      for num in nums:
        hmap[num] += 1
      
      res = []
      count = sorted(hmap.items(), key=lambda tup: -tup[1])
      for i in range(k):
        res.append(count[i][0])

      return res