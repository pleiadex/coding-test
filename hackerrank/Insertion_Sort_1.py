#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
    
def insertionSort1(n, arr):
    # Write your code here
    curr = arr[n - 1]

    for i in range(n - 2, -2, -1):
        if i == -1:
            arr[0] = curr
            print(*arr)
        elif arr[i] > curr:
            arr[i + 1] = arr[i]
            print(*arr)
        else:
            arr[i + 1] = curr
            print(*arr)         
            break

    # Debug
    return arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
