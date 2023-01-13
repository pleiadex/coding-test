class Solution:
    def climbStairs(self, n: int) -> int:
      if n <= 2:
        return n
      
      steps = [0, 1, 2] + [0 for _ in range(n - 2)]

      for i in range(2, n):
        steps[i + 1] = steps[i] + steps[i - 1]

      return steps[n]