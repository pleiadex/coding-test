from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        res = []

        for s in strs:
          count = [0] * 26
          for ch in s:
            count[ord(ch) - ord('a')] += 1
          
          hmap[tuple(count)].append(s)
        
        for key in hmap:
          res.append(hmap[key])


        # count by each word + linear traversal => Time O(k * n)
        #                                       => Mem  O(n)

        return res