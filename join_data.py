import pandas

df1 = pandas.read_csv('static/data/companies.csv', index_col=0)
df2 = pandas.read_csv('static/data/coordinates.csv', index_col=0)

df = df1.join(df2)

df.to_csv('static/data/data.csv')