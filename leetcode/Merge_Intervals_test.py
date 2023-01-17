import unittest
from Merge_Intervals import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
      ( [[1,4],[4,5]], [[1,5]])
    ]
  def test_erase_overlap_intervals(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.merge(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    