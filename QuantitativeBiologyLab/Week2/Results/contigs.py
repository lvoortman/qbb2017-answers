#!/usr/bin/env python

"""
Write a python script to compute the number of contigs, minimum/maximum/average contig length, and N50. (Remember, you already have a FASTA parser from Bootcamp)
"""

import sys
import fastaParser as fasta
import numpy as np

configs = open(sys.argv[1])

nuc_seq = []

for ident, sequence in fasta.FASTAReader(configs):
    nuc_seq.append(sequence)
    
nuc_seq.sort()

contig_count = len(nuc_seq)

nuc_len = []

for i in range(len(nuc_seq)):
    nuc_len.append(len(nuc_seq[i]))
    
nuc_len.sort()

nuc_len_mean = np.mean(nuc_len)

print "Contig Count = " + str(contig_count)
print "Max = " + str(max(nuc_len))
print "Min = " + str(min(nuc_len))
print "Mean Length = " + str(nuc_len_mean)

contig_len = 0
for i in nuc_len:
    contig_len += i
    
print "L/2 = " + str(contig_len/2)
count = 0
for i in nuc_len:
    if count < int(contig_len)/2:
        count += i
    else:
        print "N50 = " + str(i)
        break



