import unittest
from Number_of_Islands import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ], 1),
      ([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ], 3),
      ([
        ["1","0","1","1","0","1","1"]
       ], 3)
    ]
  def test_num_islands(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.numIslands(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    