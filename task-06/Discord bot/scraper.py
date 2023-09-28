import csv
import os
from datetime import date
import requests
from bs4 import BeautifulSoup

def onStart():
	url = "https://www.espncricinfo.com/live-cricket-score"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	a1=soup.find(class_="ds-flex ds-flex-col ds-mt-2 ds-mb-2")
	b1=soup.find(class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")

	f1="Fetching the live scores..."
	a2=a1.get_text()
	b2=b1.get_text()
	d=str(date.today())

	f=open("livescore.csv",'w')

	for j in range(1,len(a2)):
		if a2[j].isupper():
			a3=a2.split(a2[j])
			a4=a2[j]+a3[1]
			break


	a3.remove(a3[1])

	s1="Fetching the live scores..."
	writer = csv.writer(f)
	writer.writerow([s1])
	writer.writerow(a3)
	writer.writerow([a4])
	writer.writerow([b2])
	writer.writerow([d])

	f.flush()
	f.close()
	return s1,a3,a4,b2,d
