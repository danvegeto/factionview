import sys
import pandas as pd 

votes = pd.read_csv(sys.argv[1], sep='\t')

reps = {}

for i in range(1, len(votes)):

	rep_id = votes.ix[i]['id']

	if not rep_id in reps:

		reps[rep_id] = votes.ix[i][['name', 'party', 'state']]

reps_df = pd.DataFrame(reps).transpose()

reps_df.to_csv('reps.tsv', sep='\t')