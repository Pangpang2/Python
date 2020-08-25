import bs4 as bs
import urllib2
import pandas as pd

# sause = urllib2.urlopen('https://pythonprogramming.net/parsememcparseface').read()
#
# soup = bs.BeautifulSoup(sause, 'lxml')


# print(soup.title)
#
#
# print(soup.p)
#
# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     print paragraph.text
#
# print soup.get_text()
#
# for url in soup.find_all('a'):
#     print url.get('href')

# nav = soup.nav
#
# for url in nav.find_all('a'):
#     print url.get('href')

#
# for div in soup.find_all('div', class_='body'):
#     print div.text

#------------------------------------------------------------------------
# table
#table = soup.table
# table = soup.find('table')
# table_rows = table.find_all('tr')
#
# for tr in table_rows:
#     td = tr.find_all('td')
#     row =[i.text for i in td]
#     print row

# parse all tables
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface')
# for df in dfs:
#     print df

#------------------------------------------------------------------------
#xml
#sitemap

# sause = urllib2.urlopen('https://pythonprogramming.net/sitemap.xml').read()
# soup = bs.BeautifulSoup(sause, 'xml')
# for url in soup.find_all('loc'):
#     print url.text

#------------------------------------------------------------------------
# Dynamic js
file = open('C:\Users\MayLi\Desktop\E2E\d3.ibexdtx01_2018-12-18_06_16_45_563.xml', 'r').read()

soup = bs.BeautifulSoup(file)
a = soup.prettify()
print a






