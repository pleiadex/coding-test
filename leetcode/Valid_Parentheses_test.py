import unittest
from Valid_Parentheses import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ("()", True),
      ("()[]{}", True),
      ("(]", False)

    ]
  def test_is_valid(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.isValid(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    