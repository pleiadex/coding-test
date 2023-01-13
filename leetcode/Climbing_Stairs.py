class Solution:
    def climbStairs(self, n: int) -> int:
      if n <= 2:
        return n
      
      twoStepBehind = 1
      oneStepBehind = 2

      for _ in range(n - 2):
        curr = oneStepBehind + twoStepBehind
        twoStepBehind =  oneStepBehind
        oneStepBehind = curr

      return oneStepBehind