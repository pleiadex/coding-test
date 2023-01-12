import unittest
from Container_With_Most_Water import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([1,8,6,2,5,4,8,3,7], 49),
      ([1, 1], 1),
      ([1,8,6,2,15,14,8,13,7,9,20], 90)

    ]
  def test_max_area(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.maxArea(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    