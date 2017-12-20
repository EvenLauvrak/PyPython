from bs4 import BeautifulSoup
import requests

kilde = requests.get('https://www.komplett.no/search?q=led%20strips&hits=48').text

soup = BeautifulSoup(kilde, 'lxml')

for article in soup.find_all('div', {"class":"product-list-item"}):

	header = article.h2.text
	print 'vare: ', header

	try:
		cont = article.p.text
		print 'beskrivelse: ',cont
	except Exception, e:
		pass

	try:
		buyer = article.find('div', {"class":"product-seller"}).a.text
		print 'Produkt selger: ',buyer
	except Exception, e:
		pass


	try:
		lager = article.find('span', {"class":"stockstatus-stock-details"}).text
		print 'Lager status :',lager
	except Exception, e:
		pass

	try:
		price = article.find('span', {"class":"product-price-now"}).text
		print 'Koster :',price 
	except Exception, e:
		pass

	rating = article.find('div', {"class":"review"})
	print rating.span.text

	print ' '
