import unittest
from Longest_Palindromic_Substrings import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ("babad", "bab"),
      ("cbbd", "bb")
    ]
  def test_longest_palindrome(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.longestPalindrome(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    