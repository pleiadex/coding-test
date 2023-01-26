#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    count = [[] for i in range(100)]
    
    for i, pair in enumerate(arr):
        index = int(pair[0])
        if i < len(arr) // 2:
            count[index].append('-')
        else:
            count[index].append(pair[1])
        
    for s in count:
        if s:
            print(*s, end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
