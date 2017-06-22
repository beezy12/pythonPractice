
import urllib.request
from bs4 import BeautifulSoup


#url = 'https://finance.yahoo.com/quote/FB?p=FB'
url = 'https://gemini.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)

#sending the request and storing the response
resp = urllib.request.urlopen(req) 

html = resp.read()

# passing the html to BeautifulSoup for parsing
soup = BeautifulSoup(html, 'html.parser') 

#finding all the <td> tags with the specified class
#tagged_values = soup.find_all("td", {'class': 'Ta(end) Fw(b)'})
tagged_values = soup.find_all("div", {'class': 'stat'})
print(tagged_values)
