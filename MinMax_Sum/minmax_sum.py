#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum_arr = []
    for positive_int in arr:
        if positive_int>0:
            each_sum_of_four_nums = sum(arr) - positive_int
            total_sum_arr.append(each_sum_of_four_nums)
    print(min(total_sum_arr), max(total_sum_arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
