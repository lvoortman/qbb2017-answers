#!/usr/bin/env python

"""

"""

import sys
import fasta
# import 02-kmer-count

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])


target_dict = {}


# Put target file into readable format
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in target_dict:
            target_dict = []
            target_dict[kmer].append((indent, i))
        else:
            target_dict[kmer].append((indent, i))
        
print "Target Sequence Name: %s Target Position: %s Query Psition: %s Kmer: %s"
#print sequence
ident, sequence_q = fasta.FASTAReader(query).next()    
for i in range(0, len(sequence)-k):
    qkmer = sequence_q[i:i+k]
    if q_kmer in target_dict:
        result = target_dict[kmer]
    print q[0], "\t", q[1] , "\t", i, qkmer
