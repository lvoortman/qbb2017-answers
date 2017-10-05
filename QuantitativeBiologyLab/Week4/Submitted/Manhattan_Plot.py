#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

pvalue = []
pnumbers = []
pvas = []
x = []
y = []
bad_x = []
bad_y = []

phens = open( sys.argv[1] )
count = 0
for line in phens:
    if line.startswith(" ") or "NA" in line:
        continue
    else:
        cutoff = -np.log( 0.00005 )
        line = line.rstrip("\r\n").split()
        count += 1
        # print count
        pvalue = -np.log( float(line[8]) )
        # print pvalue
        if pvalue > cutoff:
            x.append( count )
            y.append( pvalue )
        else: 
            bad_x.append( count )
            bad_y.append( pvalue )


plt.figure()
plt.scatter( x, y, color = 'blue', alpha = 0.5 )
plt.scatter( bad_x, bad_y, color = 'red', alpha = 0.5 )
plt.title("Manhattan Plot")
plt.ylabel("-log(P-Value)")
plt.xlabel("SNP")
plt.savefig( "Manhattan_" + sys.argv[1] + ".png")
plt.close()