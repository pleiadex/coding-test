class Solution:
    def countSubstrings(self, s: str) -> int:

      res = 0

      # odd number of length
      for i in range(len(s)):
        l, r = i, i
        while 0 <= l and r < len(s):
          if s[l] == s[r]:
            res +=1
            l += -1
            r += +1
          else:
            break 

      # even number of length
      for i in range(len(s) - 1):
        l, r = i, i + 1
        while 0 <= l and r < len(s):
          if s[l] == s[r]:
            res += 1
            l += -1
            r += +1
          else: 
            break
      
      return res