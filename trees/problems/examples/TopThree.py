#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys

#solution for https://www.hackerrank.com/challenges/most-commons/

if __name__ == '__main__':
    s = input()
    d = defaultdict(lambda : 0)
    for l in s:
        d[l] = d[l] + 1
    buckets = defaultdict(list)
    for k,v in d.items():
        buckets[v].append((k,v))
    prints = 0
    while prints < 3:
        m = max(buckets.keys())
        arr = buckets[m]
        arr.sort(key=lambda x : x[0])
        for i in arr:
            if prints > 2:
                break
            prints = prints + 1
            print( i[0] + ' ' + str(i[1]) )
        del buckets[m]