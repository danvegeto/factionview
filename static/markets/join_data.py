import pandas

df1 = pandas.read_csv('data/companies.csv', index_col=0)
df2 = pandas.read_csv('data/coordinates.csv', index_col=0)

df = df1.join(df2)

df.to_csv('data/data.csv')