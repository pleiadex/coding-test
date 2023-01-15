from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        res = []

        for s in strs:
          key = ''.join(sorted(s))
          hmap[key].append(s)
        
        for key in hmap:
          res.append(hmap[key])


        # sort + linear traversal => Time O(klogk + n)
        #                         => Mem  O(n)

        return res