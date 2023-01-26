#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    
    for i in range(1, n):
        key = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > key:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = key
        print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
