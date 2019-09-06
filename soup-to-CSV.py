import csv
import re
import urllib2
import csv
from urllib2 import urlopen

from bs4 import BeautifulSoup

portalMetadata = []

f = csv.writer(open('pas2.csv', 'w'))
f.writerow(['Title','Date','Publisher','Description','Metadata'])

with open('archivedlinks.csv','r') as harvest:
    urls = csv.reader(harvest)
    for url in urls:
        portalMetadata.append(url)

for url in contents:
	page = urlopen(url[0]).read()
	soup = BeautifulSoup(page, "html.parser")

	titleField = soup.find(attrs={'id': 'Label1'})
	dateField = soup.find(attrs={'id': 'Label2'})
	publisherField = soup.find(attrs={'id': 'Label3'})
	descriptionField = soup.find(attrs={'id': 'Label14'})
	metadataLink = soup.find('a', href=True, text='Metadata')
	downloadLink = soup.find('a', href=True, text='Download historic versions of this dataset')


	title = titleField.text.strip(),
	date = dateField.text.strip(),
	publisher = publisherField.text.strip(),
	description = descriptionField.text.strip(),
	metadata = metadataLink['href'],
	download = downloadLink['href'],


	f.writerow([title,date,publisher,description,metadata])
















