#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#
def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


def maximumToys(a, k):
    spend = 0
    counter = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                # swap(a, j, j + 1)
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp

        # if spend + a[i] > k:
        #     break
        # else:
        #     spend += a[i]
        #     counter += 1

    # print("sorted: ", a)
    for i in range(len(a)):
        if spend + a[i] > k:
            break
        else:
            spend += a[i]
            counter += 1
    # print(a)
    return counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
