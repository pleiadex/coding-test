from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

      res = []

      for i in range(len(intervals)):
        # when newInterval is left to the rest of intervals
        if intervals[i][0] > newInterval[1]:
          res.append(newInterval)
          return res + intervals[i:]
        
        # when newInterval is right to the current interval
        elif intervals[i][1] < newInterval[0]:
          res.append(intervals[i])
        
        # merge them when newInterval and the current interval have a overlapping portion.
        else:
          newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
      
      res.append(newInterval)
      return res