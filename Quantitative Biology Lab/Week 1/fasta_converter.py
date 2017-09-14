#!/usr/bin/env python
"""
Intended to put tsv file into fa formatted file
    -insert the carrot in the beginning of the header
    -print ID, followed by the sequence
"""


import sys

f = open(sys.argv[1])

for line in f:
    line = line.rstrip("\r\n").split("\t")
    seq = line[1].replace("-", "")
    label = '>%s\n%s' % (line[0], seq)
    print label
    