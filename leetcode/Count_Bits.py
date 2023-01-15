from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:

      res = [0, 1]
      if n < 2:
        return res[:n + 1]

      # FIXME: how to make it cleaner?
      while len(res) < n + 1:
        length = len(res)
        for i in range(length):
          if i + length < n + 1:
            res.append(res[i] + 1)
          else:
            break
      return res