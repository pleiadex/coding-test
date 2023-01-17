import unittest
from Insert_Interval import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (([[1,3],[6,9]], [2,5]), [[1,5],[6,9]]),
      (([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]]),
      (([], [1,4]), [[1,4]]),
      (([[1,5]], [0,0]), [[0,0],[1,5]]),
      (([[1,1],[6,9]], [3,4]), [[1,1],[3,4],[6,9]])
    ]
  def test_insert(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.insert(*testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    