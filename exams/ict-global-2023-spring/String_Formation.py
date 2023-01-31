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

# words = [
#     'valya',
#     'vvdoh',
#     'lyalb'
#   ]
# target = 'val'

# print(numWays(words, target))
