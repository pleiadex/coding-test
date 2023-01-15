class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
          stack.append(ch)

        else:
          if not stack:
            return False
          curr = stack.pop()
          if ch == ")" and curr == "(":
            continue
          elif ch == "]" and curr == "[":
            continue
          elif ch == "}" and curr == "{":
            continue
          else:
            return False

      return len(stack) == 0