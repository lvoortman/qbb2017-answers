#!/usr/bin/env python

"""
Usage: ./Day4-Lunch-Exercise1.py

-Visualize the FPKM values in a scatter plot for:
    -SRR072893
    -SRR072915
"""


import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy


df = pd.read_csv(sys.argv[1], sep = "\t")

gene_names2 = {}    
df2 = pd.read_csv(sys.argv[2], sep = "\t")

x = numpy.log1p(df["FPKM"])
y = numpy.log1p(df2["FPKM"])
m = numpy.polyfit(x, y, 1)

#print df2["FPKM"]
plt.figure()
plt.scatter(numpy.log1p(df["FPKM"]), numpy.log1p(df2["FPKM"]), alpha = 0.5, c = "orange")
#plt.scatter(df["FPKM"], df2["FPKM"])
#plt.close()
plt.xlabel("log(FPKM) of SRR072893")
plt.ylabel("log(FPKM) of SRR072915")
plt.title("Comparison of FPKM Values \nBetween SRR072915 and SRR072893")
plt.plot(numpy.unique(x), numpy.poly1d(numpy.polyfit(x, y, deg = 1))(numpy.unique(x)))
plt.savefig(sys.argv[3] + ".png")
#plt.show()