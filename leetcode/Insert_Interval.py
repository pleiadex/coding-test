from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

      res = []
      i = 0
      while i < len(intervals):
        if intervals[i][0] > newInterval[0] or self.isOverlapped(intervals[i], newInterval):
          break
        res.append(intervals[i])
        i += 1
      
      res.append(newInterval)

      while i < len(intervals):
        if self.isOverlapped(intervals[i], res[-1]):
          res[-1] = self.merge(intervals[i], res[-1])
        else:
          res.append(intervals[i])
        
        i += 1

      return res


    def isOverlapped(self, iv1, iv2):
      if iv1[1] < iv2[0]:
        return False
      if iv1[0] > iv2[1]:
        return False
      return True

    def merge(self, iv1, iv2):
      return [min(iv1[0], iv2[0]), max(iv1[1], iv2[1])]
