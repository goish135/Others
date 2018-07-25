import requests
from bs4 import BeautifulSoup
import time

# get html 
url = 'http://sa.ntcu.edu.tw/news.php?page_num=1&type=20&unit=4'
html = requests.get(url).text

# get location of all message & time
soup = BeautifulSoup(html,'lxml')
location = soup.find('ul',{"class":"tbody"})
test=location.find_all('li')
ok=location.find_all('span')

# get today's date
ft = time.strftime("%Y-%m-%d")
print('today is: '+ft+'\n')
str1 = ft
for t in ok:
    print(t.text,end='')
    str2 = t.text
    if str1==str2:
        #print('go notifying')
        print(': O')
    else :
        #print('do not need to do')
        print(': X')



