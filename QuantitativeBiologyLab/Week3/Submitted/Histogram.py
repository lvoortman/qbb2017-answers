#!/usr/bin/env python

"""

"""

import sys
import matplotlib.pyplot as plt

variants = open(sys.argv[1])


variant_freq = []
for i in variants:
    if i.startswith("#"):
        continue 
    line = i.rstrip("\t\n").split()
    af = line[7].split(";")
    af1 = af[3][3:]
    if "," in af1:
        af2 = af1.split(",")
        for i in af2:
            variant_freq.append(float(i))
    else:
        print af1
        variant_freq.append(float(af1))

plt.figure()
plt.hist(variant_freq, bins=20)
plt.savefig("histogram.png")
plt.close()




