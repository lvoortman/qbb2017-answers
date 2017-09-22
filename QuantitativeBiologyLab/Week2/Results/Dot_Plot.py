#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

first_plot = open(sys.argv[1])

count = 1
plt.figure()
for i in first_plot:
    if "zstart1" in i:
        continue
    fields = i.split("\t")
    plt.plot([count,count+float(fields[1])],[float(fields[0]),float(fields[3])])
    count += float(fields[1])

plt.xlabel("Contig Names")
plt.ylabel("Position")
plt.xlim(0,100000)
plt.ylim(0,100000)
plt.savefig( "(SOURCE)" + ".png")
plt.close