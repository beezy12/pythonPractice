
import urllib.request
from bs4 import BeautifulSoup

symbols = ['FB', 'GOOG', 'AAPL']

for symbol in symbols:

    print('Company: ' + symbol)
    url = 'https://finance.yahoo.com/quote/'+symbol+'/'
    #url = 'https://gemini.com/'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    req = urllib.request.Request(url, headers=headers)

    #sending the request and storing the response
    resp = urllib.request.urlopen(req) 

    html = resp.read()

    # passing the html to BeautifulSoup for parsing
    soup = BeautifulSoup(html, 'html.parser') 

    #finding all the <td> tags with the specified class. TAGGED VALUES IS A THING IN SOUP, look it up
    tagged_values = soup.find_all("td", {'class': 'Ta(end) Fw(b) Lh(14px)'})
    #tagged_values = soup.find_all("div", {'class': 'stat'})
    #print(tagged_values)


    #list comprehension....the python way is below this
    #values = [x.get_text() for x in tagged_values]

    values = []
    for tv in tagged_values:
        values.append(tv.get_text())

    for value in values:
        print(value)

    print('\n')
