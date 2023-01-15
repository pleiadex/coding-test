from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:

      res = [0, 1]
      if n < 2:
        return res[:n + 1]

      for i in range(2, n + 1):
        res.append(i % 2 + res[i//2])
      return res