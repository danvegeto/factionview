import sys
import pandas as pd 
from scipy.spatial.distance import cosine

vote_matrix = pd.read_csv(sys.argv[1], sep='\t', header=0, index_col=0)

n = len(vote_matrix.columns)


#vote_sums = pd.DataFrame(vote_matrix.sum(axis=0)).ix[1:].astype(int)
#vote_sums.columns = ['sum']
#print vote_sums.sort(columns='sum')


dist = []
rep_ids = []

for i in range(n):

	rep_ids.append(vote_matrix.columns[i])

	dist_row = []

	for j in range(n):

		dist_row.append(cosine(vote_matrix.ix[:,i], vote_matrix.ix[:,j]))

	dist.append(dist_row)


dist_df = pd.DataFrame(dist)

dist_df.to_csv('dist_matrix.tsv', sep='\t', header=False, index=False)

rep_ids_df = pd.DataFrame(rep_ids, columns=['id'])

rep_ids_df.to_csv('rep_ids.tsv', sep='\t')