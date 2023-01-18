#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    count = [0] * 26
    for ch in s:
        if ch.isalpha():  
            count[ord(ch.lower()) - ord('a')] += 1
    
    for cnt in count:
        if cnt == 0:
            return 'not pangram'
    return 'pangram'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
