from typing import List
import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

      heapq.heapify(intervals)
      prev = heapq.heappop(intervals)
      res = 0

      while intervals:
        curr = heapq.heappop(intervals)

        # overlap occurs
        if curr[0] < prev[1]:
          res += 1  

          # remove only if the previous interval overlaps the entire current interval
          if curr[1] > prev[1]:
            continue
        prev = curr
      return res