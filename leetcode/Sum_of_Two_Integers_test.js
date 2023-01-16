const Solution = require('./Sum_of_Two_Integers');

const testcases =  [
  [2, 3, 5],
  [1, 2, 3],
  [-10, 9, -1],
  [-1, -1, -2],
  [-1, 1, 0]
]

testcases.forEach(testcase => {
  console.assert(Solution.getSum(testcase[0], testcase[1]) === testcase[2]);
})
/*
import unittest
from Sum_of_Two_Integers import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (2, 3, 5),
      (1, 2, 3),
      (-10, 9, -1),
      (-1, -1, -2),
      (-1, 1, 0)

    ]
  def test_get_sum(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.getSum(testcase[0], testcase[1]), testcase[2])

if __name__ == '__main__':
  unittest.main()
*/