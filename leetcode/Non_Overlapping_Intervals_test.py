import unittest
from Non_Overlapping_Intervals import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([[1,2],[2,3],[3,4],[1,3]], 1),
      ([[1,2],[1,2],[1,2]], 2),
      ([[1,2],[2,3]], 0),
      ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2),
      ([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]], 7)
    ]
  def test_erase_overlap_intervals(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.eraseOverlapIntervals(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    