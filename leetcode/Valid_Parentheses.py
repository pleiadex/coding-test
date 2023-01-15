class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      bracket = {'(': ')', '[': ']', '{': '}'}
      for ch in s:
        if ch in bracket:
          stack.append(ch)

        else:
          if not stack or bracket[stack.pop()] != ch:
            return False

      return len(stack) == 0