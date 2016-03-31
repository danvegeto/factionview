import pandas

rdiffs = pandas.read_csv('static/data/prices.csv', index_col=0)

rdiffs = rdiffs.drop('date', 1)

n = len(rdiffs.columns)

corr = []

for i in range(n):

	row = []

	for j in range(n):

		c = rdiffs.ix[:365,i].corr(rdiffs.ix[:365,j])

		row.append(c)

	corr.append(row)

df = pandas.DataFrame(corr, index=rdiffs.columns, columns=rdiffs.columns).fillna(0)

df.to_csv('static/data/correlations.csv')