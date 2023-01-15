import unittest
from Reverse_Bits import Solution

class TestCase(unittest.TestCase):
  def setUp(self):
    self.testcases = [
      (int('00000010100101000001111010011100', 2), 964176192),
      (int('11111111111111111111111111111101', 2), 3221225471)
    ]
  def test_reverse_bits(self):
    solution = Solution()

    for testcase in self.testcases:
      self.assertEqual(solution.reverseBits(testcase[0]), testcase[1])

if __name__ == '__main__':
  unittest.main()
    