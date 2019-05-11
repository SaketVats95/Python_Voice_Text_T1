import urllib.request
from bs4 import BeautifulSoup
import webbrowser


def OpenYotube(data):
    textToSearch = 'Hello World'
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    f= open("guru99.txt","w+")
    f.write(soup.prettify)
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        print('https://www.youtube.com' + vid['href']+vid['text'])

OpenYotube('Hello')

def openLink(link):
    webbrowser.open(link)
