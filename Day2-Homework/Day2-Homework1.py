#!/usr/bin/env python

import sys

f = open(sys.argv[1])
AC_list = []
gene_ID_list = []

for line in f:    
    if ("DROME" in line) and ("FBgn" in line):
        columns = line.strip("\r\n").split()
        AC_num = columns[-2]
        gene_ID = columns [-1]
        #print AC_num + "\t" + gene_ID
        print("%s\t%s" % (AC_num,gene_ID))
        
    

