from bs4 import BeautifulSoup
import requests
from datetime import datetime

startTime = datetime.now()

kilde = requests.get('https://www.komplett.no/search?q=pc&hits=1000').text

soup = BeautifulSoup(kilde, 'lxml')
stykk = 0
for article in soup.find_all('div', {"class":"product-list-item"}):
	if article.find('span', {"class":"discount-label"}):

		header = article.h2.text	
		print 'vare: ', header

		try:
			cont = article.p.text
			print 'beskrivelse: ',cont
		except Exception, e:
			pass

		try:
			sale_price = article.find('span', {"class":"discount-label"}).text
			print "Rabbat :", sale_price
		except Exception, e:
			pass

		try:
			org_price = article.find('div', {"class":"product-price-before"}).text
			print "orginal pris", org_price
		except Exception, e:
			pass 

		try:
			cur_price = article.find('span', {"class":"product-price-now"}).text
			print "Gjelende pris :", cur_price
		except Exception as e:
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
			rating = article.find('div', {"class":"review"}).text
			star = rating.span.text
			print star
		except Exception as e:
			pass

		print ""

		stykk += 1

print "produkter til salg: ", stykk
print datetime.now() - startTime