from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False

      sMap = {}
      tMap = {}
      
      # count the number of each char
      for i in range(len(s)):
        sMap[s[i]] = sMap.get(s[i], 0) + 1
        tMap[t[i]] = tMap.get(t[i], 0) + 1
      
      # FIXME: unneccesary condition
      if len(sMap) != len(tMap):
        return False

      for ch in sMap:
        if sMap[ch] != tMap.get(ch, 0):
          return False
      
      return True