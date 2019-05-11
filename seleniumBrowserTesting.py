from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
def SearchYoutube(searchString):
    try:
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        driver = webdriver.Firefox(
            firefox_binary=binary)
        # driver.get("http://econpy.pythonanywhere.com/ex/001.html")
        if searchString == "":
            searchString = input("Enter the search query:  ")
        driver.get("http://viewpure.com/search?q="+searchString)
        # driver.implicitly_wait(40)

        linksInfo = driver.find_elements_by_xpath('//a[@class="live-link2"]')
        # for i in range(len(buyers)):
        links = []
        for link in linksInfo:
            links.append(link.get_attribute('href'))

        for i in range(len(links)):
            print(i+1, ":", linksInfo[i].text)
        videoitem = int(input("Enter which video you want to play"))
        driver.get(links[i-1])  # links[0])
        playlink = driver.find_element_by_xpath('//div[@class="video"]')
        print(playlink.text)
        playlink.click()
    except Exception as e:
        print("Recog Error; {0}".format(e))
