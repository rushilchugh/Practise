import urllib.request
from bs4 import BeautifulSoup
import re

html_source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').read()

soup = BeautifulSoup(html_source , 'html.parser')

#Extracting the php link

base_link = 'http://www.pythonchallenge.com/pc/def/'
php_link = soup.a.get('href') #This means, get the href attribute from the a tag



m_page_link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=37278'
php_link_2 = m_page_link.split('/')[-1]

for i in range(0,400):
    
    php_source = urllib.request.urlopen(m_page_link).read().decode('utf-8')

    #PHP Number

    
    num = re.findall(r'\d+' , php_source)[0]
    php_nonum = re.findall(r'.+[^0-9]' , php_link_2)[0]
    php_link_2 = php_nonum + num
    m_page_link = base_link + php_link_2
    print(i , m_page_link ,sep = "|")  
