# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('https://en.wikipedia.org/wiki/Telangana')
# rhtml = html.read()
# bsObj = BeautifulSoup(rhtml,'html.parser').prettify()

# for sp in bsObj.findAll('div'):
# 	print (sp)


from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('https://www.mapsofindia.com/railway-timetable/')

soup = BeautifulSoup(html,'html.parser')

#print (soup.find('span',{'class':'currencyINR'}))
# for sp in soup.findAll('a') :#,{"class":"a-lineitem"}):
# 	print (sp.text)


for ele in soup.select('table'):
        print (ele.text)

##divTag = soup.findAll('table',{'class':'tableizer-table'});
##
##for tag in divTag:
##	tdTag =[]
##	tdTag = tag.findAll('td')
##	for tag in tdTag:
##		lst =[]
##		lst = tag.text
##
##		print(lst[0])
		
