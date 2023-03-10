class Solution:
    def isPalindrome(self, s: str) -> bool:
      l, r = 0, len(s) - 1

      while l <= r:
        if s[l].isalnum():
          while not s[r].isalnum():
            r += -1
          if s[l].lower() != s[r].lower():
            return False
          r += -1
        l += 1
      return True