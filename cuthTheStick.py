#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # index = {}
    # for i in range(len(a)):
    #     index[i] = a[i]

    currentPos = 0
    for i in range(k):
        currentPos += 1
        if currentPos == k + 1:
            currentPos = 0

    FirstIndexIncrement = currentPos
    # print("Current Pos", currentPos)
    # print("currentPos: ", currentPos)
    print(queries)
    for i in range(len(queries)):

        if  FirstIndexIncrement - queries[i]   < 0:
            # print("inside if")
            newIndex =  (len(a)-1) - (queries[i] + FirstIndexIncrement )
        else:
            # print("inside else")
            newIndex =   queries[i] - FirstIndexIncrement

        # print("NewIndex = ", newIndex)

        print(a[newIndex])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    # print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
