#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt


freq = open(sys.argv[1])


allele_freq=[]
for i in freq:
    if i.startswith("#"):
        continue 
    lines = i.rstrip("\t\n").split()
    for i in lines[4]:
        if i in lines[4] == "MAF":
            continue
        else:
            allele_freq.append(float(lines[4]))

#print allele_freq


plt.figure()
plt.hist(allele_freq, bins=20)
plt.savefig("histogram.png")
plt.close()
