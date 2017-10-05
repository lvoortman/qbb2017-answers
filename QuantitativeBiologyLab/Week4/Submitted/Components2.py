#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

samples = open(sys.argv[1])

comp1 = []
comp2 = []
for line in samples:
    line = line.rstrip("\r\n").split("\t")    
    comp1.append(line[2])
    comp2.append(line[3])

print line


plt.figure()
plt.scatter(comp1, comp2)
plt.title("Plot of Two Principle Components")
plt.xlabel("Component 1")
plt.ylabel("Component 2")

plt.savefig("components.png")
plt.close()