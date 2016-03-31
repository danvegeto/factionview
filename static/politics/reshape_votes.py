import sys
import pandas as pd 

votes = pd.read_csv(sys.argv[1], sep='\t')

matrix = votes.pivot(index='vote_id', columns='id', values='value_quant')

matrix = matrix.fillna(0).astype(int)

matrix.to_csv('vote_matrix.tsv', sep='\t', float_format='0')