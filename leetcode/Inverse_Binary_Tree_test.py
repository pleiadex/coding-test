import unittest
from Inverse_Binary_Tree import Solution
from utils.Tree_Utils import convertListToTree, convertTreetoList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([2,1,3], [2,3,1]),
        ([], []),
        ([3,9,20,None,None,15,7, None, 1], [3,20,9,7,15,None,None,None,None,1])
    ]
  def test_insert(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        convertTreetoList(solution.invertTree(convertListToTree(testcase[0]))), 
        testcase[1]
        )

if __name__ == '__main__':
  unittest.main()
    