from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort()
      res = [intervals[0]]

      for i in range(1, len(intervals)):
        # not overlapping
        if res[-1][1] < intervals[i][0]:
          res.append(intervals[i])

        # overlapping
        else:
          # res[-1] = [min(intervals[i][0], res[-1][0]), max(intervals[i][1], res[-1][1])]
          # it saved around 40ms
          res[-1][1] = max(intervals[i][1], res[-1][1])
      
      return res
