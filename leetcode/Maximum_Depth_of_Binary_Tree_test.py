import unittest
from Maximum_Depth_of_Binary_Tree import Solution
from utils.Tree_Utils import convertListToTree, convertTreetoList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2], 2),
        ([3,9,20,None,None,15,7, None, 1], 4)
    ]
  def test_maxDepth(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        solution.maxDepth(convertListToTree(testcase[0])), 
        testcase[1]
      )

if __name__ == '__main__':
  unittest.main()
    