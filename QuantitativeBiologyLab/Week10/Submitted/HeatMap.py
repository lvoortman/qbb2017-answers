#!/usr/bin/env python

import scipy.cluster as sc
import sys
import numpy as np
import matplotlib.pyplot as plt

array = np.loadtxt(sys.argv[1], dtype = str)
headerless_array = np.delete(array, (0), axis=0)
final_array = headerless_array[:,1:]
float_array = final_array.astype(np.float)
#print float_array
#generate the linkage matrix
Z = sc.hierarchy.linkage(float_array, method = 'average')
#print Z
#reorder the linkage matrix
ordered_heatmap_idx = sc.hierarchy.leaves_list(Z)
#print ordered_heatmap_idx.shape

ordered_heatmap = float_array[ordered_heatmap_idx, :]


column_labels = ["CFU", "poly", "unk", "int", "mys", "mid"]
plt.pcolor(ordered_heatmap, cmap = 'PuBuGn')
plt.xticks(range(len(column_labels)), column_labels)

plt.savefig("heatmap.png")


Z = sc.hierarchy.linkage(float_array.T, method = 'average')
column_labels = ["CFU", "poly", "unk", "int", "mys", "mid"]
plt.figure()
sc.hierarchy.dendrogram(Z, labels = column_labels)
#print sc.hierarchy.dendrogram(Z)
plt.savefig("dendrogram.png")
