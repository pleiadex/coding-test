import unittest
from Linked_List_Cycle import Solution
from utils.Linked_List_Utils import convertLinkedListToList, convertListToLinkedList

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
        (([3,2,0,-4], 1), True),
        (([1,2], 0), True),
        (([1], -1), False)
    ]
  def test_has_cycle(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(
        solution.hasCycle(convertListToLinkedList(*testcase[0])), 
        testcase[1]
        )

if __name__ == '__main__':
  unittest.main()
    