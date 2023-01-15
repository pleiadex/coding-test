import unittest
from Group_Anagram import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (["eat","tea","tan","ate","nat","bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
      ([""], [[""]]),
      (["a"], [["a"]])

    ]
  def test_is_anagram(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.groupAnagrams(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    