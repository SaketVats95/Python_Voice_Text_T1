import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
from lxml import etree

f=open("htmlForContacts.html","r+")
htmlContent=f.read()
#driver=webdriver.get("file:///C:/Saket Vats/Jarvis testphase 1/Python_Voice_Text_T1/htmlForContacts.html")
#selenium = new selenium.WebDriverBackedSelenium(driver, "file:///D:/folder/abcd.html");

#driver.find
html = '''<body><div class="container"> 
<p class="row"> 
<a href="#123333" class="box"> I love xpath </a> 
<a href="#123333" class="box"> I love Saket Vats </a> 
</p> 

</div><script>function a(){alert("Saket Vats");}</script></body>'''

#print(html)
# Use etree to process html text and return an _Element object which is a dom object.
dom = etree.HTML(htmlContent)

# Get a tag's text. Please Note: The _Element's xpath method always return a list of html nodes.Because there is only one a tag's text, so we can do like below.
#a_tag_text = dom.xpath('//div/p/a/text()')
a_tag_text = dom.xpath("//div[contains(@class,'E6Tb7b')]/span/text()")#('//div/p/a/text()')
#print(a_tag_text)

#htmlparser = etree.HTMLParser()
#tree = BeautifulSoup(htmlContent, 'html.parser')
#t=etree.parse(htmlContent,etree.HTMLParser())
#a=t.xpath("//div[contains(@class,'E6Tb7b')]")
#a=tree.body.findAll('div')#("//div[@class='XXcuqd']")
#rint(a)
for i in a_tag_text:
    if i.strip()!="":
        print(i)

