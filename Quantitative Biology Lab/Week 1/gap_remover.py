#/usr/bin/env python

"""
Intention is to remove gaps (-) from the tsv file
"""

import sys

open sys.argv[1]

for line in sys.argv[1]:
    line.replace("-","")
    
    