#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    Chr_List = line.split("\t")[2]
    print Chr_List
    count += 1
    if count > 9:
        break

# cat ~/qbb2017-answers/day1-homework/Output.sam | ./Day2-Exercise4.py > Day2-Exercise4.out
