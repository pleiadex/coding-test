class Solution:
    def countSubstrings(self, s: str) -> int:

      res = 0

      for i in range(len(s)):
        # odd number of length
        l = r = i
        while 0 <= l and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1 

        # even number of length
        l, r = i, i + 1
        while 0 <= l and r < len(s) and s[l] == s[r]:
            res += 1
            l += -1
            r += +1
      
      return res