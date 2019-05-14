import urllib.request
from bs4 import BeautifulSoup

f=open("ne.txt","r")
#print(f.read())
soup=BeautifulSoup(f.read(), 'html.parser')
strhtm = soup.prettify()

# Print the first few characters
print (strhtm)
f.close()
f=open("newFormated.html","w+")
f.write(strhtm)
f.close()
