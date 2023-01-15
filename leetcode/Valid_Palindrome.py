class Solution:
    def isPalindrome(self, s: str) -> bool:
      l, r = 0, len(s) - 1

      while l < r:
        # skip a non alphabet character
        while l < len(s) and not s[l].isalnum():
          l += 1
        while r >= 0 and not s[r].isalnum():
          r += -1
        
        # exit the loop if l or r is out of range
        if l == len(s) or r == -1:
          break

        if s[l].lower() != s[r].lower():
          return False

        else:
          l += 1
          r += -1
      return True