class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for exp in range(31, -1, -1):
          bit = n % 2
          n = n // 2
          res += 2 ** exp * bit

        return res