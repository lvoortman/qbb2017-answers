#!/usr/bin/env python

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np

codon_wheel = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

nucleotide = open(sys.argv[1])

dN = []

dS = []

for i in range(0,4871):
    dN.append(0)
    dS.append(0)


nucleotide_seq = []
for ident, sequences in fasta.FASTAReader( nucleotide ):
    nucleotide_seq.append(sequences)


query_seq = nucleotide_seq[:1]
target_seq = nucleotide_seq[1:]


codon_query = []
target_query = []
nuc_count = 0
while nuc_count < 14614:
    query = query_seq[0][nuc_count:nuc_count+3]
    target = target_seq[0][nuc_count:nuc_count+3]
    codon_query.append(query)
    target_query.append(target)
    nuc_count +=3



#for c in itertools.izip(codon_query, target_query):
#    print c
print len(target_seq)

for n in range(len(target_seq)):
    count = 0
    prot_count = 0
    while count < 14614:
        target = target_seq[n][count:count+3]
        query = query_seq[0][count:count+3]
        if "-" in target_seq[n][count:count+3]:
            count += 3
            prot_count += 1
        elif "-" in query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target_seq[n][count:count+3] == query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target not in codon_wheel:
            count += 3
        elif codon_wheel[target] != codon_wheel[query]:
            dN[prot_count] = dN[prot_count] + 1
            count += 3
            prot_count += 1
        elif codon_wheel[target] == codon_wheel[query]:
            dS[prot_count] = dS[prot_count] + 1
            count += 3
            prot_count += 1      
        else:
            print "Error in code"

dN_dS = [int(n) - int(s) for n,s in zip (dN, dS)]

print len(dN)
print len(dS)        
#print dN_dS

plt.figure()
plt.plot(dN_dS)
plt.xlabel("Gene Loc")
plt.ylabel("dN-dS")
plt.savefig( "dN_dS_plot" + ".png")
plt.close()