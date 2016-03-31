import sys
import urllib
import json
from bs4 import BeautifulSoup

print '\t'.join(['congress', 'year', 'vote_name', 'vote_id', 'id', 'name', 'party', 'state', 'value', 'value_quant'])

congress = int(sys.argv[1])

year1 = 1941 + (congress - 77)*2
year2 = year1 + 1

for year in [year1, year2]:

	dir_url = 'https://www.govtrack.us/data/congress/' + str(congress) + '/votes/' + str(year) + '/'

	dir_text = urllib.urlopen(dir_url).read()
	dir_doc = BeautifulSoup(dir_text)

	for link in dir_doc.find_all('a')[1:]:

		vote_name = link['href'][:-1]

		if not vote_name.startswith(sys.argv[2]):
			continue

		url = dir_url + vote_name + '/data.json'

		text = urllib.urlopen(url).read()
		data = json.loads(text)

		category = data['category']
		
		#if category != 'passage':
		#	continue

		for choice in data['votes'].keys():

			quant = '0'

			if choice == 'Aye' or choice == 'Yes' or choice == 'Present':
				quant = '1'
			elif choice == 'Nay' or choice == 'No':
				quant = '-1'

			for voter in data['votes'][choice]:
				
				row = '\t'.join([str(congress), str(year), vote_name, data['vote_id'], voter['id'], voter['display_name'], voter['party'], voter['state'], choice, quant])

				row = row.encode('utf8')

				print row