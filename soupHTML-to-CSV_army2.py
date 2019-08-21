# import libraries

import csv
import re
import urllib2
import csv
from urllib2 import urlopen

# from urllib.request import urlopen
from bs4 import BeautifulSoup

contents = []

f = csv.writer(open('armyResults2.csv', 'w'))
f.writerow(['Title','Date','Publisher','Description','Metadata','Download'])

with open('armyCorps.csv','r') as csvf: # Open file in read mode
    urls = csv.reader(csvf)
    for url in urls:
        contents.append(url) # Add each url to list contents

for url in contents:  # Parse through each url in the list.
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")

	titleField = soup.find(attrs={'id': 'Title:'})
# 	dateField = soup.find(attrs={'id': 'Label2'})
# 	publisherField = soup.find(attrs={'id': 'Label3'})
# 	descriptionField = soup.find(attrs={'id': 'Label14'})
# 	metadataLink = soup.find('a', href=True, text='Metadata')
#  	downloadLink = soup.find('a', href=True, text='Download')

	title = titleField.text.strip(),
# 	date = dateField.text.strip(),
# 	publisher = publisherField.text.strip(),
# 	description = descriptionField.text.strip(),
# 	metadata = metadataLink['href'],
#
# 	try:
# 		download = downloadLink['href']
# 	except:
# 		download = "undefined"

	f.writerow([title])
# 	f.writerow([title,date,publisher,description,metadata,download])
















