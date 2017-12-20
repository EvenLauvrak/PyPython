from bs4 import BeautifulSoup
import requests
import csv #Legger det i en csv fil, trengs ikke

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

#print soup.prettify()


for article in soup.find_all('article'):

	headline = article.h2.a.text
	print headline

	summary = article.find('div', {"class":"entry-content"}).p.text
	print summary

	date = article.find('p', {"class":"entry-meta"}).time.text
	print date

	print ' '
