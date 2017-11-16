#!/usr/bin/env python

"""
Getting the differential expression in the cell types
"""

import sys
import pandas as pd
from scipy.stats import ttest_ind, ttest_rel

def average_early_late( early, late ):
    data = pd.read_csv( sys.argv[1], sep='\t' ).dropna(how='any') # opens file and drops and NA values
    data['ave_early'] = data[early].mean( axis=1 )
    data['ave_late'] = data[late].mean( axis=1 )
    return data.dropna()
    
def get_diff_stats( average_df, early, late ):
    average_df['ratio'] = average_df['ave_early'] / average_df['ave_late']
    stat, p = ttest_ind( average_df[early], average_df[late], axis=1 )
    average_df['p-value'] = p
    average_df = average_df.dropna()
    average_df = average_df.mask(average_df['p-value'] > 0.05).dropna()
    down_df = average_df.mask(average_df['ratio'] > 1.0).dropna()
    up_df = average_df.mask(average_df['ratio'] < 1.0).dropna()
    return pd.concat([down_df, up_df])[['gene','ratio','p-value']].sort_values('ratio')
    
def main():
    early = [ 'CFU', 'poly', 'unk' ]
    late = [ 'mys', 'mid', 'int' ]
    averaged = average_early_late( early, late )
    avg_and_stats = get_diff_stats( averaged, early, late )
    print avg_and_stats.to_csv( index=False, sep='\t' )

main()