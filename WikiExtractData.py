import urllib.request

link="https://en.wikipedia.org/wiki/List_of_Prime_Ministers_of_India"

import requests
from lxml import etree

# manually storing desired URL
url = 'https://en.wikipedia.org/wiki/Delhi_Public_School_Society'

# fetching its url through requests module
req = requests.get(url)

store = etree.fromstring(req.text)

# this will give Motto portion of above
# URL's info box of Wikipedia's page
output = store.xpath('//table[@class="infobox vcard"]/tr[th/text()="Motto"]/td/i')

# printing the text portion
print(output[0].text)
#x = urllib.request.urlopen(link)
#print(x.read())




