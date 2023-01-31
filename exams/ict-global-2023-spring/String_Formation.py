#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING target
#

# FIXME: call depth exceed
def numWays(words, target):
    # Write your code here
    wLen = len(words[0])
    tLen = len(target)
    
    # (index, char) -> counts
    count = {}
    for w in words:
        for i, ch in enumerate(w):
            count[(i, ch)] = count.get((i, ch), 0) + 1
    
    # (word pointer, target pointer) // to reduce the number of recursive calls
    dp = {}
    
    def dfs(wIndex, tIndex):        
        if tIndex == tLen:
            return 1
        if wIndex == wLen or tLen - tIndex > wLen - wIndex: 
            return 0
        
        if (wIndex, tIndex) in dp:
            return dp[(wIndex, tIndex)]
        
        res = 0
        
        key = (wIndex, target[tIndex])
        
        # if the target char exists at the word pointer, 
        # multiply the number of the target character to the result from the recursive call
        if key in count:
            res += dfs(wIndex + 1, tIndex + 1) * count[key]
        res += dfs(wIndex + 1, tIndex)
           
        dp[(wIndex, tIndex)] = res
        return res

    return dfs(0, 0) % (10**9 + 7)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    target = input()

    result = numWays(words, target)

    fptr.write(str(result) + '\n')

    fptr.close()#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING target
#
def numWays(words, target):
    # Write your code here
    wLen = len(words[0])
    tLen = len(target)
    
    count = {}
    for w in words:
        for i, ch in enumerate(w):
            count[(i, ch)] = count.get((i, ch), 0) + 1
    
    
    dp = {}
    
    def dfs(wIndex, tIndex):        
        if tIndex == tLen:
            return 1
        if wIndex == wLen or tLen - tIndex > wLen - wIndex: 
            return 0
        
        if (wIndex, tIndex) in dp:
            return dp[(wIndex, tIndex)]
        
        res = 0
        
        key = (wIndex, target[tIndex])
        if key in count:
            res += dfs(wIndex + 1, tIndex + 1) * count[key]
        res += dfs(wIndex + 1, tIndex)
           
        dp[(wIndex, tIndex)] = res
        return res

    return dfs(0, 0) % (10**9 + 7)

words = [
    'valya',
    'vvdoh',
    'lyalb'
  ]
target = 'val'

print(numWays(words, target))
