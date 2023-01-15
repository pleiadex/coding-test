import unittest
from Number_of_1_Bits import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (int('00000000000000000000000000001011', 2), 3),
      (int('00000000000000000000000010000000', 2), 1),
      (int('11111111111111111111111111111101', 2), 31)
    ]
  def test_reverse_bits(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.hammingWeight(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    