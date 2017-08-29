#!/usr/bin/env python

import sys

MAPQ_List = []

for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    iMAPQ = line.split( "\t" )[4]
    fMAPQ = float( iMAPQ )
    MAPQ_List.append( fMAPQ )

Ave_MAPQ = sum(MAPQ_List)/len(MAPQ_List)

print Ave_MAPQ
    

# cat ~/qbb2017-answers/day1-homework/Output.sam | ./Day2-Exercise5.py > Day2-Exercise5.out