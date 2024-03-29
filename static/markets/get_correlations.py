import pandas

rdiffs = pandas.read_csv('data/prices.csv', index_col=0)

rdiffs = rdiffs.drop('date', 1)

n = len(rdiffs.columns)

corr = []

for i in range(n):

	row = []

	for j in range(n):

		c = rdiffs.ix[:,i].corr(rdiffs.ix[:,j])

		row.append(c)

	corr.append(row)

df = pandas.DataFrame(corr, index=rdiffs.columns, columns=rdiffs.columns).fillna(0)

df.to_csv('data/correlations.csv')