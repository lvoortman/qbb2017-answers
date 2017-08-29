#!/usr/bin/env python

import sys

perfect_align_count = 0

for line in sys.stdin:
    if "NM:i:0" in line:
        perfect_align_count += 1 

print perfect_align_count

# cat ~/qbb2017-answers/day1-homework/Output.sam | ./Day2-Exercise2.py > Day2-Exercise2.out