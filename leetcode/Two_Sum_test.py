import unittest
from Two_Sum import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([2,7,11,15], 9, [0,1]),
      ([3,2,4], 6, [1,2]),
      ([3,3], 6, [0,1])
    ]
  def test_two_sum(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.twoSum(testcase[0], testcase[1]), testcase[2])

if __name__ == '__main__':
  unittest.main()
    