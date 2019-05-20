import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver


url="https://contacts.google.com/"
driver=webdriver.Firefox()
driver.get(url)

f=open("userinfo.txt","r+")
username=f.readline()
#f.write(driver.page_source)
userNameInput=driver.find_element_by_xpath("//input[@name='identifier']")
print(userNameInput.get_attribute('type'))
userNameInput.send_keys(username)
button=driver.find_element_by_xpath("//*[text()='Next']")
#driver.get(url)
print(button.text)
button.click()
driver.get(url)
print(driver.page_source)
contactName=driver.find_element_by_xpath("//div[contains(@class,'E6Tb7b')]")
print(len(contactName))
for i in contactName:
    print(i.text)

f.close()


#f=open("ne.txt","r")
#print(f.read())
#soup=BeautifulSoup(f.read(), 'html.parser')
#strhtm = soup.prettify()


# Print the first few characters
#print (strhtm)
#f.close()

