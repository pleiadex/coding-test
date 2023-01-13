import unittest
from Valid_Anagram import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ("anagram", "nagaram", True),
      ("rat", "car", False)

    ]
  def test_is_anagram(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.isAnagram(testcase[0], testcase[1]), testcase[2])

if __name__ == '__main__':
  unittest.main()
    