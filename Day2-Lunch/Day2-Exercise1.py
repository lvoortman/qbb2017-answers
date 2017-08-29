#!/usr/bin/env python

import sys

align_count = 0

for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    align_count += + 1 

print align_count

# cat ~/qbb2017-answers/day1-homework/Output.sam | ./Day2-Exercise1.py > Day2-Exercise1.out
