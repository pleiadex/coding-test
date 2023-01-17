import unittest
from Maximum_Subarray import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([-2,1,-3,4,-1,2,1,-5,4], 6),
      ([1], 1),
      ([5,4,-1,7,8], 23),
      ([-2,1,-3,4,-1,2,1,-5,14], 15),
      ([-2,1,-3,4,-1,2,1,-5,-9, 14], 14),
      ([-1, -3, 2], 2),
      ([-1], -1)

    ]
  def test_max_sub_array(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.maxSubArray(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()