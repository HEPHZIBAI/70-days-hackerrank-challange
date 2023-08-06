/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/array-left-rotation
*/



import math
import os
import random
import re
import sys

def rotateLeft(d, arr):
    m=arr[0:d]
    h=[]
    h.extend(arr[d:len(arr)])
    h.extend(m)
    return(h)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
