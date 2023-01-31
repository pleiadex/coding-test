#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getGroupedAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

from collections import defaultdict

def getGroupedAnagrams(words):
    # Write your code here
    hmap = defaultdict(list)
    res = []
    
    for s in words:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        hmap[tuple(count)].append(s)
    
    for key in hmap:
        res.append(hmap[key])
    
    return len(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = getGroupedAnagrams(words)

    fptr.write(str(result) + '\n')

    fptr.close()
