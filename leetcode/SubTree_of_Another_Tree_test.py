import unittest
from SubTree_of_Another_Tree import Solution
from utils.Tree_Utils import convertListToTree

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([3,4,5,1,2], [4,1,2], True),
        ([3,4,5,1,2,None,None,None,None,0], [4,1,2], False)
    ]
  def test_is_subtree(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        solution.isSubtree(
          convertListToTree(testcase[0]),
          convertListToTree(testcase[1])
        ), 
        testcase[2]
      )

if __name__ == '__main__':
  unittest.main()
    