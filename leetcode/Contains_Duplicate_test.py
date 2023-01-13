import unittest
from Contains_Duplicate import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([1,2,3,1], True),
      ([1,2,3,4], False),
      ([1,1,1,3,3,4,3,2,4,2], True)

    ]
  def test_contains_duplicate(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.containsDuplicate(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    