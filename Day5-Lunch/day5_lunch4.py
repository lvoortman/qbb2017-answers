#!/usr/bin/env python

"""
Usage:
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import statsmodels.api as sm


mean_1 = []
mean_2 = []
mean_3 = []
mean_4 = []

t_names = []

fh_1 = open(sys.argv[2])

for line in fh_1:
    fields = line.rstrip("\r\n").split()
    mean_1.append(float(fields[-1]))
    t_names.append(fields[0])
fh_2 = open(sys.argv[3])
for line in fh_2:
    fields = line.rstrip("\r\n").split()
    mean_2.append(float(fields[-1]))
fh_3 = open(sys.argv[4])
for line in fh_3:
    fields = line.rstrip("\r\n").split()
    mean_3.append(float(fields[-1]))
fh_4 = open(sys.argv[5])
for line in fh_4:
    fields = line.rstrip("\r\n").split()
    mean_4.append(float(fields[-1]))
    
means = zip(mean_1, mean_2, mean_3, mean_4)
#print means

df = pd.read_csv(sys.argv[1], sep="\t")
df.set_index("t_name")
fpkms = df.loc[df['t_name'].isin(t_names)]["FPKM"].values.tolist()
# fpkms = df["FPKM"].values.tolist()

model = sm.OLS(fpkms, means)
result = model.fit()
print(result.summary())

