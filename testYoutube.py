import urllib.request
from bs4 import BeautifulSoup
import webbrowser





def OpenYotube(data):
    textToSearch = data
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html=response.read()
    #urllib.request.urlretrieve(url, "ne.txt")

    soup = BeautifulSoup(html, 'html.parser')
    elements=soup.find_all(attrs={'class':'yt-uix-tile-link'})
    obj=[]
    for vid in elements:
        if vid.text.strip()!="" and  vid['href'] !="":
            obj.append([vid.text.strip(),'https://www.youtube.com' + vid['href']])

    return obj

    #for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        #print('https://www.youtube.com' + vid['href']+vid.text.strip())


OpenYotube('Hello')

def openLink(link):
    webbrowser.open(link)

