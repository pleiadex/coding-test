import unittest
from Reverse_Linked_List import Solution
from utils.Linked_List_Utils import convertLinkedListToList, convertListToLinkedList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([], [])
    ]
  def test_reverse_list(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        convertLinkedListToList(solution.reverseList(convertListToLinkedList(testcase[0]))), 
        testcase[1]
        )

if __name__ == '__main__':
  unittest.main()
    