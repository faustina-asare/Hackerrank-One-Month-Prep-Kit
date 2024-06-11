#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    total_no_of_elements = len(arr)
    positive_arr = []
    neg_arr = []
    zero_arr = []

    for a in arr:
        if a > 0:
            positive_arr.append(a)
        elif a < 0:
            neg_arr.append(a)
        else:
            zero_arr.append(a)

    positive_ratio = len(positive_arr) / total_no_of_elements
    print(round(positive_ratio, 6))
    negative_ratio = len(neg_arr) / total_no_of_elements
    print(round(negative_ratio, 6))
    zero_ratio = len(zero_arr) / total_no_of_elements
    print(round(zero_ratio, 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
