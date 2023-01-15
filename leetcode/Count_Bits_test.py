import unittest
from Count_Bits import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (2, [0,1,1]),
      (5, [0,1,1,2,1,2]),
      (0, [0]),
      (1, [0, 1])
    ]
  def test_count_bits(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.countBits(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    