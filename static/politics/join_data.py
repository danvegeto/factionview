import sys
import pandas as pd 

reps = pd.read_csv(sys.argv[1], sep='\t', index_col=0)
rep_ids = pd.read_csv(sys.argv[2], sep='\t')
coordinates = pd.read_csv(sys.argv[3], sep='\t')


rows = {}

for i in range(len(coordinates)):

	rep_id = rep_ids.ix[i]['id']

	row = [rep_id]

	row.extend(reps.ix[rep_id])
	row.extend(coordinates.ix[i])

	rows[i] = row

data = pd.DataFrame(rows).transpose()
data.columns = ['id', 'name', 'party', 'state', 'x', 'y']

data.to_csv('data.tsv', sep='\t')