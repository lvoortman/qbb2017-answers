#!/usr/bin/env python

import sys

# File 1 is the output file from homework part 1
# File 2 is the t_cata.ctab file from results
file_1 = open(sys.argv[1])
file_2 = open(sys.argv[2])

gene_ID = {}

for line in file_1:
    columns_1 = line.rstrip("\r\n").split()
    fbgn = columns_1[1]
    uniprot = columns_1[0]
    gene_ID[fbgn] = uniprot
    #print gene_ID

argument = sys.argv[-1]

for line in file_2:
    columns_2 = line.rstrip("\r\n").split()
    fbgn_2 = columns_2[8]
    if argument == "-e":
        if fbgn_2 in gene_ID:
            print line + "\t" + gene_ID[fbgn_2]
        else:
            print "Error in finding", fbgn_2
    else:
        if fbgn_2 in gene_ID:
            print line + "\t" + gene_ID[fbgn_2]
        else:
            continue

# ./Day2-Homework2.py Day2-Homework1.out ~/data/results/stringtie/SRR072893/t_data.ctab 