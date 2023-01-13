import unittest
from House_Robber_II import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([2,3,2], 3),
      ([1,2,3,1], 4),
      ([1,2,3], 3),
      ([1], 1)
    ]
  def test_rob(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.rob(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    