#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cardinalitySort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY nums as parameter.
#
def countBits(n):
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res

def cardinalitySort(nums):
    # Write your code here
    nums.sort(key = lambda x: (countBits(x), x))
    return nums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = cardinalitySort(nums)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
