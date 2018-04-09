
import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://73.58.142.135', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False
