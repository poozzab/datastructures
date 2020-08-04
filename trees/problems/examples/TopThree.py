#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys

#solution for https://www.hackerrank.com/challenges/most-commons/

if __name__ == '__main__':
    # s is length n
    s = input()
    # d will become size O(n)
    d = defaultdict(lambda : 0)
    # run time O(n)
    # multimap for tracking occurrances of letters from s
    for l in s:
        d[l] = d[l] + 1
    # buckets will have, at most, 27 key value pairs stored where number of unique keys <= 27
    buckets = defaultdict(list)
    # load all letter-multiplicity pairs by their multiplicity
    # common multiplicities will be available in a list
    for k,v in d.items():
        buckets[v].append((k,v))
    # only want to print top three multiplicities
    prints = 0
    while prints < 3 and len(buckets) > 0:
        # get the letter(s) with most multiplicity
        m = max(buckets.keys())
        arr = buckets[m]
        # alphabetize pairs with common multiplicity; O(27) as each letter can occur one time in this map
        arr.sort(key=lambda x : x[0])
        for i in arr:
            if prints > 2:
                break
            prints = prints + 1
            print( i[0] + ' ' + str(i[1]) )
        # remove existing max multiplicity from dictionary to move on to the next max multiplicity
        del buckets[m]