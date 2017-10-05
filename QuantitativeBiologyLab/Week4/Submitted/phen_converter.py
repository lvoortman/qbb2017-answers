#!/usr/bin/env python

"""
To conver the chromosome name in the phenotype file to A#   #, instead of A#_#

"""
import sys
import pandas as pd



phenosplit = []
phenoid = []

pheno = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")

for line in pheno:
    if line.startswith("\t"):
        outfile.write("\t" + line + "\n")
        continue
    if line.startswith("A"):
        phenosplit = line.split()
        phenoid = phenosplit[0].replace("_", "\t")
        #print phenoid
        remainder = "\t".join(phenosplit[1:])
        # print remainder
        outfile.write(phenoid + "\t" + remainder + "\n")
