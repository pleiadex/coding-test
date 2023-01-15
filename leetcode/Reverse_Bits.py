class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
          # get each bit from LSD
          bit = n >> i & 1 
          res = (bit << (31 - i)) | res

        return res