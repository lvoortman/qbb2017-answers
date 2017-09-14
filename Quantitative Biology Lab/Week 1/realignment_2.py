#!/usr/bin/env python

import sys
import itertools
import fasta


dnaFile = open(sys.argv[1])
aminoFile = open(sys.argv[2])
alignmentFile = open("alignment_nuc.fa", "w")

for (dnaIdent, dnaSeq), (aminoIdent, aminoSeq) in itertools.izip(fasta.FASTAReader(dnaFile), fasta.FASTAReader(aminoFile)):
    alignmentFile.write(dnaIdent + "\n")
    for amino in aminoSeq:
        if amino == "-":
            alignmentFile.write("---")
        else:
            alignmentFile.write(dnaSeq[:3])
            dnaSeq = dnaSeq[3:]

    alignmentFile.write("\n")

print alignmentFile    
    