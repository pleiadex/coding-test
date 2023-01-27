#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    return min(helper(arr[:]), helper(arr[::-1]))
            
            
def helper(arr):
    sortedArray = sorted(arr)
    
    # every element is distinct
    value2Index = {}
    for i, n in enumerate(arr):
        value2Index[n] = i
    
    res = 0
    for i, n in enumerate(arr):
        
        goodValue = sortedArray[i]
        badIndex = value2Index[goodValue]
        
        if i != badIndex: 
            res += 1
            arr[i] = goodValue
            arr[badIndex] = n
            
            value2Index[n] = badIndex
        
    return res
    
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
