import sys
import random
import pandas as pd 
from scipy.spatial.distance import cosine

print 'i\tj\tval'

vote_matrix = pd.read_csv(sys.argv[1], sep='\t', header=0, index_col=0)

n = len(vote_matrix.columns)

for i in range(n):

	min_val = -1
	min_j = []

	for j in range(n):

		if i != j:

			val = cosine(vote_matrix.ix[:,i], vote_matrix.ix[:,j])

			if val < min_val or min_val == -1:

				min_val = val
				min_j = [j]

			elif val == min_val:

				min_j.append(j)

	
	j = min_j[0]

	if len(min_j) > 1:
		j = min_j[int(random.random() * len(min_j))]

	print str(i) + '\t' + str(j) + '\t' + str(min_val)



