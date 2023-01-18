#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    weightMap = {}
    prev = ''
    count = 0
    for curr in s:
        if prev != curr:
            prev = curr
            count = 0
        count += 1

        weight = (ord(prev) - ord('a') + 1) * count
        weightMap[weight] = True

    res = []
    for q in queries:
        if q in weightMap:
            res.append('Yes')
        else:
            res.append('No')
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
