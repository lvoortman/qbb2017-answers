#!/usr/bin/env python

import sys

single_align = 0

for line in sys.stdin:
    if "NH:i:1" in line:
        single_align += 1 

print single_align

# cat ~/qbb2017-answers/day1-homework/Output.sam | ./Day2-Exercise3.py > Day2-Exercise3.out