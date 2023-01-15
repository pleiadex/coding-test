import unittest
from Valid_Palindrome import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ("A man, a plan, a canal: Panama", True),
      ("race a car", False),
      (" ", True),
      (".,", True),
      ("0P", False)

    ]
  def test_is_palindrome(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.isPalindrome(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    