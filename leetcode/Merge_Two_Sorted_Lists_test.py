import unittest
from Merge_Two_Sorted_Lists import Solution
from utils.Linked_List_Utils import convertLinkedListToList, convertListToLinkedList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
        ([], [], []),
        ([], [0], [0])
    ]
  def test_merge_two_lists(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        convertLinkedListToList(solution.mergeTwoLists(
            convertListToLinkedList(testcase[0]), 
            convertListToLinkedList(testcase[1])
            )), 
        testcase[2]
        )

if __name__ == '__main__':
  unittest.main()
    