from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      freq = [[] for _ in range(len(nums) + 1)]

      # count using a hash map
      for num in nums:
        count[num] = 1 + count.get(num, 0)
      
      # bucket sort -> Time O(n) Space O(n)
      for num, cnt in count.items():
        freq[cnt].append(num)
      
      res = []

      for i in range(len(freq)-1, 0, -1):
        res += freq[i]
        if len(res) == k:
          return res

      return []