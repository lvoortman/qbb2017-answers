#!/usr/bin/env python

"""

"""


import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="\t")
roi_f = df["strand"] == "+"
roi_r = df["strand"] == "-"


f_df = pd.DataFrame()


genestart_f = df["start"][roi_f]
f_df["chr"] = df["chr"][roi_f]
f_df["start"] = genestart_f - 500
f_df["end"] = genestart_f + 500
f_df["t_name"] = df["t_name"][roi_f]
    
    
r_df = pd.DataFrame()  


genestart_r = df["end"][roi_r]
r_df["chr"] = df["chr"][roi_r]
r_df["start"] = genestart_r - 500
r_df["end"] = genestart_r + 500
r_df["t_name"] = df["t_name"][roi_r]
    

df_final = pd.concat([f_df, r_df])

pos_hit = df_final["start"] >= 0 

final = df_final[pos_hit]
final.to_csv("day5-lunch2.bed", "\t", header = False, index = False)

