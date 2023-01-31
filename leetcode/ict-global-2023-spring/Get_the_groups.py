#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTheGroups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY queryType
#  3. INTEGER_ARRAY students1
#  4. INTEGER_ARRAY students2
#
# from collections import defaultdict
def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    res = []
    circleMap = {}
    
    for i in range(len(queryType)):
        q = queryType[i]
        s1 = students1[i]
        s2 = students2[i]

        if not s1 in circleMap:
            circleMap[s1] = set([s1])
        
        if not s2 in circleMap:
            circleMap[s2] = set([s2])
        
        if q == 'Friend':
            newCircle = circleMap[s1].union(circleMap[s2])
            for member in newCircle:
                circleMap[member] = newCircle
            
        if q == 'Total':
            c1 = circleMap[s1]
            c2 = circleMap[s2]
            
            if c1 == c2:
                res.append(len(c1))
            else:
                res.append(len(c1) + len(c2))
            
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    queryType_count = int(input().strip())

    queryType = []

    for _ in range(queryType_count):
        queryType_item = input()
        queryType.append(queryType_item)

    students1_count = int(input().strip())

    students1 = []

    for _ in range(students1_count):
        students1_item = int(input().strip())
        students1.append(students1_item)

    students2_count = int(input().strip())

    students2 = []

    for _ in range(students2_count):
        students2_item = int(input().strip())
        students2.append(students2_item)

    result = getTheGroups(n, queryType, students1, students2)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
