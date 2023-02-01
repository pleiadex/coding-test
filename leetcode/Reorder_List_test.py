import unittest
from Reorder_List import Solution
from utils.Linked_List_Utils import convertLinkedListToList, convertListToLinkedList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        ([1,2,3,4], [1,4,2,3]),
        ([1,2,3,4,5], [1,5,2,4,3])
    ]
  def test_reorder_list(self):
    solution = Solution()

    for testcase in self.testcases:
      head = convertListToLinkedList(testcase[0])
      solution.reorderList(head)
      self.assertEqual(convertLinkedListToList(head), testcase[1])

if __name__ == '__main__':
  unittest.main()
    