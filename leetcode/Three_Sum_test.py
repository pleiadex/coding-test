import unittest
from Three_Sum import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
      ([0,1,1], []),
      ([0,0,0], [[0,0,0]]),
      ([-2,0,0,2,2], [[-2,0,2]])

    ]
  def test_three_sum(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.threeSum(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    