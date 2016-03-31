import pandas

print 'downloading company names'

companies = pandas.read_csv('https://github.com/datasets/s-and-p-500-companies/raw/master/data/constituents-financials.csv', index_col=0)

companies.to_csv('static/data/companies.csv')

df = pandas.DataFrame()

i = 0

for code in companies.index:

	print 'downloading price history (' + str(i) + '/' + str(len(companies)) + '): ' + code

	url = 'https://www.quandl.com/api/v1/datasets/WIKI/' + code + '.csv?rows=90&column=4&transformation=rdiff&api_key=msf-SgTxxaB2iDtazzBm'

	try:

		new_df = pandas.read_csv(url, names=['date', code], skiprows=1)

		if df.empty:
			df = new_df
		else:
			df = df.merge(new_df, on='date', how='outer')

	except:

		continue

	i += 1

df.to_csv('static/data/prices.csv')