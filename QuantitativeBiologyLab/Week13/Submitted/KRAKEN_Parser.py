#!/usr/bin/env python

import sys

dt = open(sys.argv[1])
output = open(sys.argv[2], "w")

c2 = {}

for line in dt:
    dt2 = line.strip().split("\t")
    
    if dt2[1] not in c2:
        c2[dt2[1]] = 1
    else:
        c2[dt2[1]] += 1

for key in c2:
    output.write(str(c2[key]) + "\t")
    key2 = key.split(";")
    for index in key2:
        output.write(str(index) + "\t")
    output.write('\n')
    
    
    
    