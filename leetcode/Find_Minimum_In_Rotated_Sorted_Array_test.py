import unittest
from Find_Minimum_In_Rotated_Sorted_Array import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([3,4,5,1,2], 1),
      ([4,5,6,7,0,1,2], 0),
      ([11,13,15,17], 11),
      ([2,1], 1)
    ]
  def test_find_min(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.findMin(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    