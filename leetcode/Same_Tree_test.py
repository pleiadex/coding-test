import unittest
from Same_Tree import Solution
from utils.Tree_Utils import convertListToTree

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([1,2,3], [1,2,3], True),
        ([1,2], [1, None, 2], False),
        ([1,1,2], [1,2,1], False),
    ]
  def test_is_same_tree(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        solution.isSameTree(
          convertListToTree(testcase[0]),
          convertListToTree(testcase[1])
        ), 
        testcase[2]
      )

if __name__ == '__main__':
  unittest.main()
    