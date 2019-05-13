import urllib
from bs4 import BeautifulSoup
import webbrowser


def OpenYotube(data):
    textToSearch = 'Hello World'
    #query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + textToSearch
    response = urllib.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    #f= open("guru99.txt","w+")
    #f.write(soup.prettify)
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        print('https://www.youtube.com' + vid['href'])

OpenYotube('Hello')

def openLink(link):
    webbrowser.open(link)
