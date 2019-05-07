from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(
    firefox_binary=binary, executable_path=r'C:\Users\Saket\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
# driver.get("http://econpy.pythonanywhere.com/ex/001.html")
#searchString = input("Enter the search query")
#driver.get("http://viewpure.com/search?q="+"old bollywood songs")
# driver.implicitly_wait(40)

#linksInfo = driver.find_elements_by_xpath('//a[@class="live-link2"]')
# for i in range(len(buyers)):
# for link in linksInfo:
#   links.append(link.get_attribute('href'))
# print(links)
driver.get('http://viewpure.com/PGaREkyfKPs?ref=search')  # links[0])
playlink = driver.find_element_by_xpath('//div[@class="video"]')
print(playlink.text)
playlink.click()
# driver.close()
# <button class="ytp-large-play-button ytp-button" aria-label="Play">
