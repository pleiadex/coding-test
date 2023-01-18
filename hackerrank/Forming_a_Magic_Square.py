#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    minCost = 100
    answer = [4,9,2,7,6,1,8,3]
    
    # get the input sequence
    arr = [s[0][0],s[0][1], s[0][2], s[1][2],s[2][2],s[2][1],s[2][0],s[1][0]]

    # compare
    for i in range(0, len(answer), 2):
      cost = 0
      for j in range(len(answer)):
        cost += abs(arr[j] - answer[(i + j) % len(answer)])

      minCost = min(minCost, cost)
    
    answer = answer[::-1]
    for i in range(1, len(answer), 2):
      cost = 0
      for j in range(len(answer)):
        cost += abs(arr[j] - answer[(i + j) % len(answer)])

      minCost = min(minCost, cost)


    return minCost + abs(s[1][1] - 5)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
