#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER people
#  2. INTEGER groups
#

def countOptions(p, g):
    if p < g: 
        return 0
    
    # matrix: p by g
    dp = [[0 for i in range(g + 1)] for i in range(p + 1)]
    
    # countOption(p, 1) => 1
    for i in range(1, p + 1):
        dp[i][1] = 1
    
    for i in range(1, p + 1):
        for j in range(2, g + 1):
            # always 0 if num of group is greater then num of people
            if i < j:
                dp[i][j] = dp[i-1][j-1]
            else: 
                dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
    return dp[p][g]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    people = int(input().strip())

    groups = int(input().strip())

    result = countOptions(people, groups)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
