import unittest
from Climbing_Stairs import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (2, 2),
      (3, 3),
      (5, 8)

    ]
  def test_climb_stairs(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.climbStairs(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    