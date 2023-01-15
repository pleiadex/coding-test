import unittest
from Best_Time_To_Buy_And_Sell_Stock import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      ([7,1,5,3,6,4], 5),
      ([7,6,4,3,1], 0),
      ([4], 0)

    ]
  def test_max_profit(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.maxProfit(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    