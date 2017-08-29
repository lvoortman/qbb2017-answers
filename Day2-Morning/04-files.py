#!/usr/bin/env python

import sys

# Opening file with open
f = open( "/Users/cmdb/data/genomes/BDGP6.fa" )

# Opens file using input at command line
f = open( sys.argv[1] )

# If nothing is denoted as being the input by sys.argv, then use whatever the standard input is (eg. porting in to python program from cat)
if len( sys.argv ) > 1:
    f = open( sys.argv[1] )
    first_line = f.readline()
else:
    first_line = sys.stdin.readline()

print first_line

#first_line = f.readline()

# Allows for input of file for processing in the command line instead of being locked into the program (use cat to specify file then port into python program)
first_line = sys.stdin.readline()

print first_line