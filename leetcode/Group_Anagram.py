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
        return res

        # return hmap.values()

        # count by each word + linear traversal => Time O(k * n * 26) ; The reason it is multiplied by 26 is Python hashes each tuple element and do Xor with the previous result.
        #                                       => Mem  O(n)
