#!/usr/bin/env python3

import os
import sys

if len(sys.argv) < 2:
    print("Please provide a test number to execute")
    exit()

testNumber = sys.argv[1]

os.system("python3 medianAVL.py {0}".format(testNumber))
os.system("python3 Utils/testRunner.py q act testOutput{0}.txt exp testAnswer{0}.txt".format(testNumber))