#!/usr/bin/env python

"""
-
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv(sys.argv[1])
df_samples_r = pd.read_csv(sys.argv[2])
soi_f = df_samples["sex"] == "female"
soi_m = df_samples["sex"] == "male"

fpkms_f = []
fpkms_m = []
fpkms_fr = [0, 0, 0, 0]
fpkms_mr = [0, 0, 0, 0]

for sample in df_samples["sample"][soi_f]:
    # builds a compete file path
    fname = os.path.join(sys.argv[3], sample, "t_data.ctab")
    # read current sample and separates by tab
    df = pd.read_csv(fname, sep = "\t")    
    roi_f = df["t_name"] == transcript
    fpkms_f.append(df[roi_f]["FPKM"].values)
    

for sample in df_samples["sample"][soi_m]:
    # builds a compete file path
    fname = os.path.join(sys.argv[3], sample, "t_data.ctab")
    # read current sample and separates by tab
    df = pd.read_csv(fname, sep = "\t")
    roi_m = df["t_name"] == transcript
    fpkms_m.append(df[roi_m]["FPKM"].values)

soi_f = df_samples_r["sex"] == "female"
soi_m = df_samples_r["sex"] == "male"
for sample in df_samples_r["sample"][soi_f]:
    # builds a compete file path
    fname = os.path.join(sys.argv[3], sample, "t_data.ctab")
    # read current sample and separates by tab
    df = pd.read_csv(fname, sep = "\t")   
    roi_fr = df["t_name"] == transcript
    fpkms_fr.append(df[roi_fr]["FPKM"].values)
    

for sample in df_samples_r["sample"][soi_m]:
    # builds a compete file path
    fname = os.path.join(sys.argv[3], sample, "t_data.ctab")
    # read current sample and separates by tab
    df = pd.read_csv(fname, sep = "\t")    
    roi_mr = df["t_name"] == transcript
    fpkms_mr.append(df[roi_mr]["FPKM"].values)
    
#print roi_f
#print roi_m

plt.figure()

plt.plot(fpkms_f, c = "red", label = "Female")
plt.plot(fpkms_m, c = "blue", label = "Male")
plt.plot(fpkms_fr, c = "orange", label = "Female_R")
plt.plot(fpkms_mr, c = "green", label = "Male_R")
plt.title("Sxl")
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA Abundance (FPKM)")
plt.xticks(range(len(fpkms_f)), ["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
plt.legend(bbox_to_anchor = (1.01, 0.5), loc='center left')
plt.subplots_adjust(left=None, bottom=None, right=.75, top=None,
                wspace=None, hspace=None)

plt.savefig("plot.png")
plt.close()




