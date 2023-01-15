import unittest
from Missing_Number import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([3,0,1], 2),
      ([0,1], 2),
      ([9,6,4,2,3,5,7,0,1], 8),
      ([1], 0),
      ([0], 1),
      ([0,1,2], 3)

    ]
  def test_missing_number(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.missingNumber(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    