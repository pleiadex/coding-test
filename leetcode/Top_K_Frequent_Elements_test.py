import unittest
from Top_K_Frequent_Elements import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([1,1,1,2,2,3], 2, [1,2]),
      ([1], 1, [1])
    ]
  def test_top_k_frequent_elements(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.topKFrequent(testcase[0], testcase[1]), testcase[2])

if __name__ == '__main__':
  unittest.main()
    