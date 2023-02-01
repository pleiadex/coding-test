import unittest
from Remove_Nth_Node_From_End_Of_List import Solution
from utils.Linked_List_Utils import convertLinkedListToList, convertListToLinkedList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1], 1, []),
        ([1,2], 1, [1])
    ]
  def test_reverse_list(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        convertLinkedListToList(
          solution.removeNthFromEnd(convertListToLinkedList(testcase[0]), testcase[1])
        ), 
        testcase[2]
        )

if __name__ == '__main__':
  unittest.main()
    